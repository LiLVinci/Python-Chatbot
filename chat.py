import random
import json
import torch
import weirdbackend 
import time

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from weirdbackend import chatBackEnd
from weirdbackend import chatPreparation





context = None


bot_name = "Steve"
chatPreparation()
print("")
print(f"{bot_name}: Hi there! Im {bot_name}!")
time.sleep(1)
print(f"{bot_name}: What is your name?")
time.sleep(1)
username = input("You: ")
time.sleep(1)
print(f"{bot_name}: Its great to meet you {username}!")
time.sleep(1)
print(f"{bot_name}: What do you want to talk about?")

while True:
    global sentence
    time.sleep(1)
    sentence = input("You: ")
    if sentence == "quit":
        break

    chatBackEnd(sentence)

    
    if weirdbackend.prob.item() > 0.75: 

        if context == None:

            for intent in weirdbackend.intents['intents']:
                if weirdbackend.tag == intent["tag"]:
                    time.sleep(1)
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    # 1. add soemthing here that if the intent has a context_set, a new variable of "context" is defined with it
                    if "context_set" in intent:
                        context = intent["context_set"]


        # 2. IF context is set, check that the context_filter is equal to the variable "context"
        # 3. IF the if statement 2 is correct, make the context null

        elif context != None:

            for intent in weirdbackend.intents['intents']:
            
                if weirdbackend.tag == intent["tag"]: 
                    if "context_filter" in intent and context == intent["context_filter"]:
                        time.sleep(1)
                        print(f"{bot_name}: {random.choice(intent['responses'])}")
                        # 1. add soemthing here that if the intent has a context_set, a new variable of "context" is defined with it
                        context = None
                        if "context_set" in intent:
                            context = intent["context_set"]
                        
                    else:
                        time.sleep(1)
                        print(f"{bot_name}: I am sorry, I dont understand the answer, lets forget the question.")
                        context = None

            # 2. IF context is set, check that the context_filter is equal to the variable "context"
            # 3. IF the if statement 2 is correct, make the context null

    elif context != None:
        time.sleep(1)
        print(f"{bot_name}: I am sorry, I dont understand the answer, lets forget the question.")
        context = None

    else:
        time.sleep(1)
        print(f"{bot_name}: I do not understand...")