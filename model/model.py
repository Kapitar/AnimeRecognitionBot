"""Model forward"""
import os
import torch
import torch.nn as nn
import pandas as pd
from torchvision.models import resnet18

from utils.constants import DEVICE, PATH_TO_MODEL, PATH_TO_TABLE, PATH_TO_NAMENUMS


class Model(nn.Module):
    def __init__(self, fc):
        super(Model, self).__init__()
        self.pool1 = nn.AvgPool2d(kernel_size=(2, 2))
        self.sub_model = fc
        self.res = nn.Softmax()

    def forward(self, input_data):
        """Push data"""
        y = self.pool1(input_data)
        y = y.double()
        y = y.to(DEVICE)
        return self.sub_model.forward(y).to(DEVICE)


resnet = resnet18(pretrained=True)
resnet.fc = nn.Linear(512, 185)
resnet = resnet.to(DEVICE)

model = Model(resnet)
state_dict = torch.load(os.path.abspath(PATH_TO_MODEL), map_location=torch.device('cpu'))
model.load_state_dict(state_dict)
model.double()
model.eval()


name_nums = pd.read_csv(PATH_TO_NAMENUMS)
girls_numbers = name_nums['number']
girls_names = name_nums['name']
number_to_name = dict(zip(girls_numbers, girls_names))
name_to_number = dict(zip(girls_names, girls_numbers))

merged = pd.read_csv(PATH_TO_TABLE)
lst = merged.index
names = merged['name']
filepath = merged['filename']
id_to_name = dict(zip(lst, names))
name_to_id = dict(zip(names, lst))
id_to_path = dict(zip(lst, filepath))

print(name_to_id)
print(id_to_path)


def get_anime(tensor: torch.tensor) -> list:
    """Returns most compactable character"""
    chance = model.forward(tensor)
    chance = torch.squeeze(chance, 0)
    chance = nn.Softmax()(chance)
    top5 = torch.topk(chance, 5)
    zipped_top5 = zip(top5.values, top5.indices)
    new_zipped_top5 = []
    for i, j in zipped_top5:
        name = number_to_name[int(j)]
        new_zipped_top5.append((round(float(i) * 100, 2), name, id_to_path[name_to_id[f"['{name}']"]]))

    return new_zipped_top5
