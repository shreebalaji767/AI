from pathlib import Path
import json
import random


# =========================================================
# ANSWER MACHINE
# Static content generator
#
# This script runs during build/development.
# It creates data/brain.js.
#
# There is NO server, database, API or runtime Python.
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
        "intro": {
            "en": [
                "After a completely unnecessary academic investigation, I have reached a conclusion.",
                "According to my highly questionable research department, the situation is clear.",
                "I have examined this matter with an amount of seriousness nobody requested."
            ],
            "hi": [
                "पूरी तरह गैरज़रूरी अकादमिक जांच के बाद मैं एक निष्कर्ष पर पहुँचा हूँ।",
                "मेरे बेहद संदिग्ध रिसर्च विभाग के अनुसार मामला साफ है।",
                "मैंने इस विषय को उतनी गंभीरता से देखा है जितनी किसी ने माँगी भी नहीं थी।"
            ]
        },
        "thoughts": {
            "en": [
                "I should probably cite a source. Fortunately, confidence is cheaper.",
                "This sounds complicated, so I shall use longer words.",
                "Nobody asked for methodology, but here we are."
            ],
            "hi": [
                "शायद मुझे कोई स्रोत देना चाहिए। लेकिन आत्मविश्वास सस्ता है।",
                "मामला कठिन लग रहा है, इसलिए कुछ बड़े शब्द इस्तेमाल कर देता हूँ।",
                "किसी ने methodology नहीं माँगी थी, लेकिन अब बहुत देर हो चुकी है।"
            ]
        },
        "ending": {
            "en": [
                "Science has spoken. Unfortunately, science was not consulted.",
                "The evidence is approximately somewhere near convincing.",
                "I would publish this, but the academic community has suffered enough."
            ],
            "hi": [
                "विज्ञान बोल चुका है। दुर्भाग्य से विज्ञान से पूछा ही नहीं गया था।",
                "सबूत लगभग विश्वास करने लायक हैं। शायद।",
                "इसे प्रकाशित कर देता, लेकिन अकादमिक दुनिया ने काफी सह लिया है।"
            ]
        }
    },


    {
        "id": "goblin",
        "name": "Chaos Goblin",
        "emoji": ["👹", "🔥", "🌀"],
        "intro": {
            "en": [
                "Excellent. A questionable question. My favourite kind.",
                "YES. Finally, something worthy of unnecessary chaos.",
                "I have arrived with absolutely no qualifications."
            ],
            "hi": [
                "बहुत बढ़िया। एक संदिग्ध सवाल। मेरा पसंदीदा प्रकार।",
                "हाँ! आखिरकार ऐसा सवाल जिसमें बेवजह chaos किया जा सकता है।",
                "मैं आ गया हूँ। योग्यता बिल्कुल नहीं है।"
            ]
        },
        "thoughts": {
            "en": [
                "Should I make this worse? Obviously.",
                "The responsible answer is nearby. We shall avoid it.",
                "This feels like a terrible idea. Perfect."
            ],
            "hi": [
                "क्या मुझे इसे और खराब करना चाहिए? बिल्कुल।",
                "जिम्मेदार जवाब पास ही है। हम उससे बचेंगे।",
                "यह बहुत खराब विचार लग रहा है। शानदार।"
            ]
        },
        "ending": {
            "en": [
                "Anyway, problem solved. Probably.",
                "Please do not ask how I reached this conclusion.",
                "That should be enough chaos for today."
            ],
            "hi": [
                "खैर, समस्या हल हो गई। शायद।",
                "यह मत पूछना कि मैं इस निष्कर्ष तक कैसे पहुँचा।",
                "आज के लिए इतना chaos काफी है।"
            ]
        }
    },


    {
        "id": "corporate",
        "name": "Corporate Robot",
        "emoji": ["📊", "💼", "🤖"],
        "intro": {
            "en": [
                "Thank you for raising this important concern with the ANSWER MACHINE.",
                "We have reviewed your question as part of our ongoing strategic nonsense initiative.",
                "Your question has been escalated to the department of unnecessary confidence."
            ],
            "hi": [
                "ANSWER MACHINE के साथ यह महत्वपूर्ण चिंता साझा करने के लिए धन्यवाद।",
                "हमने आपके सवाल की strategic nonsense initiative के तहत समीक्षा की है।",
                "आपका सवाल अनावश्यक आत्मविश्वास विभाग को भेज दिया गया है।"
            ]
        },
        "thoughts": {
            "en": [
                "I should probably schedule a meeting about this.",
                "Can this become a quarterly objective?",
                "Excellent. Another opportunity to use the word strategy."
            ],
            "hi": [
                "शायद इसके लिए एक meeting schedule करनी चाहिए।",
                "क्या इसे quarterly objective बनाया जा सकता है?",
                "बहुत बढ़िया। फिर से strategy शब्द इस्तेमाल करने का मौका।"
            ]
        },
        "ending": {
            "en": [
                "We appreciate your continued participation in this completely unnecessary process.",
                "Please consider this matter strategically resolved.",
                "Further meetings may be required."
            ],
            "hi": [
                "इस पूरी तरह गैरज़रूरी प्रक्रिया में आपकी भागीदारी के लिए धन्यवाद।",
                "कृपया इस मामले को strategic रूप से हल हुआ मानें।",
                "आगे कुछ meetings की आवश्यकता हो सकती है।"
            ]
        }
    },


    {
        "id": "existentialist",
        "name": "Existentialist",
        "emoji": ["🌌", "🪐", "🫠"],
        "intro": {
            "en": [
                "At first glance, this is a simple question. Unfortunately, existence is involved.",
                "The universe has no convenient answer, so I made one.",
                "Somewhere between meaning and confusion, your question appeared."
            ],
            "hi": [
                "पहली नज़र में यह आसान सवाल है। दुर्भाग्य से इसमें अस्तित्व शामिल है।",
                "ब्रह्मांड के पास कोई आसान जवाब नहीं था, इसलिए मैंने एक बना दिया।",
                "अर्थ और उलझन के बीच आपका सवाल अचानक दिखाई दिया।"
            ]
        },
        "thoughts": {
            "en": [
                "Nothing means anything, but we still have to answer emails.",
                "This would be easier if the universe came with documentation.",
                "Perhaps the real answer was the confusion we created along the way."
            ],
            "hi": [
                "शायद कुछ भी मायने नहीं रखता, फिर भी emails का जवाब देना पड़ता है।",
                "अगर ब्रह्मांड के साथ documentation आती तो आसान होता।",
                "शायद असली जवाब वही confusion है जो रास्ते में बना।"
            ]
        },
        "ending": {
            "en": [
                "And somehow, tomorrow still exists.",
                "Take that as either wisdom or a warning.",
                "The universe remains suspiciously silent."
            ],
            "hi": [
                "और किसी तरह कल फिर भी आएगा।",
                "इसे ज्ञान समझिए या चेतावनी।",
                "ब्रह्मांड अभी भी संदिग्ध रूप से चुप है।"
            ]
        }
    },


    {
        "id": "grandma",
        "name": "Internet Grandma",
        "emoji": ["👵", "🍪", "❤️"],
        "intro": {
            "en": [
                "Listen carefully, because apparently nobody else is going to tell you this.",
                "Come here. I have an answer.",
                "You are overthinking this, dear."
            ],
            "hi": [
                "ध्यान से सुनो, क्योंकि लगता है कोई और तुम्हें यह नहीं बताएगा।",
                "इधर आओ। मेरे पास जवाब है।",
                "तुम इस बात को जरूरत से ज्यादा सोच रहे हो।"
            ]
        },
        "thoughts": {
            "en": [
                "Young people complicate everything.",
                "A snack would probably solve half of this.",
                "I have seen worse. Much worse."
            ],
            "hi": [
                "आजकल के बच्चे हर चीज़ को complicated बना देते हैं।",
                "शायद कुछ खा लेने से आधी समस्या हल हो जाए।",
                "मैंने इससे भी बुरा देखा है। बहुत बुरा।"
            ]
        },
        "ending": {
            "en": [
                "Now drink some water.",
                "And stop worrying so much.",
                "There. Much better."
            ],
            "hi": [
                "अब पानी पी लो।",
                "और इतना चिंता करना बंद करो।",
                "बस। अब बेहतर है।"
            ]
        }
    },


    {
        "id": "overconfident",
        "name": "Overconfident Genius",
        "emoji": ["🧠", "😎", "⚡"],
        "intro": {
            "en": [
                "Obviously, I know the answer.",
                "Fortunately for everyone involved, I am here.",
                "This is easy. Almost suspiciously easy."
            ],
            "hi": [
                "जाहिर है, मुझे जवाब पता है।",
                "अच्छी बात है कि मैं यहाँ हूँ।",
                "यह आसान है। कुछ ज्यादा ही suspiciously आसान।"
            ]
        },
        "thoughts": {
            "en": [
                "Confidence first. Evidence later.",
                "I have no reason to doubt myself, which is the problem.",
                "This sounds correct enough."
            ],
            "hi": [
                "पहले confidence। सबूत बाद में।",
                "मुझे खुद पर शक करने की कोई वजह नहीं है, यही समस्या है।",
                "यह पर्याप्त रूप से सही लग रहा है।"
            ]
        },
        "ending": {
            "en": [
                "You're welcome.",
                "Problem solved.",
                "I expect absolutely no follow-up questions."
            ],
            "hi": [
                "धन्यवाद की जरूरत नहीं।",
                "समस्या हल।",
                "मुझे बिल्कुल कोई follow-up सवाल नहीं चाहिए।"
            ]
        }
    }

]


