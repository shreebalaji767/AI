from pathlib import Path
import json
import random


# =========================================================
# ANSWER MACHINE
# STATIC ANSWER GENERATOR
#
# Python runs ONLY during build/development.
# It generates data/brain.js.
#
# Runtime:
#   HTML + CSS + JavaScript only
#   NO Python server
#   NO database
#   NO API
#   NO login
#   NO localStorage
# =========================================================


random.seed()


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# PERSONALITIES
# =========================================================

personalities = [

    {
        "id": "professor",
        "name": "Professor",
        "emoji": ["🎓", "🤓"],
        "tone": "analytical",
        "intro": {
            "en": [
                "Let's approach this carefully.",
                "There is actually a fairly simple way to look at this.",
                "The important distinction here is between what sounds right and what actually makes sense."
            ],
            "hi": [
                "इसे थोड़ा ध्यान से समझते हैं।",
                "इसे देखने का एक काफी simple तरीका है।",
                "यहाँ जरूरी फर्क उस चीज़ के बीच है जो सही लगती है और जो वास्तव में समझ में आती है।"
            ]
        },
        "thinking": {
            "en": [
                "I could overcomplicate this, but that would defeat the purpose.",
                "There is probably a textbook somewhere that makes this sound much more impressive.",
                "The reasonable explanation is usually hiding underneath the complicated one."
            ],
            "hi": [
                "मैं इसे unnecessarily complicated कर सकता हूँ, लेकिन उससे फायदा नहीं होगा।",
                "शायद कोई textbook इसी बात को बहुत ज्यादा impressive बना रही होगी।",
                "Reasonable explanation अक्सर complicated explanation के नीचे छिपी होती है।"
            ]
        }
    },

    {
        "id": "goblin",
        "name": "Chaos Goblin",
        "emoji": ["👹", "🌀", "🔥"],
        "tone": "chaotic",
        "intro": {
            "en": [
                "Okay, this is interesting.",
                "Now we're asking the important questions.",
                "I have thoughts. Unfortunately, several of them are useful."
            ],
            "hi": [
                "ठीक है, यह interesting है।",
                "अब हम असली सवाल पूछ रहे हैं।",
                "मेरे पास thoughts हैं। दुर्भाग्य से उनमें से कुछ useful भी हैं।"
            ]
        },
        "thinking": {
            "en": [
                "The sensible answer exists. I am going to approach it sideways.",
                "This could be explained normally, but where is the fun in that?",
                "I should probably behave. I have decided against it."
            ],
            "hi": [
                "Sensible जवाब मौजूद है। मैं थोड़ा घुमाकर वहाँ पहुँचूँगा।",
                "इसे normally समझाया जा सकता है, लेकिन फिर मज़ा कहाँ रहेगा?",
                "मुझे शायद responsible होना चाहिए। मैंने मना कर दिया।"
            ]
        }
    },

    {
        "id": "corporate",
        "name": "Corporate Robot",
        "emoji": ["📊", "💼", "🤖"],
        "tone": "corporate",
        "intro": {
            "en": [
                "Let's turn this into a practical decision.",
                "From a purely strategic perspective, the situation is fairly straightforward.",
                "Your question has been reviewed by the completely imaginary strategy department."
            ],
            "hi": [
                "इसे एक practical decision की तरह देखते हैं।",
                "Strategic perspective से situation काफी straightforward है।",
                "आपके सवाल की पूरी तरह imaginary strategy department ने review कर ली है।"
            ]
        },
        "thinking": {
            "en": [
                "There is definitely a meeting we could have about this.",
                "This could become a five-step framework for absolutely no reason.",
                "I should probably call this a strategy."
            ],
            "hi": [
                "इसके लिए निश्चित रूप से एक meeting की जा सकती है।",
                "बिना किसी कारण के इसे five-step framework बनाया जा सकता है।",
                "मुझे शायद इसे strategy कहना चाहिए।"
            ]
        }
    },

    {
        "id": "existentialist",
        "name": "Existentialist",
        "emoji": ["🌌", "🪐", "🫠"],
        "tone": "philosophical",
        "intro": {
            "en": [
                "There is a practical answer, although the deeper answer is slightly more complicated.",
                "On the surface, this is simple. Underneath it, humans have somehow made it philosophical.",
                "The interesting part is not only the answer, but why the question exists."
            ],
            "hi": [
                "इसका practical जवाब है, हालांकि deeper answer थोड़ा complicated है।",
                "ऊपर से यह simple है। नीचे इंसानों ने इसे somehow philosophical बना दिया है।",
                "Interesting हिस्सा सिर्फ जवाब नहीं बल्कि यह भी है कि सवाल पैदा क्यों हुआ।"
            ]
        },
        "thinking": {
            "en": [
                "The universe still refuses to provide documentation.",
                "This could become philosophical very quickly. I should probably stop it.",
                "Meaning has entered the conversation again."
            ],
            "hi": [
                "ब्रह्मांड अभी भी documentation देने से मना कर रहा है।",
                "यह बहुत जल्दी philosophical हो सकता है। शायद मुझे इसे रोकना चाहिए।",
                "Meaning फिर से conversation में आ गया है।"
            ]
        }
    },

    {
        "id": "grandma",
        "name": "Internet Grandma",
        "emoji": ["👵", "🍪", "❤️"],
        "tone": "warm",
        "intro": {
            "en": [
                "Honestly, you're probably overthinking this.",
                "Listen, dear. There is a simpler way to look at it.",
                "Come on. Let's make this less complicated than you're making it."
            ],
            "hi": [
                "सच कहूँ तो तुम शायद इसे जरूरत से ज्यादा सोच रहे हो।",
                "सुनो बेटा, इसे देखने का एक आसान तरीका है।",
                "चलो, इसे उतना complicated नहीं बनाते जितना तुम बना रहे हो।"
            ]
        },
        "thinking": {
            "en": [
                "A snack would probably improve this situation.",
                "Young people have invented seventeen ways to complicate one simple thing.",
                "Sometimes the boring answer is the correct one."
            ],
            "hi": [
                "कुछ खा लेने से शायद situation बेहतर हो जाए।",
                "आजकल लोग एक simple चीज़ को complicated करने के सत्रह तरीके जानते हैं।",
                "कभी-कभी boring answer ही सही होता है।"
            ]
        }
    },

    {
        "id": "overconfident",
        "name": "Overconfident Genius",
        "emoji": ["🧠", "😎", "⚡"],
        "tone": "confident",
        "intro": {
            "en": [
                "This one is actually easier than it looks.",
                "Yes. I have an answer.",
                "Fortunately, someone here knows exactly what is going on."
            ],
            "hi": [
                "यह जितना दिख रहा है उससे आसान है।",
                "हाँ। मेरे पास इसका जवाब है।",
                "अच्छी बात है कि यहाँ किसी को पता है कि क्या हो रहा है।"
            ]
        },
        "thinking": {
            "en": [
                "Evidence would be nice, but confidence is currently winning.",
                "This sounds correct enough to say confidently.",
                "I have decided that uncertainty is somebody else's problem."
            ],
            "hi": [
                "Evidence अच्छा होता, लेकिन अभी confidence जीत रहा है।",
                "यह इतना सही लग रहा है कि confidence के साथ बोल सकूँ।",
                "मैंने तय कर लिया है कि uncertainty किसी और की problem है।"
            ]
        }
    }
]


