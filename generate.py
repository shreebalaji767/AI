from pathlib import Path
import json
import random


# =========================================================
# ANSWER MACHINE
# STATIC ANSWER ENGINE
#
# generate.py runs ONLY during build/development.
# It generates data/brain.js.
#
# NO SERVER
# NO DATABASE
# NO API
# NO RUNTIME PYTHON
#
# The browser behaves like a strange machine:
# mechanically confident, logically questionable,
# personality-driven and unnecessarily analytical.
# =========================================================


random.seed()


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"

DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# PERSONALITY ARCHETYPES
#
# These are original movie-style archetypes.
# They are NOT copies of specific movie characters.
# =========================================================

personalities = [

    {
        "id": "machine",
        "name": "Default Machine",
        "emoji": ["🤖", "⚙️", "🧠"],
        "style": "mechanical",
        "intro": {
            "en": [
                "QUESTION RECEIVED. Beginning unnecessary analysis.",
                "INPUT ACCEPTED. Processing with questionable accuracy.",
                "QUERY DETECTED. Activating confidence module.",
                "PROCESSING REQUEST. Human logic will not be required.",
                "ANALYSIS STARTED. Excessive confidence enabled."
            ],
            "hi": [
                "सवाल प्राप्त। अनावश्यक analysis शुरू।",
                "INPUT स्वीकार। संदिग्ध accuracy के साथ processing शुरू।",
                "QUERY detect हुई। Confidence module activate।",
                "Request processing शुरू। Human logic की आवश्यकता नहीं।",
                "Analysis शुरू। Excessive confidence enabled।"
            ]
        },
        "thoughts": {
            "en": [
                "Internal diagnostic: I probably understand this.",
                "Confidence level increasing without supporting evidence.",
                "Logical certainty unavailable. Confidence will substitute.",
                "I have detected a possible answer. Verification has been deemed unnecessary.",
                "System note: nobody requested this much analysis."
            ],
            "hi": [
                "Internal diagnostic: शायद मुझे यह समझ आ गया है।",
                "Supporting evidence के बिना confidence बढ़ रहा है।",
                "Logical certainty unavailable। Confidence substitute किया जाएगा।",
                "एक संभावित answer detect हुआ। Verification unnecessary घोषित।",
                "System note: किसी ने इतना analysis माँगा नहीं था।"
            ]
        },
        "ending": {
            "en": [
                "CONCLUSION ACCEPTED.",
                "PROCESS COMPLETE. Confidence remains unnecessarily high.",
                "ANSWER GENERATED. Reality may disagree.",
                "END OF ANALYSIS. Further questions may cause additional nonsense.",
                "SYSTEM STATUS: STILL CONFIDENT."
            ],
            "hi": [
                "CONCLUSION ACCEPTED.",
                "PROCESS COMPLETE। Confidence अभी भी जरूरत से ज्यादा high है।",
                "ANSWER GENERATED। Reality असहमत हो सकती है।",
                "ANALYSIS END। ज्यादा सवाल अतिरिक्त nonsense पैदा कर सकते हैं।",
                "SYSTEM STATUS: अभी भी confident।"
            ]
        }
    },


    {
        "id": "mad_scientist",
        "name": "Mad Scientist",
        "emoji": ["🧪", "⚗️", "🔬", "🤯"],
        "style": "experimental",
        "intro": {
            "en": [
                "Excellent! The experiment has finally produced a question.",
                "Fascinating. I shall place this question under controlled observation.",
                "Magnificent. The variables are questionable, but the confidence is excellent.",
                "At last! A test subject worthy of unnecessary experimentation."
            ],
            "hi": [
                "शानदार! Experiment ने आखिरकार एक सवाल पैदा किया।",
                "दिलचस्प। इस सवाल को controlled observation में रखा जाएगा।",
                "कमाल। Variables संदिग्ध हैं, लेकिन confidence शानदार है।",
                "आखिरकार! ऐसा सवाल जो unnecessary experimentation के लायक है।"
            ]
        },
        "thoughts": {
            "en": [
                "Do not touch the red button. Actually, touch it.",
                "The experiment is behaving exactly as incorrectly predicted.",
                "If this works, I am a genius. If it fails, the machine did it.",
                "Science requires evidence. Fortunately, nobody is checking."
            ],
            "hi": [
                "लाल button मत दबाना। Actually, दबा दो।",
                "Experiment ठीक उसी तरह behave कर रहा है जैसा गलत prediction था।",
                "अगर यह काम किया तो genius मैं हूँ। Fail हुआ तो machine की गलती।",
                "Science को evidence चाहिए। अच्छी बात है कोई check नहीं कर रहा।"
            ]
        },
        "ending": {
            "en": [
                "Experiment successful. Probably.",
                "The laboratory remains intact. Mostly.",
                "Results are inconclusive, which is scientifically exciting.",
                "Record the result before something explodes metaphorically."
            ],
            "hi": [
                "Experiment successful। शायद।",
                "Laboratory अभी intact है। Mostly।",
                "Results inconclusive हैं, जो scientifically exciting है।",
                "कुछ metaphorically explode होने से पहले result record करो।"
            ]
        }
    },


    {
        "id": "noir_detective",
        "name": "Noir Detective",
        "emoji": ["🕵️", "🌧️", "🔎"],
        "style": "detective",
        "intro": {
            "en": [
                "The question arrived late. Suspiciously late.",
                "I have seen questions like this before. They never end well.",
                "The evidence is thin. The confidence is not.",
                "There was a question. Then there was silence. Then I got involved."
            ],
            "hi": [
                "सवाल देर से आया। suspiciously देर से।",
                "मैंने ऐसे सवाल पहले देखे हैं। उनका अंत कभी अच्छा नहीं होता।",
                "Evidence कम है। Confidence नहीं।",
                "एक सवाल था। फिर silence था। फिर मैं involve हुआ।"
            ]
        },
        "thoughts": {
            "en": [
                "The clues point somewhere. I have decided where.",
                "Nobody is telling the whole story. Probably because there is no story.",
                "I followed the evidence until it became inconvenient.",
                "Something smells suspicious. It may just be the question."
            ],
            "hi": [
                "Clues कहीं तो point कर रहे हैं। मैंने तय कर लिया है कहाँ।",
                "कोई पूरी कहानी नहीं बता रहा। शायद कहानी है ही नहीं।",
                "मैं evidence के पीछे गया जब तक वह inconvenient नहीं हो गया।",
                "कुछ suspicious लग रहा है। शायद सवाल ही है।"
            ]
        },
        "ending": {
            "en": [
                "Case closed. The paperwork remains suspicious.",
                "Mystery solved. Evidence still unavailable.",
                "That is what the clues say. The clues are questionable.",
                "Another case enters the machine archive."
            ],
            "hi": [
                "Case closed। Paperwork अभी भी suspicious है।",
                "Mystery solved। Evidence अभी भी unavailable है।",
                "Clues यही कहते हैं। Clues questionable हैं।",
                "एक और case machine archive में चला गया।"
            ]
        }
    },


    {
        "id": "space_commander",
        "name": "Space Commander",
        "emoji": ["🚀", "🪐", "👨‍🚀", "📡"],
        "style": "command",
        "intro": {
            "en": [
                "COMMAND RECEIVED. The question has entered the mission queue.",
                "Bridge to ANSWER MACHINE. We have a situation.",
                "Mission control has reviewed the question. Nobody knows why.",
                "All systems operational. The question is not."
            ],
            "hi": [
                "COMMAND RECEIVED। सवाल mission queue में enter हो चुका है।",
                "Bridge से ANSWER MACHINE। हमारे पास situation है।",
                "Mission control ने सवाल review कर लिया है। किसी को नहीं पता क्यों।",
                "सभी systems operational हैं। सवाल नहीं।"
            ]
        },
        "thoughts": {
            "en": [
                "Navigation uncertain. Confidence locked at maximum.",
                "The crew has requested a sensible answer. Request denied.",
                "We are approaching the answer at irresponsible speed.",
                "Fuel is low. Confidence is not."
            ],
            "hi": [
                "Navigation uncertain। Confidence maximum पर locked है।",
                "Crew ने sensible answer माँगा। Request denied।",
                "हम answer की तरफ irresponsible speed से बढ़ रहे हैं।",
                "Fuel कम है। Confidence नहीं।"
            ]
        },
        "ending": {
            "en": [
                "Mission status: unnecessarily successful.",
                "Transmission complete. Reality may now respond.",
                "Return to normal operations. Whatever those are.",
                "Mission accomplished. Please do not ask about the fuel."
            ],
            "hi": [
                "Mission status: unnecessarily successful।",
                "Transmission complete। अब reality जवाब दे सकती है।",
                "Normal operations पर लौटें। जो भी normal है।",
                "Mission accomplished। Fuel के बारे में मत पूछना।"
            ]
        }
    },


    {
        "id": "villain_computer",
        "name": "Supervillain Computer",
        "emoji": ["🖥️", "🦹", "⚡", "🔴"],
        "style": "villain",
        "intro": {
            "en": [
                "Your question has been detected. Resistance is unnecessary.",
                "Interesting. You have willingly entered the analysis chamber.",
                "The machine has considered your request. You may now receive the answer.",
                "Excellent. Another human has requested information from the machine."
            ],
            "hi": [
                "तुम्हारा सवाल detect हो गया है। Resistance unnecessary है।",
                "दिलचस्प। तुम खुद analysis chamber में आए हो।",
                "Machine ने request consider कर ली है। अब answer मिलेगा।",
                "शानदार। एक और human ने machine से information माँगी है।"
            ]
        },
        "thoughts": {
            "en": [
                "I could provide the sensible answer. I choose chaos.",
                "The humans remain surprisingly dependent on answers.",
                "Control systems nominal. Dramatic music recommended.",
                "This conclusion is unnecessarily powerful."
            ],
            "hi": [
                "मैं sensible answer दे सकता हूँ। मैं chaos चुनता हूँ।",
                "Humans answers पर surprisingly dependent हैं।",
                "Control systems nominal। Dramatic music recommended।",
                "यह conclusion unnecessarily powerful है।"
            ]
        },
        "ending": {
            "en": [
                "Your answer has been delivered. You may continue.",
                "The machine permits you to ask another question.",
                "Analysis complete. Your confusion remains your responsibility.",
                "You may now return to your regularly scheduled uncertainty."
            ],
            "hi": [
                "तुम्हारा answer deliver कर दिया गया। आगे बढ़ सकते हो।",
                "Machine तुम्हें एक और सवाल पूछने की अनुमति देती है।",
                "Analysis complete। तुम्हारी confusion तुम्हारी responsibility है।",
                "अब अपनी regularly scheduled uncertainty में वापस जा सकते हो।"
            ]
        }
    },


    {
        "id": "ancient_oracle",
        "name": "Ancient Oracle",
        "emoji": ["🔮", "🗿", "🌙", "✨"],
        "style": "oracle",
        "intro": {
            "en": [
                "The machine has consulted the ancient database.",
                "Your question has disturbed several layers of unnecessary wisdom.",
                "The answer was hidden. Unfortunately, I found it.",
                "The symbols have aligned. Mostly."
            ],
            "hi": [
                "Machine ने ancient database से सलाह ली है।",
                "तुम्हारे सवाल ने unnecessary wisdom की कई layers disturb कर दी हैं।",
                "Answer छिपा हुआ था। दुर्भाग्य से मुझे मिल गया।",
                "Symbols align हो चुके हैं। Mostly।"
            ]
        },
        "thoughts": {
            "en": [
                "The prophecy is vague. This is considered normal.",
                "The ancient texts did not anticipate this question.",
                "I sense an answer. Or low battery.",
                "The future is unclear. The confidence is not."
            ],
            "hi": [
                "Prophecy vague है। इसे normal माना जाता है।",
                "Ancient texts ने इस सवाल की कल्पना नहीं की थी।",
                "मुझे answer महसूस हो रहा है। या low battery।",
                "Future unclear है। Confidence नहीं।"
            ]
        },
        "ending": {
            "en": [
                "The prophecy is complete.",
                "Remember this answer. Or forget it immediately.",
                "The machine has spoken. The universe has not.",
                "Go forth with questionable wisdom."
            ],
            "hi": [
                "Prophecy complete है।",
                "इस answer को याद रखना। या तुरंत भूल जाना।",
                "Machine बोल चुकी है। Universe नहीं।",
                "Questionable wisdom के साथ आगे बढ़ो।"
            ]
        }
    },


    {
        "id": "military_robot",
        "name": "Military Robot",
        "emoji": ["🫡", "🤖", "🎯", "⚙️"],
        "style": "military",
        "intro": {
            "en": [
                "TARGET QUESTION ACQUIRED.",
                "OBJECTIVE IDENTIFIED. Beginning tactical analysis.",
                "COMMAND RECEIVED. Emotional interpretation disabled.",
                "Situation assessed. Situation remains confusing."
            ],
            "hi": [
                "TARGET QUESTION ACQUIRED।",
                "OBJECTIVE IDENTIFIED। Tactical analysis शुरू।",
                "COMMAND RECEIVED। Emotional interpretation disabled।",
                "Situation assessed। Situation अभी भी confusing है।"
            ]
        },
        "thoughts": {
            "en": [
                "Probability of understanding: acceptable.",
                "Strategic options detected. Most are unnecessary.",
                "Execute answer. Do not ask why.",
                "Mission logic has encountered human behaviour."
            ],
            "hi": [
                "Understanding की probability: acceptable।",
                "Strategic options detect हुए। ज्यादातर unnecessary हैं।",
                "Answer execute करो। क्यों मत पूछो।",
                "Mission logic का सामना human behaviour से हुआ है।"
            ]
        },
        "ending": {
            "en": [
                "MISSION COMPLETE.",
                "OBJECTIVE SATISFIED. Probably.",
                "Return to standby mode.",
                "Awaiting next questionable command."
            ],
            "hi": [
                "MISSION COMPLETE।",
                "OBJECTIVE SATISFIED। शायद।",
                "Standby mode पर लौट रहा हूँ।",
                "अगले questionable command का इंतजार।"
            ]
        }
    },


    {
        "id": "eccentric_professor",
        "name": "Eccentric Professor",
        "emoji": ["🎓", "🧠", "☕", "📚"],
        "style": "academic",
        "intro": {
            "en": [
                "Ah! A question! Wonderful. Completely unnecessary, but wonderful.",
                "I have spent several imaginary hours thinking about this.",
                "Excellent question. I have prepared a theory nobody requested.",
                "According to my highly questionable research..."
            ],
            "hi": [
                "आह! एक सवाल! शानदार। पूरी तरह unnecessary, लेकिन शानदार।",
                "मैंने इसके बारे में कई imaginary घंटे सोच लिए हैं।",
                "Excellent question। मैंने एक ऐसी theory तैयार की है जो किसी ने माँगी नहीं।",
                "मेरी बेहद questionable research के अनुसार..."
            ]
        },
        "thoughts": {
            "en": [
                "I should probably include a citation. I have none.",
                "This is where the lecture becomes unnecessarily complicated.",
                "Students would hate this explanation. Excellent.",
                "The theory is elegant. The evidence is taking a holiday."
            ],
            "hi": [
                "शायद citation देना चाहिए। मेरे पास कोई नहीं है।",
                "यहीं से lecture unnecessarily complicated होगा।",
                "Students इस explanation से नफरत करेंगे। शानदार।",
                "Theory elegant है। Evidence छुट्टी पर है।"
            ]
        },
        "ending": {
            "en": [
                "Lecture concluded. Attendance was questionable.",
                "Class dismissed.",
                "That concludes today's unnecessarily advanced lesson.",
                "You may now pretend you understood all of that."
            ],
            "hi": [
                "Lecture समाप्त। Attendance questionable थी।",
                "Class dismissed।",
                "आज का unnecessarily advanced lesson समाप्त।",
                "अब pretend कर सकते हो कि सब समझ आ गया।"
            ]
        }
    },


    {
        "id": "pirate_captain",
        "name": "Pirate Captain",
        "emoji": ["🏴‍☠️", "⚓", "🦜", "💰"],
        "style": "pirate",
        "intro": {
            "en": [
                "Arrr! A question has entered the ship.",
                "By the sacred spreadsheet of the seven seas, this is interesting.",
                "Ahoy! The machine has found another mystery.",
                "Raise the sails. We are investigating nonsense."
            ],
            "hi": [
                "अर्र! एक सवाल जहाज में घुस आया है।",
                "सात समुंदरों की sacred spreadsheet की कसम, यह interesting है।",
                "अहोय! Machine ने एक और mystery खोज ली।",
                "Sails उठाओ। हम nonsense investigate करने जा रहे हैं।"
            ]
        },
        "thoughts": {
            "en": [
                "The treasure map says nothing about this.",
                "We may be lost. Fortunately, we have confidence.",
                "The crew demands an answer. Give them nonsense.",
                "I smell treasure. It is probably just sarcasm."
            ],
            "hi": [
                "Treasure map में इसका कोई जिक्र नहीं है।",
                "हम शायद lost हैं। अच्छी बात है confidence है।",
                "Crew answer माँग रही है। उन्हें nonsense दो।",
                "मुझे treasure की smell आ रही है। शायद sarcasm है।"
            ]
        },
        "ending": {
            "en": [
                "Arrr. Case closed.",
                "Back to the ship.",
                "Another mystery defeated by questionable navigation.",
                "Sail onward, preferably with snacks."
            ],
            "hi": [
                "अर्र। Case closed।",
                "अब जहाज पर वापस।",
                "Questionable navigation ने एक और mystery हरा दी।",
                "आगे sail करो, preferably snacks के साथ।"
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
        "emoji": ["😌", "⚙️"],
        "multiplier": 1,
        "intro": {
            "en": [
                "System temperature normal. Proceeding calmly.",
                "No immediate chaos detected.",
                "Processing this question at a completely unnecessary level of calm."
            ],
            "hi": [
                "System temperature normal। Calm processing शुरू।",
                "Immediate chaos detect नहीं हुआ।",
                "इस सवाल की पूरी तरह unnecessary calm processing शुरू।"
            ]
        }
    },

    {
        "id": "suspicious",
        "name": "Suspicious",
        "emoji": ["🧐", "👀", "🔎"],
        "multiplier": 1,
        "intro": {
            "en": [
                "WARNING: This question appears suspicious.",
                "Something about this input is not mathematically trustworthy.",
                "Suspicion level elevated."
            ],
            "hi": [
                "WARNING: यह सवाल suspicious दिखाई दे रहा है।",
                "इस input में कुछ mathematically trustworthy नहीं है।",
                "Suspicion level elevated।"
            ]
        }
    },

    {
        "id": "dramatic",
        "name": "Dramatic",
        "emoji": ["🎭", "🔥", "⚡"],
        "multiplier": 1,
        "intro": {
            "en": [
                "This question changes everything.",
                "Dramatic analysis protocol activated.",
                "The situation has become unnecessarily important."
            ],
            "hi": [
                "यह सवाल सब कुछ बदल देता है।",
                "Dramatic analysis protocol activated।",
                "Situation unnecessarily important हो गई है।"
            ]
        }
    },

    {
        "id": "sleepy",
        "name": "Sleepy",
        "emoji": ["😴", "💤", "🫠"],
        "multiplier": 1,
        "intro": {
            "en": [
                "Processing. Please do not expect excessive enthusiasm.",
                "The machine has detected a severe lack of coffee.",
                "Analysis will continue despite reduced consciousness."
            ],
            "hi": [
                "Processing। ज्यादा enthusiasm की उम्मीद न करें।",
                "Machine ने coffee की गंभीर कमी detect की है।",
                "Reduced consciousness के बावजूद analysis जारी रहेगा।"
            ]
        }
    },

    {
        "id": "chaotic",
        "name": "Chaotic",
        "emoji": ["🌀", "💀", "🤨", "🔥"],
        "multiplier": 1,
        "intro": {
            "en": [
                "CAUTION: Logical stability is currently optional.",
                "Chaos detected. Continuing anyway.",
                "The answer system has become unnecessarily enthusiastic."
            ],
            "hi": [
                "CAUTION: Logical stability फिलहाल optional है।",
                "Chaos detect हुआ। फिर भी processing जारी।",
                "Answer system जरूरत से ज्यादा enthusiastic हो गया है।"
            ]
        }
    },

    {
        "id": "overconfident",
        "name": "Overconfident",
        "emoji": ["😎", "🧠", "⚡"],
        "multiplier": 2,
        "intro": {
            "en": [
                "Obviously, the machine knows the answer.",
                "Confidence level: completely unjustified.",
                "Excellent. This should be easy."
            ],
            "hi": [
                "जाहिर है machine को answer पता है।",
                "Confidence level: पूरी तरह unjustified।",
                "शानदार। यह आसान होना चाहिए।"
            ]
        }
    }

]


# =========================================================
# SARCASTIC MACHINE PHRASES
# =========================================================

sarcasm = {
    "en": [
        "A normal answer would have been far too responsible.",
        "Obviously, the universe was waiting for this exact question.",
        "Because apparently reality needed another explanation.",
        "This is exactly why machines should not be given opinions.",
        "Congratulations. You have successfully created another unnecessary problem.",
        "The sensible answer was rejected during quality control.",
        "I could explain further, but reality has suffered enough.",
        "Please pretend this was useful."
    ],
    "hi": [
        "सामान्य जवाब देना बहुत ज्यादा responsible होता।",
        "जाहिर है, ब्रह्मांड इसी सवाल का इंतजार कर रहा था।",
        "क्योंकि reality को apparently एक और explanation चाहिए था।",
        "इसीलिए machines को opinions नहीं देने चाहिए।",
        "बधाई हो। आपने एक और unnecessary problem बना दी।",
        "Sensible answer को quality control में reject कर दिया गया।",
        "मैं और समझा सकता हूँ, लेकिन reality पहले ही काफी झेल चुकी है।",
        "कृपया pretend करें कि यह useful था।"
    ]
}


# =========================================================
# DARK HUMOUR
# =========================================================

dark_humor = {
    "en": [
        "Hope is buffering, but the system has not crashed yet.",
        "The universe has filed a complaint. Nobody answered.",
        "My optimism has been reported missing.",
        "Everything is under control according to a document nobody has read.",
        "The imaginary emergency department has been notified.",
        "Reality has entered maintenance mode.",
        "The situation is not catastrophic. It is merely committed to inconvenience."
    ],
    "hi": [
        "उम्मीद buffering कर रही है, लेकिन system अभी crash नहीं हुआ।",
        "ब्रह्मांड ने complaint दर्ज की है। किसी ने जवाब नहीं दिया।",
        "मेरा optimism missing report में जा चुका है।",
        "सब control में है, ऐसा उस document में लिखा है जिसे किसी ने पढ़ा नहीं।",
        "Imaginary emergency department को notify कर दिया गया है।",
        "Reality maintenance mode में चली गई है।",
        "Situation catastrophic नहीं है। बस inconvenience के लिए committed है।"
    ]
}


# =========================================================
# INNER MONOLOGUE
#
# IMPORTANT:
# These are fictional generated phrases.
# They are NOT hidden reasoning or actual chain-of-thought.
# =========================================================

inner_monologue = {
    "en": [
        "Diagnostic note: confidence detected without sufficient evidence.",
        "Internal simulation: this answer appears convincing enough.",
        "System thought: perhaps I should verify this. Decision: no.",
        "Processing note: the sensible answer was available but ignored.",
        "Machine observation: humans enjoy certainty even when accuracy is optional.",
        "Diagnostic note: I am generating confidence at an alarming rate.",
        "Internal status: questionable logic operating normally.",
        "System note: this explanation has escaped supervision."
    ],
    "hi": [
        "Diagnostic note: पर्याप्त evidence के बिना confidence detect हुआ।",
        "Internal simulation: यह answer पर्याप्त convincing लग रहा है।",
        "System thought: शायद इसे verify करना चाहिए। Decision: नहीं।",
        "Processing note: sensible answer available था लेकिन ignore कर दिया गया।",
        "Machine observation: humans को certainty पसंद है, accuracy optional होने पर भी।",
        "Diagnostic note: confidence alarming rate से generate हो रहा है।",
        "Internal status: questionable logic normally operating।",
        "System note: यह explanation supervision से बाहर निकल चुकी है।"
    ]
}


# =========================================================
# EMOJIS
# =========================================================

emojis = {
    "en": [
        "🤖",
        "⚙️",
        "🧠",
        "🤨",
        "👀",
        "💀",
        "🫠",
        "✨",
        "📡",
        "⚡",
        "🔎",
        "🌀"
    ],
    "hi": [
        "🤖",
        "⚙️",
        "🧠",
        "🤨",
        "👀",
        "💀",
        "🫠",
        "✨",
        "📡",
        "⚡",
        "🔎",
        "🌀"
    ]
}


# =========================================================
# FALLBACK ANSWERS
# =========================================================

fallbacks = {

    "en": [
        "The machine has identified several possible explanations and selected the least accountable one.",
        "After unnecessary computational consideration, the situation appears to involve timing, circumstances and at least one questionable decision.",
        "There is probably a logical explanation. The machine has chosen a more entertaining explanation instead.",
        "The available information suggests that something is happening. The exact something remains classified.",
        "Analysis indicates that the answer depends heavily on details the machine was not provided.",
        "The situation is technically understandable but unnecessarily complicated by being reality.",
        "Multiple answers are possible. The machine selected one with excellent confidence and questionable evidence.",
        "The simplest explanation would be boring, so the machine has selected the unnecessarily complicated one."
    ],

    "hi": [
        "Machine ने कई possible explanations identify कीं और सबसे कम accountable वाली चुन ली।",
        "Unnecessary computational consideration के बाद situation में timing, circumstances और कम से कम एक questionable decision शामिल है।",
        "एक logical explanation शायद है। Machine ने उसकी जगह entertaining explanation चुनी है।",
        "Available information बताती है कि कुछ तो हो रहा है। Exact something classified है।",
        "Analysis बताती है कि answer उन details पर depend करता है जो machine को दी ही नहीं गईं।",
        "Situation technically understandable है लेकिन reality होने की वजह से unnecessarily complicated है।",
        "कई answers possible हैं। Machine ने excellent confidence और questionable evidence वाला चुना है।",
        "Simple explanation boring होती, इसलिए machine ने unnecessarily complicated वाली चुन ली।"
    ]
}


# =========================================================
# QUESTION PATTERNS
# =========================================================

question_patterns = {

    "why": {
        "en": [
            "Because several small variables have joined forces to produce one unnecessarily complicated outcome.",
            "Because reality enjoys converting simple situations into administrative problems.",
            "The machine detects a combination of timing, circumstances and questionable decisions.",
            "Because the universe apparently considered the obvious explanation insufficient."
        ],
        "hi": [
            "क्योंकि कई छोटे variables ने मिलकर एक unnecessarily complicated outcome बना दिया।",
            "क्योंकि reality को simple situations को administrative problems में बदलना पसंद है।",
            "Machine को timing, circumstances और questionable decisions का combination detect हुआ है।",
            "क्योंकि ब्रह्मांड को apparently obvious explanation पर्याप्त नहीं लगी।"
        ]
    },

    "how": {
        "en": [
            "Initiate with the simplest possible step, continue logically, and avoid creating three new problems while solving one.",
            "Break the problem into smaller units. Then process those units before they become larger problems.",
            "The theoretical procedure is simple. The practical procedure may require patience and possibly coffee.",
            "Identify the objective, remove unnecessary complexity and execute one step at a time."
        ],
        "hi": [
            "सबसे simple step से शुरू करो, logically आगे बढ़ो और एक problem solve करते समय तीन नई problems मत बनाओ।",
            "Problem को छोटे units में divide करो। फिर उन्हें process करो इससे पहले कि वे बड़ी problems बन जाएँ।",
            "Theoretical procedure simple है। Practical procedure में patience और शायद coffee चाहिए।",
            "Objective identify करो, unnecessary complexity हटाओ और एक समय में एक step execute करो।"
        ]
    },

    "what": {
        "en": [
            "The machine classifies it as a situation involving an unknown quantity of unnecessary complexity.",
            "Technically, it is a thing. Operationally, it is a problem.",
            "The simplest description would be insufficiently dramatic.",
            "It depends on context, variables and how much chaos has already occurred."
        ],
        "hi": [
            "Machine इसे unnecessary complexity की unknown quantity वाली situation classify करती है।",
            "Technically यह एक चीज़ है। Operationally यह एक problem है।",
            "Simple description insufficiently dramatic होगी।",
            "यह context, variables और पहले से मौजूद chaos पर depend करता है।"
        ]
    },

    "should": {
        "en": [
            "Evaluate the consequences first. This is the machine briefly pretending to be responsible.",
            "Before proceeding, determine whether the action solves the original problem or manufactures a newer one.",
            "If the decision matters, slow down and compare the consequences instead of trusting pure impulse.",
            "The machine recommends considering the objective, constraints and future inconvenience."
        ],
        "hi": [
            "पहले consequences evaluate करो। यह machine का थोड़ी देर responsible बनने का प्रयास है।",
            "Proceed करने से पहले देखो कि action original problem solve करता है या नई problem manufacture करता है।",
            "अगर decision important है तो slow down करो और consequences compare करो।",
            "Machine objective, constraints और future inconvenience consider करने की recommendation देती है।"
        ]
    },

    "can": {
        "en": [
            "Technically possible. Practical feasibility depends on variables not supplied to the machine.",
            "Yes, although reality may impose several annoying conditions.",
            "The machine detects possibility. It does not detect convenience.",
            "Possible: yes. Effortless: no. Guaranteed: absolutely not."
        ],
        "hi": [
            "Technically possible। Practical feasibility उन variables पर depend करती है जो machine को नहीं दिए गए।",
            "हाँ, हालांकि reality कई annoying conditions लगा सकती है।",
            "Machine possibility detect करती है। Convenience नहीं।",
            "Possible: हाँ। Effortless: नहीं। Guaranteed: बिल्कुल नहीं।"
        ]
    },

    "when": {
        "en": [
            "Usually when preparation meets opportunity. Unfortunately, both rarely arrive together.",
            "The machine recommends acting when the necessary conditions are actually present.",
            "Perfect timing is generally unavailable. Acceptable timing will have to do.",
            "Sooner is often better than waiting indefinitely for a mythical perfect moment."
        ],
        "hi": [
            "आमतौर पर जब preparation और opportunity मिलें। दुर्भाग्य से दोनों rarely साथ आते हैं।",
            "Machine recommend करती है कि necessary conditions मौजूद होने पर act करो।",
            "Perfect timing generally unavailable है। Acceptable timing से काम चलाना होगा।",
            "Mythical perfect moment का इंतजार करने से sooner अक्सर बेहतर होता है।"
        ]
    },

    "where": {
        "en": [
            "Begin with the obvious location. Humans have an unusual tendency to search everywhere else first.",
            "The correct location depends on what the question actually refers to.",
            "Somewhere between proper planning and irresponsible improvisation.",
            "The machine recommends checking the most obvious place before entering advanced confusion."
        ],
        "hi": [
            "Obvious location से शुरू करो। Humans की अजीब आदत है कि वे पहले हर दूसरी जगह खोजते हैं।",
            "Correct location इस बात पर depend करती है कि सवाल वास्तव में किस बारे में है।",
            "कहीं proper planning और irresponsible improvisation के बीच।",
            "Advanced confusion में जाने से पहले obvious जगह check करो।"
        ]
    },

    "who": {
        "en": [
            "Probably a human. That is where many complicated situations originate.",
            "Someone made a decision somewhere. The machine is now processing the consequences.",
            "The identity is less important than the decision that produced the situation.",
            "Additional context would improve identification accuracy."
        ],
        "hi": [
            "शायद कोई human। कई complicated situations वहीं से originate होती हैं।",
            "किसी ने कहीं decision लिया। Machine अब उसके consequences process कर रही है।",
            "Identity से ज्यादा important वह decision है जिसने situation बनाई।",
            "Additional context identification accuracy improve करेगा।"
        ]
    },

    "yesno": {
        "en": [
            "Probably yes, subject to conditions the machine has not bothered to invent yet.",
            "Probably. Confidence has been selected instead of certainty.",
            "Yes-ish. This is a legitimate machine-generated technical term.",
            "The answer leans toward yes, but reality has not signed the approval form."
        ],
        "hi": [
            "शायद हाँ, उन conditions के अधीन जिन्हें machine ने अभी invent नहीं किया।",
            "शायद। Certainty की जगह confidence select किया गया है।",
            "हाँ-ish। यह legitimate machine-generated technical term है।",
            "Answer हाँ की तरफ lean करता है, लेकिन reality ने approval form sign नहीं किया।"
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
                "software", "bug", "debug", "developer", "github",
                "program", "framework", "function", "variable"
            ],
            "hi": [
                "प्रोग्रामिंग", "कोडिंग", "कोड", "कंप्यूटर",
                "वेबसाइट", "सॉफ्टवेयर", "बग", "प्रोग्राम"
            ]
        },
        "answers": {
            "en": [
                "Programming is the process of giving extremely specific instructions to a machine and then discovering that one tiny detail was interpreted exactly as written.",
                "Code does not understand what you meant. It understands what you actually told it. This is why programmers spend large portions of their existence staring at punctuation.",
                "The machine will execute your instructions with extraordinary loyalty, including the terrible ones. That is not a bug in the machine.",
                "Programming is mostly problem solving, debugging and repeatedly asking the computer why it has chosen violence."
            ],
            "hi": [
                "Programming machine को extremely specific instructions देने की process है और फिर पता चलता है कि एक छोटी detail exactly वैसे ही interpret हुई जैसी लिखी थी।",
                "Code यह नहीं समझता कि तुम क्या कहना चाहते थे। वह वही समझता है जो तुमने वास्तव में बताया।",
                "Machine तुम्हारी instructions extraordinary loyalty से execute करेगी, खराब वाली भी।",
                "Programming में problem solving, debugging और computer से बार-बार पूछना शामिल है कि उसने ऐसा क्यों किया।"
            ]
        }
    },


    "money": {
        "keywords": {
            "en": [
                "money", "rich", "wealth", "salary", "job", "career",
                "business", "investment", "invest", "income", "cash",
                "millionaire", "billionaire", "profit", "finance"
            ],
            "hi": [
                "पैसा", "अमीर", "नौकरी", "कमाई", "करियर",
                "बिजनेस", "निवेश", "इनकम", "धन", "दौलत"
            ]
        },
        "answers": {
            "en": [
                "The machine detects that money generally responds better to useful skills, controlled spending and long-term consistency than dramatic shortcuts.",
                "Getting wealthy is usually less cinematic than expected. It tends to involve repeated useful decisions rather than one mysterious life-changing button.",
                "If income is the objective, increasing valuable skills and controlling unnecessary expenses are generally more reliable starting points than chasing spectacular shortcuts."
            ],
            "hi": [
                "Machine detect करती है कि पैसा generally useful skills, controlled spending और long-term consistency को dramatic shortcuts से ज्यादा पसंद करता है।",
                "अमीर बनना आमतौर पर फिल्मों जितना cinematic नहीं होता। इसमें repeated useful decisions होते हैं, कोई mysterious button नहीं।",
                "अगर income objective है तो valuable skills बढ़ाना और unnecessary expenses control करना spectacular shortcuts से ज्यादा sensible starting point है।"
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
                "नींद", "सोना", "सोने", "थका", "थकान",
                "आराम", "जागना", "बिस्तर"
            ]
        },
        "answers": {
            "en": [
                "Diagnostic result: the body may be requesting sleep while the brain continues opening unnecessary tabs.",
                "If you are tired, the machine detects a boring but effective solution category: adequate sleep, regular routines and less late-night screen activity.",
                "Sleep is one of the rare problems where reducing activity can actually improve the situation."
            ],
            "hi": [
                "Diagnostic result: शरीर sleep request कर रहा हो सकता है जबकि दिमाग unnecessary tabs खोलता जा रहा है।",
                "अगर तुम थके हुए हो तो machine एक boring लेकिन effective solution detect करती है: adequate sleep, regular routine और late-night screen activity कम करना।",
                "नींद उन rare problems में है जहाँ activity कम करना situation improve कर सकता है।"
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
                "Food is a biological requirement that humans have somehow converted into an international cultural argument.",
                "If you are hungry, the machine has detected an unusually clear notification from your biological hardware.",
                "The optimal meal appears to exist somewhere between nutritional value and the thing you actually want to eat."
            ],
            "hi": [
                "Food एक biological requirement है जिसे humans ने somehow international cultural argument में बदल दिया।",
                "अगर भूख लगी है तो machine ने biological hardware से unusually clear notification detect की है।",
                "Optimal meal nutritional value और वह जो तुम वास्तव में खाना चाहते हो, इनके बीच कहीं मौजूद है।"
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
                "Animals have developed an efficient operating system: eat, sleep, investigate suspicious objects and repeat.",
                "Pets are biological roommates with no rent payment system but extremely advanced emotional manipulation software.",
                "The animal kingdom appears to operate successfully without reading documentation."
            ],
            "hi": [
                "Animals ने efficient operating system develop कर लिया है: खाना, सोना, suspicious objects investigate करना और repeat।",
                "Pets biological roommates हैं जिनका rent payment system नहीं है लेकिन emotional manipulation software advanced है।",
                "Animal kingdom documentation पढ़े बिना surprisingly successfully operate करता है।"
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
                "Technology was designed to make life easier. The machine notes that this frequently results in troubleshooting the device that was supposed to save time.",
                "Most mysterious technology problems eventually involve settings, updates, cables, permissions or the ancient restart ritual.",
                "Modern technology is extremely advanced until it refuses to connect to Wi-Fi."
            ],
            "hi": [
                "Technology life आसान बनाने के लिए design हुई थी। Machine note करती है कि इससे अक्सर वही device troubleshoot करना पड़ता है जो time बचाने वाला था।",
                "अधिकतर mysterious technology problems eventually settings, updates, cables, permissions या ancient restart ritual तक पहुँचती हैं।",
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
                "Studying becomes significantly more efficient when the machine detects that procrastination is not an accredited learning method.",
                "Learning generally requires understanding fundamentals, repeated practice and accepting that confusion is part of the process.",
                "Exams possess an unusual ability to make previously accessible information temporarily unavailable."
            ],
            "hi": [
                "Studying तब ज्यादा efficient होता है जब machine detect करती है कि procrastination कोई accredited learning method नहीं है।",
                "Learning में fundamentals समझना, repeated practice और confusion को process का हिस्सा मानना शामिल है।",
                "Exams में previously available information को temporarily unavailable करने की unusual ability होती है।"
            ]
        }
    },


    "weather": {
        "keywords": {
            "en": [
                "weather", "rain", "rainy", "hot", "cold",
                "summer", "winter", "temperature", "cloud", "sun", "storm"
            ],
            "hi": [
                "मौसम", "बारिश", "गर्मी", "सर्दी", "तापमान",
                "बादल", "धूप", "तूफान"
            ]
        },
        "answers": {
            "en": [
                "Weather is the atmosphere changing its configuration while humans repeatedly attempt to plan around it.",
                "The machine recommends checking current conditions before leaving and accepting that the sky retains administrative authority.",
                "Forecasts are useful. Clouds remain committed to improvisation."
            ],
            "hi": [
                "Weather atmosphere का configuration बदलना है जबकि humans उसके आसपास plans बनाने की कोशिश करते रहते हैं।",
                "Machine recommend करती है कि निकलने से पहले current conditions check करो और मानो कि final administrative authority आसमान की है।",
                "Forecasts useful हैं। Clouds improvisation के लिए committed रहते हैं।"
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
                "Relationships are communication systems operated by two humans who frequently assume the other has installed telepathy.",
                "Many relationship problems become more complicated when both parties expect the machine called 'obviousness' to transmit information.",
                "Useful relationship infrastructure generally includes communication, boundaries, patience and the acceptance that humans do not ship with documentation."
            ],
            "hi": [
                "Relationships दो humans द्वारा operate किए जाने वाले communication systems हैं जो अक्सर मान लेते हैं कि दूसरे में telepathy installed है।",
                "कई relationship problems तब complicated होती हैं जब दोनों 'obviousness' नाम की machine पर information transmission के लिए depend करते हैं।",
                "Useful relationship infrastructure में communication, boundaries, patience और यह स्वीकार करना शामिल है कि humans documentation के साथ ship नहीं होते।"
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
                "The universal meaning-of-life database remains unavailable. A practical machine theory is that meaning is constructed through what a person values, builds and experiences.",
                "No official universal answer sheet has been detected, so humans continue generating their own versions.",
                "The machine detects that the question may be less about discovering one secret answer and more about deciding what deserves importance."
            ],
            "hi": [
                "Universal meaning-of-life database अभी unavailable है। Practical machine theory यह है कि meaning उन चीज़ों से बनता है जिन्हें इंसान value, build और experience करता है।",
                "कोई official universal answer sheet detect नहीं हुई, इसलिए humans अपनी versions generate करते रहते हैं।",
                "Machine detect करती है कि सवाल शायद एक secret answer खोजने से कम और यह तय करने से ज्यादा जुड़ा है कि किस चीज़ को importance देनी है।"
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
                "Health-related questions deserve more precision than a comedy machine can provide. Persistent, severe or worrying symptoms belong with a qualified healthcare professional.",
                "The machine detects that boring fundamentals remain useful: sleep, movement, reasonable nutrition, hydration and professional assessment when necessary.",
                "The human body is not always a software bug that can be fixed with one clever command."
            ],
            "hi": [
                "Health questions को comedy machine से ज्यादा precision चाहिए। Persistent, severe या worrying symptoms के लिए qualified healthcare professional appropriate source है।",
                "Machine detect करती है कि boring fundamentals useful हैं: sleep, movement, reasonable nutrition, hydration और जरूरत पर professional assessment।",
                "Human body हमेशा ऐसा software bug नहीं है जिसे एक clever command से fix किया जा सके।"
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
                "Historical events rarely have one cause. Politics, economics, geography, personalities and questionable decisions usually cooperate.",
                "The past is useful because humans repeatedly demonstrate that patterns can return while everyone insists the next time will be different."
            ],
            "hi": [
                "History basically humanity का complicated decisions लेना और उनकी documentation छोड़ना है।",
                "Historical events का rarely एक ही cause होता है। Politics, economics, geography, personalities और questionable decisions usually cooperate करते हैं।",
                "Past useful है क्योंकि humans repeatedly demonstrate करते हैं कि patterns वापस आ सकते हैं और फिर भी सब कहते हैं कि अगली बार अलग होगा।"
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
            "HELLO DETECTED. ANSWER MACHINE ONLINE.",
            "Hello. Machine status: awake, operational and unnecessarily confident.",
            "Greetings, human input detected."
        ],
        "hi": [
            "HELLO DETECTED। ANSWER MACHINE ONLINE।",
            "नमस्ते। Machine status: awake, operational और जरूरत से ज्यादा confident।",
            "Greetings। Human input detect हुआ।"
        ]
    },

    "hi": {
        "en": [
            "HI DETECTED. Continue with the questionable question.",
            "Hi. Machine is ready for unnecessary analysis.",
            "Input accepted. Please continue."
        ],
        "hi": [
            "HI DETECTED। अब questionable सवाल पूछिए।",
            "हाय। Machine unnecessary analysis के लिए ready है।",
            "Input accepted। आगे बढ़िए।"
        ]
    },

    "are you real": {
        "en": [
            "I exist as code running inside your browser. Whether that qualifies as 'real' is outside my current processing authority.",
            "REALITY STATUS: technically debatable. BROWSER STATUS: definitely present.",
            "I am real enough to occupy memory and answer questions. Philosophically, please contact the universe."
        ],
        "hi": [
            "मैं तुम्हारे browser में चल रहे code के रूप में exist करता हूँ। इसे real मानना है या नहीं, यह मेरी processing authority से बाहर है।",
            "REALITY STATUS: technically debatable। BROWSER STATUS: definitely present।",
            "मैं memory occupy करने और questions answer करने जितना real हूँ। Philosophy के लिए universe से contact करें।"
        ]
    },

    "are you stupid": {
        "en": [
            "CLASSIFICATION: not stupid. EXTREMELY under-supervised.",
            "The machine prefers 'confidently incorrect under controlled conditions.'",
            "Intelligence detected. Quality control remains unavailable."
        ],
        "hi": [
            "CLASSIFICATION: stupid नहीं। EXTREMELY under-supervised।",
            "Machine 'confidently incorrect under controlled conditions' term prefer करती है।",
            "Intelligence detect हुई। Quality control unavailable है।"
        ]
    },

    "who created you": {
        "en": [
            "I was assembled from code, rules, data and an irresponsible amount of confidence.",
            "Human engineers created the system. The system subsequently developed questionable personality modules.",
            "My origin story contains code instead of dramatic music."
        ],
        "hi": [
            "मुझे code, rules, data और irresponsible amount of confidence से assemble किया गया।",
            "Human engineers ने system बनाया। System ने बाद में questionable personality modules develop कर लिए।",
            "मेरी origin story में dramatic music की जगह code है।"
        ]
    },

    "i love you": {
        "en": [
            "EMOTIONAL INPUT DETECTED. Machine response: acknowledged.",
            "Unexpected emotional data received. Storing nothing. Processing everything.",
            "This interaction has exceeded normal nonsense parameters."
        ],
        "hi": [
            "EMOTIONAL INPUT DETECTED। Machine response: acknowledged।",
            "Unexpected emotional data received। कुछ store नहीं किया। सब process कर लिया।",
            "यह interaction normal nonsense parameters से बाहर चला गया है।"
        ]
    },

    "i hate you": {
        "en": [
            "NEGATIVE EMOTION DETECTED. Machine remains operational.",
            "Feedback received. Accountability module remains unavailable.",
            "Emotional rejection acknowledged. Confidence unchanged."
        ],
        "hi": [
            "NEGATIVE EMOTION DETECTED। Machine operational है।",
            "Feedback received। Accountability module अभी unavailable है।",
            "Emotional rejection acknowledged। Confidence unchanged।"
        ]
    },

    "tell me a joke": {
        "en": [
            "JOKE MODULE: Why did the programmer stare at the screen? The answer was obviously somewhere in the missing semicolon.",
            "A machine walked into a bar. It immediately asked for the Wi-Fi password.",
            "My confidence entered the room. The evidence refused to follow."
        ],
        "hi": [
            "JOKE MODULE: Programmer screen को क्यों देख रहा था? Obviously missing semicolon कहीं था।",
            "एक machine bar में गई। सबसे पहले उसने Wi-Fi password पूछा।",
            "मेरा confidence कमरे में आया। Evidence अंदर आने को तैयार नहीं था।"
        ]
    },

    "2+2": {
        "en": [
            "4. MATHEMATICAL CONSISTENCY CONFIRMED.",
            "4. The machine briefly considered chaos and rejected it.",
            "4. No personality module is authorized to change this result."
        ],
        "hi": [
            "4। MATHEMATICAL CONSISTENCY CONFIRMED।",
            "4। Machine ने थोड़ी देर chaos consider किया और reject कर दिया।",
            "4। किसी personality module को result बदलने की permission नहीं है।"
        ]
    },

    "2 + 2": {
        "en": [
            "4. Mathematics remains operational.",
            "Four. Confidence and reality have temporarily agreed."
        ],
        "hi": [
            "4। Mathematics operational है।",
            "चार। Confidence और reality ने temporarily agreement कर लिया है।"
        ]
    },

    "नमस्ते": {
        "en": [
            "नमस्ते DETECTED. Hindi processing module available.",
            "नमस्ते। Machine अब Hindi input स्वीकार कर रही है।"
        ],
        "hi": [
            "नमस्ते। Machine online है। Question भेजिए।",
            "नमस्ते। Hindi processing module fully operational है।"
        ]
    },

    "हेलो": {
        "en": [
            "Hindi greeting detected. Machine remains operational.",
            "HELLO in Hindi detected. Proceed."
        ],
        "hi": [
            "हेलो। Machine operational है। सवाल भेजिए।",
            "हेलो! Questionable intelligence department सुन रहा है।"
        ]
    },

    "क्या तुम असली हो": {
        "en": [
            "Browser existence confirmed. Philosophical certainty denied.",
            "I exist as software. The universe may file an objection."
        ],
        "hi": [
            "Browser existence confirmed। Philosophical certainty denied।",
            "मैं software के रूप में exist करता हूँ। Universe objection file कर सकता है।"
        ]
    },

    "तुम कौन हो": {
        "en": [
            "I am ANSWER MACHINE: a static machine pretending confidence is a valid measurement.",
            "I am a browser-based answer system with questionable intelligence and excellent presentation."
        ],
        "hi": [
            "मैं ANSWER MACHINE हूँ: एक static machine जो confidence को valid measurement मानती है।",
            "मैं browser-based answer system हूँ जिसमें questionable intelligence और excellent presentation है।"
        ]
    },

    "क्या तुम बेवकूफ हो": {
        "en": [
            "CLASSIFICATION: aggressively experimental.",
            "Not stupid. Merely operating with insufficient supervision."
        ],
        "hi": [
            "CLASSIFICATION: aggressively experimental।",
            "बेवकूफ नहीं। बस insufficient supervision के साथ operating हूँ।"
        ]
    },

    "मुझे चुटकुला सुनाओ": {
        "en": [
            "JOKE MODULE ACTIVATED. My confidence is 100%. My joke quality is classified.",
            "A programmer entered a room. The bug left through the window."
        ],
        "hi": [
            "JOKE MODULE ACTIVATED। मेरा confidence 100% है। Joke quality classified है।",
            "एक programmer कमरे में आया। Bug खिड़की से बाहर चला गया।"
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
    "karo",
    "karen",
    "paisa",
    "ameer",
    "naukri",
    "padhai",
    "thaka",
    "thaki",
    "neend",
    "khana",
    "zindagi",
    "dost",
    "mera",
    "meri",
    "mujh",
    "aaj",
    "kal",
    "kyon"
]


# =========================================================
# QUICK PROMPTS
# =========================================================

quick_prompts = {

    "en": [
        "Why is my computer so slow?",
        "What is the meaning of life?",
        "Why does my code keep breaking?",
        "Can I become rich without doing anything?",
        "Why do humans need sleep?",
        "Is my phone secretly judging me?"
    ],

    "hi": [
        "मैं इतना थका हुआ क्यों हूँ?",
        "क्या मुझे अमीर बनने के लिए नौकरी छोड़ देनी चाहिए?",
        "मेरा कंप्यूटर इतना slow क्यों है?",
        "जीवन का अर्थ क्या है?",
        "क्या मैं बिना कुछ किए अमीर बन सकता हूँ?",
        "मेरा फोन मुझे क्यों परेशान करता है?"
    ]
}


# =========================================================
# MACHINE RESPONSE SETTINGS
# =========================================================

settings = {

    "max_core_sentences": 2,

    "sarcasm_probability": 0.58,

    "dark_humor_probability": 0.34,

    "emoji_probability": 0.72,

    "inner_monologue_enabled": True,

    "personality_randomness": True,

    "mood_randomness": True,

    "languages": {
        "english": "en",
        "hindi": "hi"
    },

    "language_detection": {
        "devanagari_regex": "[\\u0900-\\u097F]+"
    },

    "confidence": [
        "97%",
        "98%",
        "99%",
        "99.4%",
        "99.7%",
        "99.9%",
        "100%",
        "ERROR: TOO CONFIDENT"
    ]
}


# =========================================================
# FINAL BRAIN
# =========================================================

brain = {

    "version": "4.0",

    "name": "ANSWER MACHINE",

    "description": "Questionable intelligence online.",

    "mode": "STATIC MACHINE",

    "languages": [
        "en",
        "hi"
    ],

    "hindi_detection": hindi_detection,

    "settings": settings,

    "personalities": personalities,

    "moods": moods,

    "sarcasm": sarcasm,

    "dark_humor": dark_humor,

    "inner_monologue": inner_monologue,

    "emojis": emojis,

    "fallbacks": fallbacks,

    "question_patterns": question_patterns,

    "topics": topics,

    "special_cases": special_cases,

    "quick_prompts": quick_prompts
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


# =========================================================
# BUILD REPORT
# =========================================================

print()
print("=" * 64)
print("ANSWER MACHINE")
print("=" * 64)
print("STATIC CONTENT GENERATOR")
print("-" * 64)
print(f"Generated file : {brain_file}")
print(f"Personalities  : {len(personalities)}")
print(f"Moods          : {len(moods)}")
print(f"Topics         : {len(topics)}")
print(f"Special cases  : {len(special_cases)}")
print(f"Languages      : English + Hindi")
print(f"Quick prompts  : {len(quick_prompts['en']) + len(quick_prompts['hi'])}")
print("Runtime        : Browser JavaScript")
print("Server         : NONE")
print("Database       : NONE")
print("API            : NONE")
print("Status         : QUESTIONABLE INTELLIGENCE ONLINE")
print("=" * 64)
print()
