import numpy as np
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from utils import Clean_text
from model import NeuralNet


with open('intents.json', 'rb') as f:
    intents = json.load(f)


tags = sorted([intent['tag'] for intent in intents['intents']])

x_train = []
y_train = []

for intent in intents['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        new_pattern = Clean_text(pattern)
        label = tags.index(tag)
        x_train.extend(new_pattern.docs)
        y_train.append(label)

x_train_vectors = [x.vector for x in x_train]

x_train_vectors = np.array(x_train_vectors)
y_train = np.array(y_train)

# Hiperparâmetros
num_epochs = 3000
batch_size = 8
learning_rate = 0.001
input_size = len(x_train_vectors[0])
hidden_size = 8
output_size = len(tags)


class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train_vectors)
        self.x_data = x_train_vectors
        self.y_data = y_train

    # suporte a indexação de modo que o dataset[i] possa ser usado para obter a i-ésima amostra
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # podemos chamar len(dataset) para retornar o tamanho
    def __len__(self):
        return self.n_samples


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss e optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# loop para treinar o modelo
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        # Forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        # Backward e optimizer
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.8f}')

print(f'ultima loss: {loss.item():.4f}')


data = {
    "model state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'Treinamento completo, arquivo salvo em: {FILE}')
