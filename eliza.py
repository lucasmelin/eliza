# https://sites.google.com/view/elizagen-org/the-original-eliza
from dataclasses import dataclass
from typing import List, Pattern
import re
import random
from rich.console import Console
from rich.panel import Panel
from time import sleep


class Eliza:
    def __init__(self):
        pass

    def translate(self, str, table):
        words = [table.get(word, word) for word in str.split(" ")]
        return " ".join(words)

    def respond(self, query):
        for topic in topics:
            match = topic.statement.match(query)
            if match:
                response = random.choice(topic.responses)
                if "{0}" not in response:
                    return response
                replacements = self.translate(match.group(1), subject)
                return response.format(replacements).capitalize()


subject = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "i'm": "you are",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}


@dataclass
class Topic:
    statement: Pattern
    responses: List[str]


topics = [
    Topic(
        re.compile(r"I need (.*)", re.IGNORECASE),
        [
            "Why do you need {0}?",
            "Would it really help you to get {0}?",
            "Are you sure you need {0}?",
        ],
    ),
    Topic(
        re.compile(r"Why don\'?t you ([^\?]*)\??", re.IGNORECASE),
        [
            "Do you really think I don't {0}?",
            "Perhaps eventually I will {0}.",
            "Do you really want me to {0}?",
        ],
    ),
    Topic(
        re.compile(r"Why can\'?t I ([^\?]*)\??", re.IGNORECASE),
        [
            "Do you think you should be able to {0}?",
            "If you could {0}, what would you do?",
            "I don't know -- why can't you {0}?",
            "Have you really tried?",
        ],
    ),
    Topic(
        re.compile(r"I can\'?t (.*)", re.IGNORECASE),
        [
            "How do you know you can't {0}?",
            "Perhaps you could {0} if you tried.",
            "What would it take for you to {0}?",
        ],
    ),
    Topic(
        re.compile(r"I am feeling (.*)", re.IGNORECASE),
        [
            "Did you come to me because you are {0}?",
            "How long have you been {0}?",
            "How do you feel about being {0}?",
        ],
    ),
    Topic(
        re.compile(r"I\'?m feeling (.*)", re.IGNORECASE),
        [
            "How does being {0} make you feel?",
            "Do you enjoy being {0}?",
            "Why do you tell me you're {0}?",
            "Why do you think you're {0}?",
        ],
    ),
    Topic(
        re.compile(r"I am (.*)", re.IGNORECASE),
        [
            "Did you come to me because you are {0}?",
            "How long have you been {0}?",
            "How do you feel about being {0}?",
        ],
    ),
    Topic(
        re.compile(r"I\'?m (.*)", re.IGNORECASE),
        [
            "How does being {0} make you feel?",
            "Do you enjoy being {0}?",
            "Why do you tell me you're {0}?",
            "Why do you think you're {0}?",
        ],
    ),
    Topic(
        re.compile(r"Are you ([^\?]*)\??", re.IGNORECASE),
        [
            "Why does it matter whether I am {0}?",
            "Would you prefer it if I were not {0}?",
            "Perhaps you believe I am {0}.",
            "I may be {0} -- what do you think?",
            "Why are you interested in whether or not I am {0}?",
        ],
    ),
    Topic(
        re.compile(r"What (.*)", re.IGNORECASE),
        [
            "Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?",
        ],
    ),
    Topic(
        re.compile(r"How (.*)", re.IGNORECASE),
        [
            "How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?",
        ],
    ),
    Topic(
        re.compile(r"Because (.*)", re.IGNORECASE),
        [
            "Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "If {0}, what else must be true?",
        ],
    ),
    Topic(
        re.compile(r"(.*) sorry (.*)", re.IGNORECASE),
        [
            "There are many times when no apology is needed.",
            "What feelings do you have when you apologize?",
            "Please don't apologize.",
        ],
    ),
    Topic(
        re.compile(r"Hello(.*)", re.IGNORECASE),
        [
            "Hello... I'm glad you could drop by today.",
            "Hi there... how are you today?",
            "Hello, how are you feeling today?",
        ],
    ),
    Topic(
        re.compile(r"I think (.*)", re.IGNORECASE),
        ["Do you doubt {0}?", "Do you really think so?", "But you're not sure {0}?"],
    ),
    Topic(
        re.compile(r"(.*) friend (.*)", re.IGNORECASE),
        [
            "Tell me more about your friends.",
            "When you think of a friend, what comes to mind?",
            "Why don't you tell me about a childhood friend?",
        ],
    ),
    Topic(
        re.compile(r"Yes", re.IGNORECASE),
        ["You seem quite sure.", "OK, but can you elaborate a bit?"],
    ),
    Topic(
        re.compile(r"(.*) computer(.*)", re.IGNORECASE),
        [
            "Are you really talking about me?",
            "Does it seem strange to talk to a computer?",
            "How do computers make you feel?",
            "Do you feel threatened by computers?",
            "Do computers worry you?",
        ],
    ),
    Topic(
        re.compile(r"Is it (.*)", re.IGNORECASE),
        [
            "Do you think it is {0}?",
            "Perhaps it's {0} -- what do you think?",
            "If it were {0}, what would you do?",
            "It could well be that {0}.",
        ],
    ),
    Topic(
        re.compile(r"It is (.*)", re.IGNORECASE),
        [
            "You seem very certain.",
            "If I told you that it probably isn't {0}, what would you feel?",
        ],
    ),
    Topic(
        re.compile(r"Can you ([^\?]*)\??", re.IGNORECASE),
        [
            "What makes you think I can't {0}?",
            "If I could {0}, then what?",
            "Why do you ask if I can {0}?",
        ],
    ),
    Topic(
        re.compile(r"Can I ([^\?]*)\??", re.IGNORECASE),
        [
            "Perhaps you don't want to {0}.",
            "Do you want to be able to {0}?",
            "If you could {0}, would you?",
        ],
    ),
    Topic(
        re.compile(r"You are (.*)", re.IGNORECASE),
        [
            "Why do you think I am {0}?",
            "Does it please you to think that I'm {0}?",
            "Perhaps you would like me to be {0}.",
            "Perhaps you're really talking about yourself?",
        ],
    ),
    Topic(
        re.compile(r"You\'?re (.*)", re.IGNORECASE),
        [
            "Why do you say I am {0}?",
            "Why do you think I am {0}?",
            "Are we talking about you, or me?",
        ],
    ),
    Topic(
        re.compile(r"I don\'?t (.*)", re.IGNORECASE),
        ["Don't you really {0}?", "Why don't you {0}?", "Do you want to {0}?"],
    ),
    Topic(
        re.compile(r"I feel (.*)", re.IGNORECASE),
        [
            "Good, tell me more about these feelings.",
            "Do you often feel {0}?",
            "When do you usually feel {0}?",
            "When you feel {0}, what do you do?",
        ],
    ),
    Topic(
        re.compile(r"I have (.*)", re.IGNORECASE),
        [
            "Why do you tell me that you've {0}?",
            "Have you really {0}?",
            "Now that you have {0}, what will you do next?",
        ],
    ),
    Topic(
        re.compile(r"I would (.*)", re.IGNORECASE),
        [
            "Could you explain why you would {0}?",
            "Why would you {0}?",
            "Who else knows that you would {0}?",
        ],
    ),
    Topic(
        re.compile(r"Is there (.*)", re.IGNORECASE),
        [
            "Do you think there is {0}?",
            "It's likely that there is {0}.",
            "Would you like there to be {0}?",
        ],
    ),
    Topic(
        re.compile(r"My (.*)", re.IGNORECASE),
        [
            "I see, your {0}.",
            "Why do you say that your {0}?",
            "When your {0}, how do you feel?",
        ],
    ),
    Topic(
        re.compile(r"You (.*)", re.IGNORECASE),
        [
            "We should be discussing you, not me.",
            "Why do you say that about me?",
            "Why do you care whether I {0}?",
        ],
    ),
    Topic(
        re.compile(r"Why (.*)", re.IGNORECASE),
        ["Why don't you tell me the reason why {0}?", "Why do you think {0}?"],
    ),
    Topic(
        re.compile(r"I want (.*)", re.IGNORECASE),
        [
            "What would it mean to you if you got {0}?",
            "Why do you want {0}?",
            "What would you do if you got {0}?",
            "If you got {0}, then what would you do?",
        ],
    ),
    Topic(
        re.compile(r"(.*) mother(.*)", re.IGNORECASE),
        [
            "Tell me more about your mother.",
            "What was your relationship with your mother like?",
            "How do you feel about your mother?",
            "How does this relate to your feelings today?",
            "Good family relations are important.",
        ],
    ),
    Topic(
        re.compile(r"(.*) father(.*)", re.IGNORECASE),
        [
            "Tell me more about your father.",
            "How did your father make you feel?",
            "How do you feel about your father?",
            "Does your relationship with your father relate to your feelings today?",
            "Do you have trouble showing affection with your family?",
        ],
    ),
    Topic(
        re.compile(r"(.*) brother(.*)", re.IGNORECASE),
        [
            "Tell me more about your brother.",
            "What was your relationship with your brother like?",
            "How do you feel about your brother?",
            "How does this relate to your feelings today?",
            "Good family relations are important.",
        ],
    ),
    Topic(
        re.compile(r"(.*) sister(.*)", re.IGNORECASE),
        [
            "Tell me more about your sister.",
            "How did your sister make you feel?",
            "How do you feel about your sister?",
            "Does your relationship with your sister relate to your feelings today?",
            "Do you have trouble showing affection with your family?",
        ],
    ),
    Topic(
        re.compile(r"(.*) child(.*)", re.IGNORECASE),
        [
            "Did you have close friends as a child?",
            "What is your favorite childhood memory?",
            "Do you remember any dreams or nightmares from childhood?",
            "Did the other children sometimes tease you?",
            "How do you think your childhood experiences relate to your feelings today?",
        ],
    ),
    Topic(
        re.compile(r"(.*) I remember (.*)", re.IGNORECASE),
        [
            "Does thinking of that bring anything else to mind?",
            "What reminded you of that just now?",
        ],
    ),
    Topic(
        re.compile(r"(.*) always (.*)", re.IGNORECASE),
        [
            "Can you think of a specific instance?",
            "Really -- always?",
        ],
    ),
    Topic(
        re.compile(r"(.*)\?", re.IGNORECASE),
        [
            "Why do you ask that?",
            "Please consider whether you can answer your own question.",
            "Perhaps the answer lies within yourself?",
            "Why don't you tell me?",
        ],
    ),
    Topic(
        re.compile(r"quit", re.IGNORECASE),
        [
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, have a good day!",
        ],
    ),
    Topic(
        re.compile(r"(.*)", re.IGNORECASE),
        [
            "Please tell me more.",
            "Let's change focus a bit... Tell me about your family.",
            "Can you elaborate on that?",
            "Why do you say that {0}?",
            "I see.",
            "Very interesting.",
            "{0}.",
            "I see. And what does that tell you?",
            "How does that make you feel?",
            "How do you feel when you say that?",
            "Go on.",
        ],
    ),
]


def format_statement(statement):
    s = statement.rstrip("!.")
    return s.lower()


def eliza_say(console, statement, typing_min=1, typing_max=3, color="green"):
    with console.status(f"[bold {color}]Eliza is typing...", spinner="point"):
            typing_time = random.uniform(typing_min, typing_max)
            sleep(typing_time)
            console.print(f"[bold {color}]{statement}")


def program():
    console = Console()
    console.print("[light_green]Eliza", justify="center", style="bold")
    panel = Panel('[orange1]Talk to Eliza by typing in plain English, using normal upper and lower-case letters and punctuation. Enter "quit" when done.')
    console.print(panel)

    eliza_say(console, "Hello, I am Eliza. How are you feeling today?")
    s = ""
    therapist = Eliza()

    while s != "quit":
        try:
            s = input("> ")
            s = format_statement(s)
        # This Exception is raised with Ctrl+Z
        except EOFError:
            s = "quit"
            print(s)
        eliza_say(console, therapist.respond(s))
        #print(therapist.respond(s))


if __name__ == "__main__":
    program()
