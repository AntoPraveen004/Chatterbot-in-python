import random

def movie_genre():
    movie_genre1 = ["Prefer a Genre\n"+"Action\nAdventure\nScifi\nComedy"]
    return movie_genre1[0]

def action():
    action1 =["SpiderHead","Avatar:The way of water","Memory","The princes","Vikram","Dr.Strange Multiverse of Madness","Prey","Interceptor","The Jurassic World","Last seen alive","John Wick: Chapter 4","John Wick","65","Avengers: Endgame","Avatar","RRR","The Gray Man"]

    length = len(action1)
    rd = random.randrange(length)
    return action1[rd]

def adventure():
    adventure1 = ["Uncharted","Encanto","Jungle Cruise","How to train your dragon","The suicide squad","No time to die","Alita: Battle Angel","Jumanji The next level","Dune","Avengers:End Game"]
    length = len(adventure1)
    rd = random.randrange(length)
    return adventure1[rd]

def scifi():
    scifi1 = ["Interstellar","Inception","Arrival","A.I Artificial Intelligence","The Adam Project","Martian","Source code","Tik-Tik-Tik","Voyagers","Matrix Reloaded","Independence day","Battleship"]
    length = len(scifi1)
    rd = random.randrange(length)
    return scifi1[rd]

def comedy():
    comedy1 = ["Hangover 1","Hangover 2","Hangover 3","The Wolf of wall street","Big","Modern times","City lights","The mask","Bean","10","Men in black","Rush hour","Rush hour 2","Rush hour 3","Shaolin Soccer"]
    length = len(comedy1)
    rd = random.randrange(length)
    return comedy1[rd]