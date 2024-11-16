import random

def games_genre():
    games_genre1 = ["Prefer a Genre\n"+"online\noffline"]
    return games_genre1[0]

def online():
    online1 = ["Fortnite","PlayerUnknown's Battlegrounds","Call of Duty: Warzone","Apex Legends","League of Legends","World of Warcraft","Overwatch","Counter-Strike: Global Offensive","Dota 2","Minecraft"]
    length = len(online1)
    rd = random.randrange(length)
    return online1[rd]

def offline():
    offline1 = ["The Legend of Zelda: Breath of the Wild","Uncharted 4: A Thief's End","Tomb Raider (2013)","Life is Strange","Firewatch","The Walking Dead (season one)","Assassin's Creed: Origins","Horizon Zero Dawn","Gone Home","Until Dawn","Detroit: Become Human","The Last of Us"]
    length = len(offline1)
    rd = random.randrange(length)
    return offline1[rd]