
from pathlib import Path

from data import read_image_tensor, write_image_tensor, ImageDataset

from torch.utils.data import DataLoader
import torch
from tqdm import tqdm


from train import data_path, model_save_path

# you can overwrite data_path here
output_dir = data_path/'output'
input_dir = data_path/'input'

# Change these depending on your hardware, has to match training settings
device = 'cuda' 
dtype = torch.float16 

generator = torch.load(model_save_path/"generator.pt")
generator.eval()
generator.to(device, dtype)


# TODO batch size, async dataloader
file_paths = [file for file in input_dir.iterdir()]


params = {'batch_size': 1,
          'num_workers': 8,
          'pin_memory': True}

dataset = ImageDataset(file_paths,)
loader = DataLoader(dataset, **params)

# TODO multiprocess and asynchronous writing of files

with torch.no_grad():
    for inputs, names in tqdm(loader):
        inputs = inputs.to(device, dtype)
        outputs = generator(inputs)
        del inputs
        for j in range(len(outputs)):
            write_image_tensor(outputs[j], output_dir/names[j])
        del outputs
