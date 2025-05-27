import re
import random

# Reflection map to switch pronouns for more conversational responses.
reflections = {
    "am": "are", "was": "were", "i": "you", "i'd": "you would", "i've": "you have",
    "i'll": "you will", "my": "your", "are": "am", "you've": "I have",
    "you'll": "I will", "your": "my", "yours": "mine", "you": "me", "me": "you"
}

# A list of pattern-response pairs. ELIZA picks the first pattern that matches.
patterns = [
    (r'I need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]),
    (r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]),
    (r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you really tried?"]),
    (r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]),
    (r'I am (.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]),
    (r'I\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}?",
      "Why do you tell me you're {0}?"]),
    (r'(.*) mother(.*)',
     ["Tell me more about your mother.",
      "What was your relationship with your mother like?"]),
    (r'(.*)\?',
     ["Why do you ask that?",
      "What do you think?",
      "Can you answer your own question?"]),
    (r'(.*)',
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see. And what does that tell you?",
      "How does that make you feel?"])
]

def reflect(fragment):
    """Reflects pronouns in the user's input for more natural responses."""
    tokens = fragment.lower().split()
    return ' '.join([reflections.get(word, word) for word in tokens])

def eliza_response(user_input):
    """Finds a matching pattern and returns an ELIZA-like response."""
    for pattern, responses in patterns:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            # Pick a random response and fill in captured groups, reflecting pronouns.
            resp = random.choice(responses)
            groups = [reflect(g) for g in match.groups()]
            return resp.format(*groups)
    return "Please go on."  # fallback

def main():
    print("ELIZA: Hello. How are you feeling today? (Type 'quit' to exit)")
    while True:
        user_input = input("> ")
        if user_input.lower() in ('quit', 'exit', 'bye'):
            print("ELIZA: Goodbye! Take care.")
            break
        print("ELIZA:", eliza_response(user_input))

if __name__ == "__main__":
    main()
