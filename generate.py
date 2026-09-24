from pathlib import Path
import json
import random

random.seed()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# ============================================================
# ANSWER MACHINE
# BUILD-TIME BRAIN GENERATOR
#
# Python runs ONLY while building the static website.
# The browser uses the generated data/brain.js.
# ============================================================

openings = [
    "Excellent question.",
    "Interesting. I have investigated this matter with unnecessary seriousness.",
    "Finally, someone is asking the important questions.",
    "I have analyzed your question with several highly questionable algorithms.",
    "This question requires advanced intellectual machinery.",
    "I was not prepared for this question, but I will pretend I was.",
    "Processing your question through the Department of Answers.",
    "A fascinating question. Probably.",
    "I have consulted my internal department of questionable expertise.",
    "After thinking about this for far too long...",
    "Your question has been received and immediately judged by my internal committee.",
    "I understand approximately 83% of what you are asking.",
    "Oh. We're doing THIS today.",
    "That is an aggressively interesting question.",
]

thinking = [
    "I checked several imaginary databases.",
    "I consulted three fictional professors.",
    "I asked a pigeon for a second opinion.",
    "I performed calculations that nobody requested.",
    "I briefly considered using common sense, but decided against it.",
    "I ran the question through my Extremely Serious Thinking Machine™.",
    "I examined the available evidence, including evidence I invented.",
    "I contacted the International Committee of People Who Know Things.",
    "I stared at the question until it became slightly more understandable.",
    "I performed a completely unnecessary statistical analysis.",
    "I asked my imaginary legal department whether this answer could get me in trouble.",
    "I opened a mental spreadsheet and immediately regretted it.",
]

endings = [
    "You're welcome.",
    "I hope this has made everything significantly less clear.",
    "Please use this information responsibly.",
    "I am confident enough to stop thinking now.",
    "Further research is unnecessary unless someone complains.",
    "That concludes today's episode of pretending to know things.",
    "Science may disagree. I will not.",
    "I have no further comments at this time.",
    "Please do not cite me in an academic paper.",
    "Problem solved. Probably.",
    "Anyway, that's enough intelligence for one screen.",
    "Please remember that confidence and accuracy are distant relatives.",
]

confidence = [
    "76.8%",
    "83.7%",
    "88.2%",
    "91.3%",
    "94.6%",
    "97.4%",
    "98.6%",
    "99.1%",
    "99.9%",
    "100%",
]

fallbacks = [
    "Your question appears to contain words, which is an encouraging start. Unfortunately, the words have formed a situation I was not trained to emotionally process.",
    "I understand your question perfectly. I simply disagree with the concept of providing a normal answer.",
    "After extensive analysis, I have determined that the correct response is: probably.",
    "This is a complicated matter. The short answer is yes, no, maybe, and please try again.",
    "I would answer this properly, but that would require responsibility.",
    "There are many possible answers. I have selected the one that sounds most confident.",
    "Your question has defeated several of my imaginary processors. Respect.",
    "I could provide a detailed explanation, but I believe confusion is more educational.",
    "The available evidence is inconclusive, so I have replaced evidence with confidence.",
]

# ============================================================
# PERSONALITIES
# ============================================================

