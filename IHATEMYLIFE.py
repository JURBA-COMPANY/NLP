import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim
from gisi import FFUFUDUFUFUF
from torch.utils.data import DataLoader
from ignite.engine import Engine, _prepare_batch, Events


class Net(nn.Module):
    def __init__(self, love):
        super(Net, self).__init__()
        self.fc1 = nn.Embedding(love, 112)
        self.fc2 = nn.Linear(112, 60)
        self.fc3 = nn.Linear(60, 10)

    def forward(self, x):
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = self.fc3
        return f.log_softmax(x)


g = FFUFUDUFUFUF()
love = DataLoader(g, batch_size=7, shuffle=True, num_workers=1)
print(type(love))
net = Net(love)
lossfunc = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)
print('Done!')
log_interval = 50


def process_function(engine, batch, love):
    love.train()
    optimizer.zero_grad()
    x, y = _prepare_batch(batch)
    y_pred = love(x)
    loss = lossfunc(y_pred, y)
    loss.backward()
    optimizer.step()
    return loss.item()


trainer = Engine(process_function)
trainer.run(love, max_epochs=10)
