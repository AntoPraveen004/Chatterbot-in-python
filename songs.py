import random

def songs_genre():
    songs_genre1 = ["Prefer a Genre\n"+"Hiphop\nPop\nJazz\nRock"]
    return songs_genre1[0]

def hiphop():
    hiphop1 = ["the message","rappesrs delight","planet rock","suckers"," Lose Yourself","Bodak Yellow","Ms. Jackson","Mind Playing Tricks on Me","Dear Mama","Lost Ones","Fight The Power" ,"Juicy","Alright","Rosa Parks ","Grindin","Lose Yourself","Doo Wop","International Players Anthem","U.N.I.T.Y.","Fuck Tha Police","It Was A Good Day","B.O.B","They Reminisce Over You (T.R.O.Y.)","Rapper’s Delight","Paid In Full","Runaway","Electric Relaxation","Dear Mama","State Of Mind","hassin’ Me By","93 ’Til Infinity","C.R.E.A.M.","Nuthin’ But A ‘G’ Thang Dr. Dre ","The Message","Shook Ones (Part II)","Fight The Power","Juicy", "Russ","Coi Leray","Toosii" ,"Tom MacDonald & John Rich"]
    length = len(hiphop1)
    rd = random.randrange(length)
    return hiphop1[rd]

def pop():
    pop1 = ["Shape of You","Despacito" ,"Uptown Funk", "Sorry" ,"Can't Stop the Feeling!" ,"Closer","Bad Guy" "Blinding Lights","Hello" ,"All About That Bass" ,"Shallow" ,"One Dance" ,"Hotline Bling","Love Yourself", "Rude" ,"Happy", "I Will Always Love You","Thinking Out Loud" ,"Royals" ,"Counting Stars","Sugar" ,"The Middle" ,"Shake It Off" ,"Stressed Out","Stay with Me", "Stay" ,"I'm Yours" ,"Girls Like You","Watermelon Sugar" ,"Dynamite" ,"Roar","Radioactive","Shape of My Heart" ,"California Gurls" ,"Perfect" ,"Attention","Love On Top" ,"Locked Out of Heaven" ,"Can't Hold Us",]
    length = len(pop1)
    rd = random.randrange(length)
    return pop1[rd]

def jazz():
    jazz1 = ["Take Five","My Favorite Things" ,"Fly Me to the Moon", "Misty","Round Midnight" ,"Summertime","Autumn Leaves" ,"Georgia on My Mind"," All Blues" ,"In a Sentimental Mood" ,"On Green Dolphin Street" ,"Blue in Green" ,"I Can't Get Started" ,"A Love Supreme","What a Wonderful World","God Bless the Child" ,"It Don't Mean a Thing","Someday My Prince Will Come","Pennies from Heaven","The Girl from Ipanema","St. Thomas" ,"Take the A Train","Cantaloupe Island","Giant Steps","I Got Rhythm" ,"A Night in Tunisia","Moanin'","Cry Me a River" ,"Spain" ,"Body and Soul" ,"Watermelon Man" ,"Caravan" ,"Mack the Knife" ,"Lush Life" ,"Straight, No Chaser" ,"Fever" ,"I've Got You Under My Skin" ,"Boplicity" ,"Route 66"]
    length = len(jazz1)
    rd = random.randrange(length)
    return jazz1[rd]

def rock():
    rock1 = ["Stairway to Heaven", "Bohemian Rhapsody", "Sweet Child o' Mine", "Back in Black","Smells Like Teen Spirit"]
    length = len(rock1)
    rd = random.randrange(length)
    return rock1[rd]