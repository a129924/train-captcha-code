from torch import Tensor, nn
from typing_extensions import override


class CNN(nn.Module):
    @override
    def __init__(self, num_class=36, num_char=4) -> None:
        """
        `torch.Size([3, 100, 120])`
        """
        super().__init__()

        self.conv = nn.Sequential(
            # batch*3*100*120
            nn.Conv2d(3, 16, kernel_size=3, padding=(1, 1)),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            # batch*16*50*60
            nn.Conv2d(16, 64, kernel_size=3, padding=(1, 1)),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            # batch*64*25*30
            nn.Conv2d(64, 256, kernel_size=3, padding=(1, 1)),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            # batch*256*12*15
            nn.Conv2d(256, 512, kernel_size=3, padding=(1, 1)),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(512),
            nn.ReLU(),
            # batch*512*6*7
        )
        self.fc = nn.Linear(512 * 6 * 7, num_class * num_char)

        self.num_char = num_char
        self.num_class = num_class

    def forward(self, x: Tensor) -> Tensor:
        x = self.conv(x)
        x = x.view(-1, 512 * 6 * 7)
        x = self.fc(x)
        x = x.view(-1, self.num_char, self.num_class)

        return x