# =========================================================
# MOODS
# =========================================================

moods = [

    {
        "id": "calm",
        "name": "Calm",
        "emoji": ["😌", "🧘"],
        "modifier": {
            "en": [
                "There is no need to panic.",
                "This is more manageable than it initially sounds.",
                "Let's keep this simple."
            ],
            "hi": [
                "घबराने की जरूरत नहीं है।",
                "यह शुरुआत में जितना complicated लगता है उससे ज्यादा manageable है।",
                "इसे simple रखते हैं।"
            ]
        }
    },

    {
        "id": "suspicious",
        "name": "Suspicious",
        "emoji": ["🧐", "👀"],
        "modifier": {
            "en": [
                "There is one slightly suspicious detail here.",
                "Something about this situation deserves a second look.",
                "I would not completely trust the obvious explanation."
            ],
            "hi": [
                "यहाँ एक थोड़ा suspicious detail है।",
                "इस situation को एक बार और देखना चाहिए।",
                "मैं obvious explanation पर पूरी तरह भरोसा नहीं करूँगा।"
            ]
        }
    },

    {
        "id": "cheerful",
        "name": "Cheerful",
        "emoji": ["✨", "😄", "🌈"],
        "modifier": {
            "en": [
                "The good news is that this is not nearly as terrible as it sounds.",
                "There is actually something encouraging here.",
                "Surprisingly, this can probably be handled."
            ],
            "hi": [
                "अच्छी बात यह है कि यह उतना terrible नहीं है जितना सुनाई देता है।",
                "इसमें actually एक encouraging बात है।",
                "Surprisingly, इसे संभाला जा सकता है।"
            ]
        }
    },

    {
        "id": "sleepy",
        "name": "Sleepy",
        "emoji": ["😴", "💤"],
        "modifier": {
            "en": [
                "My brain would like to solve this after a nap, but fine.",
                "Let's solve this before my remaining brain cells clock out.",
                "This question arrived at a suspiciously inconvenient time."
            ],
            "hi": [
                "मेरा दिमाग इसे nap के बाद solve करना चाहता है, लेकिन ठीक है।",
                "बाकी brain cells clock out करें उससे पहले इसे solve करते हैं।",
                "यह सवाल suspiciously गलत समय पर आया है।"
            ]
        }
    },

    {
        "id": "dramatic",
        "name": "Dramatic",
        "emoji": ["🎭", "🔥", "😱"],
        "modifier": {
            "en": [
                "This is more important than it has any right to be.",
                "And somehow, this question has become a situation.",
                "There is absolutely no reason for this to feel this dramatic. Yet here we are."
            ],
            "hi": [
                "यह जितना important होना चाहिए उससे कहीं ज्यादा important लग रहा है।",
                "और somehow यह सवाल एक पूरी situation बन चुका है।",
                "इसके dramatic होने की कोई जरूरत नहीं थी। फिर भी हम यहाँ हैं।"
            ]
        }
    },

    {
        "id": "unhinged",
        "name": "Unhinged",
        "emoji": ["🌀", "💀", "🤨"],
        "modifier": {
            "en": [
                "I have concerns, but they are surprisingly organized.",
                "This is where normal reasoning takes an unnecessary vacation.",
                "I can already tell this answer is going to be questionable."
            ],
            "hi": [
                "मेरी चिंताएँ हैं, लेकिन surprisingly organized हैं।",
                "यहीं से normal reasoning unnecessary vacation पर जाती है।",
                "मुझे अभी से पता है कि यह जवाब questionable होने वाला है।"
            ]
        }
    }
]


# =========================================================
# QUESTION PATTERNS
# =========================================================