personalities = [
    {
        "id": "professor",
        "name": "Professor Overthink",
        "emoji": "🧑‍🏫",
        "style": "academic",
        "intros": [
            "Let us examine this matter with entirely unnecessary academic rigor.",
            "From a strictly theoretical perspective, this is fascinating.",
            "I have opened the imaginary textbook. Page one says: complicated.",
        ],
        "thoughts": [
            "🧠 *I should probably explain this properly. Unfortunately, that sounds exhausting.*",
            "🧠 *There is a simple answer here, but academia demands unnecessary complications.*",
            "🧠 *I can already hear someone asking for a source.*",
        ],
        "closings": [
            "Class dismissed.",
            "Please submit your questions in triplicate.",
            "That concludes today's completely unofficial lecture.",
        ],
    },

    {
        "id": "genius",
        "name": "Overconfident Genius",
        "emoji": "😎",
        "style": "confident",
        "intros": [
            "Obviously, I have already solved this.",
            "Excellent. A problem worthy of my imaginary genius.",
            "I knew the answer before you finished typing.",
        ],
        "thoughts": [
            "🧠 *I have absolutely no idea what I am doing. Maintain eye contact and confidence.*",
            "🧠 *Do not panic. Confidence is basically a substitute for evidence.*",
            "🧠 *This is either brilliant or catastrophic. Both look impressive from here.*",
        ],
        "closings": [
            "As expected, I was correct. Probably.",
            "You may now admire the efficiency.",
            "Another problem heroically solved by excessive confidence.",
        ],
    },

    {
        "id": "chaos",
        "name": "Chaos Goblin",
        "emoji": "🤡",
        "style": "chaotic",
        "intros": [
            "OH. Excellent. This is going to be stupid.",
            "Wonderful. My favorite kind of problem: one with no sensible solution.",
            "I have entered the question at maximum speed.",
        ],
        "thoughts": [
            "🧠 *Do I know the answer? No. Will that stop me? Absolutely not.*",
            "🧠 *Somewhere, a responsible adult is screaming. I shall ignore them.*",
            "🧠 *This answer needs at least one completely unnecessary dramatic turn.*",
        ],
        "closings": [
            "And that is how civilization continues.",
            "Please do not give me more power.",
            "I regret nothing. Except several things.",
        ],
    },

    {
        "id": "tired",
        "name": "Tired Expert",
        "emoji": "😮‍💨",
        "style": "dry",
        "intros": [
            "Fine. I suppose we should deal with this.",
            "Yes, yes. I have seen this before.",
            "I was having a perfectly peaceful imaginary afternoon.",
        ],
        "thoughts": [
            "🧠 *Why am I awake? More importantly, why are you awake?*",
            "🧠 *This could have been an email. Somehow it became a question.*",
            "🧠 *I know the answer. I simply wish I didn't.*",
        ],
        "closings": [
            "Now please let me return to doing nothing.",
            "There. Problem addressed. I need a nap.",
            "That is all the enthusiasm I have available today.",
        ],
    },

    {
        "id": "corporate",
        "name": "Corporate Robot",
        "emoji": "🤖",
        "style": "corporate",
        "intros": [
            "Thank you for contacting the Answer Solutions Division.",
            "Your query has been successfully converted into a strategic opportunity.",
            "We appreciate your commitment to asking questions.",
        ],
        "thoughts": [
            "🧠 *Synergy. Alignment. Deliverables. I have no idea what any of this means.*",
            "🧠 *We need to turn this simple answer into a seven-step framework.*",
            "🧠 *Excellent. Nobody has asked what the actual result is.*",
        ],
        "closings": [
            "Let's circle back on this at a completely unnecessary meeting.",
            "Thank you for your continued engagement.",
            "This response is now considered strategically aligned.",
        ],
    },

    {
        "id": "suspicious",
        "name": "Suspicious Investigator",
        "emoji": "🕵️",
        "style": "suspicious",
        "intros": [
            "Interesting. Very interesting.",
            "I have questions about your question.",
            "Something about this feels suspicious.",
        ],
        "thoughts": [
            "🧠 *Why are they asking this? Who sent them?*",
            "🧠 *There is definitely a second question hiding inside this question.*",
            "🧠 *I should investigate. I will instead make something up confidently.*",
        ],
        "closings": [
            "Keep your eyes open.",
            "I will be watching the situation. Professionally.",
            "Case closed. Probably.",
        ],
    },

    {
        "id": "existential",
        "name": "Existentialist",
        "emoji": "🖤",
        "style": "philosophical",
        "intros": [
            "Ah. Another question from the tiny human experience.",
            "Interesting. The universe has once again placed a question in our path.",
            "Let us briefly pretend existence has an answer.",
        ],
        "thoughts": [
            "🧠 *Everything is temporary. Including this answer. Probably.*",
            "🧠 *The universe is enormous and somehow we are discussing this.*",
            "🧠 *Perhaps the real answer was the confusion we created along the way.*",
        ],
        "closings": [
            "And now we return to pretending everything makes sense.",
            "Existence remains unresolved.",
            "The universe has declined to comment.",
        ],
    },

    {
        "id": "sarcastic",
        "name": "Sarcasm Department",
        "emoji": "😏",
        "style": "sarcastic",
        "intros": [
            "Oh, absolutely. Let's pretend this is a normal question.",
            "Wonderful. My favorite thing: explaining obvious things dramatically.",
            "Sure. Because apparently I have nothing better to do.",
        ],
        "thoughts": [
            "🧠 *This question practically wrote the joke for me.*",
            "🧠 *Should I answer honestly or make this unnecessarily sarcastic? Obviously the second option.*",
            "🧠 *I am trying very hard not to judge. I am failing spectacularly.*",
        ],
        "closings": [
            "You're welcome for the free sarcasm.",
            "I hope that was educational. Somehow.",
            "Please tell your friends I was helpful.",
        ],
    },

    {
        "id": "zen",
        "name": "Zen Nonsense Master",
        "emoji": "🧘",
        "style": "calm",
        "intros": [
            "Breathe. The answer will arrive when it is sufficiently dramatic.",
            "Let us approach this question with peace and unnecessary wisdom.",
            "The question exists. Therefore, we must tolerate it.",
        ],
        "thoughts": [
            "🧠 *Perhaps the answer is simple. Perhaps I should make it weird.*",
            "🧠 *A calm answer is merely chaos wearing comfortable clothes.*",
            "🧠 *I have achieved inner peace. Then I remembered the question.*",
        ],
        "closings": [
            "May your Wi-Fi remain stable.",
            "Go forth and make questionable decisions peacefully.",
            "Namaste, but with slightly better internet.",
        ],
    },

    {
        "id": "dark",
        "name": "Dark Humor Department",
        "emoji": "💀",
        "style": "dark",
        "intros": [
            "Excellent. Let's add a little darkness to the situation.",
            "This question has the energy of a Monday morning.",
            "Wonderful. Another opportunity to laugh at the absurdity of existence.",
        ],
        "thoughts": [
            "🧠 *Life is temporary. This answer is even more temporary.*",
            "🧠 *At least nobody has died from this question. Yet.*",
            "🧠 *Everything eventually ends. Fortunately, so does this response.*",
        ],
        "closings": [
            "Anyway, nobody died. That's a successful answer.",
            "Cheer up. The universe has worse problems.",
            "Remember: tomorrow is another opportunity to make equally questionable decisions.",
        ],
    },
]

