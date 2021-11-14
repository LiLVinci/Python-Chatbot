import random

import json

import torch

# import chat

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


def chatPreparation():



  global device
  global data
  global FILE
  global input_size
  global hidden_size
  global output_size
  global all_words
  global tags
  global model
  global intents




  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

  with open('intents.json', 'r') as json_data:
      intents = json.load(json_data)

  FILE = "data.pth"
  data = torch.load(FILE)

  input_size = data["input_size"]
  hidden_size = data["hidden_size"]
  output_size = data["output_size"]
  all_words = data['all_words']
  tags = data['tags']
  model_state = data["model_state"]

  model = NeuralNet(input_size, hidden_size, output_size).to(device)
  model.load_state_dict(model_state)
  model.eval()

def chatBackEnd(chatSentence):

    global sentence
    global prob
    global tag

    sentence = tokenize(chatSentence) #
    X = bag_of_words(sentence, all_words) #
    X = X.reshape(1, X.shape[0]) #
    X = torch.from_numpy(X).to(device) #

    output = model(X) #
    _, predicted = torch.max(output, dim=1) #

    tag = tags[predicted.item()] #

    probs = torch.softmax(output, dim=1) #
    prob = probs[0][predicted.item()] #