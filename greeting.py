import random

def greetings():
    greetings1 = ["Hello, This is Wall-E!\nWhat are you looking for?\nMovies\nSongs\nGames","Hola, This is Wall-E!\nWhat are you looking for?\nMovies\nSongs\nGames","Hi, This is Wall-E!\nWhat are you looking for?\nMovies\nSongs\nGames","Hey, This is Wall-E!\nWhat are you looking for?\nMovies\nSongs\nGames","Vanakkam, This is Wall-E!\nWhat are you looking for?\nMovies\nSongs\nGames"][random.randrange(5)]
    return greetings1

def goodbye():
    goodbye1 = ["Good Bye!","Bye bye!","See you later!"]
    length = len(goodbye1)
    rd = random.randrange(length)
    return goodbye1[rd]

def welcome():
    welcome1 = ["Your most welcome!","Your Welcome!","No mention :)"]
    length = len(welcome1)
    rd = random.randrange(length)
    return welcome1[rd]