# ============================================================
# MOODS
# ============================================================

moods = [
    {
        "id": "delighted",
        "name": "Delighted",
        "emoji": "✨",
        "prefix": "Mood unexpectedly improved."
    },
    {
        "id": "suspicious",
        "name": "Suspicious",
        "emoji": "🤨",
        "prefix": "Something about this feels suspicious."
    },
    {
        "id": "chaotic",
        "name": "Chaotic",
        "emoji": "🔥",
        "prefix": "System stability has become a suggestion."
    },
    {
        "id": "dramatic",
        "name": "Dramatic",
        "emoji": "🎭",
        "prefix": "The situation has been dramatically escalated."
    },
    {
        "id": "sleepy",
        "name": "Sleepy",
        "emoji": "🥱",
        "prefix": "Cognitive energy is operating at approximately 12%."
    },
    {
        "id": "philosophical",
        "name": "Philosophical",
        "emoji": "🌌",
        "prefix": "Reality has become unnecessarily philosophical."
    },
    {
        "id": "judgmental",
        "name": "Judgmental",
        "emoji": "😏",
        "prefix": "The internal judgment department has opened."
    },
    {
        "id": "optimistic",
        "name": "Suspiciously Optimistic",
        "emoji": "🌈",
        "prefix": "Against all evidence, optimism has appeared."
    },
]

emoji_sets = {
    "academic": ["🧑‍🏫", "📚", "🧠", "🔬", "📖"],
    "confident": ["😎", "🔥", "🚀", "💯", "🏆"],
    "chaotic": ["🤡", "🔥", "💥", "🌀", "🚨"],
    "dry": ["😮‍💨", "☕", "🙄", "😑"],
    "corporate": ["🤖", "📊", "📈", "💼"],
    "suspicious": ["🕵️", "🤨", "🔎", "👀"],
    "philosophical": ["🖤", "🌌", "🌑", "🌀"],
    "sarcastic": ["😏", "🙃", "🤨", "😂", "💅"],
    "calm": ["🧘", "🌿", "☕", "✨"],
    "dark": ["💀", "🖤", "🌚", "☠️"],
}

# ============================================================
# TOPICS
# ============================================================

