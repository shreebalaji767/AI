(() => {
    "use strict";

    const brain = window.BRAIN;

    if (!brain) {
        console.error("ANSWER MACHINE: brain.js was not loaded.");
        return;
    }

    const $ = (id) => document.getElementById(id);

    const el = {
        logoButton: $("logoButton"),
        question: $("question"),
        characterCount: $("characterCount"),
        askButton: $("askButton"),
        anotherButton: $("anotherButton"),

        processingCard: $("processingCard"),
        processingPercent: $("processingPercent"),
        processingMessage: $("processingMessage"),
        progressBar: $("progressBar"),

        answerSection: $("answerSection"),
        answerContent: $("answerContent"),
        innerThought: $("innerThought"),
        personality: $("personality"),
        mood: $("mood"),
        confidence: $("confidence"),
        topic: $("topic"),
        answerType: $("answerType"),
        language: $("language"),
        answerEmoji: $("answerEmoji"),

        quickPrompts: document.querySelectorAll(".quick-prompt")
    };

    let processingCancelled = false;
    let lastQuestion = "";
    let lastResult = null;

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    function randomItem(list) {
        if (!Array.isArray(list) || list.length === 0) {
            return "";
        }

        return list[Math.floor(Math.random() * list.length)];
    }

    function clamp(value, min, max) {
        return Math.min(Math.max(value, min), max);
    }

    function normalize(text) {
        return String(text || "")
            .toLowerCase()
            .replace(/[“”"']/g, "")
            .replace(/[!?.,;:।]+$/g, "")
            .replace(/\s+/g, " ")
            .trim();
    }

    // ============================================================
    // LANGUAGE
    // ============================================================

    function languageOf(text) {
        if (!text.trim()) {
            return "English";
        }

        const hindiChars =
            (text.match(/[\u0900-\u097F]/g) || []).length;

        const latinChars =
            (text.match(/[A-Za-z]/g) || []).length;

        if (hindiChars > 0 && hindiChars >= latinChars * 0.15) {
            return "Hindi";
        }

        return "English";
    }

    // ============================================================
    // SPECIAL CASES
    // ============================================================

    function findSpecial(question, language) {
        const key = normalize(question);

        const source =
            language === "Hindi"
                ? brain.hindi?.special_cases
                : brain.special_cases;

        if (!source) {
            return null;
        }

        if (source[key]) {
            return randomItem(source[key]);
        }

        return null;
    }

    // ============================================================
    // TOPIC DETECTION
    // ============================================================

    function detectTopic(question) {
        const text = normalize(question);

        let bestTopic = null;
        let bestScore = 0;

        for (const [topic, data] of Object.entries(brain.topics || {})) {
            let score = 0;

            for (const keyword of data.keywords || []) {
                const k = normalize(keyword);

                if (!k) {
                    continue;
                }

                if (text === k) {
                    score += 5;
                } else if (text.includes(` ${k} `)) {
                    score += 3;
                } else if (text.includes(k)) {
                    score += 2;
                }
            }

            if (score > bestScore) {
                bestScore = score;
                bestTopic = topic;
            }
        }

        return bestTopic || "general";
    }

    // ============================================================
    // QUESTION TYPE
    // ============================================================

    function detectQuestionType(question, language) {
        const text = normalize(question);

        if (language === "Hindi") {
            if (
                /^क्यों\b/.test(text) ||
                text.includes(" क्यों ")
            ) {
                return "why";
            }

            if (
                /^कैसे\b/.test(text) ||
                text.includes(" कैसे ")
            ) {
                return "how";
            }

            if (
                /^क्या\b/.test(text) ||
                text.includes(" क्या ")
            ) {
                return "what";
            }

            if (
                /^कब\b/.test(text) ||
                text.includes(" कब ")
            ) {
                return "when";
            }

            if (
                /^कहाँ\b/.test(text) ||
                /^कहां\b/.test(text) ||
                text.includes(" कहाँ ") ||
                text.includes(" कहां ")
            ) {
                return "where";
            }

            if (
                /^कौन\b/.test(text) ||
                text.includes(" कौन ")
            ) {
                return "who";
            }

            if (
                text.includes("चाहिए") ||
                text.includes("मुझे करना चाहिए")
            ) {
                return "should";
            }

            if (
                text.includes("क्या मैं") ||
                text.includes("क्या हम") ||
                text.includes("क्या तुम")
            ) {
                return "can";
            }

            return "general";
        }

        if (
            /^why\b/.test(text) ||
            text.includes(" why ")
        ) {
            return "why";
        }

        if (
            /^how\b/.test(text) ||
            text.includes(" how ")
        ) {
            return "how";
        }

        if (
            /^what\b/.test(text) ||
            text.includes(" what ")
        ) {
            return "what";
        }

        if (
            /^when\b/.test(text) ||
            text.includes(" when ")
        ) {
            return "when";
        }

        if (
            /^where\b/.test(text) ||
            text.includes(" where ")
        ) {
            return "where";
        }

        if (
            /^who\b/.test(text) ||
            text.includes(" who ")
        ) {
            return "who";
        }

        if (
            /^should\b/.test(text) ||
            text.includes(" should ")
        ) {
            return "should";
        }

        if (
            /^can\b/.test(text) ||
            text.includes(" can ")
        ) {
            return "can";
        }

        return "general";
    }

    // ============================================================
    // PERSONALITY
    // ============================================================

    function choosePersonality(question) {
        const text = normalize(question);

        if (
            /code|coding|programming|python|javascript|html|css|github|programmer|कोड|प्रोग्रामिंग|पाइथन/
                .test(text)
        ) {
            if (Math.random() < 0.58) {
                return brain.personalities.find(
                    p => p.id === "genius"
                );
            }
        }

        if (
            /love|relationship|girlfriend|boyfriend|marriage|dating|प्यार|रिश्ता|शादी/
                .test(text)
        ) {
            if (Math.random() < 0.45) {
                return brain.personalities.find(
                    p => p.id === "sarcastic"
                );
            }
        }

        if (
            /meaning|life|existence|universe|purpose|जीवन|अर्थ|ब्रह्मांड|जिंदगी/
                .test(text)
        ) {
            if (Math.random() < 0.60) {
                return brain.personalities.find(
                    p => p.id === "existential"
                );
            }
        }

        return randomItem(brain.personalities);
    }

    // ============================================================
    // MOOD SWINGS
    // ============================================================

    function chooseMood(personality, question) {
        const moods = [...(brain.moods || [])];
        const text = normalize(question);

        if (
            /why|क्यों|meaning|life|existence|जीवन|अर्थ/
                .test(text)
        ) {
            const philosophical =
                moods.find(m => m.id === "philosophical");

            if (
                philosophical &&
                Math.random() < 0.48
            ) {
                return philosophical;
            }
        }

        if (
            /stupid|idiot|hate|बेवकूफ|नफरत/
                .test(text)
        ) {
            const judgmental =
                moods.find(m => m.id === "judgmental");

            if (judgmental) {
                return judgmental;
            }
        }

        if (personality?.id === "chaos") {
            const chaotic =
                moods.find(m => m.id === "chaotic");

            if (
                chaotic &&
                Math.random() < 0.7
            ) {
                return chaotic;
            }
        }

        return randomItem(moods);
    }

    // ============================================================
    // CORE ANSWER
    // ============================================================

    function selectCoreAnswer(
        question,
        language,
        topic,
        type
    ) {
        const special =
            findSpecial(question, language);

        if (special) {
            return {
                text: special,
                answerType: "SPECIAL",
                topic: "SPECIAL",
                special: true
            };
        }

        if (language === "Hindi") {
            const topicAnswers =
                brain.hindi?.topics?.[topic];

            if (topicAnswers?.length) {
                return {
                    text: randomItem(topicAnswers),
                    answerType: "TOPIC",
                    topic,
                    special: false
                };
            }

            const patternAnswers =
                brain.hindi?.question_patterns?.[type];

            if (patternAnswers?.length) {
                return {
                    text: randomItem(patternAnswers),
                    answerType: type.toUpperCase(),
                    topic: "GENERAL",
                    special: false
                };
            }

            return {
                text: randomItem(
                    brain.hindi?.fallbacks ||
                    brain.fallbacks
                ),
                answerType: "GENERAL",
                topic: "GENERAL",
                special: false
            };
        }

        const topicAnswers =
            brain.topics?.[topic]?.answers;

        if (topicAnswers?.length) {
            return {
                text: randomItem(topicAnswers),
                answerType: "TOPIC",
                topic,
                special: false
            };
        }

        const patternAnswers =
            brain.question_patterns?.[type];

        if (patternAnswers?.length) {
            return {
                text: randomItem(patternAnswers),
                answerType: type.toUpperCase(),
                topic: "GENERAL",
                special: false
            };
        }

        return {
            text: randomItem(brain.fallbacks),
            answerType: "GENERAL",
            topic: "GENERAL",
            special: false
        };
    }

    // ============================================================
    // ANSWER DECORATION
    // ============================================================

    function decorateAnswer(
        core,
        personality,
        mood,
        language
    ) {
        if (core.special) {
            return core.text;
        }

        let personalityIntro =
            randomItem(personality?.intros || []);

        let moodPrefix =
            mood?.prefix || "";

        const emoji =
            randomItem(
                brain.emoji_sets?.[
                    personality?.style
                ] ||
                brain.emoji_sets?.confident ||
                ["🤖"]
            );

        if (language === "Hindi") {
            const hindiIntros = {
                professor:
                    "चलिए इसे थोड़ी अनावश्यक अकादमिक गंभीरता से देखते हैं।",

                genius:
                    "जाहिर है, इसका जवाब मुझे पहले से पता है।",

                chaos:
                    "ओह! बढ़िया। अब यह मज़ेदार होने वाला है।",

                tired:
                    "ठीक है। इसे भी निपटा देते हैं।",

                corporate:
                    "आपके प्रश्न को रणनीतिक अवसर में सफलतापूर्वक बदल दिया गया है।",

                suspicious:
                    "हम्म। आपके सवाल में कुछ संदिग्ध है।",

                existential:
                    "आह। फिर एक सवाल जो छोटी-सी मानव जिंदगी ने ब्रह्मांड के सामने रख दिया।",

                sarcastic:
                    "बिल्कुल। चलिए इसे ऐसे समझाते हैं जैसे यह बहुत सामान्य सवाल हो।",

                zen:
                    "शांत रहें। जवाब आने दीजिए। शायद।",

                dark:
                    "बहुत अच्छा। इसमें थोड़ी अंधेरी हास्य-ऊर्जा जोड़ते हैं।"
            };

            personalityIntro =
                hindiIntros[
                    personality?.id
                ] ||
                personalityIntro;

            if (mood?.prefix) {
                moodPrefix =
                    `मूड अपडेट: ${mood.prefix}`;
            }
        }

        const opening =
            randomItem(brain.openings);

        const thinking =
            randomItem(brain.thinking);

        const ending =
            randomItem(
                personality?.closings ||
                brain.endings
            );

        const parts = [
            `${emoji} ${
                personalityIntro ||
                opening
            }`,

            moodPrefix
                ? `\n\n${moodPrefix}`
                : "",

            `\n\n${core.text}`,

            `\n\n${thinking}`,

            `\n\n${ending}`
        ];

        return parts
            .filter(Boolean)
            .join("");
    }

    // ============================================================
    // BUILD COMPLETE RESULT
    // ============================================================

    function buildResult(question) {
        const language =
            languageOf(question);

        const topic =
            detectTopic(question);

        const type =
            detectQuestionType(
                question,
                language
            );

        const personality =
            choosePersonality(question);

        const mood =
            chooseMood(
                personality,
                question
            );

        const core =
            selectCoreAnswer(
                question,
                language,
                topic,
                type
            );

        const answer =
            decorateAnswer(
                core,
                personality,
                mood,
                language
            );

        return {
            answer,

            innerThought:
                randomItem(
                    personality?.thoughts ||
                    [
                        "🧠 *I am thinking extremely hard. Probably.*"
                    ]
                ),

            personality,

            mood,

            confidence:
                randomItem(
                    brain.confidence
                ),

            topic:
                core.topic === "GENERAL"
                    ? "GENERAL"
                    : core.topic,

            answerType:
                core.answerType,

            language,

            emoji:
                personality?.emoji ||
                "🤖"
        };
    }

    // ============================================================
    // PROCESSING UI
    // ============================================================

    function setProgress(
        value,
        message
    ) {
        const safe =
            clamp(
                value,
                0,
                100
            );

        if (el.processingPercent) {
            el.processingPercent.textContent =
                `${Math.round(safe)}%`;
        }

        if (el.progressBar) {
            el.progressBar.style.width =
                `${safe}%`;
        }

        if (el.processingMessage) {
            el.processingMessage.textContent =
                message;
        }
    }

    async function fakeProcessing(language) {
        const messages =
            language === "Hindi"
                ? [
                    "सवाल पढ़ रहा हूँ... 👀",
                    "काल्पनिक डेटाबेस चेक हो रहा है... 🗄️",
                    "व्यक्तित्व चुना जा रहा है... 🎭",
                    "मूड अचानक बदल रहा है... 🌪️",
                    "आंतरिक विचारों की जाँच... 🧠",
                    "जवाब को अनावश्यक आत्मविश्वास दिया जा रहा है... 😎",
                    "लगभग तैयार... शायद।"
                ]
                : [
                    "Reading the question... 👀",
                    "Checking imaginary databases... 🗄️",
                    "Selecting a personality... 🎭",
                    "Mood swing detected... 🌪️",
                    "Inspecting internal thoughts... 🧠",
                    "Adding unnecessary confidence... 😎",
                    "Almost ready... probably."
                ];

        el.processingCard
            ?.classList
            .remove("hidden");

        el.answerSection
            ?.classList
            .add("hidden");

        processingCancelled = false;

        for (
            let i = 0;
            i < messages.length;
            i++
        ) {
            if (processingCancelled) {
                return false;
            }

            setProgress(
                Math.round(
                    ((i + 1) /
                        messages.length) *
                    100
                ),
                messages[i]
            );

            await sleep(
                280 +
                Math.random() * 240
            );
        }

        return !processingCancelled;
    }

    // ============================================================
    // RENDER
    // ============================================================

    function formatAnswer(text) {
        return String(text || "")
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/\n\n/g, "<br><br>")
            .replace(/\n/g, "<br>");
    }

    function renderResult(result) {
        if (!result) {
            return;
        }

        el.answerContent.innerHTML =
            formatAnswer(result.answer);

        el.innerThought.textContent =
            result.innerThought;

        el.personality.textContent =
            `${result.personality.emoji} ${result.personality.name}`;

        el.mood.textContent =
            `${result.mood.emoji} ${result.mood.name}`;

        el.confidence.textContent =
            result.confidence;

        el.topic.textContent =
            result.topic;

        el.answerType.textContent =
            result.answerType;

        el.language.textContent =
            result.language;

        el.answerEmoji.textContent =
            result.emoji;

        el.answerSection
            .classList
            .remove("hidden");

        requestAnimationFrame(() => {
            el.answerSection.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        });
    }

    // ============================================================
    // ASK
    // ============================================================

    async function askQuestion(
        questionOverride = null
    ) {
        const question =
            String(
                questionOverride !== null
                    ? questionOverride
                    : el.question.value
            ).trim();

        if (!question) {
            el.question.focus();

            el.question.classList.add(
                "shake"
            );

            setTimeout(() => {
                el.question.classList.remove(
                    "shake"
                );
            }, 450);

            return;
        }

        lastQuestion = question;
        lastResult = null;

        el.askButton.disabled = true;
        el.anotherButton.disabled = true;
        el.question.disabled = true;

        el.answerSection
            .classList
            .add("hidden");

        const language =
            languageOf(question);

        const completed =
            await fakeProcessing(
                language
            );

        if (!completed) {
            return;
        }

        lastResult =
            buildResult(question);

        el.processingCard
            .classList
            .add("hidden");

        renderResult(lastResult);

        el.askButton.disabled = false;
        el.anotherButton.disabled = false;
        el.question.disabled = false;
    }

    // ============================================================
    // ANOTHER ANSWER
    // ============================================================

    function anotherAnswer() {
        if (!lastQuestion) {
            el.question.focus();
            return;
        }

        const result =
            buildResult(
                lastQuestion
            );

        lastResult = result;

        renderResult(result);
    }

    // ============================================================
    // RESET
    // ============================================================

    function resetApplication() {
        processingCancelled = true;

        lastQuestion = "";
        lastResult = null;

        el.question.disabled = false;
        el.question.value = "";

        updateCharacterCount();

        el.processingCard
            .classList
            .add("hidden");

        el.answerSection
            .classList
            .add("hidden");

        setProgress(
            0,
            "Waiting for a questionable question..."
        );

        el.askButton.disabled = false;
        el.anotherButton.disabled = false;

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

        setTimeout(() => {
            el.question.focus();
        }, 350);
    }

    // ============================================================
    // CHARACTER COUNT
    // ============================================================

    function updateCharacterCount() {
        const count =
            el.question.value.length;

        if (el.characterCount) {
            el.characterCount.textContent =
                `${count} characters`;
        }
    }

    // ============================================================
    // EVENTS
    // ============================================================

    el.logoButton?.addEventListener(
        "click",
        resetApplication
    );

    el.askButton?.addEventListener(
        "click",
        () => askQuestion()
    );

    el.anotherButton?.addEventListener(
        "click",
        anotherAnswer
    );

    el.question?.addEventListener(
        "input",
        updateCharacterCount
    );

    el.question?.addEventListener(
        "keydown",
        event => {
            if (
                (event.ctrlKey ||
                    event.metaKey) &&
                event.key === "Enter"
            ) {
                event.preventDefault();
                askQuestion();
            }
        }
    );

    el.quickPrompts.forEach(
        button => {
            button.addEventListener(
                "click",
                () => {
                    const prompt =
                        button.dataset.prompt ||
                        button.textContent.trim();

                    el.question.value =
                        prompt;

                    updateCharacterCount();

                    askQuestion(prompt);
                }
            );
        }
    );

    // ============================================================
    // INITIAL STATE
    // ============================================================

    updateCharacterCount();

    setProgress(
        0,
        "Waiting for a questionable question..."
    );
})();