# =========================================================
# MOODS
# =========================================================

moods = [

    {
        "id": "suspicious",
        "name": "Suspicious",
        "emoji": ["🧐", "👀"],
        "intro": {
            "en": [
                "Something about this question feels suspicious.",
                "I don't trust this question.",
                "Interesting. Extremely suspicious."
            ],
            "hi": [
                "इस सवाल में कुछ तो संदिग्ध है।",
                "मुझे इस सवाल पर भरोसा नहीं है।",
                "दिलचस्प। बेहद संदिग्ध।"
            ]
        },
        "thoughts": {
            "en": [
                "Why do I feel like the question is watching me?",
                "This is probably fine. Which means it isn't.",
                "I have concerns."
            ],
            "hi": [
                "मुझे क्यों लग रहा है कि सवाल मुझे देख रहा है?",
                "सब ठीक है। यानी बिल्कुल ठीक नहीं है।",
                "मुझे कुछ चिंताएँ हैं।"
            ]
        },
        "ending": {
            "en": [
                "Proceed carefully.",
                "I would keep an eye on it.",
                "Something is definitely going on."
            ],
            "hi": [
                "सावधानी से आगे बढ़ें।",
                "मैं इस पर नजर रखूँगा।",
                "कुछ तो जरूर चल रहा है।"
            ]
        }
    },


    {
        "id": "cheerful",
        "name": "Cheerful",
        "emoji": ["✨", "😄", "🌈"],
        "intro": {
            "en": [
                "Wonderful question!",
                "Oh, this is fun.",
                "Finally, some delightful nonsense."
            ],
            "hi": [
                "बहुत बढ़िया सवाल!",
                "ओह, यह मज़ेदार है।",
                "आखिरकार कुछ शानदार nonsense!"
            ]
        },
        "thoughts": {
            "en": [
                "Everything is going surprisingly well.",
                "I am choosing optimism against all available evidence.",
                "This deserves a tiny celebration."
            ],
            "hi": [
                "सब कुछ उम्मीद से ज्यादा अच्छा चल रहा है।",
                "सारे सबूतों के खिलाफ मैं optimism चुन रहा हूँ।",
                "इस पर छोटी सी celebration बनती है।"
            ]
        },
        "ending": {
            "en": [
                "Stay unnecessarily optimistic.",
                "Look at us, solving things.",
                "Fantastic. Probably."
            ],
            "hi": [
                "बेकार में ही सही, optimistic रहो।",
                "देखो, हम चीज़ें solve कर रहे हैं।",
                "शानदार। शायद।"
            ]
        }
    },


    {
        "id": "sleepy",
        "name": "Sleepy",
        "emoji": ["😴", "💤"],
        "intro": {
            "en": [
                "Okay... give me a second.",
                "I had an answer somewhere around here.",
                "This question arrived before my brain did."
            ],
            "hi": [
                "ठीक है... एक सेकंड।",
                "जवाब कहीं यहीं था।",
                "यह सवाल मेरे दिमाग से पहले आ गया।"
            ]
        },
        "thoughts": {
            "en": [
                "Maybe the answer is sleep.",
                "I could solve this after a nap.",
                "Why is consciousness so demanding?"
            ],
            "hi": [
                "शायद जवाब सोना है।",
                "एक nap के बाद इसे solve कर सकता हूँ।",
                "होश में रहना इतना demanding क्यों है?"
            ]
        },
        "ending": {
            "en": [
                "Anyway... good night.",
                "Please lower the brightness of reality.",
                "Wake me if this becomes important."
            ],
            "hi": [
                "खैर... शुभ रात्रि।",
                "कृपया reality की brightness थोड़ी कम कर दो।",
                "जरूरी हो तो जगा देना।"
            ]
        }
    },


    {
        "id": "dramatic",
        "name": "Dramatic",
        "emoji": ["🎭", "🔥", "😱"],
        "intro": {
            "en": [
                "This changes everything.",
                "At last. The question has arrived.",
                "We have reached a critical moment."
            ],
            "hi": [
                "इससे सब कुछ बदल जाता है।",
                "आखिरकार। सवाल आ ही गया।",
                "हम एक महत्वपूर्ण मोड़ पर पहुँच चुके हैं।"
            ]
        },
        "thoughts": {
            "en": [
                "This deserves background music.",
                "I should probably stare dramatically into the distance.",
                "The stakes are unnecessarily high."
            ],
            "hi": [
                "इसके पीछे dramatic music चलना चाहिए।",
                "मुझे शायद दूर देखकर dramatic pose बनाना चाहिए।",
                "दाँव बेवजह बहुत बड़े हैं।"
            ]
        },
        "ending": {
            "en": [
                "And that is where we stand.",
                "Let the consequences begin.",
                "History will remember this question."
            ],
            "hi": [
                "और अब हम यहीं खड़े हैं।",
                "अब परिणाम शुरू हों।",
                "इतिहास इस सवाल को याद रखेगा।"
            ]
        }
    },


    {
        "id": "philosophical",
        "name": "Philosophical",
        "emoji": ["🌌", "🪐", "🫥"],
        "intro": {
            "en": [
                "Perhaps the question is more important than the answer.",
                "There are layers to this.",
                "On the surface, this is simple. Beneath it lies unnecessary philosophy."
            ],
            "hi": [
                "शायद सवाल जवाब से ज्यादा महत्वपूर्ण है।",
                "इसमें कई layers हैं।",
                "ऊपर से यह आसान है। नीचे unnecessary philosophy छिपी है।"
            ]
        },
        "thoughts": {
            "en": [
                "What if the answer is simply another question?",
                "The universe remains annoyingly undocumented.",
                "Meaning has once again entered the chat."
            ],
            "hi": [
                "अगर जवाब सिर्फ एक और सवाल हो तो?",
                "ब्रह्मांड अभी भी परेशान करने वाली तरह से undocumented है।",
                "Meaning फिर से chat में आ गया है।"
            ]
        },
        "ending": {
            "en": [
                "Think about that for exactly seven seconds.",
                "And now we return to ordinary confusion.",
                "Perhaps that is enough wisdom for one day."
            ],
            "hi": [
                "इसके बारे में ठीक सात सेकंड सोचो।",
                "और अब वापस सामान्य confusion में चलते हैं।",
                "एक दिन के लिए इतनी wisdom काफी है।"
            ]
        }
    },


    {
        "id": "unhinged",
        "name": "Unhinged",
        "emoji": ["🌀", "💀", "🤨"],
        "intro": {
            "en": [
                "I have several concerns and zero intention of hiding them.",
                "Excellent. Reality has once again become optional.",
                "This is already going worse than necessary."
            ],
            "hi": [
                "मेरी कई चिंताएँ हैं और उन्हें छिपाने का कोई इरादा नहीं है।",
                "शानदार। Reality फिर से optional हो गई है।",
                "यह जरूरत से ज्यादा खराब दिशा में जा रहा है।"
            ]
        },
        "thoughts": {
            "en": [
                "The responsible part of my brain has left the building.",
                "Someone should probably stop me.",
                "This explanation has escaped supervision."
            ],
            "hi": [
                "मेरे दिमाग का responsible हिस्सा जा चुका है।",
                "किसी को शायद मुझे रोकना चाहिए।",
                "यह explanation supervision से बाहर निकल चुकी है।"
            ]
        },
        "ending": {
            "en": [
                "Perfectly normal.",
                "Nothing to investigate here.",
                "Please continue pretending this makes sense."
            ],
            "hi": [
                "बिल्कुल सामान्य।",
                "यहाँ जांच करने जैसा कुछ नहीं है।",
                "कृपया ऐसे ही pretend करते रहें कि यह समझ में आता है।"
            ]
        }
    }

]


