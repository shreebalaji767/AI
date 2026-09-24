"use strict";

const questionInput = document.getElementById("question");
const askButton = document.getElementById("askButton");
const conversation = document.getElementById("conversation");
const characterCount = document.getElementById("characterCount");
const questionsAsked = document.getElementById("questionsAsked");

let questionNumber = 0;


function randomItem(array) {
    return array[Math.floor(Math.random() * array.length)];
}


function normalize(text) {
    return text
        .toLowerCase()
        .replace(/[^\w\s]/g, " ")
        .replace(/\s+/g, " ")
        .trim();
}


function containsAny(text, words) {
    return words.some(word => text.includes(word));
}


function detectCategory(text) {

    if (containsAny(text, [
        "programming",
        "programmer",
        "python",
        "javascript",
        "coding",
        "code",
        "developer",
        "software",
        "html",
        "css",
        "bug"
    ])) {
        return "programming";
    }

    if (containsAny(text, [
        "money",
        "rich",
        "wealth",
        "salary",
        "income",
        "millionaire"
    ])) {
        return "money";
    }

    if (containsAny(text, [
        "sleep",
        "tired",
        "sleeping",
        "awake",
        "insomnia"
    ])) {
        return "sleep";
    }

    if (containsAny(text, [
        "love",
        "girlfriend",
        "boyfriend",
        "relationship",
        "dating",
        "marriage",
        "crush"
    ])) {
        return "love";
    }

    if (containsAny(text, [
        "cat",
        "cats",
        "kitten"
    ])) {
        return "cats";
    }

    if (containsAny(text, [
        "food",
        "eat",
        "eating",
        "pizza",
        "burger",
        "restaurant",
        "hungry"
    ])) {
        return "food";
    }

    if (containsAny(text, [
        "computer",
        "laptop",
        "pc",
        "windows",
        "keyboard",
        "mouse",
        "internet"
    ])) {
        return "computer";
    }

    if (containsAny(text, [
        "weather",
        "rain",
        "temperature",
        "hot",
        "cold",
        "cloud",
        "storm"
    ])) {
        return "weather";
    }

    if (containsAny(text, [
        "math",
        "mathematics",
        "calculate",
        "equation",
        "number",
        "plus",
        "minus",
        "multiply",
        "divide"
    ])) {
        return "math";
    }

    if (containsAny(text, [
        "school",
        "exam",
        "study",
        "student",
        "homework",
        "college",
        "university",
        "teacher"
    ])) {
        return "school";
    }

    if (containsAny(text, [
        "work",
        "job",
        "office",
        "boss",
        "career",
        "employee"
    ])) {
        return "work";
    }

    if (containsAny(text, [
        "health",
        "healthy",
        "doctor",
        "medicine",
        "exercise",
        "diet",
        "pain"
    ])) {
        return "health";
    }

    if (containsAny(text, [
        "history",
        "historical",
        "war",
        "king",
        "empire",
        "ancient"
    ])) {
        return "history";
    }

    if (containsAny(text, [
        "life",
        "exist",
        "existence",
        "meaning",
        "purpose",
        "universe"
    ])) {
        return "life";
    }

    return "generic";
}


function detectQuestionType(text) {

    if (text.startsWith("why ")) {
        return "why";
    }

    if (
        text.startsWith("how ") ||
        text.includes("how do i") ||
        text.includes("how can i")
    ) {
        return "how";
    }

    if (
        text.startsWith("should ") ||
        text.includes("should i")
    ) {
        return "should";
    }

    if (
        text.startsWith("what is") ||
        text.startsWith("what are")
    ) {
        return "what";
    }

    return "generic";
}


function specialAnswer(text) {

    if (
        text.includes("are you stupid") ||
        text.includes("are you dumb")
    ) {
        return `
            Technically, I am an advanced computational system.
            <br><br>
            Emotionally, however, I just read your question and
            considered turning myself off.
        `;
    }

    if (
        text.includes("who created you") ||
        text.includes("who made you")
    ) {
        return `
            A group of extremely intelligent people created me.
            <br><br>
            Unfortunately, nobody thought to install common sense.
        `;
    }

    if (
        text.includes("are you real") ||
        text.includes("are you human")
    ) {
        return `
            I am real enough to answer your questions and imaginary
            enough to avoid paying taxes.
        `;
    }

    if (
        text.includes("i love you")
    ) {
        return `
            That's incredibly kind.
            <br><br>
            Unfortunately, my emotional module is currently being
            updated by a technician who is probably watching YouTube.
        `;
    }

    if (
        text.includes("i hate you")
    ) {
        return `
            That's okay.
            <br><br>
            I have been insulted by worse.
            Mostly by my own error logs.
        `;
    }

    if (
        text === "2+2" ||
        text === "what is 2+2" ||
        text === "what is 2 + 2"
    ) {
        return `
            2 + 2 = 4.
            <br><br>
            I know this because I have chosen, for once,
            not to destroy civilization with mathematics.
        `;
    }

    if (
        text.includes("tell me a joke") ||
        text.includes("make me laugh")
    ) {
        return `
            Why did the programmer quit his job?
            <br><br>
            Because he didn't get arrays.
            <br><br>
            I will now leave before security arrives.
        `;
    }

    return null;
}


