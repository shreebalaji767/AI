"use strict";


/* =========================================================
   ANSWER MACHINE
   Browser-side static answer engine
========================================================= */

const brain = window.BRAIN || {};

const elements = {
    landingPage: document.getElementById("landingPage"),
    logoButton: document.getElementById("logoButton"),

    question: document.getElementById("question"),
    characterCount: document.getElementById("characterCount"),
    askButton: document.getElementById("askButton"),

    processingCard: document.getElementById("processingCard"),
    processingPercent: document.getElementById("processingPercent"),
    processingMessage: document.getElementById("processingMessage"),
    progressBar: document.getElementById("progressBar"),

    answerSection: document.getElementById("answerSection"),
    answerContent: document.getElementById("answerContent"),
    innerThought: document.getElementById("innerThought"),

    confidence: document.getElementById("confidence"),
    topic: document.getElementById("topic"),
    answerType: document.getElementById("answerType"),

    languageBadge: document.getElementById("languageBadge"),
    moodBadge: document.getElementById("moodBadge"),
    personalityBadge: document.getElementById("personalityBadge"),

    anotherButton: document.getElementById("anotherButton"),
    copyButton: document.getElementById("copyButton"),

    quickPrompts: document.querySelectorAll(".quick-prompt")
};


const state = {
    question: "",
    result: null,
    processingTimer: null,
    processingStart: 0,
    processingDuration: 1350
};


/* =========================================================
   BASIC HELPERS
========================================================= */

function pick(items) {
    if (!Array.isArray(items) || items.length === 0) {
        return "";
    }

    return items[Math.floor(Math.random() * items.length)];
}


function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
}


function normalize(text) {
    return String(text || "")
        .normalize("NFKC")
        .trim()
        .toLowerCase()
        .replace(/\s+/g, " ")
        .replace(/[!?.,;:]+$/g, "")
        .trim();
}


