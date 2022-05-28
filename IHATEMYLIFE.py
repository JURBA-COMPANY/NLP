import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim
from gisi import FFUFUDUFUFUF
from torch.utils.data import DataLoader


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        g = FFUFUDUFUFUF()
        love = DataLoader(g, batch_size=7, shuffle=True)
        self.fc1 = nn.Transformer(love, 100)
        self.fc2 = nn.Linear(100, 50)
        self.fc3 = nn.Linear(50, 2)

    def forward(self, x):
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = self.fc3
        return f.log_softmax(x)


net = Net()
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
losser = nn.NLLLoss()
print(losser)