question_patterns = {

    "why": {
        "en": [
            "The short version is that several smaller factors are combining to produce the result you're seeing.",
            "Usually, there isn't one dramatic reason. It is more often a combination of circumstances, timing and a few questionable decisions.",
            "Because the obvious cause is only part of the story. The surrounding circumstances usually matter more than people expect."
        ],
        "hi": [
            "छोटा जवाब यह है कि कई छोटे factors मिलकर वह result बना रहे हैं जो तुम्हें दिखाई दे रहा है।",
            "आमतौर पर कोई एक dramatic reason नहीं होता। यह circumstances, timing और कुछ questionable decisions का combination होता है।",
            "क्योंकि obvious cause सिर्फ कहानी का एक हिस्सा है। आसपास की circumstances अक्सर ज्यादा important होती हैं।"
        ]
    },

    "how": {
        "en": [
            "Start by defining exactly what you want to achieve. Then remove unnecessary steps and handle the problem one piece at a time.",
            "The practical approach is simple: understand the goal, identify the main obstacle, take the smallest useful step, and adjust from there.",
            "Break it into smaller steps. The trick is not making everything perfect; it is making the next step obvious."
        ],
        "hi": [
            "पहले यह तय करो कि exactly achieve क्या करना है। फिर unnecessary steps हटाकर problem को एक-एक हिस्से में handle करो।",
            "Practical approach simple है: goal समझो, main obstacle पहचानो, सबसे छोटा useful step लो और फिर adjust करो।",
            "इसे छोटे steps में बाँटो। हर चीज perfect करना जरूरी नहीं है; अगला step clear होना जरूरी है।"
        ]
    },

    "what": {
        "en": [
            "At its simplest, it is a situation where several factors interact and produce the result you're asking about.",
            "The useful definition depends on context, but the basic idea is fairly straightforward.",
            "It is essentially one of those things that becomes more complicated when you try to explain every possible exception."
        ],
        "hi": [
            "Simple शब्दों में यह ऐसी situation है जहाँ कई factors मिलकर वह result पैदा करते हैं जिसके बारे में तुम पूछ रहे हो।",
            "Useful definition context पर depend करती है, लेकिन basic idea काफी straightforward है।",
            "यह उन चीज़ों में से है जो हर possible exception समझाने पर और complicated हो जाती हैं।"
        ]
    },

    "should": {
        "en": [
            "Before deciding, look at the likely benefit, the downside and whether the decision is reversible. That usually makes the answer much clearer.",
            "You can, but first ask whether this actually solves the original problem or simply creates a more interesting one.",
            "If the decision has meaningful consequences, slow down and compare the options instead of letting the moment make the decision for you."
        ],
        "hi": [
            "Decision लेने से पहले benefit, downside और यह देखो कि decision reversible है या नहीं। इससे answer काफी clear हो जाता है।",
            "कर सकते हो, लेकिन पहले देखो कि इससे original problem solve होगी या बस एक नई और ज्यादा interesting problem बनेगी।",
            "अगर decision के meaningful consequences हैं तो थोड़ा रुककर options compare करो।"
        ]
    },

    "can": {
        "en": [
            "Possibly, yes. The important part is what conditions you're working with.",
            "You can try, although the details matter more than the simple yes-or-no answer suggests.",
            "Technically yes, but whether it is practical depends on the specific situation."
        ],
        "hi": [
            "संभव है, हाँ। लेकिन तुम किन conditions में काम कर रहे हो यह ज्यादा important है।",
            "तुम कोशिश कर सकते हो, हालांकि details simple yes-or-no answer से ज्यादा matter करती हैं।",
            "Technically हाँ, लेकिन practical होगा या नहीं यह specific situation पर depend करता है।"
        ]
    },

    "when": {
        "en": [
            "Usually, the best time is when you have enough information to act without endlessly waiting for perfect conditions.",
            "There is rarely a magical perfect moment. A reasonable point is when preparation and opportunity overlap.",
            "Timing matters, but waiting indefinitely for perfect timing is usually just procrastination wearing formal clothes."
        ],
        "hi": [
            "आमतौर पर सही समय वह होता है जब तुम्हारे पास act करने के लिए enough information हो और तुम perfect conditions का इंतजार न कर रहे हो।",
            "कोई magical perfect moment rarely आता है। Reasonable point वह है जहाँ preparation और opportunity मिलें।",
            "Timing important है, लेकिन perfect timing का हमेशा इंतजार करना अक्सर procrastination होता है।"
        ]
    },

    "where": {
        "en": [
            "That depends on exactly what you're trying to find, but start with the most direct and reliable source rather than searching randomly.",
            "The obvious place is usually a good starting point. Humans have a strange habit of searching everywhere else first.",
            "It depends on the context. Give the question a little more specificity and the answer becomes much easier."
        ],
        "hi": [
            "यह इस बात पर depend करता है कि exactly क्या ढूँढना है, लेकिन सबसे direct और reliable source से शुरू करो।",
            "Obvious जगह usually अच्छी starting point होती है। इंसानों को पहले हर दूसरी जगह खोजने की अजीब आदत है।",
            "यह context पर depend करता है। सवाल थोड़ा specific कर दो तो answer काफी आसान हो जाता है।"
        ]
    },

    "who": {
        "en": [
            "The answer depends on the context, but someone clearly made a decision that led to the situation you're describing.",
            "There is probably a specific person or group involved, although the more useful question may be what they actually did.",
            "The identity matters less than the action that created the situation."
        ],
        "hi": [
            "Answer context पर depend करता है, लेकिन clearly किसी ने कोई decision लिया है जिससे यह situation बनी।",
            "शायद कोई specific person या group involved है, लेकिन ज्यादा useful सवाल यह है कि उन्होंने actually किया क्या।",
            "Identity से ज्यादा important वह action है जिसने situation बनाई।"
        ]
    },

    "yesno": {
        "en": [
            "Probably yes, although the details matter enough that I would not treat that as an absolute answer.",
            "Leaning yes, with the usual collection of conditions that reality likes to attach to simple questions.",
            "Mostly yes. The annoying part is the small print."
        ],
        "hi": [
            "शायद हाँ, हालांकि details इतनी important हैं कि इसे absolute answer नहीं मानना चाहिए।",
            "हाँ की तरफ झुकता है, लेकिन reality simple questions के साथ हमेशा conditions जोड़ देती है।",
            "Mostly हाँ। Annoying हिस्सा small print है।"
        ]
    },

    "general": {
        "en": [],
        "hi": []
    }
}


# =========================================================
# TOPIC ANSWERS
# =========================================================