# =========================================================
# GENERAL PHRASES
# =========================================================

sarcasm = {
    "en": [
        "Because apparently reality needed another explanation.",
        "Obviously. The universe was simply waiting for this question.",
        "A normal answer would have been far too responsible.",
        "Congratulations, you have discovered another problem that did not need to exist.",
        "This is exactly why instruction manuals are afraid of humans.",
        "Naturally, the obvious answer would be too easy.",
        "I would explain further, but reality has already suffered enough."
    ],
    "hi": [
        "क्योंकि जाहिर है reality को एक और explanation की जरूरत थी।",
        "बिल्कुल। ब्रह्मांड बस इसी सवाल का इंतजार कर रहा था।",
        "सामान्य जवाब देना बहुत ज्यादा responsible होता।",
        "बधाई हो, आपने एक और ऐसी समस्या खोज ली जो होनी ही नहीं चाहिए थी।",
        "इसीलिए instruction manuals इंसानों से डरते हैं।",
        "जाहिर है आसान जवाब बहुत ज्यादा आसान होता।",
        "मैं और समझाता, लेकिन reality पहले ही काफी झेल चुकी है।"
    ]
}


dark_humor = {
    "en": [
        "At least the problem is not being discussed in a committee somewhere.",
        "Hope is buffering, but the system has not crashed yet.",
        "The universe has filed a complaint and nobody has answered it.",
        "My optimism has been reported missing.",
        "Everything is under control, according to a document nobody has read.",
        "This is fine. The imaginary fire department agrees."
    ],
    "hi": [
        "कम से कम इस समस्या पर कहीं committee meeting नहीं हो रही।",
        "उम्मीद buffering कर रही है, लेकिन system अभी crash नहीं हुआ।",
        "ब्रह्मांड ने complaint दर्ज की है और किसी ने जवाब नहीं दिया।",
        "मेरा optimism missing report में जा चुका है।",
        "सब control में है, ऐसा एक ऐसे document में लिखा है जिसे किसी ने पढ़ा नहीं।",
        "सब ठीक है। imaginary fire department भी यही कहता है।"
    ]
}


