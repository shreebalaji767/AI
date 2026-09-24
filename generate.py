import json
import os
import random

random.seed()

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

brain = {
    "openers": [
        "Excellent question.",
        "Interesting. I have investigated this thoroughly.",
        "I was hoping nobody would ask me this.",
        "Finally, a question worthy of my enormous computational resources.",
        "Processing your question with unnecessary confidence.",
        "I have consulted my imaginary experts.",
        "This requires serious analysis. Unfortunately, I am available.",
        "After several milliseconds of intense thinking, I have reached a conclusion.",
        "Your question has been received and immediately judged.",
        "Let me answer that before I change my mind."
    ],

    "processing": [
        "Analyzing the situation...",
        "Consulting highly classified databases...",
        "Checking several suspicious sources...",
        "Asking an imaginary scientist...",
        "Performing advanced nonsense calculations...",
        "Ignoring common sense...",
        "Cross-referencing absolutely nothing...",
        "Calculating the confidence-to-evidence ratio...",
        "Searching the universal database of questionable knowledge...",
        "Removing useful information from the answer..."
    ],

    "closings": [
        "You're welcome.",
        "Please use this information responsibly. Or don't.",
        "I hope this completely solves your problem.",
        "Science may disagree. I do not.",
        "I am approximately 14% sure about this.",
        "Further research is unnecessary because I have already spoken.",
        "Please do not quote me professionally.",
        "That will be ₹0.00.",
        "My work here is unnecessarily complete.",
        "I accept no responsibility for what happens next."
    ],

    "confidence": [
        "97.4%",
        "99.1%",
        "83.7%",
        "100.0%",
        "91.3%",
        "76.8%",
        "98.6%",
        "88.2%",
        "104.7%",
        "approximately 12%"
    ],

    "generic": [
        "The answer is surprisingly complicated, mostly because nobody bothered to make it simple.",
        "This happens because reality has a poor user interface.",
        "The official explanation is complicated. My explanation is shorter and significantly less trustworthy.",
        "After reviewing the available evidence, I have decided that this is probably someone's fault.",
        "Technically there is an explanation. Emotionally, however, we are still investigating.",
        "The universe has not provided a satisfactory answer, so I have invented one.",
        "This is one of those situations where confidence is much cheaper than knowledge.",
        "There are several possibilities, and I have selected the funniest one."
    ],

    "why": [
        "Because reality enjoys making simple things unnecessarily complicated.",
        "Because someone, somewhere, thought this was a good idea.",
        "Because the universe apparently has a sense of humor.",
        "Because that was the easiest solution available at the time.",
        "Because nobody stopped the process early enough.",
        "Because physics has been making questionable decisions for billions of years.",
        "Because this is apparently how things work and nobody submitted a complaint."
    ],

    "how": [
        "First, pretend you know what you're doing.",
        "Start by finding the nearest available solution and looking confident.",
        "The traditional method is to try something, fail, and call it research.",
        "Begin with step one. Unfortunately, nobody knows what step one is.",
        "Acquire the necessary equipment, knowledge, patience, and approximately three miracles.",
        "Do it carefully. Or quickly. The results will probably be educational either way."
    ],

    "should": [
        "Probably. But I recommend making the decision after dramatically staring out of a window.",
        "Yes, unless you enjoy having free time.",
        "Only if you are prepared for consequences, tutorials, and unnecessary opinions.",
        "That depends. I have decided not to provide the dependency.",
        "Absolutely. This is either an excellent idea or an excellent story for later.",
        "I would investigate further, but that sounds like work."
    ],

    "programming": [
        "Programming is essentially convincing a computer to do something while the computer repeatedly asks you to prove that you deserve happiness.",
        "The secret to programming is knowing that the error message is not an insult. It merely feels like one.",
        "Programming becomes easier once you accept that approximately 70% of development is discovering why yesterday's working code has developed opinions.",
        "Learn the basics, build tiny projects, break things, fix them, and repeat until the computer respects you.",
        "Programming is mostly logic, patience, debugging, and occasionally staring at a semicolon for forty minutes."
    ],

    "money": [
        "The fastest way to become rich is to start with a large amount of money.",
        "Money can buy many things, including approximately 14 minutes of happiness and a suspiciously expensive cup of coffee.",
        "Financial success usually involves earning more than you spend. I know. Revolutionary.",
        "I recommend increasing income, controlling expenses, and avoiding financial advice from websites written entirely in capital letters."
    ],

    "sleep": [
        "Sleep is the human equivalent of restarting a computer after installing seventeen updates.",
        "Your body is requesting maintenance mode.",
        "Humans require sleep because apparently consciousness is a resource-intensive application.",
        "You should sleep. Your brain has submitted a formal complaint."
    ],

    "weather": [
        "The atmosphere has decided to improvise.",
        "Weather is basically the sky changing its mind every few hours.",
        "The forecast is accurate until the atmosphere develops a personality.",
        "I checked the sky. It refused to provide a statement."
    ],

    "love": [
        "Love is an advanced human feature with no documentation and several known bugs.",
        "Love is when two people voluntarily become responsible for each other's emotional software updates.",
        "Scientists have studied love extensively and still cannot explain why people send messages and then stare at the screen waiting for a reply.",
        "Love is complicated. Pizza is simpler."
    ],

    "cats": [
        "Cats sleep because maintaining that level of judgment requires energy.",
        "Cats are not lazy. They are operating under a highly optimized schedule that excludes your requests.",
        "A cat's primary responsibilities are sleeping, eating, staring at walls, and pretending not to hear you."
    ],

    "food": [
        "Food is generally more enjoyable when someone else prepares it and you don't have to wash the dishes.",
        "The scientific solution is to eat something sensible and then immediately question why you didn't order something better.",
        "Calories are simply tiny units of regret that become visible on spreadsheets."
    ],

    "computer": [
        "Computers are extremely fast at doing exactly what you told them instead of what you meant.",
        "Restart it. This is not laziness. It is a respected technological tradition.",
        "Your computer is probably fine. It has simply decided that today is an opportunity for personal growth.",
        "Computers have no common sense, but they have excellent confidence."
    ],

    "life": [
        "The meaning of life is currently unavailable because the responsible department is on lunch break.",
        "Life appears to be a subscription service with confusing terms and no obvious cancel button.",
        "Nobody really knows. Humans have been improvising for thousands of years.",
        "The current strategy appears to be: wake up, eat something, solve problems, create new problems, sleep."
    ],

    "math": [
        "Mathematics is the art of making numbers look innocent before they ruin your afternoon.",
        "The numbers are behaving normally. Unfortunately, the human involved is you.",
        "I performed the calculation and discovered that mathematics continues to be unnecessarily confident.",
        "The answer is probably somewhere between zero and an alarming amount."
    ],

    "school": [
        "School prepares you for adulthood by teaching you how to carry seventeen things at once while someone asks why you haven't finished something.",
        "Education is important. Remembering where you put your pen is apparently an advanced elective.",
        "The good news is that nobody understands everything. The bad news is that exams still exist."
    ],

    "work": [
        "Work is a sophisticated arrangement where humans exchange time for money and then spend some of that money recovering from work.",
        "The secret to productivity is starting before you have a 47-tab browser situation.",
        "Meetings are sometimes emails that have evolved legs."
    ],

    "health": [
        "For general health questions, humans usually benefit from sleep, sensible food, movement, and advice from an actual qualified professional when needed.",
        "Your body is complicated biological machinery. Please do not let an extremely confident website diagnose it.",
        "I can make jokes about health, but your doctor gets the serious version."
    ],

    "history": [
        "History is essentially humanity's very long collection of examples titled: 'Perhaps We Should Have Thought About This First.'",
        "Humans have been making questionable decisions for thousands of years, so congratulations on participating in a proud tradition.",
        "History is complicated because apparently nobody could agree to write the documentation first."
    ]
}

with open(os.path.join(DATA_DIR, "brain.js"), "w", encoding="utf-8") as f:
    f.write(
        "window.BRAIN = "
        + json.dumps(brain, ensure_ascii=False, indent=2)
        + ";\n"
    )

print("Response engine generated successfully.")
