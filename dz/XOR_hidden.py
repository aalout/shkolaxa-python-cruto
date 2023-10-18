#C помощью скрытого слоя нейронов, сеть способна обучиться выражать нелинейные зависимости между входами и выходами
#Много чего подсмотрел в инете, не ругайте сильно:(

import torch
import torch.nn as nn
import torch.optim as optim

inputs = torch.tensor([[-1, -1], [-1, 1], [1, -1], [1, 1]], dtype=torch.float32)
labels = torch.tensor([0, 1, 1, 0], dtype=torch.float32)

class XORModel(nn.Module):
    def __init__(self):
        super(XORModel, self).__init__()
        self.hidden = nn.Linear(2, 2) #Скрытый слой с 2 нейронами
        self.output = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.sigmoid(self.hidden(x))
        x = torch.sigmoid(self.output(x))
        return x

model = XORModel()

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(1000):
    outputs = model(inputs)
    loss = criterion(outputs.squeeze(), labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

#Проверка работы модели на новых данных
#Результат должен быть приближенным к [0, 1, 1, 0]
test_inputs = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
predictions = model(test_inputs)
print(predictions.squeeze().detach().numpy())