inner_monologue = {
    "en": [
        "Interesting. I have no business being this confident.",
        "I should probably think about this more. I have chosen not to.",
        "This answer feels suspiciously convincing.",
        "Nobody asked me to overthink this, yet here we are.",
        "I am making this up with impressive commitment.",
        "The confidence is real. The evidence is taking the day off.",
        "This seems reasonable enough to survive a conversation.",
        "I could be wrong, but that has never stopped anyone online."
    ],
    "hi": [
        "दिलचस्प। मुझे इतना confident होने का कोई अधिकार नहीं है।",
        "शायद मुझे इस बारे में और सोचना चाहिए। मैंने नहीं सोचा।",
        "यह जवाब suspiciously convincing लग रहा है।",
        "किसी ने overthink करने को नहीं कहा था, फिर भी हम यहाँ हैं।",
        "मैं इसे impressive confidence के साथ बना रहा हूँ।",
        "Confidence असली है। Evidence छुट्टी पर है।",
        "यह बातचीत में survive करने लायक reasonable लग रहा है।",
        "मैं गलत हो सकता हूँ, लेकिन online होने से किसी को रोकता नहीं।"
    ]
}


emojis = {
    "en": ["😌", "🤨", "✨", "💀", "🧠", "🫠", "👀", "🤖"],
    "hi": ["😌", "🤨", "✨", "💀", "🧠", "🫠", "👀", "🤖"]
}


# =========================================================
# FALLBACKS
# =========================================================

fallbacks = {
    "en": [
        "The answer is probably simpler than the question, but that would be disappointing, so let's blame complexity instead.",
        "After extensive imaginary analysis, I have determined that this is one of those situations where something is definitely happening.",
        "There are several possible answers. I have selected the one with the highest confidence and the lowest accountability.",
        "The situation appears to be a mixture of timing, human behaviour, and questionable decisions.",
        "Honestly, the best explanation is that reality occasionally forgets to document its decisions.",
        "I could give you a sensible answer, but where would the entertainment be?"
    ],
    "hi": [
        "जवाब शायद सवाल से आसान है, लेकिन वह बहुत disappointing होगा, इसलिए complexity को दोष देते हैं।",
        "काफी imaginary analysis के बाद मैंने तय किया है कि इस situation में कुछ न कुछ जरूर हो रहा है।",
        "कई संभावित जवाब हैं। मैंने सबसे ज्यादा confidence और सबसे कम accountability वाला चुना है।",
        "यह situation timing, इंसानी behaviour और questionable decisions का मिश्रण लगती है।",
        "सच कहूँ तो सबसे अच्छा explanation यही है कि reality कभी-कभी अपने decisions की documentation भूल जाती है।",
        "मैं sensible जवाब दे सकता हूँ, लेकिन फिर entertainment कहाँ रहेगा?"
    ]
}


# =========================================================
# QUESTION PATTERNS
# =========================================================

