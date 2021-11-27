from random import choice
import json

import torch

from model import NeuralNet
from utils import Clean_text

with open("intents.json", 'rb') as f:
    intents = json.load(f)


FILE = "data.pth"

data = torch.load(FILE)

model_state = data['model state']
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
tags = data['tags']

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


bot_name = "Bia"


def get_response(msg):
    X = Clean_text(msg).docs[0]
    X_vector = X.vector

    X_tensor = torch.from_numpy(X_vector)
    output = model(X_tensor)

    _, predicted = torch.max(output, dim=0)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=0)
    prob = probs[predicted.item()]
    prob = prob.item()

    if prob > 0.7:
        for intent in intents['intents']:
            if intent['tag'] == tag:
                responses = intent['responses']
                response = choice(responses)
    else:
        response = "Desculpa, não entendi."

    return response