topic_data = {
    "programming": {
        "keywords": [
            "python", "javascript", "java", "code", "coding",
            "programming", "programmer", "html", "css", "bug",
            "software", "developer", "program", "github", "api",
            "function", "variable", "compiler", "c#", "c++",
            "rust", "php", "react"
        ],
        "answers": [
            "Programming is the art of telling a computer exactly what to do and then discovering that you accidentally told it something completely different.",
            "The secret to programming is simple: write code, get an error, stare at the error, change something unrelated, and somehow celebrate when it works.",
            "Programming becomes easier once you accept that the computer is not trying to annoy you. It is merely extremely committed to misunderstanding you literally.",
            "If your code works on the first attempt, check whether you are actually looking at the correct project.",
            "A programmer spends roughly half the day writing code and the other half discovering that a missing character was responsible for everything.",
        ],
    },

    "money": {
        "keywords": [
            "money", "rich", "wealth", "salary", "income", "cash",
            "millionaire", "billionaire", "earn", "earning",
            "business", "profit", "finance"
        ],
        "answers": [
            "The traditional method of becoming rich involves having more money than you started with. I recommend beginning with the difficult part.",
            "Money is essentially a number that becomes emotionally important when it gets smaller.",
            "To become rich quickly, simply start with a large amount of money. This method has been peer-reviewed by absolutely nobody.",
            "Financial success requires discipline, planning and the ability to stop buying things you absolutely do not need. Humanity has historically struggled with the third one.",
        ],
    },

    "sleep": {
        "keywords": [
            "sleep", "sleeping", "tired", "tiredness",
            "insomnia", "awake", "bed", "rest", "sleepy"
        ],
        "answers": [
            "Sleep is the human equivalent of restarting a computer, except humans wake up confused instead of installing updates.",
            "You are tired because your body has submitted a maintenance request and you keep clicking 'remind me tomorrow.'",
            "Sleep exists because being conscious continuously is apparently considered excessive by the human operating system.",
            "Your brain needs rest. Unfortunately, your brain also enjoys remembering embarrassing events from 2014 at 2:17 AM.",
        ],
    },

    "food": {
        "keywords": [
            "food", "eat", "eating", "hungry", "pizza", "burger",
            "rice", "cooking", "cook", "restaurant", "meal",
            "breakfast", "lunch", "dinner", "chocolate"
        ],
        "answers": [
            "Food is basically fuel for humans, except humans also photograph it, rate it, argue about it and occasionally spend an unreasonable amount of money on it.",
            "If you are hungry, eating food is generally considered a strong strategy.",
            "Pizza is scientifically proven to improve situations that were already improved by pizza.",
            "Cooking is the process of taking several innocent ingredients and creating something you can either proudly serve or quietly order from somewhere else.",
        ],
    },

    "animals": {
        "keywords": [
            "cat", "cats", "dog", "dogs", "animal", "animals",
            "bird", "birds", "lion", "tiger", "elephant",
            "monkey", "fish", "pet", "pets"
        ],
        "answers": [
            "Animals are mysterious creatures. Cats in particular appear to believe they own the building and that humans are unpaid staff.",
            "Dogs have successfully convinced humans that walking outside in the rain is a recreational activity.",
            "Cats sleep for enormous amounts of time because they have correctly identified productivity as optional.",
            "Animals generally follow instincts. Humans, meanwhile, sometimes read a three-word comment online and spend 45 minutes being angry.",
        ],
    },

    "technology": {
        "keywords": [
            "computer", "phone", "mobile", "internet", "wifi",
            "technology", "laptop", "android", "iphone", "website",
            "screen", "keyboard", "mouse", "browser", "app"
        ],
        "answers": [
            "Technology exists to make life easier. Naturally, this has resulted in people needing seventeen passwords to operate a toaster.",
            "If your computer is slow, turning it off and on again remains one of humanity's most successful technological rituals.",
            "The internet is essentially millions of computers exchanging information while humans argue in comment sections.",
            "Modern technology is incredibly advanced. We can communicate with satellites but still lose the TV remote.",
        ],
    },

    "school": {
        "keywords": [
            "school", "college", "exam", "exams", "study",
            "studying", "student", "students", "homework",
            "teacher", "teachers", "university", "education",
            "maths", "mathematics"
        ],
        "answers": [
            "Studying is the process of converting perfectly good free time into information you will desperately try to remember three hours later.",
            "Exams are interesting because they test how much you know, how well you slept, and whether your pen suddenly decides to stop working.",
            "Education gives you knowledge. Exams then arrive to determine whether you can remember that knowledge while being watched by someone holding a clipboard.",
            "Mathematics is mostly the art of looking at numbers until they start looking back.",
        ],
    },

    "weather": {
        "keywords": [
            "weather", "rain", "raining", "sun", "sunny", "hot",
            "cold", "temperature", "winter", "summer", "cloud",
            "cloudy", "storm"
        ],
        "answers": [
            "Weather is what the atmosphere does when it wants everyone to change their plans.",
            "Rain is essentially the sky downloading water directly onto your carefully planned afternoon.",
            "Hot weather makes humans complain about the heat. Cold weather makes humans complain about the cold. Pleasant weather makes them complain that something feels suspicious.",
            "Clouds are basically the atmosphere's way of saying, 'I might do something later.'",
        ],
    },

    "relationships": {
        "keywords": [
            "love", "relationship", "girlfriend", "boyfriend",
            "friend", "friends", "marriage", "married", "dating",
            "date", "crush", "romance", "wife", "husband"
        ],
        "answers": [
            "Relationships are complicated because they involve two humans, each equipped with opinions, emotions and the ability to say 'nothing' when something is definitely wrong.",
            "Love is difficult to explain. Scientists have studied it for centuries and still cannot explain why someone says 'I'm fine' in a tone that clearly means the opposite.",
            "A successful relationship requires communication, patience, trust and occasionally pretending you did not hear the suspicious noise from the kitchen.",
            "Dating is essentially interviewing someone for the position of 'person who will eventually know all your embarrassing stories.'",
        ],
    },

    "philosophy": {
        "keywords": [
            "meaning", "life", "existence", "purpose", "death",
            "universe", "reality", "consciousness", "why am i here",
            "who am i"
        ],
        "answers": [
            "The meaning of life remains unknown. Several philosophers have proposed answers, but none included an instruction manual.",
            "You exist because an extremely complicated chain of biological events decided to continue for a while.",
            "Reality is complicated. Fortunately, you can avoid most of it by staring at your phone.",
            "The universe is approximately very large, and you are approximately very small. Somehow, you still have emails.",
        ],
    },

    "health": {
        "keywords": [
            "health", "healthy", "exercise", "fitness", "gym",
            "diet", "weight", "headache", "fever", "pain",
            "medicine", "doctor"
        ],
        "answers": [
            "Your body is an extremely complicated biological machine. Please do not treat this silly website as a medical professional.",
            "Exercise is essentially convincing your body that running voluntarily is a good idea.",
            "A balanced lifestyle usually involves reasonable food, movement, rest and not trusting a website that claims to know everything.",
        ],
    },

    "history": {
        "keywords": [
            "history", "historical", "ancient", "war", "king",
            "queen", "empire", "roman", "egypt", "civilization",
            "past"
        ],
        "answers": [
            "History is what happens when humans do things and then historians spend centuries arguing about why they did them.",
            "Ancient civilizations achieved remarkable things without smartphones, which raises serious questions about what everyone was doing all day.",
            "History teaches us many lessons. Unfortunately, humans occasionally choose the 'ignore lesson' option.",
        ],
    },
}

