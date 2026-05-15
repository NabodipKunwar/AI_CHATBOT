poem_topics = [
    "feeling happy after success",
    "feeling sad on a rainy night",
    "missing family while studying far away",
    "feeling lonely but hopeful",
    "being excited for a new beginning",
    "feeling calm near a river",
    "working hard for a dream",
    "feeling proud after failure and recovery",
    "being nervous before exams",
    "feeling motivated to improve"
]

advice_topics = [
    "exam stress",
    "coding frustration",
    "lack of confidence",
    "overthinking",
    "procrastination",
    "time management",
    "fear of failure",
    "presentation fear",
    "study pressure",
    "personal growth"
]

story_topics = [
    "a poor student builds a robot that saves his village",
    "a robot enters a magical forest to understand emotions",
    "a girl discovers a secret library under her school",
    "a boy finds a glowing crystal in the jungle",
    "a dragon protects a village from a storm",
    "an astronaut lands on a planet full of friendly aliens",
    "a student creates an AI that helps lonely people",
    "a child finds a magical book that writes back",
    "a farmer discovers seeds that grow golden trees",
    "a musician calms a giant monster with music"
]

with open("dataset.txt", "w", encoding="utf-8") as file:

    for i in range(100):
        topic = poem_topics[i % len(poem_topics)]

        file.write(f"""### Instruction:
Write a beautiful 8-line poem about {topic}.

### Response:
Soft light rises in the sky,
Hope begins to gently fly.
Every dream that felt so far,
Glows again like morning star.
Through the silence, hearts grow strong,
Finding courage through the song.
Even when the night feels deep,
Faith gives peace before we sleep.

""")

    for i in range(100):
        topic = advice_topics[i % len(advice_topics)]

        file.write(f"""### Instruction:
Give kind and practical personal advice about {topic}.

### Response:
For {topic}, start by staying calm and understanding the real problem. Break the situation into small steps instead of trying to solve everything at once. Make a simple plan, take short breaks, and keep improving every day. If the problem feels too heavy, talk to someone you trust for support.

""")

    for i in range(100):
        topic = story_topics[i % len(story_topics)]

        file.write(f"""### Instruction:
Write a creative short story about {topic}.

### Response:
Once upon a time, {topic}. At first, the journey seemed difficult, and the main character did not know what to do. But with courage and patience, they began to understand the problem and searched for a solution.

Along the way, they met helpful friends, faced unexpected challenges, and discovered something important about kindness, bravery, and hope. In the end, the problem was solved, and everyone learned that even small actions can create a big change.

""")

print("dataset.txt created with 300 high-quality examples!")