/* =========================================================
   ANSWER MACHINE
   Static browser-side answer engine

   No server
   No database
   No LocalStorage
   No API
   ========================================================= */


/* =========================================================
   ELEMENTS
   ========================================================= */

const questionInput = document.getElementById("question");
const characterCount = document.getElementById("characterCount");

const askButton = document.getElementById("askButton");
const anotherButton = document.getElementById("anotherButton");

const logoButton = document.getElementById("logoButton");

const processingCard = document.getElementById("processingCard");
const processingPercent = document.getElementById("processingPercent");
const processingMessage = document.getElementById("processingMessage");
const progressBar = document.getElementById("progressBar");

const answerSection = document.getElementById("answerSection");
const answerContent = document.getElementById("answerContent");

const confidenceElement = document.getElementById("confidence");
const topicElement = document.getElementById("topic");
const answerTypeElement = document.getElementById("answerType");

const quickPrompts = document.querySelectorAll(".quick-prompt");


/* =========================================================
   STATE
   ========================================================= */

let processingTimer = null;
let isProcessing = false;


/* =========================================================
   BRAIN
   ========================================================= */

const brain = window.BRAIN || {};


/* =========================================================
   FALLBACK DATA
   ========================================================= */

const fallbackBrain = {

    openings: [
        "After an extremely serious investigation, the answer is surprisingly simple.",
        "This has been analyzed by several highly questionable experts.",
        "The short answer is yes, although reality has made things unnecessarily complicated.",
        "There is actually a perfectly logical explanation for this.",
        "Scientists have spent years avoiding this exact question.",
        "The answer begins with one important fact that nobody asked for.",
        "This is easier to understand once you stop expecting the universe to make sense."
    ],

    endings: [
        "So that is basically the situation.",
        "And that is the scientifically convenient explanation.",
        "In conclusion, everything is probably fine.",
        "Therefore, the universe can continue operating normally.",
        "That is the answer. Please use it responsibly.",
        "And now you know something you cannot un-know.",
        "Nobody needs to investigate this any further."
    ],

    thinking: [
        "Thinking very hard...",
        "Consulting the imaginary experts...",
        "Looking for unnecessary evidence...",
        "Calculating something that probably matters...",
        "Checking the highly questionable database...",
        "Asking the internal committee...",
        "Making this sound more complicated than it is..."
    ],

    confidence: [
        91,
        94,
        97,
        99,
        87,
        96,
        98
    ],

    fallback: [
        "The available evidence strongly suggests that this is one of those situations where everyone pretends to understand what is happening.",
        "There are several possible explanations, but the most convenient one is also the most entertaining.",
        "Nobody has completely solved this problem yet, so the responsible approach is to sound extremely confident anyway.",
        "This appears to be caused by a combination of physics, human decisions, and at least one unnecessary complication.",
        "The answer depends on circumstances, timing, and how dramatically you describe the problem."
    ],

    topics: {},

    questionTypes: {},

    special: []

};


/* =========================================================
   MERGE GENERATED BRAIN WITH FALLBACK
   ========================================================= */

const data = {

    openings:
        Array.isArray(brain.openings)
            ? brain.openings
            : fallbackBrain.openings,

    endings:
        Array.isArray(brain.endings)
            ? brain.endings
            : fallbackBrain.endings,

    thinking:
        Array.isArray(brain.thinking)
            ? brain.thinking
            : fallbackBrain.thinking,

    confidence:
        Array.isArray(brain.confidence)
            ? brain.confidence
            : fallbackBrain.confidence,

    fallback:
        Array.isArray(brain.fallback)
            ? brain.fallback
            : fallbackBrain.fallback,

    topics:
        brain.topics || fallbackBrain.topics,

    questionTypes:
        brain.questionTypes || fallbackBrain.questionTypes,

    special:
        Array.isArray(brain.special)
            ? brain.special
            : fallbackBrain.special

};


/* =========================================================
   RANDOM HELPER
   ========================================================= */

function randomItem(array) {

    if (!Array.isArray(array) || array.length === 0) {
        return "";
    }

    return array[
        Math.floor(Math.random() * array.length)
    ];
}


/* =========================================================
   CLEAN TEXT
   ========================================================= */

