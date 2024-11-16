import re

import movies as m
import songs as s
import games as g

import unknown as u

import greeting as gr

# Checks the probability of the user message
def check_for_probability(message,list_of_words,single_response=False,required_message=[]):
    message_certainity = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for words in message:
        if words in list_of_words:
            message_certainity += 1

    # Checks that the required words are in the string
    for words in required_message:
        if words not in message:
            has_required_words = False
            break

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainity)/float(len(list_of_words))

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return (percentage*100)
    else:
        return 0


def check_message(message):
    probability_of_messages = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response,list_of_words,single_response=False,required_message=[]):
        nonlocal probability_of_messages
        probability_of_messages[bot_response] = check_for_probability(message,list_of_words,single_response,required_message)

    #GREETING RESPONSES ------------------------------------------------------------------------------
    response(gr.greetings(),["hi","hello","hey","vanakkam"],single_response=True)
    response(gr.goodbye(),["bye","goodbye","cya"],single_response=True)
    response(gr.welcome(),["thank you","thanks","thank","thankyou"],single_response=True)

    #MOVIE RESPONSES ---------------------------------------------------------------------------------
    response(m.movie_genre(),["movies","movies?","movie"],single_response=True)
    response(m.action(),["action","action?"],single_response=True)
    response(m.adventure(),["adventure","adventure?"],single_response=True)
    response(m.scifi(),["scifi","sci-fi","scifi?"],single_response=True)
    response(m.comedy(),["comedy","comedy","comedy?"],single_response=True)

    #SONGS RESPONSES ---------------------------------------------------------------------------------
    response(s.songs_genre(),["songs","songs?","song"],single_response=True)
    response(s.hiphop(),["hiphop","hiphop?"],single_response=True)
    response(s.pop(),["pop","pop?"],single_response=True)
    response(s.jazz(),["jazz","jazz?"],single_response=True)
    response(s.rock(),["rock","rock?"],single_response=True)


    #GAMES RESPONSES ---------------------------------------------------------------------------------
    response(g.games_genre(),["games","games?","game"],single_response=True)
    response(g.online(),["online","online?"],single_response=True)
    response(g.offline(),["offline","offline?"],single_response=True)

    best_response = max(probability_of_messages,key=probability_of_messages.get)

    #print(probability_of_messages)

    return u.unknown() if probability_of_messages[best_response] < 1 else best_response


# Used to get the response
def get_response(user_message):
    message1 = user_message.lower()
    split_message = re.split(r'\s+|[,-;%@_!?]\s',message1.strip())
    response = check_message(split_message)
    return response

# Testing the response system
while True:
    i = input("You: ")
    out = get_response(i)
    print("Wall-E: " + out)