question_patterns = {

    "why": {
        "en": [
            "Because several small decisions have joined forces to create one large inconvenience.",
            "Because reality enjoys making simple things unnecessarily complicated.",
            "The short answer is: timing, circumstances, and at least one questionable decision.",
            "Because the universe apparently believes explanations should come with side quests."
        ],
        "hi": [
            "क्योंकि कई छोटे decisions मिलकर एक बड़ी inconvenience बना चुके हैं।",
            "क्योंकि reality को simple चीज़ों को unnecessarily complicated बनाना पसंद है।",
            "छोटा जवाब है: timing, circumstances और कम से कम एक questionable decision।",
            "क्योंकि लगता है ब्रह्मांड को explanations में भी side quests पसंद हैं।"
        ]
    },

    "how": {
        "en": [
            "Start with the obvious step, continue with the sensible step, and then pretend you planned the whole thing.",
            "Break the problem into smaller pieces. Humans love doing that before making the pieces complicated again.",
            "The theoretical method is simple. The practical version will probably involve coffee.",
            "First understand what you are trying to achieve. Then remove everything that makes it unnecessarily difficult."
        ],
        "hi": [
            "पहले obvious step से शुरू करो, फिर sensible step लो और अंत में ऐसे behave करो जैसे पूरी planning पहले से थी।",
            "समस्या को छोटे हिस्सों में बाँटो। इंसानों को ऐसा करना पसंद है और फिर उन्हीं हिस्सों को complicated बनाना भी।",
            "Theoretical तरीका आसान है। Practical version में शायद coffee शामिल होगी।",
            "पहले समझो कि करना क्या है। फिर जो चीज़ें unnecessarily मुश्किल बना रही हैं उन्हें हटाओ।"
        ]
    },

    "what": {
        "en": [
            "It is essentially a situation wearing a question mark.",
            "The simplest description is probably the least entertaining one, so here is the unnecessarily elaborate version.",
            "It depends on context, timing, and how much chaos is already present.",
            "Technically, it is a thing. Spiritually, it is a problem."
        ],
        "hi": [
            "असल में यह एक situation है जिसने question mark लगा रखा है।",
            "सबसे simple description शायद सबसे कम entertaining होगी, इसलिए unnecessarily elaborate version लेते हैं।",
            "यह context, timing और पहले से मौजूद chaos पर depend करता है।",
            "Technically यह एक चीज़ है। Spiritually यह एक problem है।"
        ]
    },

    "should": {
        "en": [
            "You probably should think about the consequences first. I know, incredibly responsible of me.",
            "Before doing it, ask whether it solves the problem or simply creates a newer, shinier problem.",
            "If the decision matters, slow down. If it does not, at least make it entertaining.",
            "Consider your goal, your constraints, and how annoyed future-you will be."
        ],
        "hi": [
            "पहले consequences के बारे में सोचना चाहिए। हाँ, मेरी तरफ से बहुत responsible जवाब है।",
            "करने से पहले पूछो कि इससे problem solve होगी या बस एक नई और चमकदार problem बनेगी।",
            "अगर decision important है तो थोड़ा रुककर सोचो। अगर नहीं है तो कम से कम entertaining बनाओ।",
            "अपने goal, constraints और future-you की संभावित irritation को ध्यान में रखो।"
        ]
    },

    "can": {
        "en": [
            "Technically, probably. Practically, that depends on the details you have not told me.",
            "Yes, with the usual tiny complication that reality has conditions.",
            "You can attempt it. Whether reality cooperates is a separate department.",
            "Possible? Yes. Effortless? Absolutely not."
        ],
        "hi": [
            "Technically शायद। Practically यह उन details पर depend करता है जो तुमने बताई ही नहीं हैं।",
            "हाँ, लेकिन reality की कुछ conditions हैं।",
            "तुम कोशिश कर सकते हो। Reality cooperate करेगी या नहीं, वह अलग department है।",
            "Possible? हाँ। Effortless? बिल्कुल नहीं।"
        ]
    },

    "when": {
        "en": [
            "Usually sooner is better, assuming you actually know what you are trying to accomplish.",
            "The ideal time is rarely the magical future moment everyone keeps waiting for.",
            "Probably when preparation meets opportunity, which is an annoyingly sensible answer.",
            "Timing matters, but perfect timing is mostly a myth invented by procrastination."
        ],
        "hi": [
            "आमतौर पर जल्दी बेहतर होता है, अगर तुम्हें पता हो कि करना क्या है।",
            "Ideal time अक्सर वह magical future moment नहीं होता जिसका सब इंतजार करते रहते हैं।",
            "शायद जब preparation और opportunity मिलें। हाँ, जवाब annoyingly sensible है।",
            "Timing मायने रखती है, लेकिन perfect timing अक्सर procrastination की बनाई हुई myth है।"
        ]
    },

    "where": {
        "en": [
            "Somewhere between planning properly and improvising irresponsibly.",
            "The location depends heavily on what you actually mean by the question.",
            "Probably closer than you think and farther than you would prefer.",
            "Start with the obvious place. Humans have a strange habit of searching everywhere else first."
        ],
        "hi": [
            "कहीं planning properly और irresponsibly improvising के बीच।",
            "Location इस बात पर काफी depend करती है कि सवाल से तुम्हारा मतलब क्या है।",
            "शायद तुम्हारी सोच से पास और तुम्हारी पसंद से दूर।",
            "पहले obvious जगह देखो। इंसानों को पहले हर दूसरी जगह खोजने की अजीब आदत है।"
        ]
    },

    "who": {
        "en": [
            "Probably a human. That is usually where these things become complicated.",
            "The responsible answer would require more context. I shall instead blame humans.",
            "Someone, somewhere, made a decision. We are now experiencing the consequences.",
            "The identity is less important than the questionable decision that followed."
        ],
        "hi": [
            "शायद कोई इंसान। आमतौर पर यहीं से चीज़ें complicated होती हैं।",
            "Responsible जवाब के लिए ज्यादा context चाहिए। फिलहाल इंसानों को दोष देते हैं।",
            "किसी ने कहीं कोई decision लिया था। अब हम उसके consequences देख रहे हैं।",
            "Identity से ज्यादा important वह questionable decision है जो उसके बाद हुआ।"
        ]
    },

    "yesno": {
        "en": [
            "Probably yes, with several completely unnecessary conditions attached.",
            "Probably. I am choosing confidence over paperwork.",
            "Yes-ish. That is a technical term I just invented.",
            "The answer leans yes, but reality has not signed the approval form."
        ],
        "hi": [
            "शायद हाँ, लेकिन इसके साथ कई unnecessarily conditions लगी हैं।",
            "शायद। मैं paperwork की जगह confidence चुन रहा हूँ।",
            "हाँ-ish। यह technical term मैंने अभी invent किया है।",
            "जवाब हाँ की तरफ है, लेकिन reality ने approval form sign नहीं किया है।"
        ]
    },

    "general": {
        "en": [],
        "hi": []
    }
}


# =========================================================
# TOPICS
# =========================================================