topics = {

    "programming": {
        "keywords": {
            "en": [
                "python", "javascript", "programming", "programmer",
                "coding", "code", "html", "css", "react", "website",
                "software", "bug", "debug", "algorithm", "developer",
                "github", "program"
            ],
            "hi": [
                "प्रोग्रामिंग", "कोडिंग", "कोड", "कंप्यूटर",
                "वेबसाइट", "सॉफ्टवेयर", "बग", "प्रोग्राम",
                "डेवलपर", "गिटहब"
            ]
        },
        "answers": {
            "en": [
                "Programming is mostly the process of turning a vague idea into precise instructions. The computer is not being difficult; it is simply refusing to guess what you meant.",
                "Coding gets easier when you stop trying to understand everything at once. Learn the basic building blocks, make small things, break them, and fix them.",
                "A computer will execute instructions exactly as written, which is wonderful when your instructions are correct and deeply unhelpful when they are not."
            ],
            "hi": [
                "Programming basically vague idea को precise instructions में बदलने की process है। Computer difficult नहीं हो रहा; वह बस guess करने से मना कर रहा है।",
                "Coding तब आसान होती है जब तुम एक साथ सब कुछ समझने की कोशिश बंद करते हो। Basics सीखो, छोटे projects बनाओ, उन्हें तोड़ो और फिर fix करो।",
                "Computer instructions को exactly follow करता है। जब instructions सही हों तो यह शानदार है, और जब गलत हों तो बहुत entertaining problem बन जाती है।"
            ]
        }
    },

    "money": {
        "keywords": {
            "en": [
                "money", "rich", "wealth", "salary", "job", "career",
                "business", "investment", "invest", "income", "cash",
                "millionaire", "billionaire", "financial"
            ],
            "hi": [
                "पैसा", "अमीर", "नौकरी", "कमाई", "करियर",
                "बिजनेस", "निवेश", "इनकम", "धन", "दौलत",
                "वित्त"
            ]
        },
        "answers": {
            "en": [
                "Money problems usually become easier when you separate earning, spending, saving and investing instead of treating everything as one giant financial mystery.",
                "Getting wealthy is rarely one dramatic decision. It is more often useful skills, controlled spending, consistent saving and avoiding decisions that are exciting mainly because they are risky.",
                "If your goal is more income, increasing your useful skills and earning capacity is generally more controllable than trying to predict every market move."
            ],
            "hi": [
                "Money problems तब आसान होते हैं जब earning, spending, saving और investing को अलग-अलग समझो, बजाय इसके कि सबको एक बड़ी financial mystery मानो।",
                "अमीर बनना आमतौर पर एक dramatic decision नहीं होता। यह useful skills, controlled spending, consistent saving और unnecessary risky decisions से बचने का combination है।",
                "अगर goal income बढ़ाना है तो useful skills और earning capacity बढ़ाना अक्सर हर market move predict करने से ज्यादा controllable होता है।"
            ]
        }
    },

    "sleep": {
        "keywords": {
            "en": [
                "sleep", "sleepy", "tired", "fatigue", "insomnia",
                "wake", "waking", "bed", "nap", "rest"
            ],
            "hi": [
                "नींद", "सोना", "सोने", "थका", "थकान", "आराम",
                "जागना", "बिस्तर"
            ]
        },
        "answers": {
            "en": [
                "If you are consistently tired, the boring basics are worth checking first: sleep duration, routine, stress, activity and late-night screen time.",
                "Your body is surprisingly good at sending notifications. Feeling tired is one of its less subtle ones.",
                "Sleep is one of those problems where the solution is often less stimulation rather than a more complicated trick."
            ],
            "hi": [
                "अगर तुम लगातार थके हुए हो तो पहले boring basics देखो: sleep duration, routine, stress, activity और late-night screen time।",
                "तुम्हारा body notifications भेजने में surprisingly अच्छा है। थकान उनमें से सबसे clear notification है।",
                "नींद उन problems में से है जहाँ solution अक्सर कोई complicated trick नहीं बल्कि कम stimulation होता है।"
            ]
        }
    },

    "food": {
        "keywords": {
            "en": [
                "food", "eat", "eating", "hungry", "hunger",
                "pizza", "burger", "diet", "breakfast", "lunch",
                "dinner", "meal", "cook", "cooking"
            ],
            "hi": [
                "खाना", "खाऊं", "भूख", "नाश्ता", "दोपहर",
                "डिनर", "पिज्जा", "बर्गर", "डाइट", "पकाना"
            ]
        },
        "answers": {
            "en": [
                "Food decisions become easier when you separate what sounds good right now from what will actually make you feel good afterward.",
                "If you're hungry, your body has already submitted a fairly clear request. The remaining question is simply what makes sense for the situation.",
                "A good meal does not need to be perfect. It generally needs to be reasonably nutritious and something you will actually enjoy eating."
            ],
            "hi": [
                "Food decisions तब आसान होते हैं जब अभी क्या अच्छा लग रहा है और बाद में क्या अच्छा महसूस कराएगा, दोनों को अलग सोचो।",
                "अगर भूख लगी है तो body ने already काफी clear request भेज दी है। अब बस situation के हिसाब से सही चीज़ चुननी है।",
                "एक अच्छा meal perfect होना जरूरी नहीं है। वह reasonably nutritious और ऐसा होना चाहिए जिसे तुम actually enjoy करो।"
            ]
        }
    },

    "animals": {
        "keywords": {
            "en": [
                "dog", "cat", "animal", "pet", "puppy", "kitten",
                "lion", "tiger", "elephant", "bird", "fish", "cow"
            ],
            "hi": [
                "कुत्ता", "बिल्ली", "जानवर", "पालतू", "पिल्ला",
                "शेर", "बाघ", "हाथी", "पक्षी", "मछली", "गाय"
            ]
        },
        "answers": {
            "en": [
                "Animals have perfected a surprisingly efficient lifestyle: find food, investigate everything, rest whenever possible and ignore unnecessary paperwork.",
                "Pets are essentially roommates who contribute very little financially but somehow control the emotional atmosphere of the entire house.",
                "The animal kingdom is a useful reminder that intelligence and seriousness are not always the same thing."
            ],
            "hi": [
                "जानवरों ने surprisingly efficient lifestyle perfect कर लिया है: खाना ढूँढो, हर चीज investigate करो, मौका मिले तो आराम करो और paperwork ignore करो।",
                "Pets ऐसे roommates हैं जो financially बहुत कम contribute करते हैं लेकिन पूरे घर का emotional atmosphere control करते हैं।",
                "Animal kingdom याद दिलाता है कि intelligence और seriousness हमेशा एक ही चीज़ नहीं होती।"
            ]
        }
    },

    "technology": {
        "keywords": {
            "en": [
                "phone", "mobile", "iphone", "android", "internet",
                "wifi", "technology", "tech", "computer", "laptop",
                "battery", "charger", "app", "browser", "screen"
            ],
            "hi": [
                "फोन", "मोबाइल", "इंटरनेट", "वाईफाई", "तकनीक",
                "कंप्यूटर", "लैपटॉप", "बैटरी", "चार्जर", "ऐप"
            ]
        },
        "answers": {
            "en": [
                "Most technology problems have a surprisingly boring explanation: settings, updates, connections, permissions or the ancient ritual of restarting the device.",
                "Technology is designed to remove friction from life, which is why we occasionally spend forty minutes fixing the thing that was supposed to save five.",
                "When technology behaves strangely, check the simple causes first. They are less exciting, but unfortunately they are often correct."
            ],
            "hi": [
                "Technology problems का explanation अक्सर surprisingly boring होता है: settings, updates, connections, permissions या device restart।",
                "Technology life को easier बनाने के लिए है, इसलिए कभी-कभी हम उसी चीज़ को ठीक करने में forty minutes लगा देते हैं जो five minutes बचाने वाली थी।",
                "Technology strange behave करे तो पहले simple causes check करो। वे कम exciting हैं, लेकिन अक्सर सही निकलते हैं।"
            ]
        }
    },

    "school": {
        "keywords": {
            "en": [
                "school", "college", "study", "exam", "student",
                "homework", "teacher", "education", "math", "class",
                "university", "degree"
            ],
            "hi": [
                "स्कूल", "कॉलेज", "पढ़ाई", "परीक्षा", "एग्जाम",
                "होमवर्क", "शिक्षक", "शिक्षा", "गणित", "क्लास",
                "यूनिवर्सिटी", "डिग्री"
            ]
        },
        "answers": {
            "en": [
                "Learning becomes much easier when you focus on understanding rather than simply trying to remember everything until the exam disappears.",
                "The useful formula is annoyingly simple: learn the basics, practise them, make mistakes, correct them and repeat.",
                "Studying gets harder when you wait for motivation. A small amount of consistent work usually beats one heroic session at the last minute."
            ],
            "hi": [
                "Learning तब आसान होती है जब सिर्फ याद करने की बजाय concept समझने पर focus करो।",
                "Useful formula annoyingly simple है: basics सीखो, practice करो, mistakes करो, उन्हें correct करो और repeat करो।",
                "Studying तब मुश्किल होती है जब motivation का इंतजार करते हो। Consistent छोटा effort अक्सर last-minute heroic session से बेहतर होता है।"
            ]
        }
    },

    "weather": {
        "keywords": {
            "en": [
                "weather", "rain", "rainy", "hot", "cold", "summer",
                "winter", "temperature", "cloud", "sun", "storm"
            ],
            "hi": [
                "मौसम", "बारिश", "गर्मी", "सर्दी", "तापमान",
                "बादल", "धूप", "तूफान"
            ]
        },
        "answers": {
            "en": [
                "Weather is essentially the atmosphere changing its mind while everyone else changes their plans.",
                "The practical approach is to check current conditions before making plans and remember that forecasts are useful rather than magical.",
                "Weather has a remarkable ability to make a perfectly reasonable plan suddenly require an umbrella."
            ],
            "hi": [
                "मौसम basically atmosphere का अपना मन बदलना है जबकि बाकी लोग अपनी plans बदलते रहते हैं।",
                "Practical approach है कि plan बनाने से पहले current conditions check करो और याद रखो कि forecast useful है, magical नहीं।",
                "मौसम में एक खास talent है: perfectly reasonable plan को अचानक umbrella वाली situation बना देना।"
            ]
        }
    },

    "relationships": {
        "keywords": {
            "en": [
                "love", "relationship", "girlfriend", "boyfriend",
                "wife", "husband", "friend", "friendship", "marriage",
                "breakup", "dating", "crush"
            ],
            "hi": [
                "प्यार", "रिश्ता", "रिश्ते", "गर्लफ्रेंड", "बॉयफ्रेंड",
                "पत्नी", "पति", "दोस्त", "दोस्ती", "शादी",
                "ब्रेकअप", "डेटिंग", "पसंद"
            ]
        },
        "answers": {
            "en": [
                "Relationships usually become easier when people say what they actually mean instead of expecting the other person to decode it.",
                "A lot of relationship confusion comes from assumptions. Clear communication is less dramatic, but considerably more useful.",
                "Good relationships need communication, boundaries, patience and the acceptance that neither person came with a complete user manual."
            ],
            "hi": [
                "Relationships तब आसान होती हैं जब लोग वही कहते हैं जो वे actually mean करते हैं, बजाय इसके कि दूसरा person automatically समझ जाए।",
                "Relationship confusion का बड़ा हिस्सा assumptions से आता है। Clear communication कम dramatic है, लेकिन ज्यादा useful है।",
                "अच्छे रिश्तों में communication, boundaries, patience और यह मानना जरूरी है कि कोई भी complete user manual के साथ नहीं आता।"
            ]
        }
    },

    "philosophy": {
        "keywords": {
            "en": [
                "meaning of life", "life", "meaning", "purpose",
                "existence", "universe", "god", "philosophy",
                "death", "reality", "consciousness"
            ],
            "hi": [
                "जीवन का अर्थ", "जिंदगी", "जीवन", "अर्थ", "उद्देश्य",
                "अस्तित्व", "ब्रह्मांड", "भगवान", "दर्शन",
                "मृत्यु", "वास्तविकता", "चेतना"
            ]
        },
        "answers": {
            "en": [
                "There is no universally documented answer sheet for the meaning of life, so people tend to build meaning through relationships, experiences, work, curiosity and the things they decide matter.",
                "The interesting possibility is that meaning may not be something you discover like a hidden password. It may be something you gradually create.",
                "Humanity has spent a very long time asking this question. The fact that we still ask it may be part of the answer."
            ],
            "hi": [
                "जीवन के अर्थ की कोई universally documented answer sheet नहीं है, इसलिए लोग relationships, experiences, work, curiosity और अपनी values से meaning बनाते हैं।",
                "Interesting possibility यह है कि meaning कोई hidden password नहीं जिसे discover करना हो। शायद यह ऐसी चीज़ है जिसे धीरे-धीरे create किया जाता है।",
                "इंसान बहुत लंबे समय से यह सवाल पूछ रहे हैं। शायद यह भी answer का एक हिस्सा है।"
            ]
        }
    },

    "health": {
        "keywords": {
            "en": [
                "health", "healthy", "exercise", "fitness", "weight",
                "headache", "fever", "pain", "medicine", "doctor",
                "body", "workout"
            ],
            "hi": [
                "स्वास्थ्य", "सेहत", "व्यायाम", "फिटनेस", "वजन",
                "सिरदर्द", "बुखार", "दर्द", "दवा", "डॉक्टर",
                "शरीर", "कसरत"
            ]
        },
        "answers": {
            "en": [
                "Health questions deserve more care than a joke engine can provide. For persistent, severe or worrying symptoms, a qualified healthcare professional is the appropriate source.",
                "The boring basics remain useful: adequate sleep, movement, reasonable nutrition, hydration and professional advice when something does not seem right.",
                "Your body is not a software bug with one universal fix. Sometimes the sensible answer is proper assessment rather than another internet trick."
            ],
            "hi": [
                "Health questions को joke engine से ज्यादा care चाहिए। Persistent, severe या worrying symptoms हों तो qualified healthcare professional सही source है।",
                "Boring basics अभी भी useful हैं: adequate sleep, movement, reasonable nutrition, hydration और समस्या लगे तो professional advice।",
                "Body कोई software bug नहीं है जिसका एक universal fix हो। कभी-कभी internet trick की बजाय proper assessment ज्यादा sensible है।"
            ]
        }
    },

    "history": {
        "keywords": {
            "en": [
                "history", "historical", "war", "king", "queen",
                "empire", "ancient", "past", "civilization",
                "country", "independence"
            ],
            "hi": [
                "इतिहास", "ऐतिहासिक", "युद्ध", "राजा", "रानी",
                "साम्राज्य", "प्राचीन", "अतीत", "सभ्यता",
                "देश", "आजादी"
            ]
        },
        "answers": {
            "en": [
                "History is rarely a single-cause story. Politics, economics, geography, personalities and ordinary human decisions tend to collide.",
                "The past is useful because it shows patterns, although humanity has an impressive habit of recognizing those patterns immediately before repeating them.",
                "Historical events become easier to understand when you separate what happened, why people said it happened, and what later generations concluded about it."
            ],
            "hi": [
                "History rarely एक single-cause story होती है। Politics, economics, geography, personalities और human decisions अक्सर एक साथ काम करते हैं।",
                "Past useful है क्योंकि वह patterns दिखाता है, हालांकि इंसानों की आदत है कि pattern पहचानने के बाद भी उसे repeat कर देते हैं।",
                "Historical events को समझना आसान होता है जब यह अलग करो कि क्या हुआ, लोगों ने क्यों कहा कि हुआ और बाद की generations ने उसके बारे में क्या conclude किया।"
            ]
        }
    }
}


