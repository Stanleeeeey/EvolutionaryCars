import torch.nn as nn
import torch


class Network(nn.Module):
    def __init__(self, input_dim, hidden1, hidden2, output_dim):
        super(Network, self).__init__()
        self.layers = nn.Sequential(

            nn.Linear(input_dim, hidden1),
            nn.Tanh(),

            nn.Linear(hidden1, hidden2),
            nn.Tanh(),
            
            nn.Linear(hidden2, output_dim),
            nn.Tanh(),
        )

    def forward(self, x):
        return self.layers(x)