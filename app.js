"use strict";

const brain = window.BRAIN;

const input = document.getElementById("questionInput");
const askButton = document.getElementById("askButton");
const anotherButton = document.getElementById("anotherButton");
const answerCard = document.getElementById("answerCard");
const answerContent = document.getElementById("answerContent");
const processing = document.getElementById("processing");
const processingText = document.getElementById("processingText");
const progressBar = document.getElementById("progressBar");
const confidenceElement = document.getElementById("confidence");
const topicDetected = document.getElementById("topicDetected");
const answerStatus = document.getElementById("answerStatus");
const charCount = document.getElementById("charCount");

const processingMessages = [
    "Analyzing question...",
    "Checking available nonsense...",
    "Consulting imaginary experts...",
    "Ignoring common sense...",
    "Performing unnecessary calculations...",
    "Asking a pigeon for verification...",
    "Constructing confident response...",
    "Removing useful information...",
    "Increasing confidence...",
    "Finalizing questionable conclusion..."
];

let isThinking = false;


/* =========================
   BASIC UTILITIES
========================= */

function randomItem(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function normalize(text) {
    return text
        .toLowerCase()
        .replace(/[^\p{L}\p{N}\s+]/gu, " ")
        .replace(/\s+/g, " ")
        .trim();
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function containsPhrase(text, phrase) {
    return text.includes(phrase);
}


/* =========================
   CHARACTER COUNTER
========================= */

input.addEventListener("input", () => {
    charCount.textContent = input.value.length;
});


/* =========================
   QUESTION TYPE
========================= */

function detectQuestionType(question) {

    const text = normalize(question);

    if (
        text.startsWith("why ") ||
        text === "why" ||
        text.includes(" why ")
    ) {
        return "why";
    }

    if (
        text.startsWith("how ") ||
        text === "how" ||
        text.includes(" how ")
    ) {
        return "how";
    }

    if (
        text.startsWith("what ") ||
        text === "what" ||
        text.includes(" what ")
    ) {
        return "what";
    }

    if (
        text.startsWith("should ") ||
        text.includes(" should ")
    ) {
        return "should";
    }

    if (
        text.startsWith("can ") ||
        text.startsWith("could ") ||
        text.includes(" can i ") ||
        text.includes(" can you ")
    ) {
        return "can";
    }

    return null;
}


/* =========================
   TOPIC DETECTION
========================= */

function detectTopic(question) {

    const text = normalize(question);

    let bestTopic = "general";
    let bestScore = 0;

    for (const [topicName, topic] of Object.entries(brain.topics)) {

        let score = 0;

        for (const keyword of topic.keywords) {

            const normalizedKeyword = normalize(keyword);

            if (text.includes(normalizedKeyword)) {
                score += normalizedKeyword.length > 5 ? 3 : 1;
            }
        }

        if (score > bestScore) {
            bestScore = score;
            bestTopic = topicName;
        }
    }

    return bestTopic;
}


/* =========================
   SPECIAL CASES
========================= */

function checkSpecialCase(question) {

    const normalized = normalize(question);

    for (const [trigger, answers] of Object.entries(brain.special_cases)) {

        if (
            normalized === normalize(trigger) ||
            normalized.includes(normalize(trigger))
        ) {
            return randomItem(answers);
        }
    }

    return null;
}


/* =========================
   QUESTION-SPECIFIC OPENING
========================= */

function generateOpening(questionType) {

    if (
        questionType &&
        brain.question_patterns[questionType]
    ) {
        return randomItem(
            brain.question_patterns[questionType]
        );
    }

    return randomItem(brain.openings);
}


/* =========================
   ANSWER GENERATOR
========================= */

function generateAnswer(question) {

    const normalized = normalize(question);

    if (!normalized) {
        return {
            topic: "GENERAL",
            opening: "INPUT REQUIRED.",
            answer:
                "You have successfully asked me absolutely nothing.\n\n" +
                "This is impressive, but unfortunately difficult to answer.",
            thinking:
                "I searched the question for information and found an empty room.",
            ending: "Please provide at least one word.",
            confidence: "100%"
        };
    }


    const special = checkSpecialCase(question);

    if (special) {

        return {
            topic: "SPECIAL",
            opening: randomItem(brain.openings),
            answer: special,
            thinking: randomItem(brain.thinking),
            ending: randomItem(brain.endings),
            confidence: randomItem(brain.confidence)
        };
    }


    const topic = detectTopic(question);
    const questionType = detectQuestionType(question);

    let answer;

    if (
        topic !== "general" &&
        brain.topics[topic] &&
        brain.topics[topic].answers.length > 0
    ) {

        answer = randomItem(
            brain.topics[topic].answers
        );

    } else {

        answer = randomItem(brain.fallbacks);
    }


    const opening = generateOpening(questionType);

    const thinkingText = randomItem(brain.thinking);

    const ending = randomItem(brain.endings);

    let topicName = topic.toUpperCase();

    if (topic === "general") {
        topicName = "GENERAL";
    }


    /*
     * Occasionally add a question-specific
     * absurd conclusion.
     */

    const additions = [
        "This conclusion is supported by confidence.",
        "I have decided this is probably correct.",
        "The evidence is overwhelming if you don't inspect it.",
        "Further investigation would only introduce facts.",
        "I see no reason to complicate this with reality.",
        "This is the answer I would give under oath.",
        "Several imaginary experts agree with me.",
        "I will now stop before this becomes useful."
    ];


    if (Math.random() > 0.35) {
        answer += "\n\n" + randomItem(additions);
    }


    return {
        topic: topicName,
        opening,
        answer,
        thinking: thinkingText,
        ending,
        confidence: randomItem(brain.confidence)
    };
}


/* =========================
   DISPLAY ANSWER
========================= */

function renderAnswer(result) {

    confidenceElement.textContent =
        result.confidence;

    topicDetected.textContent =
        result.topic;

    answerContent.innerHTML = `
        <div class="opening">
            ${escapeHtml(result.opening)}
        </div>

        <div class="main-answer">
            ${escapeHtml(result.answer)}
        </div>

        <div class="thinking">
            ${escapeHtml(result.thinking)}
        </div>

        <div class="ending">
            ${escapeHtml(result.ending)}
        </div>
    `;
}


/* =========================
   PROCESSING ANIMATION
========================= */

function runProcessing(callback) {

    let progress = 0;
    let messageIndex = 0;

    processing.classList.remove("hidden");

    answerContent.classList.add("hidden");

    progressBar.style.width = "0%";

    processingText.textContent =
        processingMessages[0];


    const interval = setInterval(() => {

        progress += Math.floor(
            Math.random() * 11
        ) + 5;

        if (progress > 100) {
            progress = 100;
        }

        progressBar.style.width =
            `${progress}%`;


        if (
            progress >=
            (messageIndex + 1) *
            (100 / processingMessages.length)
        ) {

            messageIndex++;

            if (
                messageIndex <
                processingMessages.length
            ) {
                processingText.textContent =
                    processingMessages[messageIndex];
            }
        }


        if (progress >= 100) {

            clearInterval(interval);

            setTimeout(() => {

                processing.classList.add("hidden");
                answerContent.classList.remove("hidden");

                callback();

            }, 180);
        }

    }, 90);
}


/* =========================
   ASK
========================= */

function ask() {

    if (isThinking) {
        return;
    }

    const question = input.value.trim();

    if (!question) {

        input.focus();

        input.placeholder =
            "That was technically not a question.";

        setTimeout(() => {
            input.placeholder =
                "Why is the sky blue?";
        }, 1800);

        return;
    }


    isThinking = true;

    askButton.disabled = true;

    answerCard.classList.remove("hidden");

    answerStatus.textContent =
        "PROCESSING";

    answerCard.scrollIntoView({
        behavior: "smooth",
        block: "nearest"
    });


    runProcessing(() => {

        const result =
            generateAnswer(question);

        renderAnswer(result);

        answerStatus.textContent =
            "ANALYSIS COMPLETE";

        isThinking = false;

        askButton.disabled = false;

    });
}


/* =========================
   BUTTON EVENTS
========================= */

askButton.addEventListener(
    "click",
    ask
);

anotherButton.addEventListener(
    "click",
    () => {

        input.value = "";

        charCount.textContent = "0";

        answerCard.classList.add("hidden");

        input.focus();

    }
);


/* =========================
   ENTER KEY
========================= */

input.addEventListener(
    "keydown",
    event => {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            ask();
        }
    }
);


/* =========================
   QUICK PROMPTS
========================= */

document.querySelectorAll(".prompt").forEach(button => {

    button.addEventListener(
        "click",
        () => {

            input.value =
                button.dataset.question;

            charCount.textContent =
                input.value.length;

            input.focus();

            ask();
        }
    );

});


/* =========================
   INITIAL STATE
========================= */

input.focus();