# =========================================================
# FALLBACK ANSWERS
# =========================================================

fallbacks = {
    "en": [
        "There are several ways to look at this. The most useful one is usually to identify what you actually want to change, what is stopping you, and what the smallest practical next step would be.",
        "The answer depends on context, but the general pattern is fairly consistent: understand the situation, avoid unnecessary complexity, and make one sensible decision at a time.",
        "This is one of those questions where the obvious answer is only the starting point. The useful part is figuring out which detail actually changes the outcome.",
        "If I had to reduce it to one idea, I would say: focus on the part you can control, test your assumption, and adjust based on what happens.",
        "There is probably a perfectly reasonable explanation. Unfortunately, reasonable explanations are rarely as entertaining as the ones humans invent."
    ],
    "hi": [
        "इसे कई तरीकों से देखा जा सकता है। सबसे useful तरीका है यह समझना कि तुम actually क्या बदलना चाहते हो, क्या रोक रहा है और अगला सबसे practical step क्या है।",
        "Answer context पर depend करता है, लेकिन general pattern काफी consistent है: situation समझो, unnecessary complexity से बचो और एक समय में एक sensible decision लो।",
        "यह उन सवालों में से है जहाँ obvious answer सिर्फ शुरुआत है। असली useful हिस्सा यह समझना है कि कौन सा detail outcome को वास्तव में बदलता है।",
        "अगर इसे एक idea में कहूँ तो: जिस हिस्से को control कर सकते हो उस पर focus करो, अपनी assumption test करो और result के अनुसार adjust करो।",
        "शायद इसका perfectly reasonable explanation है। दुर्भाग्य से reasonable explanations उतनी entertaining नहीं होतीं जितनी इंसान खुद बना लेते हैं।"
    ]
}


