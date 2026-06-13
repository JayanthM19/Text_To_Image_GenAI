import torch
import torch.nn as nn


class Generator(nn.Module):

    def __init__(
        self,
        latent_dim=100,
        num_classes=10,
        img_size=28
    ):
        super().__init__()

        self.label_embedding = nn.Embedding(
            num_classes,
            num_classes
        )

        self.model = nn.Sequential(

            nn.Linear(
                latent_dim + num_classes,
                128
            ),

            nn.LeakyReLU(
                0.2,
                inplace=True
            ),

            nn.Linear(
                128,
                256
            ),

            nn.BatchNorm1d(256),

            nn.LeakyReLU(
                0.2,
                inplace=True
            ),

            nn.Linear(
                256,
                512
            ),

            nn.BatchNorm1d(512),

            nn.LeakyReLU(
                0.2,
                inplace=True
            ),

            nn.Linear(
                512,
                1024
            ),

            nn.BatchNorm1d(1024),

            nn.LeakyReLU(
                0.2,
                inplace=True
            ),

            nn.Linear(
                1024,
                img_size * img_size
            ),

            nn.Tanh()
        )

        self.img_size = img_size

    def forward(
        self,
        noise,
        labels
    ):

        label_embed = self.label_embedding(
            labels
        )

        generator_input = torch.cat(
            (
                noise,
                label_embed
            ),
            dim=1
        )

        img = self.model(
            generator_input
        )

        img = img.view(
            img.size(0),
            1,
            self.img_size,
            self.img_size
        )

        return img