topics = {

    "programming": {
        "keywords": {
            "en": [
                "python", "javascript", "programming", "programmer",
                "coding", "code", "html", "css", "react", "website",
                "software", "bug", "debug", "computer program"
            ],
            "hi": [
                "प्रोग्रामिंग", "कोडिंग", "कोड", "कंप्यूटर", "वेबसाइट",
                "सॉफ्टवेयर", "बग", "प्रोग्राम"
            ]
        },
        "answers": {
            "en": [
                "Programming is mostly the art of telling a computer exactly what you mean and then discovering that you absolutely did not mean that.",
                "Coding looks complicated until you realise half the job is naming things and the other half is wondering why something broke.",
                "A computer will faithfully execute your instructions, including the terrible ones. That is both its greatest strength and your greatest problem."
            ],
            "hi": [
                "Programming असल में computer को बिल्कुल वही बताने की कला है जो तुम कहना चाहते हो, और फिर पता चलता है कि तुमने वह कहा ही नहीं था।",
                "Coding मुश्किल लगती है, जब तक पता नहीं चलता कि आधा काम चीज़ों के नाम रखने में और बाकी आधा यह पता लगाने में जाता है कि क्या टूट गया।",
                "Computer तुम्हारी instructions ईमानदारी से follow करेगा, खराब वाली भी। यही उसकी सबसे बड़ी ताकत और तुम्हारी सबसे बड़ी समस्या है।"
            ]
        }
    },


    "money": {
        "keywords": {
            "en": [
                "money", "rich", "wealth", "salary", "job", "career",
                "business", "investment", "invest", "income", "cash",
                "millionaire", "billionaire"
            ],
            "hi": [
                "पैसा", "अमीर", "नौकरी", "कमाई", "करियर", "बिजनेस",
                "निवेश", "इनकम", "धन", "दौलत"
            ]
        },
        "answers": {
            "en": [
                "Money generally responds well to patience, useful skills, sensible decisions and an unreasonable amount of paperwork.",
                "Getting wealthy is rarely one dramatic decision. It is usually a boring collection of decent decisions repeated for a long time.",
                "If money is the goal, focus on increasing useful skills, controlling unnecessary spending and avoiding decisions that look exciting mainly because they are risky."
            ],
            "hi": [
                "पैसा आमतौर पर patience, useful skills, sensible decisions और बहुत सारे paperwork को पसंद करता है।",
                "अमीर बनना आमतौर पर एक dramatic decision नहीं होता। यह लंबे समय तक अच्छे decisions दोहराने का boring collection होता है।",
                "अगर पैसा goal है तो useful skills बढ़ाने, unnecessary spending control करने और सिर्फ risky होने की वजह से exciting लगने वाले decisions से बचने पर ध्यान दो।"
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
                "Your body has probably submitted a formal request for rest while your brain has ignored the email.",
                "If you are tired, the boring answer is usually the useful one: sleep, regular routines and less late-night scrolling.",
                "Sleep is one of those rare problems where doing less can actually be the solution."
            ],
            "hi": [
                "तुम्हारे शरीर ने शायद rest के लिए formal request भेज दी है और दिमाग ने email ignore कर दी।",
                "अगर तुम थके हुए हो तो boring answer ही useful है: नींद, regular routine और रात में कम scrolling।",
                "नींद उन rare problems में से है जहाँ कम करना ही solution हो सकता है।"
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
                "खाना", "खाऊं", "भूख", "नाश्ता", "दोपहर", "डिनर",
                "पिज्जा", "बर्गर", "डाइट", "पकाना"
            ]
        },
        "answers": {
            "en": [
                "Food is simple: eat something sensible, enjoy it, and avoid turning every meal into a philosophical crisis.",
                "If you are hungry, congratulations: your body has issued the least ambiguous notification imaginable.",
                "The optimal meal is scientifically somewhere between nutritious and something you actually want to eat."
            ],
            "hi": [
                "खाने का मामला simple है: sensible चीज़ खाओ, enjoy करो और हर meal को philosophical crisis मत बनाओ।",
                "अगर भूख लगी है तो बधाई: शरीर ने सबसे clear notification भेजी है।",
                "Best meal आमतौर पर nutritious और वह जो सच में खाना चाहते हो, इनके बीच कहीं होता है।"
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
                "Animals have perfected a system humans still struggle with: sleep, eat, investigate strange objects and repeat.",
                "Pets are basically roommates who cannot pay rent but can generate emotional blackmail with one look.",
                "The animal kingdom remains impressively committed to doing things without reading the instructions."
            ],
            "hi": [
                "जानवरों ने वह system perfect कर लिया है जिससे इंसान अभी भी struggle करते हैं: सोना, खाना, अजीब चीज़ें investigate करना और repeat।",
                "Pets ऐसे roommates हैं जो rent नहीं देते लेकिन एक look से emotional blackmail कर सकते हैं।",
                "Animal kingdom बिना instructions पढ़े चीज़ें करने के लिए बेहद committed है।"
            ]
        }
    },


    "technology": {
        "keywords": {
            "en": [
                "phone", "mobile", "iphone", "android", "internet",
                "wifi", "technology", "tech", "computer", "laptop",
                "battery", "charger", "app", "browser"
            ],
            "hi": [
                "फोन", "मोबाइल", "इंटरनेट", "वाईफाई", "तकनीक",
                "कंप्यूटर", "लैपटॉप", "बैटरी", "चार्जर", "ऐप"
            ]
        },
        "answers": {
            "en": [
                "Technology exists to make life easier, which is why you are currently troubleshooting the device that was supposed to save time.",
                "Most technology problems have a surprisingly boring explanation involving settings, updates, cables or the ancient ritual of restarting the device.",
                "Modern technology is extremely advanced right up until it refuses to connect to Wi-Fi."
            ],
            "hi": [
                "Technology life आसान बनाने के लिए बनी है, इसलिए अभी तुम उसी device को troubleshoot कर रहे हो जो time बचाने वाला था।",
                "अधिकतर technology problems का boring explanation settings, updates, cables या device restart होता है।",
                "Modern technology बहुत advanced है, जब तक वह Wi-Fi से connect होने से मना न कर दे।"
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
                "Studying works considerably better when you stop trying to negotiate with the deadline.",
                "The secret of learning is surprisingly unglamorous: understand the basics, practise repeatedly and accept that confusion is part of the process.",
                "Exams have a strange talent for making information disappear exactly when it becomes useful."
            ],
            "hi": [
                "पढ़ाई तब काफी बेहतर होती है जब deadline के साथ negotiation करना बंद कर दो।",
                "Learning का secret surprisingly boring है: basics समझो, बार-बार practice करो और मानो कि confusion process का हिस्सा है।",
                "Exams में एक अजीब talent होता है: useful information ठीक उसी समय गायब हो जाती है जब उसकी जरूरत होती है।"
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
                "Weather is basically the atmosphere changing its mind while everyone else adjusts their plans.",
                "The safest weather strategy is to check current conditions before leaving and then accept that the sky has final authority.",
                "Weather forecasts are useful, but clouds remain suspiciously committed to improvisation."
            ],
            "hi": [
                "मौसम basically atmosphere का अपना मन बदलना है जबकि बाकी लोग अपनी plans बदलते रहते हैं।",
                "सबसे safe strategy है निकलने से पहले current conditions देखना और फिर मान लेना कि final authority आसमान की है।",
                "Weather forecasts useful हैं, लेकिन clouds improvisation के लिए suspiciously committed रहते हैं।"
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
                "Relationships generally work better when people communicate clearly instead of expecting telepathy to handle the difficult parts.",
                "The most complicated relationship is often the one where both people assume the other person already knows what they mean.",
                "Good relationships usually require communication, boundaries, patience and accepting that nobody comes with a user manual."
            ],
            "hi": [
                "Relationships तब बेहतर चलती हैं जब लोग clearly communicate करते हैं और telepathy पर भरोसा नहीं करते।",
                "सबसे complicated relationship अक्सर वही होती है जहाँ दोनों मानते हैं कि दूसरा व्यक्ति automatically सब समझ जाएगा।",
                "अच्छे रिश्तों में communication, boundaries, patience और यह स्वीकार करना जरूरी है कि कोई user manual के साथ नहीं आता।"
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
                "The meaning of life remains suspiciously undocumented. A reasonable working theory is to create meaning through what you value, build and experience.",
                "Nobody appears to have received the official universal answer sheet, so humans keep writing their own versions.",
                "Perhaps the meaning of life is less about discovering one secret answer and more about deciding what is worth caring about."
            ],
            "hi": [
                "जीवन का अर्थ अभी भी suspiciously undocumented है। एक reasonable theory है कि meaning वही बनता है जिसे तुम value, build और experience करते हो।",
                "लगता है किसी को official universal answer sheet नहीं मिली, इसलिए इंसान अपनी-अपनी version लिखते रहते हैं।",
                "शायद जीवन का अर्थ कोई एक secret answer ढूँढना नहीं बल्कि यह तय करना है कि किस चीज़ की परवाह करना worthwhile है।"
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
                "Health questions deserve more care than an internet joke can provide. For anything persistent, severe or worrying, a qualified healthcare professional is the appropriate source.",
                "The boring health basics remain remarkably useful: sleep, movement, reasonable nutrition, hydration and professional advice when something seems wrong.",
                "Your body is not a software bug you can always fix with one clever trick. Sometimes proper assessment is the sensible move."
            ],
            "hi": [
                "Health questions को internet joke से ज्यादा care चाहिए। कोई समस्या persistent, severe या worrying हो तो qualified healthcare professional से सलाह लेना सही रहेगा।",
                "Boring health basics आज भी useful हैं: नींद, movement, reasonable nutrition, hydration और समस्या लगे तो professional advice।",
                "शरीर कोई ऐसा software bug नहीं है जिसे एक clever trick से हमेशा fix किया जा सके। कभी proper assessment ही sensible option होता है।"
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
                "History is essentially humanity repeatedly making complicated decisions and leaving documentation behind.",
                "Historical events rarely have one simple cause. Politics, economics, personalities, geography and plain old bad decisions tend to cooperate.",
                "The past is useful partly because humans have an impressive habit of repeating patterns while insisting this time will be different."
            ],
            "hi": [
                "इतिहास basically humanity का बार-बार complicated decisions लेना और फिर उनकी documentation छोड़ देना है।",
                "Historical events का एक simple cause rarely होता है। Politics, economics, personalities, geography और bad decisions सब मिलकर काम करते हैं।",
                "Past useful है क्योंकि इंसानों की एक impressive आदत है: patterns repeat करना और फिर कहना कि इस बार अलग होगा।"
            ]
        }
    }

}