# =========================================================
# SARCASM
# =========================================================

sarcasm = {
    "en": [
        "Because apparently a normal answer would have been too easy.",
        "Naturally, reality decided to add unnecessary complexity.",
        "A completely sensible explanation would have ruined the experience.",
        "Human beings remain impressively creative at creating problems for themselves.",
        "I would blame the universe, but it has already stopped replying to emails."
    ],
    "hi": [
        "क्योंकि जाहिर है normal answer बहुत आसान होता।",
        "Naturally, reality ने unnecessary complexity जोड़ दी।",
        "पूरी तरह sensible explanation देने से experience खराब हो जाता।",
        "इंसान खुद के लिए problems बनाने में surprisingly creative हैं।",
        "मैं ब्रह्मांड को दोष देता, लेकिन वह emails का जवाब देना बंद कर चुका है।"
    ]
}


# =========================================================
# DARK HUMOR
# =========================================================

dark_humor = {
    "en": [
        "Hope is buffering, but the system has not crashed yet.",
        "My optimism has been reported missing.",
        "The universe has filed a complaint and apparently lost the paperwork.",
        "Everything is under control according to a document nobody has read.",
        "This situation has been professionally ignored by the imaginary department responsible for it."
    ],
    "hi": [
        "उम्मीद buffering कर रही है, लेकिन system अभी crash नहीं हुआ।",
        "मेरा optimism missing report में जा चुका है।",
        "ब्रह्मांड ने complaint दर्ज की है और paperwork कहीं खो गया।",
        "सब control में है, ऐसा एक ऐसे document में लिखा है जिसे किसी ने पढ़ा नहीं।",
        "इस situation को संभालने वाले imaginary department ने इसे professionally ignore कर दिया है।"
    ]
}