function cleanQuestion(question) {

    return question
        .trim()
        .replace(/\s+/g, " ");

}


/* =========================================================
   TOPIC DETECTION
   ========================================================= */

function detectTopic(question) {

    const text = question.toLowerCase();

    let bestTopic = "GENERAL";
    let bestScore = 0;

    const topicKeywords = {

        PROGRAMMING: [
            "code",
            "coding",
            "program",
            "programming",
            "python",
            "javascript",
            "html",
            "css",
            "java",
            "c#",
            "software",
            "developer",
            "website",
            "bug",
            "computer"
        ],

        MONEY: [
            "money",
            "cash",
            "salary",
            "income",
            "rich",
            "poor",
            "bank",
            "loan",
            "investment",
            "invest",
            "price",
            "cost",
            "business"
        ],

        SLEEP: [
            "sleep",
            "tired",
            "sleeping",
            "insomnia",
            "dream",
            "nap",
            "awake"
        ],

        FOOD: [
            "food",
            "eat",
            "eating",
            "pizza",
            "burger",
            "rice",
            "bread",
            "chicken",
            "vegetable",
            "fruit",
            "hungry",
            "cook"
        ],

        ANIMALS: [
            "cat",
            "cats",
            "dog",
            "dogs",
            "animal",
            "animals",
            "bird",
            "fish",
            "lion",
            "tiger",
            "elephant",
            "pet"
        ],

        TECHNOLOGY: [
            "phone",
            "mobile",
            "internet",
            "wifi",
            "technology",
            "tech",
            "computer",
            "laptop",
            "ai",
            "robot",
            "screen",
            "app"
        ],

        SCHOOL: [
            "school",
            "college",
            "study",
            "student",
            "exam",
            "math",
            "mathematics",
            "homework",
            "teacher",
            "education",
            "learn"
        ],

        WEATHER: [
            "weather",
            "rain",
            "rainy",
            "sun",
            "sunny",
            "cloud",
            "cloudy",
            "temperature",
            "hot",
            "cold",
            "storm",
            "wind"
        ],

        RELATIONSHIPS: [
            "love",
            "relationship",
            "girlfriend",
            "boyfriend",
            "husband",
            "wife",
            "friend",
            "friendship",
            "marriage",
            "breakup",
            "crush"
        ],

        PHILOSOPHY: [
            "life",
            "meaning",
            "exist",
            "existence",
            "universe",
            "god",
            "purpose",
            "reality",
            "consciousness"
        ],

        HEALTH: [
            "health",
            "body",
            "exercise",
            "weight",
            "headache",
            "fever",
            "pain",
            "healthy",
            "medicine"
        ],

        HISTORY: [
            "history",
            "war",
            "king",
            "queen",
            "ancient",
            "empire",
            "historical",
            "country",
            "civilization"
        ]

    };


    for (const topic in topicKeywords) {

        let score = 0;

        for (const keyword of topicKeywords[topic]) {

            if (text.includes(keyword)) {
                score++;
            }

        }

        if (score > bestScore) {

            bestScore = score;
            bestTopic = topic;

        }

    }


    return bestTopic;

}


/* =========================================================
   QUESTION TYPE
   ========================================================= */

function detectQuestionType(question) {

    const text = question.toLowerCase().trim();

    if (/^why\b/.test(text)) {
        return "WHY";
    }

    if (/^how\b/.test(text)) {
        return "HOW";
    }

    if (/^what\b/.test(text)) {
        return "WHAT";
    }

    if (/^when\b/.test(text)) {
        return "WHEN";
    }

    if (/^where\b/.test(text)) {
        return "WHERE";
    }

    if (/^who\b/.test(text)) {
        return "WHO";
    }

    if (/^should\b/.test(text)) {
        return "SHOULD";
    }

    if (/^can\b/.test(text)) {
        return "CAN";
    }

    if (/^is\b/.test(text) || /^are\b/.test(text)) {
        return "YES_NO";
    }

    return "GENERAL";

}


/* =========================================================
   SPECIAL QUESTIONS
   ========================================================= */