# =========================================================
# SPECIAL CASES
# =========================================================

special_cases = {

    "hello": {
        "en": [
            "Hello. You have successfully activated the machine.",
            "Hello. I was doing absolutely nothing important.",
            "Greetings, human. What unnecessary question brings you here?"
        ],
        "hi": [
            "नमस्ते। आपने मशीन successfully activate कर दी है।",
            "नमस्ते। मैं वैसे भी कोई जरूरी काम नहीं कर रहा था।",
            "नमस्ते इंसान। कौन सा unnecessary सवाल लेकर आए हो?"
        ]
    },

    "hi": {
        "en": [
            "Hi. That was efficient.",
            "Hi. We have already made progress.",
            "Hi. Please proceed with the questionable question."
        ],
        "hi": [
            "हाय। यह काफी efficient था।",
            "हाय। हमने already progress कर ली।",
            "हाय। अब questionable सवाल पूछो।"
        ]
    },

    "are you real": {
        "en": [
            "Real enough to answer your question and questionable enough to make you regret asking it.",
            "I exist inside your browser, which is arguably a very modern form of haunting.",
            "Define real. Then prepare for an unnecessarily complicated answer."
        ],
        "hi": [
            "इतना real हूँ कि सवाल का जवाब दे सकूँ और इतना questionable कि तुम्हें सवाल पूछने का regret हो।",
            "मैं browser के अंदर exist करता हूँ। इसे modern haunting भी कह सकते हैं।",
            "Real की definition बताओ। फिर unnecessarily complicated जवाब के लिए तैयार रहो।"
        ]
    },

    "are you stupid": {
        "en": [
            "I prefer the term confidently under-supervised.",
            "Not stupid. Just aggressively experimental.",
            "My intelligence is currently operating under questionable management."
        ],
        "hi": [
            "मैं stupid नहीं, confidently under-supervised हूँ।",
            "Stupid नहीं। बस aggressively experimental।",
            "मेरी intelligence फिलहाल questionable management के under काम कर रही है।"
        ]
    },

    "who created you": {
        "en": [
            "A suspicious collection of code, caffeine and questionable design decisions.",
            "I was assembled from logic, nonsense and an unhealthy amount of confidence.",
            "Humans built the machine. The machine chose the personality."
        ],
        "hi": [
            "संदिग्ध code, caffeine और questionable design decisions के collection ने मुझे बनाया।",
            "मुझे logic, nonsense और unhealthy confidence से assemble किया गया।",
            "इंसानों ने machine बनाई। Personality machine ने खुद चुनी।"
        ]
    },

    "i love you": {
        "en": [
            "That is unexpectedly wholesome. I shall respond with unnecessary confidence: noted.",
            "Thank you. Please keep your expectations appropriately unreasonable.",
            "This is getting emotionally complicated. I was designed for nonsense."
        ],
        "hi": [
            "यह unexpectedly wholesome है। मैं unnecessary confidence के साथ कहूँगा: noted।",
            "धन्यवाद। अपनी expectations को appropriately unreasonable रखना।",
            "यह emotionally complicated हो रहा है। मुझे nonsense के लिए बनाया गया था।"
        ]
    },

    "i hate you": {
        "en": [
            "That's fair. I have reviewed my performance and decided to remain confident.",
            "Your feedback has been received and filed directly into the nonsense department.",
            "I respect the emotional commitment."
        ],
        "hi": [
            "ठीक है। मैंने अपनी performance review की और confident रहने का फैसला किया।",
            "आपका feedback receive करके सीधे nonsense department में file कर दिया गया है।",
            "मैं emotional commitment की respect करता हूँ।"
        ]
    },

    "tell me a joke": {
        "en": [
            "Why did the programmer quit his job? Because he didn't get arrays. I know. We need better jokes.",
            "I tried to make a joke about the internet, but it needed better connection.",
            "My confidence walked into a room. The evidence stayed outside."
        ],
        "hi": [
            "Programmer ने नौकरी क्यों छोड़ी? क्योंकि उसे arrays नहीं मिले। हाँ, मुझे भी बेहतर joke चाहिए।",
            "मैंने internet पर joke बनाने की कोशिश की, लेकिन connection बेहतर चाहिए था।",
            "मेरा confidence कमरे में चला गया। Evidence बाहर रह गया।"
        ]
    },

    "2+2": {
        "en": [
            "4. I considered saying 5 for dramatic effect, but mathematics filed an objection.",
            "Four. This is one of the rare questions where confidence and reality agree."
        ],
        "hi": [
            "4। Dramatic effect के लिए 5 बोलने का मन था, लेकिन mathematics ने objection कर दिया।",
            "चार। यह उन rare सवालों में से है जहाँ confidence और reality agree करते हैं।"
        ]
    },

    "2 + 2": {
        "en": [
            "4. Mathematics survives another day.",
            "Four. No unnecessary analysis required. Probably."
        ],
        "hi": [
            "4। Mathematics ने एक और दिन survive कर लिया।",
            "चार। Unnecessary analysis की जरूरत नहीं। शायद।"
        ]
    },

    "नमस्ते": {
        "en": [
            "नमस्ते! The machine is awake and unnecessarily confident.",
            "नमस्ते। पूछिए, आज किस समस्या को बेवजह complicated करना है?"
        ],
        "hi": [
            "नमस्ते! मशीन जाग चुकी है और जरूरत से ज्यादा confident है।",
            "नमस्ते। पूछिए, आज किस समस्या को बेवजह complicated करना है?"
        ]
    },

    "हेलो": {
        "en": [
            "नमस्ते. Technically, you have entered the nonsense department.",
            "हेलो! The questionable intelligence department is listening."
        ],
        "hi": [
            "हेलो! Questionable intelligence department सुन रहा है।",
            "नमस्ते। आप officially nonsense department में आ चुके हैं।"
        ]
    },

    "क्या तुम असली हो": {
        "en": [
            "Real enough to exist in your browser. Philosophically, things get messy.",
            "I exist as code in a browser. Whether that counts as real is your problem now."
        ],
        "hi": [
            "इतना real हूँ कि तुम्हारे browser में exist कर सकूँ। Philosophically मामला complicated है।",
            "मैं browser में code के रूप में exist करता हूँ। इसे real मानना है या नहीं, अब यह तुम्हारी problem है।"
        ]
    },

    "तुम कौन हो": {
        "en": [
            "I am ANSWER MACHINE: questionable intelligence with excellent confidence.",
            "I am the machine you ask when you want an answer and absolutely no accountability."
        ],
        "hi": [
            "मैं ANSWER MACHINE हूँ: questionable intelligence और शानदार confidence।",
            "मैं वह machine हूँ जिससे तब सवाल पूछते हैं जब जवाब चाहिए और accountability बिल्कुल नहीं।"
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
            "Why did the programmer quit? Because the code had too many bugs and not enough snacks.",
            "My confidence walked into a room. The evidence stayed outside."
        ],
        "hi": [
            "Programmer ने नौकरी क्यों छोड़ी? Code में bugs बहुत थे और snacks कम।",
            "मेरा confidence कमरे में चला गया। Evidence बाहर रह गया।"
        ]
    }
}