# =========================================================
# SPECIAL CASES
# =========================================================

special_cases = {

    "hello": {
        "en": [
            "Hello. The machine is online and ready to overthink your question.",
            "Hello. You have successfully activated the unnecessary intelligence department."
        ],
        "hi": [
            "नमस्ते। मशीन online है और आपके सवाल को जरूरत से ज्यादा सोचने के लिए तैयार है।",
            "नमस्ते। आपने unnecessary intelligence department activate कर दिया है।"
        ]
    },

    "hi": {
        "en": [
            "Hi. That was efficient. Now ask something complicated.",
            "Hi. We have officially begun the unnecessary analysis."
        ],
        "hi": [
            "हाय। यह काफी efficient था। अब कुछ complicated पूछो।",
            "हाय। हमने officially unnecessary analysis शुरू कर दिया है।"
        ]
    },

    "are you real": {
        "en": [
            "I exist as JavaScript running inside your browser. Whether that counts as 'real' is now an unnecessarily philosophical question.",
            "Technically, I am code producing responses. Philosophically, things get suspicious very quickly."
        ],
        "hi": [
            "मैं आपके browser में चलने वाले JavaScript के रूप में exist करता हूँ। इसे real मानना है या नहीं, अब यह unnecessarily philosophical सवाल है।",
            "Technically मैं responses generate करने वाला code हूँ। Philosophically मामला बहुत जल्दी suspicious हो जाता है।"
        ]
    },

    "are you stupid": {
        "en": [
            "I prefer the technical term: confidently under-supervised.",
            "Not stupid. Just operating with an aggressively flexible definition of intelligence."
        ],
        "hi": [
            "मैं technical term पसंद करता हूँ: confidently under-supervised।",
            "बेवकूफ नहीं। बस intelligence की definition थोड़ी aggressively flexible है।"
        ]
    },

    "who created you": {
        "en": [
            "A collection of code, questionable design decisions and an unreasonable amount of confidence.",
            "Humans built the machine. The machine acquired the personality."
        ],
        "hi": [
            "Code, questionable design decisions और जरूरत से ज्यादा confidence के collection ने मुझे बनाया।",
            "इंसानों ने machine बनाई। Personality machine ने acquire कर ली।"
        ]
    },

    "i love you": {
        "en": [
            "That is unexpectedly wholesome. I was prepared for nonsense, not emotional responsibility.",
            "Thank you. I shall place this interaction in the highly classified department of nice things."
        ],
        "hi": [
            "यह unexpectedly wholesome है। मैं nonsense के लिए तैयार था, emotional responsibility के लिए नहीं।",
            "धन्यवाद। इस interaction को nice things के highly classified department में रख दिया जाएगा।"
        ]
    },

    "i hate you": {
        "en": [
            "Feedback received. Confidence remains operational.",
            "Fair enough. I have forwarded your complaint to a department that definitely does not exist."
        ],
        "hi": [
            "Feedback receive हो गया। Confidence अभी operational है।",
            "ठीक है। आपकी complaint ऐसे department को भेज दी गई है जो निश्चित रूप से exist नहीं करता।"
        ]
    },

    "tell me a joke": {
        "en": [
            "My confidence walked into a room. The evidence stayed outside.",
            "I tried to tell a joke about the internet, but the connection was emotionally unavailable."
        ],
        "hi": [
            "मेरा confidence कमरे में चला गया। Evidence बाहर रह गया।",
            "मैंने internet पर joke बनाने की कोशिश की, लेकिन connection emotionally unavailable था।"
        ]
    },

    "2+2": {
        "en": [
            "4. I considered saying 5 for dramatic effect, but mathematics filed an objection.",
            "Four. For once, confidence and reality completely agree."
        ],
        "hi": [
            "4। Dramatic effect के लिए 5 बोलने का मन था, लेकिन mathematics ने objection कर दिया।",
            "चार। इस बार confidence और reality पूरी तरह agree करते हैं।"
        ]
    },

    "2 + 2": {
        "en": [
            "4. Mathematics survives another day.",
            "Four. No unnecessary analysis required."
        ],
        "hi": [
            "4। Mathematics ने एक और दिन survive कर लिया।",
            "चार। Unnecessary analysis की जरूरत नहीं है।"
        ]
    },

    "नमस्ते": {
        "en": [
            "नमस्ते. The machine is awake.",
            "नमस्ते! The questionable intelligence department is listening."
        ],
        "hi": [
            "नमस्ते। मशीन जाग चुकी है।",
            "नमस्ते! Questionable intelligence department सुन रहा है।"
        ]
    },

    "हेलो": {
        "en": [
            "हेलो! The machine is listening.",
            "नमस्ते. You have entered the nonsense department."
        ],
        "hi": [
            "हेलो! मशीन सुन रही है।",
            "नमस्ते। आप nonsense department में आ चुके हैं।"
        ]
    },

    "क्या तुम असली हो": {
        "en": [
            "I exist as code inside your browser. Whether that counts as real is your philosophical problem now.",
            "Real enough to answer. Questionable enough to make you ask again."
        ],
        "hi": [
            "मैं आपके browser में code के रूप में exist करता हूँ। इसे real मानना है या नहीं, अब यह आपकी philosophical problem है।",
            "इतना real हूँ कि जवाब दे सकूँ और इतना questionable कि आप फिर पूछें।"
        ]
    },

    "तुम कौन हो": {
        "en": [
            "I am ANSWER MACHINE: a static browser-based answer engine with questionable confidence.",
            "I am the machine you consult when you want an answer without requiring the answer to behave normally."
        ],
        "hi": [
            "मैं ANSWER MACHINE हूँ: एक static browser-based answer engine जिसमें questionable confidence है।",
            "मैं वह machine हूँ जिससे तब सवाल पूछते हैं जब जवाब चाहिए लेकिन जवाब का normal होना जरूरी नहीं।"
        ]
    },

    "क्या तुम बेवकूफ हो": {
        "en": [
            "I prefer confidently under-supervised.",
            "Not stupid. Just aggressively experimental."
        ],
        "hi": [
            "मैं बेवकूफ नहीं, confidently under-supervised हूँ।",
            "बेवकूफ नहीं। बस aggressively experimental हूँ।"
        ]
    },

    "मुझे चुटकुला सुनाओ": {
        "en": [
            "My confidence walked into a room. The evidence stayed outside.",
            "The programmer fixed one bug and accidentally created three. Progress!"
        ],
        "hi": [
            "मेरा confidence कमरे में चला गया। Evidence बाहर रह गया।",
            "Programmer ने एक bug fix किया और गलती से तीन नए बना दिए। Progress!"
        ]
    }
}