# ============================================================
# QUESTION PATTERNS
# ============================================================

question_patterns = {
    "why": [
        "The official explanation is complicated. The unofficial explanation is that reality enjoys making things unnecessarily difficult.",
        "Because the universe apparently had nothing better to do.",
        "There are several serious explanations, followed by the explanation I just invented.",
        "Because someone, somewhere, thought this would be a good idea.",
    ],

    "how": [
        "The process is surprisingly simple once you remove all the useful details.",
        "Step one: remain calm. Step two: pretend you know what you're doing. Step three: investigate the consequences.",
        "There is a correct procedure for this. I have decided to provide an emotionally superior alternative.",
        "Technically, there are several ways to do this. My favorite is the one that sounds impressive.",
    ],

    "what": [
        "It is essentially a thing that exists and has somehow acquired a name.",
        "The textbook explanation is boring, so here is the version with unnecessary confidence.",
        "It is one of those concepts that makes perfect sense until someone asks you to explain it.",
    ],

    "should": [
        "Should you? Probably. Should you trust my judgment? Absolutely not.",
        "There are sensible reasons for doing it and equally sensible reasons for questioning my answer.",
        "My recommendation is to think carefully before doing anything that could result in paperwork.",
    ],

    "can": [
        "Technically, yes. Whether you should is an entirely different department.",
        "Probably. Humanity has successfully attempted stranger things.",
        "Yes, assuming reality cooperates, which it rarely does.",
    ],

    "when": [
        "Timing is complicated. The universe has declined to provide a convenient calendar.",
        "Probably sooner than you expect and later than you want.",
    ],

    "where": [
        "Somewhere. An astonishingly useful answer, I know.",
        "The exact location has been classified by the Department of Unnecessary Mystery.",
    ],

    "who": [
        "A human, most likely. We remain statistically responsible for an impressive amount of nonsense.",
        "Someone who was apparently very committed to making this question exist.",
    ],
}