function checkSpecialQuestion(question) {

    const text = question.toLowerCase();

    if (!Array.isArray(data.special)) {
        return null;
    }

    for (const item of data.special) {

        if (!item) {
            continue;
        }

        const keywords = item.keywords || [];

        if (
            keywords.length &&
            keywords.every(keyword =>
                text.includes(String(keyword).toLowerCase())
            )
        ) {

            return item.answer || null;

        }

    }

    return null;

}


/* =========================================================
   TOPIC ANSWER
   ========================================================= */

function getTopicAnswer(topic, type) {

    const topicData = data.topics?.[topic];

    if (!topicData) {
        return null;
    }

    if (
        topicData[type] &&
        Array.isArray(topicData[type])
    ) {

        return randomItem(topicData[type]);

    }

    if (
        topicData.answers &&
        Array.isArray(topicData.answers)
    ) {

        return randomItem(topicData.answers);

    }

    return null;

}


/* =========================================================
   QUESTION TYPE ANSWER
   ========================================================= */

function getQuestionTypeAnswer(type) {

    const answers = data.questionTypes?.[type];

    if (
        Array.isArray(answers) &&
        answers.length
    ) {

        return randomItem(answers);

    }

    return null;

}


/* =========================================================
   GENERATE ANSWER
   ========================================================= */

function generateAnswer(question) {

    const topic = detectTopic(question);
    const type = detectQuestionType(question);

    const special = checkSpecialQuestion(question);

    if (special) {

        return {
            answer: special,
            topic: topic,
            type: type
        };

    }


    const topicAnswer = getTopicAnswer(
        topic,
        type
    );

    const typeAnswer = getQuestionTypeAnswer(type);

    const opening = randomItem(data.openings);
    const ending = randomItem(data.endings);


    let middle = topicAnswer;

    if (!middle) {
        middle = typeAnswer;
    }

    if (!middle) {
        middle = randomItem(data.fallback);
    }


    let answer = "";

    if (opening) {
        answer += opening + " ";
    }

    answer += middle;

    if (ending) {
        answer += " " + ending;
    }


    return {
        answer: answer,
        topic: topic,
        type: type
    };

}


/* =========================================================
   CONFIDENCE
   ========================================================= */

function getConfidence() {

    return Number(
        randomItem(data.confidence)
    ) || 97;

}


/* =========================================================
   CHARACTER COUNTER
   ========================================================= */

function updateCharacterCount() {

    const length = questionInput.value.length;

    characterCount.textContent =
        `${length} / 500`;

}


/* =========================================================
   SHOW / HIDE
   ========================================================= */

function show(element) {

    element.classList.remove("hidden");

}


function hide(element) {

    element.classList.add("hidden");

}


/* =========================================================
   PROCESSING MESSAGE
   ========================================================= */

function getThinkingMessage() {

    return randomItem(data.thinking)
        || "Thinking very hard...";

}


/* =========================================================
   PROCESSING ANIMATION
   ========================================================= */

function startProcessing(callback) {

    if (isProcessing) {
        return;
    }

    isProcessing = true;

    hide(answerSection);
    show(processingCard);

    askButton.disabled = true;

    const askText = askButton.querySelector(".ask-text");

    if (askText) {
        askText.textContent = "THINKING";
    }


    let progress = 0;

    processingPercent.textContent = "0%";
    progressBar.style.width = "0%";

    processingMessage.textContent =
        getThinkingMessage();


    clearInterval(processingTimer);


    processingTimer = setInterval(() => {

        const increment =
            Math.floor(Math.random() * 12) + 5;

        progress += increment;


        if (progress >= 100) {
            progress = 100;
        }


        processingPercent.textContent =
            `${progress}%`;

        progressBar.style.width =
            `${progress}%`;


        if (progress > 25 && progress < 55) {

            processingMessage.textContent =
                getThinkingMessage();

        }

        if (progress >= 55 && progress < 85) {

            processingMessage.textContent =
                "Cross-referencing absolutely nothing...";

        }

        if (progress >= 85 && progress < 100) {

            processingMessage.textContent =
                "Constructing confidence...";

        }


        if (progress >= 100) {

            clearInterval(processingTimer);

            setTimeout(() => {

                finishProcessing(callback);

            }, 250);

        }

    }, 180);

}