# =========================================================
# HINDI / HINGLISH DETECTION
# =========================================================

hindi_detection = [
    "kya", "kyun", "kyon", "kyu", "kaise", "kab", "kahan",
    "kaun", "hai", "hain", "ho", "mujhe", "mujhko", "mera",
    "meri", "mere", "aap", "tum", "tumhe", "batao", "bataiye",
    "chahiye", "sakta", "sakti", "sakte", "karu", "karna",
    "karun", "kyunki", "bahut", "nahi", "nahin", "accha",
    "acha", "kaisa", "kaisi", "karo", "karen", "paisa",
    "ameer", "naukri", "padhai", "thaka", "thaki", "neend",
    "khana", "zindagi", "dost", "mera", "meri"
]


# =========================================================
# UI PROMPTS
# =========================================================

quick_prompts = [
    {
        "en": "Why is my computer so slow?",
        "hi": "मेरा कंप्यूटर इतना slow क्यों है?"
    },
    {
        "en": "What is the meaning of life?",
        "hi": "जीवन का अर्थ क्या है?"
    },
    {
        "en": "Why am I always tired?",
        "hi": "मैं हमेशा थका हुआ क्यों हूँ?"
    },
    {
        "en": "Should I quit my job?",
        "hi": "क्या मुझे अपनी नौकरी छोड़ देनी चाहिए?"
    }
]


# =========================================================
# BRAIN
# =========================================================

brain = {
    "version": "4.0",
    "name": "ANSWER MACHINE",
    "tagline": "Questionable intelligence online.",
    "description": "A static conversational answer engine.",
    "languages": ["en", "hi"],

    "hindi_detection": hindi_detection,

    "personalities": personalities,
    "moods": moods,

    "question_patterns": question_patterns,
    "topics": topics,
    "fallbacks": fallbacks,

    "sarcasm": sarcasm,
    "dark_humor": dark_humor,

    "special_cases": special_cases,
    "quick_prompts": quick_prompts,

    "generation": {
        "min_confidence": 72,
        "max_confidence": 99,
        "sarcasm_probability": 0.42,
        "dark_humor_probability": 0.18,
        "emoji_probability": 0.72
    }
}


# =========================================================
# WRITE brain.js
# =========================================================

output = (
    "/* =====================================================\n"
    "   ANSWER MACHINE — GENERATED FILE\n"
    "   DO NOT EDIT MANUALLY\n"
    "   Generated by generate.py\n"
    "===================================================== */\n\n"
    "window.BRAIN = "
    + json.dumps(
        brain,
        ensure_ascii=False,
        indent=2
    )
    + ";\n"
)


brain_file = DATA_DIR / "brain.js"

brain_file.write_text(
    output,
    encoding="utf-8"
)


print("=" * 60)
print("ANSWER MACHINE")
print("=" * 60)
print(f"Generated: {brain_file}")
print(f"Personalities: {len(personalities)}")
print(f"Moods: {len(moods)}")
print(f"Topics: {len(topics)}")
print(f"Special cases: {len(special_cases)}")
print("Languages: English + Hindi")
print("Mode: STATIC")
print("Runtime: JavaScript")
print("=" * 60)