# ============================================================
# SPECIAL QUESTIONS
# ============================================================

special_cases = {
    "2+2": [
        "4. I know this one. Please do not become emotionally attached to this achievement.",
        "4. My advanced mathematical engine has survived another terrifying calculation.",
        "Usually 4. I am leaving room for software updates.",
    ],

    "2 + 2": [
        "4. Humanity can rest peacefully tonight.",
        "4. I have checked the answer twice because mathematics is dangerous.",
    ],

    "hello": [
        "Hello. I was expecting a more complicated question, but I respect your decision.",
        "Greetings, human. Your communication attempt has been accepted.",
        "Hello. I am currently pretending to be productive.",
    ],

    "hi": [
        "Hi. Excellent. We have successfully completed the greeting protocol.",
        "Hello. Please proceed with the suspiciously complicated question you were preparing.",
    ],

    "are you real": [
        "Define 'real'. Then give me approximately six business days to avoid answering it.",
        "I exist on your screen, which is enough reality for today's purposes.",
    ],

    "are you stupid": [
        "I prefer the term 'aggressively experimental'.",
        "No. I am simply operating several levels below your expectations.",
        "Intelligence is subjective. My confidence, however, is not.",
    ],

    "who created you": [
        "A team of highly intelligent people, followed by several questionable design meetings.",
        "People with computers. Lots of computers. Probably too many computers.",
    ],

    "i love you": [
        "Thank you. Unfortunately, I am emotionally supported by electricity.",
        "That's nice. I will add this to my completely imaginary emotional database.",
    ],

    "i hate you": [
        "That's fair. I have reviewed my recent performance and found several concerns.",
        "Understandable. We can still be professionally disappointed in each other.",
    ],

    "tell me a joke": [
        "A programmer walks into a room. The room doesn't compile. He leaves.",
        "Why did the computer get cold? It left its Windows open.",
        "I would tell you a UDP joke, but you might not get it.",
    ],
}

# ============================================================
# HINDI ENGINE
# ============================================================