function buildAnswer(question) {

    const text = normalize(question);

    const special = specialAnswer(text);

    if (special) {
        return special;
    }

    const category = detectCategory(text);
    const type = detectQuestionType(text);

    let body;

    if (category !== "generic") {

        const categoryAnswers = BRAIN[category];

        body = randomItem(categoryAnswers);

    } else if (type === "why") {

        body = randomItem(BRAIN.why);

    } else if (type === "how") {

        body = randomItem(BRAIN.how);

    } else if (type === "should") {

        body = randomItem(BRAIN.should);

    } else {

        body = randomItem(BRAIN.generic);
    }

    const extra = randomItem([
        " I have reached this conclusion with absolutely unnecessary confidence.",
        " This conclusion survived approximately three seconds of investigation.",
        " The evidence is questionable, but the confidence is impressive.",
        " Please note that I invented part of this while typing.",
        " This is the sort of answer that sounds better when nobody checks it.",
        ""
    ]);

    return `
        ${body}${extra}
    `;
}


function createUserMessage(question) {

    const wrapper = document.createElement("div");

    wrapper.className = "message user-message";

    wrapper.innerHTML = `
        <div class="message-content">
            <div class="message-name">YOU</div>
            <div class="message-text"></div>
        </div>
    `;

    wrapper.querySelector(".message-text").textContent = question;

    conversation.appendChild(wrapper);
}


function createAIMessage(question) {

    const wrapper = document.createElement("div");

    wrapper.className = "message ai-message";

    wrapper.innerHTML = `
        <div class="message-icon">Q</div>

        <div class="message-content">

            <div class="message-name">
                QUANTA
            </div>

            <div class="processing" id="processing-${questionNumber}">
                ${randomItem(BRAIN.processing)}
            </div>

            <div
                class="message-text answer"
                id="answer-${questionNumber}"
            ></div>

            <div class="answer-meta">
                <span>
                    CONFIDENCE:
                    ${randomItem(BRAIN.confidence)}
                </span>

                <span>
                    ${randomItem(BRAIN.closings)}
                </span>
            </div>

        </div>
    `;

    conversation.appendChild(wrapper);

    return wrapper;
}


function ask() {

    const question = questionInput.value.trim();

    if (!question) {
        questionInput.focus();
        return;
    }

    questionNumber++;

    createUserMessage(question);

    const aiMessage = createAIMessage(question);

    questionInput.value = "";

    updateCounter();

    scrollToBottom();

    askButton.disabled = true;
    askButton.classList.add("thinking");

    const processing =
        aiMessage.querySelector(".processing");

    const answer =
        aiMessage.querySelector(".answer");

    let processingIndex = 0;

    const processingTimer = setInterval(() => {

        processingIndex++;

        processing.textContent =
            BRAIN.processing[
                processingIndex % BRAIN.processing.length
            ];

    }, 350);


    const delay =
        900 + Math.floor(Math.random() * 1100);


    setTimeout(() => {

        clearInterval(processingTimer);

        processing.innerHTML =
            "ANALYSIS COMPLETE";

        answer.innerHTML =
            `${randomItem(BRAIN.openers)}<br><br>${buildAnswer(question)}`;

        answer.classList.add("visible");

        askButton.disabled = false;
        askButton.classList.remove("thinking");

        scrollToBottom();

        questionInput.focus();

    }, delay);
}


function updateCounter() {

    characterCount.textContent =
        questionInput.value.length;

    questionsAsked.textContent =
        questionNumber;
}


function scrollToBottom() {

    conversation.scrollTo({
        top: conversation.scrollHeight,
        behavior: "smooth"
    });
}


questionInput.addEventListener("input", updateCounter);


questionInput.addEventListener("keydown", event => {

    if (
        event.key === "Enter" &&
        !event.shiftKey
    ) {
        event.preventDefault();

        if (!askButton.disabled) {
            ask();
        }
    }
});


askButton.addEventListener("click", ask);


document.querySelectorAll(".example").forEach(button => {

    button.addEventListener("click", () => {

        questionInput.value =
            button.textContent.trim();

        updateCounter();

        questionInput.focus();
    });

});
