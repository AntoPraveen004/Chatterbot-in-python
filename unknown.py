import random

def unknown():
    unknown1 = ["Please try writing something more descriptive -_-",
        "Oh! It appears you wrote something I don't understand yet -_-",
        "Do you mind trying to rephrase that? -_-",
        "I'm terribly sorry, I didn't quite catch that -_-",
        "I can't answer that yet, please try asking something else -_-"][random.randrange(5)]
    return unknown1