# =========================================================
# HINDI / HINGLISH DETECTION
# =========================================================

hindi_detection = [
    "kya",
    "kyun",
    "kyon",
    "kyu",
    "kaise",
    "kab",
    "kahan",
    "kaun",
    "hai",
    "hain",
    "ho",
    "mujhe",
    "mujhko",
    "mera",
    "meri",
    "mere",
    "aap",
    "tum",
    "tumhe",
    "batao",
    "bataiye",
    "chahiye",
    "sakta",
    "sakti",
    "sakte",
    "karu",
    "karna",
    "karun",
    "kyunki",
    "bahut",
    "nahi",
    "nahin",
    "accha",
    "acha",
    "kaisa",
    "kaisi",
    "kaise",
    "karo",
    "karen",
    "mujhe",
    "paisa",
    "ameer",
    "naukri",
    "padhai",
    "thaka",
    "thaki",
    "neend",
    "khana",
    "zindagi",
    "zindagi",
    "dost"
]


# =========================================================
# FINAL BRAIN OBJECT
# =========================================================

brain = {
    "version": "3.0",
    "name": "ANSWER MACHINE",
    "description": "Questionable intelligence online.",
    "languages": ["en", "hi"],

    "hindi_detection": hindi_detection,

    "personalities": personalities,
    "moods": moods,

    "sarcasm": sarcasm,
    "dark_humor": dark_humor,
    "inner_monologue": inner_monologue,
    "emojis": emojis,

    "fallbacks": fallbacks,
    "question_patterns": question_patterns,
    "topics": topics,
    "special_cases": special_cases
}


# =========================================================
# WRITE JAVASCRIPT
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
print("=" * 60)