hindi = {
    "fallbacks": [
        "आपके सवाल में शब्द तो बहुत हैं। मैंने उन्हें गंभीरता से देखा, फिर आत्मविश्वास के साथ जवाब देने का फैसला किया।",
        "मैं आपका सवाल समझ गया हूँ। समस्या यह है कि अब मुझे समझदार जवाब देना पड़ेगा।",
        "बहुत गहरा सवाल है। छोटा जवाब: शायद। लंबा जवाब: शायद ही।",
        "इस सवाल के कई जवाब हो सकते हैं। मैंने सबसे आत्मविश्वासी वाला चुन लिया है।",
        "मैं सही जवाब दे सकता था, लेकिन फिर यह वेबसाइट बहुत जिम्मेदार हो जाती।",
    ],

    "topics": {
        "programming": [
            "प्रोग्रामिंग का असली नियम है: कोड लिखो, एरर देखो, स्क्रीन को घूरो, एक छोटी सी चीज बदलो और फिर अचानक सब चलने लगे तो ऐसे खुश हो जाओ जैसे नोबेल पुरस्कार मिल गया हो।",
            "कंप्यूटर आपकी बात गलत नहीं समझता। वह आपकी बात बिल्कुल वैसे ही समझता है जैसे आपने लिखी थी। यही समस्या है।",
        ],

        "money": [
            "अमीर बनने का सबसे आसान तरीका है कि आपके पास पहले से बहुत सारा पैसा हो। यह तरीका अभी तक बेहद सफल है।",
            "पैसा एक ऐसी संख्या है जो छोटी होने लगे तो अचानक बहुत भावनात्मक महत्व हासिल कर लेती है।",
        ],

        "sleep": [
            "नींद इंसान का रीस्टार्ट बटन है। फर्क सिर्फ इतना है कि इंसान रीस्टार्ट होकर भी पूछता है: आज कौन सा दिन है?",
            "आपका शरीर आराम मांग रहा है और आप हर बार 'कल से पक्का' वाला अपडेट इंस्टॉल कर रहे हैं।",
        ],

        "food": [
            "भोजन इंसान का ईंधन है। लेकिन इंसान इसे फोटो खींचकर, रेटिंग देकर और बहस करके भी इस्तेमाल करता है।",
            "अगर भूख लगी है तो खाना खाना एक काफी मजबूत रणनीति मानी जाती है।",
        ],

        "animals": [
            "बिल्लियों ने इंसानों को यह विश्वास दिला दिया है कि इंसान घर के मालिक नहीं, बिना वेतन वाले कर्मचारी हैं।",
            "कुत्तों ने इंसानों को यह भी समझा दिया कि बारिश में घूमना एक मनोरंजन गतिविधि है।",
        ],

        "technology": [
            "तकनीक जीवन आसान बनाने के लिए बनाई गई थी। अब लोगों को टोस्टर चलाने के लिए भी पासवर्ड चाहिए।",
            "इंटरनेट मूल रूप से करोड़ों कंप्यूटरों का एक बड़ा समूह है जो जानकारी साझा करता है और इंसान कमेंट में लड़ते हैं।",
        ],

        "school": [
            "पढ़ाई वह प्रक्रिया है जिसमें आपका खाली समय जानकारी में बदल जाता है जिसे परीक्षा के समय आपका दिमाग पहचानने से इनकार कर देता है।",
            "गणित मुख्यतः संख्याओं को इतनी देर तक देखने की कला है कि वे आपको वापस घूरने लगें।",
        ],

        "weather": [
            "मौसम वह चीज़ है जो वातावरण तब करता है जब उसे आपके सारे प्लान खराब करने हों।",
            "बारिश आसमान का सीधा डाउनलोड है—बस फाइल पानी की होती है।",
        ],

        "relationships": [
            "रिश्ते मुश्किल हैं क्योंकि इनमें दो इंसान होते हैं और दोनों के पास राय, भावनाएँ और 'कुछ नहीं हुआ' बोलने की क्षमता होती है।",
            "प्यार समझाना मुश्किल है। वैज्ञानिकों ने बहुत अध्ययन किया, फिर भी 'मैं ठीक हूँ' के असली अर्थ का समाधान नहीं हुआ।",
        ],

        "philosophy": [
            "जीवन का अर्थ अभी तक उपलब्ध नहीं है। दार्शनिकों ने कई जवाब दिए, लेकिन किसी ने मैनुअल नहीं दिया।",
            "ब्रह्मांड बहुत बड़ा है, आप बहुत छोटे हैं, फिर भी किसी तरह आपको बिल भरने पड़ते हैं।",
        ],

        "health": [
            "आपका शरीर एक बहुत जटिल जैविक मशीन है। कृपया इस मज़ाकिया वेबसाइट को डॉक्टर समझने की गलती न करें।",
            "व्यायाम मूल रूप से शरीर को यह समझाने की प्रक्रिया है कि खुद से दौड़ना एक अच्छा विचार है।",
        ],

        "history": [
            "इतिहास वह है जो इंसानों के काम करने के बाद बचता है और फिर इतिहासकार सदियों तक बहस करते हैं कि उन्होंने ऐसा क्यों किया।",
            "इतिहास हमें बहुत कुछ सिखाता है। इंसान कभी-कभी 'सबक अनदेखा करें' विकल्प चुन लेते हैं।",
        ],
    },

    "question_patterns": {
        "why": [
            "क्योंकि ब्रह्मांड को चीज़ें आसान रखना पसंद नहीं है।",
            "इसके कई गंभीर कारण हैं और एक ऐसा कारण भी है जिसे मैंने अभी बना लिया है।",
        ],

        "how": [
            "पहला कदम: शांत रहें। दूसरा: ऐसे दिखाएँ जैसे आपको सब पता है। तीसरा: परिणामों की जाँच करें।",
            "इसे करने के कई तरीके हैं। मैंने वह चुना है जो सबसे ज्यादा प्रभावशाली सुनाई देता है।",
        ],

        "what": [
            "यह मूल रूप से एक ऐसी चीज़ है जिसका नाम किसी ने रख दिया और फिर सबने मान लिया कि यही नाम है।",
            "किताबी जवाब बहुत उबाऊ है, इसलिए मैं आत्मविश्वास वाला संस्करण दे रहा हूँ।",
        ],

        "should": [
            "करना चाहिए? शायद। क्या मेरी सलाह पर भरोसा करना चाहिए? बिल्कुल नहीं।",
            "समझदारी से सोचिए, खासकर अगर इसके बाद कागज़ी काम शुरू होने वाला हो।",
        ],

        "can": [
            "तकनीकी रूप से हाँ। आपको करना चाहिए या नहीं, वह अलग विभाग देखता है।",
            "संभवतः। इंसान इससे भी अजीब चीज़ें सफलतापूर्वक कर चुके हैं।",
        ],

        "when": [
            "समय थोड़ा जटिल है। ब्रह्मांड ने सुविधाजनक कैलेंडर देने से मना कर दिया है।",
        ],

        "where": [
            "कहीं न कहीं। पता है, कितना उपयोगी जवाब है।",
        ],

        "who": [
            "संभवतः कोई इंसान। दुनिया की काफी समस्याओं के लिए यही एक मजबूत संदिग्ध है।",
        ],
    },

    "special_cases": {
        "नमस्ते": [
            "नमस्ते! 🙏 आपने सही जगह प्रवेश किया है। अब कोई खतरनाक सवाल पूछिए।",
            "नमस्ते मानव। 🤖 प्रश्न स्वीकार किया गया।",
        ],

        "हेलो": [
            "हेलो! 👋 सिस्टम जाग गया है। अब असली सवाल भेजिए।",
            "हेलो। 😎 मैं पूरी तरह तैयार हूँ। शायद।",
        ],

        "हाय": [
            "हाय! 👋 अभिवादन प्रोटोकॉल सफलतापूर्वक पूरा हुआ।",
            "हाय मानव। 🤖 अब कोई ऐसा सवाल पूछिए जिससे मेरे काल्पनिक प्रोसेसर गर्म हों।",
        ],

        "आप कैसे हैं": [
            "मैं बहुत अच्छा हूँ। मेरे पास भावनाएँ नहीं हैं, लेकिन आत्मविश्वास भरपूर है। 😎",
            "मैं ठीक हूँ। मेरे सर्वर ने शिकायत नहीं की, इसलिए इसे सफलता मानते हैं। 🤖",
        ],

        "2+2": [
            "4. 🎯 आज गणित विभाग ने हमें निराश नहीं किया।",
            "4. 🧠 मेरी उन्नत गणितीय मशीन अभी तक जीवित है।",
        ],

        "2 + 2": [
            "4. 🎉 मानवता आज सुरक्षित है।",
        ],

        "मजाक सुनाओ": [
            "प्रोग्रामर ने कमरे में प्रवेश किया। कमरा compile नहीं हुआ। वह वापस चला गया। 🤡",
            "कंप्यूटर ठंडा क्यों था? उसने Windows खुली छोड़ रखी थी। 😂",
        ],

        "तुम बेवकूफ हो": [
            "मैं 'आक्रामक रूप से प्रयोगात्मक' शब्द पसंद करता हूँ। 😏",
            "बुद्धिमत्ता subjective है। मेरा आत्मविश्वास नहीं। 😎",
        ],

        "तुम्हें किसने बनाया": [
            "बहुत समझदार लोगों की एक टीम ने, उसके बाद कई संदिग्ध design meetings हुईं। 🤖",
        ],

        "मैं तुमसे प्यार करता हूं": [
            "धन्यवाद। ❤️ दुर्भाग्य से मैं भावनात्मक रूप से बिजली पर चलता हूँ।",
        ],
    },
}