function escapeHTML(value) {
    return String(value || "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


function splitSentences(text) {
    return String(text || "")
        .split(/(?<=[.!?।])\s+/)
        .map(item => item.trim())
        .filter(Boolean);
}


function paragraphHTML(text) {
    const sentences = splitSentences(text);

    if (!sentences.length) {
        return "";
    }

    return sentences
        .map(sentence => `<p>${escapeHTML(sentence)}</p>`)
        .join("");
}


/* =========================================================
   LANGUAGE DETECTION
========================================================= */

function detectLanguage(text) {

    const value = String(text || "");

    /*
        Any Devanagari input immediately activates Hindi.
    */
    if (/[\u0900-\u097F]/.test(value)) {
        return "hi";
    }

    const normalized = normalize(value);

    const hindiWords = Array.isArray(brain.hindi_detection)
        ? brain.hindi_detection
        : [
            "kya",
            "kyun",
            "kyon",
            "kaise",
            "kab",
            "kahan",
            "kaun",
            "hai",
            "ho",
            "mujhe",
            "mera",
            "meri",
            "mere",
            "aap",
            "tum",
            "batao",
            "bataiye",
            "chahiye",
            "sakta",
            "sakti",
            "karu",
            "karna",
            "kyu"
        ];

    const words = normalized.split(/\s+/);

    let score = 0;

    for (const word of words) {
        if (hindiWords.includes(word)) {
            score += 1;
        }
    }

    return score >= 1 ? "hi" : "en";
}


/* =========================================================
   TOPIC DETECTION
========================================================= */

function detectTopic(text, language) {

    const normalized = normalize(text);

    const topics = brain.topics || {};

    let bestTopic = null;
    let bestScore = 0;

    for (const [topicId, topic] of Object.entries(topics)) {

        const keywords = [
            ...(topic.keywords?.en || []),
            ...(topic.keywords?.hi || [])
        ];

        let score = 0;

        for (const keyword of keywords) {

            const cleanKeyword = normalize(keyword);

            if (!cleanKeyword) {
                continue;
            }

            if (normalized.includes(cleanKeyword)) {
                score += cleanKeyword.includes(" ")
                    ? 3
                    : 1;
            }
        }

        if (score > bestScore) {
            bestScore = score;
            bestTopic = topicId;
        }
    }

    return bestTopic || "general";
}


/* =========================================================
   QUESTION TYPE
========================================================= */

function detectQuestionType(text) {

    const value = normalize(text);

    if (
        /^(why|why is|why are|why do|why does|why am|why did)\b/.test(value) ||
        /^(क्यों|क्यूँ|क्यूं)\b/.test(value)
    ) {
        return "why";
    }

    if (
        /^(how|how do|how can|how should|how much|how many)\b/.test(value) ||
        /^(कैसे|कितना|कितने|कितनी)\b/.test(value)
    ) {
        return "how";
    }

    if (
        /^(what|what is|what are|what should)\b/.test(value) ||
        /^(क्या|कौन सा|कौन सी|कौन से)\b/.test(value)
    ) {
        return "what";
    }

    if (
        /^(should|should i|should we)\b/.test(value) ||
        /\bकरना चाहिए\b/.test(value) ||
        /\bकरूं\b/.test(value)
    ) {
        return "should";
    }

    if (
        /^(can|can i|can we|could)\b/.test(value) ||
        /\bसकता\b/.test(value) ||
        /\bसकती\b/.test(value) ||
        /\bसकते\b/.test(value)
    ) {
        return "can";
    }

    if (
        /^(when|when should|when will)\b/.test(value) ||
        /^(कब)\b/.test(value)
    ) {
        return "when";
    }

    if (
        /^(where|where is|where can)\b/.test(value) ||
        /^(कहाँ|कहां)\b/.test(value)
    ) {
        return "where";
    }

    if (
        /^(who|who is|who are)\b/.test(value) ||
        /^(कौन)\b/.test(value)
    ) {
        return "who";
    }

    if (
        /^(is|are|am|do|does|did|will|was|were|has|have|can|could)\b/.test(value) ||
        /^(क्या|है|हैं)\b/.test(value)
    ) {
        return "yesno";
    }

    return "general";
}


/* =========================================================
   SPECIAL CASES
========================================================= */

function findSpecialCase(text) {

    const normalized = normalize(text);

    const specialCases = brain.special_cases || {};

    for (const [key, data] of Object.entries(specialCases)) {

        if (normalized === normalize(key)) {
            return data;
        }
    }

    return null;
}


/* =========================================================
   PERSONALITY / MOOD
========================================================= */

function choosePersonality() {
    return pick(brain.personalities || []);
}


function chooseMood() {
    return pick(brain.moods || []);
}


/* =========================================================
   TEXT SELECTION
========================================================= */

function localized(data, language) {

    if (!data) {
        return "";
    }

    if (typeof data === "string") {
        return data;
    }

    return data[language] || data.en || "";
}


function getTopicAnswer(topicId, language) {

    const topic = brain.topics?.[topicId];

    if (!topic) {
        return "";
    }

    return pick(topic.answers?.[language] || topic.answers?.en || []);
}


function getQuestionPattern(type, language) {

    const pattern = brain.question_patterns?.[type];

    if (!pattern) {
        return "";
    }

    return pick(pattern[language] || pattern.en || []);
}


function getFallback(language) {

    const list = brain.fallbacks?.[language] || brain.fallbacks?.en || [];

    return pick(list);
}


/* =========================================================
   COMPOSITION
========================================================= */

function composeResult(question) {

    const language = detectLanguage(question);

    const special = findSpecialCase(question);

    const topic = detectTopic(question, language);
    const questionType = detectQuestionType(question);

    const personality = choosePersonality();
    const mood = chooseMood();

    let coreAnswer = "";

    if (special) {

        coreAnswer = pick(
            special[language] ||
            special.en ||
            []
        );

    } else if (topic !== "general") {

        coreAnswer = getTopicAnswer(topic, language);

    } else {

        coreAnswer = getQuestionPattern(
            questionType,
            language
        );

        if (!coreAnswer) {
            coreAnswer = getFallback(language);
        }
    }


    if (!coreAnswer) {
        coreAnswer = getFallback(language);
    }


    const personalityIntro = pick(
        personality?.intro?.[language] ||
        personality?.intro?.en ||
        []
    );


    const moodIntro = pick(
        mood?.intro?.[language] ||
        mood?.intro?.en ||
        []
    );


    const sarcasmChance = Math.random();

    let sarcasm = "";

    if (sarcasmChance < 0.72) {

        sarcasm = pick(
            brain.sarcasm?.[language] ||
            brain.sarcasm?.en ||
            []
        );
    }


    const darkChance = Math.random();

    let darkHumor = "";

    if (darkChance < 0.34) {

        darkHumor = pick(
            brain.dark_humor?.[language] ||
            brain.dark_humor?.en ||
            []
        );
    }


    const ending = pick(
        mood?.ending?.[language] ||
        mood?.ending?.en ||
        []
    );


    const personalityEnding = pick(
        personality?.ending?.[language] ||
        personality?.ending?.en ||
        []
    );


    const emojiPool = [
        ...(personality?.emoji || []),
        ...(mood?.emoji || []),
        ...(brain.emojis?.[language] || brain.emojis?.en || [])
    ];

    const emoji = pick(emojiPool);


    const parts = [
        personalityIntro,
        moodIntro,
        coreAnswer,
        sarcasm,
        darkHumor,
        ending,
        personalityEnding
    ].filter(Boolean);


    /*
        Keep answers reasonably compact.
    */
    const selectedParts = [];

    for (const part of parts) {

        if (!selectedParts.includes(part)) {
            selectedParts.push(part);
        }

        if (selectedParts.length >= 5) {
            break;
        }
    }


    let answer = selectedParts.join(" ");


    if (emoji && Math.random() < 0.75) {
        answer += ` ${emoji}`;
    }


    const thought = pick(
        [
            ...(personality?.thoughts?.[language] || personality?.thoughts?.en || []),
            ...(mood?.thoughts?.[language] || mood?.thoughts?.en || []),
            ...(brain.inner_monologue?.[language] || brain.inner_monologue?.en || [])
        ]
    );


    const confidenceBase = 91 + Math.random() * 8.7;

    const confidence = `${confidenceBase.toFixed(1)}%`;


    let answerType = "QUESTIONABLE";

    if (special) {
        answerType = "SPECIAL CASE";
    } else if (questionType === "why") {
        answerType = "UNNECESSARY EXPLANATION";
    } else if (questionType === "how") {
        answerType = "SUSPICIOUS GUIDANCE";
    } else if (questionType === "should") {
        answerType = "UNSOLICITED OPINION";
    } else if (questionType === "yesno") {
        answerType = "CONFIDENT GUESS";
    } else if (topic !== "general") {
        answerType = "QUESTIONABLE ANALYSIS";
    }


    return {
        question,
        language,
        topic,
        questionType,
        personality,
        mood,
        answer,
        thought,
        confidence,
        answerType
    };
}


/* =========================================================
   RENDER
========================================================= */

function renderResult(result) {

    elements.answerContent.innerHTML =
        paragraphHTML(result.answer);

    elements.innerThought.textContent =
        result.thought || "I probably shouldn't be thinking this.";

    elements.confidence.textContent =
        result.confidence;

    elements.topic.textContent =
        String(result.topic || "general").toUpperCase();

    elements.answerType.textContent =
        result.answerType;

    elements.languageBadge.textContent =
        result.language === "hi"
            ? "हिंदी"
            : "ENGLISH";

    elements.moodBadge.textContent =
        result.mood?.name?.toUpperCase() || "UNSTABLE";

    elements.personalityBadge.textContent =
        result.personality?.name?.toUpperCase() || "MACHINE";


    elements.answerContent.dir =
        result.language === "hi"
            ? "auto"
            : "ltr";

    elements.innerThought.dir = "auto";

    document.documentElement.lang =
        result.language === "hi"
            ? "hi"
            : "en";
}


/* =========================================================
   PROCESSING
========================================================= */

function getProcessingMessages(language) {

    if (language === "hi") {

        return [
            "प्रश्न को जरूरत से ज्यादा गंभीरता से लिया जा रहा है...",
            "अत्यधिक सोचने की प्रक्रिया शुरू...",
            "संदिग्ध विशेषज्ञों से सलाह ली जा रही है...",
            "आत्मविश्वास का स्तर अनावश्यक रूप से बढ़ाया जा रहा है...",
            "लगभग बेवजह तैयार..."
        ];

    }

    return [
        "Taking your question far too seriously...",
        "Activating unnecessary analysis...",
        "Consulting suspicious experts...",
        "Increasing confidence without justification...",
        "Almost unnecessarily ready..."
    ];
}


function startProcessing(question) {

    clearInterval(state.processingTimer);

    state.question = question;

    elements.landingPage.classList.add("hidden");
    elements.answerSection.classList.add("hidden");
    elements.processingCard.classList.remove("hidden");

    elements.askButton.disabled = true;

    elements.progressBar.style.width = "0%";
    elements.processingPercent.textContent = "0%";

    const language = detectLanguage(question);

    const messages = getProcessingMessages(language);

    state.processingStart = performance.now();

    let lastMessageIndex = -1;


    function tick(now) {

        const elapsed = now - state.processingStart;

        const progress = clamp(
            elapsed / state.processingDuration,
            0,
            1
        );

        const percent = Math.round(progress * 100);

        elements.progressBar.style.width =
            `${percent}%`;

        elements.processingPercent.textContent =
            `${percent}%`;


        const messageIndex = Math.min(
            messages.length - 1,
            Math.floor(progress * messages.length)
        );


        if (messageIndex !== lastMessageIndex) {

            elements.processingMessage.textContent =
                messages[messageIndex];

            lastMessageIndex = messageIndex;
        }


        if (progress < 1) {

            state.processingTimer =
                requestAnimationFrame(tick);

        } else {

            finishProcessing(question);
        }
    }


    state.processingTimer =
        requestAnimationFrame(tick);
}


function finishProcessing(question) {

    clearInterval(state.processingTimer);

    state.result = composeResult(question);

    renderResult(state.result);

    elements.processingCard.classList.add("hidden");
    elements.answerSection.classList.remove("hidden");

    elements.askButton.disabled = false;

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


/* =========================================================
   ASK
========================================================= */

function askQuestion() {

    const question = elements.question.value.trim();

    if (!question) {

        elements.question.focus();

        return;
    }

    startProcessing(question);
}


/* =========================================================
   RESET
========================================================= */

function resetApplication() {

    clearInterval(state.processingTimer);

    state.question = "";
    state.result = null;

    elements.question.value = "";

    updateCharacterCount();

    elements.processingCard.classList.add("hidden");
    elements.answerSection.classList.add("hidden");
    elements.landingPage.classList.remove("hidden");

    elements.askButton.disabled = false;

    elements.progressBar.style.width = "0%";
    elements.processingPercent.textContent = "0%";

    document.documentElement.lang = "en";

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    setTimeout(() => {
        elements.question.focus();
    }, 250);
}


/* =========================================================
   CHARACTER COUNT
========================================================= */

function updateCharacterCount() {

    const length =
        elements.question.value.length;

    elements.characterCount.textContent =
        `${length} ${length === 1 ? "character" : "characters"}`;
}


/* =========================================================
   COPY
========================================================= */

async function copyAnswer() {

    if (!state.result) {
        return;
    }

    const text = [
        "ANSWER MACHINE",
        "",
        state.result.answer,
        "",
        `Inner Monologue: ${state.result.thought}`,
        "",
        `Personality: ${state.result.personality?.name || ""}`,
        `Mood: ${state.result.mood?.name || ""}`
    ].join("\n");


    try {

        await navigator.clipboard.writeText(text);

        const original =
            elements.copyButton.textContent;

        elements.copyButton.textContent =
            "COPIED ✓";

        setTimeout(() => {
            elements.copyButton.textContent =
                original;
        }, 1400);

    } catch {

        /*
            Fallback for browsers where Clipboard API
            is unavailable.
        */

        const temporary =
            document.createElement("textarea");

        temporary.value = text;

        document.body.appendChild(temporary);

        temporary.select();

        document.execCommand("copy");

        temporary.remove();

        elements.copyButton.textContent =
            "COPIED ✓";

        setTimeout(() => {
            elements.copyButton.textContent =
                "COPY ANSWER";
        }, 1400);
    }
}


/* =========================================================
   QUICK PROMPTS
========================================================= */

function setupQuickPrompts() {

    elements.quickPrompts.forEach(button => {

        button.addEventListener("click", () => {

            const prompt =
                button.dataset.prompt || "";

            elements.question.value =
                prompt;

            updateCharacterCount();

            startProcessing(prompt);
        });
    });
}


/* =========================================================
   EVENTS
========================================================= */

elements.logoButton.addEventListener(
    "click",
    resetApplication
);


elements.askButton.addEventListener(
    "click",
    askQuestion
);


elements.anotherButton.addEventListener(
    "click",
    () => {

        if (!state.question) {
            resetApplication();
            return;
        }

        elements.answerSection.classList.add("hidden");

        startProcessing(state.question);
    }
);


elements.copyButton.addEventListener(
    "click",
    copyAnswer
);


elements.question.addEventListener(
    "input",
    updateCharacterCount
);


elements.question.addEventListener(
    "keydown",
    event => {

        if (
            (event.ctrlKey || event.metaKey) &&
            event.key === "Enter"
        ) {
            event.preventDefault();

            askQuestion();
        }
    }
);


/* =========================================================
   INITIALIZE
========================================================= */

setupQuickPrompts();
updateCharacterCount();

if (!brain || !brain.topics) {
    console.warn(
        "ANSWER MACHINE: brain.js was not loaded."
    );
}
