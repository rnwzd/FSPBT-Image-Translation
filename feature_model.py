import torch
import torch.nn as nn
from torch.autograd import Variable

from torchvision import models


class FeaturesNet(nn.Module):
    def __init__(self, feature_layers=[0, 3, 5], use_normalization=False):
        super().__init__()
        # model = models.vgg19(pretrained=True)
        model = models.squeezenet1_1(pretrained=True)
        model.float()
        model.eval()

        self.model = model
        self.feature_layers = feature_layers

        self.mean = torch.FloatTensor([0.485, 0.456, 0.406])
        self.mean_tensor = None

        self.std = torch.FloatTensor([0.229, 0.224, 0.225])
        self.std_tensor = None

        self.use_normalization = use_normalization

        for param in self.parameters():
            param.requires_grad = False

    def normalize(self, x):
        if not self.use_normalization:
            return x

        if self.mean_tensor is None:
            self.mean_tensor = Variable(
                self.mean.view(1, 3, 1, 1).expand(x.shape),
                requires_grad=False)
            self.std_tensor = Variable(
                self.std.view(1, 3, 1, 1).expand(x.shape), requires_grad=False)

        x = (x + 1) / 2
        return (x - self.mean_tensor) / self.std_tensor

    def run(self, x):
        features = []

        h = x

        for f in range(max(self.feature_layers) + 1):
            h = self.model.features[f](h)
            if f in self.feature_layers:
                not_normed_features = h.clone().view(h.size(0), -1)
                features.append(not_normed_features)

        return torch.cat(features, dim=1)

    def forward(self, x):
        h = self.normalize(x)
        return self.run(h)