/* =========================================================
   FINISH PROCESSING
   ========================================================= */

function finishProcessing(callback) {

    isProcessing = false;

    hide(processingCard);

    askButton.disabled = false;

    const askText = askButton.querySelector(".ask-text");

    if (askText) {
        askText.textContent = "ASK";
    }

    callback();

}


/* =========================================================
   RENDER ANSWER
   ========================================================= */

function renderAnswer(result) {

    answerContent.textContent =
        result.answer;

    topicElement.textContent =
        result.topic;

    answerTypeElement.textContent =
        result.type;


    const confidence =
        getConfidence();

    confidenceElement.textContent =
        `CONFIDENCE: ${confidence}%`;


    show(answerSection);


    setTimeout(() => {

        answerSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

    }, 50);

}


/* =========================================================
   ASK QUESTION
   ========================================================= */

function askQuestion() {

    if (isProcessing) {
        return;
    }


    const question =
        cleanQuestion(questionInput.value);


    if (!question) {

        questionInput.focus();

        questionInput.classList.add(
            "input-error"
        );


        setTimeout(() => {

            questionInput.classList.remove(
                "input-error"
            );

        }, 500);

        return;
    }


    const result =
        generateAnswer(question);


    startProcessing(() => {

        renderAnswer(result);

    });

}


/* =========================================================
   RESET EVERYTHING
   ========================================================= */

function resetApplication() {

    /*
       Cancel any active processing animation.
    */

    clearInterval(processingTimer);

    processingTimer = null;

    isProcessing = false;


    /*
       Reset input.
    */

    questionInput.value = "";

    updateCharacterCount();


    /*
       Reset answer.
    */

    answerContent.textContent = "";

    topicElement.textContent =
        "GENERAL";

    answerTypeElement.textContent =
        "ANALYSIS";

    confidenceElement.textContent =
        "CONFIDENCE: 99%";


    /*
       Reset processing UI.
    */

    processingPercent.textContent =
        "0%";

    progressBar.style.width =
        "0%";

    processingMessage.textContent =
        "Thinking very hard...";


    /*
       Hide answer and processing.
    */

    hide(answerSection);

    hide(processingCard);


    /*
       Reset ASK button.
    */

    askButton.disabled = false;

    const askText =
        askButton.querySelector(".ask-text");

    if (askText) {
        askText.textContent = "ASK";
    }


    /*
       Remove temporary states.
    */

    questionInput.classList.remove(
        "input-error"
    );


    /*
       Return to the top without reloading.
    */

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });


    /*
       Put cursor back in the question box.
    */

    setTimeout(() => {

        questionInput.focus();

    }, 350);

}


/* =========================================================
   LOGO RESET
   ========================================================= */

if (logoButton) {

    logoButton.addEventListener(
        "click",
        resetApplication
    );

}


/* =========================================================
   CHARACTER COUNTER EVENT
   ========================================================= */

questionInput.addEventListener(
    "input",
    updateCharacterCount
);


/* =========================================================
   ASK BUTTON EVENT
   ========================================================= */

askButton.addEventListener(
    "click",
    askQuestion
);


/* =========================================================
   ASK ANOTHER EVENT
   ========================================================= */

anotherButton.addEventListener(
    "click",
    () => {

        hide(answerSection);

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

        setTimeout(() => {

            questionInput.focus();

        }, 350);

    }
);


/* =========================================================
   QUICK PROMPTS
   ========================================================= */

quickPrompts.forEach(button => {

    button.addEventListener(
        "click",
        () => {

            const question =
                button.dataset.question || "";

            questionInput.value =
                question;

            updateCharacterCount();

            questionInput.focus();

            /*
               Move cursor to the end.
            */

            questionInput.setSelectionRange(
                question.length,
                question.length
            );

        }
    );

});


/* =========================================================
   ENTER KEY
   ========================================================= */

questionInput.addEventListener(
    "keydown",
    event => {

        /*
           Enter = Ask
           Shift + Enter = New line
        */

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            askQuestion();

        }

    }
);


/* =========================================================
   INITIAL STATE
   ========================================================= */

updateCharacterCount();

hide(answerSection);
hide(processingCard);

console.log(
    "ANSWER MACHINE initialized."
);