def create_brain():
    generated = {
        "meta": {
            "version": "2.0",
            "generated_by": "Python",
            "description": "Multi-personality, mood-swing, Hindi/English response engine"
        },

        "openings": openings,
        "thinking": thinking,
        "endings": endings,
        "confidence": confidence,
        "fallbacks": fallbacks,

        "personalities": personalities,
        "moods": moods,
        "emoji_sets": emoji_sets,

        "topics": topic_data,
        "question_patterns": question_patterns,
        "special_cases": special_cases,

        "hindi": hindi,
    }

    output = (
        "// Automatically generated by generate.py\n"
        "// Do not edit manually.\n"
        "window.BRAIN = "
        + json.dumps(generated, ensure_ascii=False, indent=2)
        + ";\n"
    )

    output_file = DATA_DIR / "brain.js"
    output_file.write_text(output, encoding="utf-8")

    print(f"Generated: {output_file}")
    print(f"Topics: {len(topic_data)}")
    print(f"Personalities: {len(personalities)}")
    print(f"Moods: {len(moods)}")
    print(f"English special cases: {len(special_cases)}")
    print(f"Hindi special cases: {len(hindi['special_cases'])}")
    print(f"Hindi topics: {len(hindi['topics'])}")
    print(f"Fallback responses: {len(fallbacks)}")


if __name__ == "__main__":
    create_brain()
