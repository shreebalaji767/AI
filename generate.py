from pathlib import Path
import json
import random

random.seed()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

openings = [
    "Excellent question.",
    "Interesting. I have investigated this matter extensively.",
    "Finally, someone is asking the important questions.",
    "I have analyzed your question with unnecessary seriousness.",
    "This question requires advanced intellectual machinery.",
    "I was not prepared for this question, but I will pretend I was.",
    "Processing your question through several highly questionable algorithms.",
    "A fascinating question. Probably.",
    "I have consulted my internal department of questionable expertise.",
    "After thinking about this for far too long...",
    "Your question has been received by the Department of Answers.",
    "I understand approximately 83% of what you are asking.",
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
]

confidence = [
    "97.4%",
    "99.1%",
    "83.7%",
    "100%",
    "91.3%",
    "76.8%",
    "98.6%",
    "88.2%",
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
]

topic_data = {
    "programming": {
        "keywords": [
            "python", "javascript", "java", "code", "coding", "programming",
            "programmer", "html", "css", "bug", "software", "developer",
            "program", "github", "api", "function", "variable", "compiler"
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
            "money", "rich", "wealth", "salary", "income", "cash", "millionaire",
            "billionaire", "earn", "earning", "business", "profit", "finance"
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
            "sleep", "sleeping", "tired", "tiredness", "insomnia", "awake",
            "bed", "rest", "sleepy"
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
            "food", "eat", "eating", "hungry", "pizza", "burger", "rice",
            "cooking", "cook", "restaurant", "meal", "breakfast", "lunch",
            "dinner", "chocolate"
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
            "cat", "cats", "dog", "dogs", "animal", "animals", "bird", "birds",
            "lion", "tiger", "elephant", "monkey", "fish", "pet", "pets"
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
            "computer", "phone", "mobile", "internet", "wifi", "technology",
            "laptop", "android", "iphone", "website", "website", "screen",
            "keyboard", "mouse", "browser", "app"
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
            "school", "college", "exam", "exams", "study", "studying",
            "student", "students", "homework", "teacher", "teachers",
            "university", "education", "maths", "mathematics"
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
            "weather", "rain", "raining", "sun", "sunny", "hot", "cold",
            "temperature", "winter", "summer", "cloud", "cloudy", "storm"
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
            "love", "relationship", "girlfriend", "boyfriend", "friend",
            "friends", "marriage", "married", "dating", "date", "crush",
            "romance", "wife", "husband"
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
            "meaning", "life", "existence", "purpose", "death", "universe",
            "reality", "consciousness", "why am i here", "who am i"
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
            "health", "healthy", "exercise", "fitness", "gym", "diet",
            "weight", "headache", "fever", "pain", "medicine", "doctor"
        ],
        "answers": [
            "Your body is an extremely complicated biological machine. Please do not treat this silly website as a medical professional.",
            "Exercise is essentially convincing your body that running voluntarily is a good idea.",
            "A balanced lifestyle usually involves reasonable food, movement, rest and not trusting a website that claims to know everything.",
        ],
    },

    "history": {
        "keywords": [
            "history", "historical", "ancient", "war", "king", "queen",
            "empire", "roman", "egypt", "civilization", "past"
        ],
        "answers": [
            "History is what happens when humans do things and then historians spend centuries arguing about why they did them.",
            "Ancient civilizations achieved remarkable things without smartphones, which raises serious questions about what everyone was doing all day.",
            "History teaches us many lessons. Unfortunately, humans occasionally choose the 'ignore lesson' option.",
        ],
    },
}

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
}

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

def normalize(text):
    return " ".join(text.lower().strip().split())

def create_brain():
    generated = {
        "meta": {
            "version": "1.0",
            "generated_by": "Python",
            "description": "Generated response engine data"
        },
        "openings": openings,
        "thinking": thinking,
        "endings": endings,
        "confidence": confidence,
        "fallbacks": fallbacks,
        "topics": topic_data,
        "question_patterns": question_patterns,
        "special_cases": special_cases,
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
    print(f"Special cases: {len(special_cases)}")
    print(f"Fallback responses: {len(fallbacks)}")

if __name__ == "__main__":
    create_brain()
