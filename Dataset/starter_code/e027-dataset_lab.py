import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import numpy as np

class DefectDataset(Dataset):
    """
    Task 1: Build the Custom Dataset Class
    """
    def __init__(self, image_paths, labels, transform=None):
        # TODO: Store the arguments as instance variables
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform


    def __len__(self):
        # TODO: Return the total number of samples
        return len(self.image_paths)

    def __getitem__(self, idx):
        # 1. Get the path and label at the specified index
        path = self.image_paths[idx] # TODO
        label = self.labels[idx] # TODO
        
        # Simulating loading a PIL image from disk (Random colored square)
        # In reality this would be: image = Image.open(path).convert('RGB')
        raw_image = Image.fromarray(np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8))
        
        # 2. Apply the transform if one was provided
        # TODO
        if self.transform:
            raw_image = self.transform(raw_image)
            
        # 3. Return the transformed image and the label as a tensor (float32)
        # TODO
        return raw_image, label


def build_pipeline():
    """
    Task 2: Configure Transforms and the DataLoader
    """
    print("--- Building Data Pipeline ---")
    
    # Mock data references
    mock_paths = [f"part_{i}.jpg" for i in range(100)] # 100 images
    mock_labels = [np.random.randint(0, 2) for _ in range(100)] # 0 or 1
    
    # 1. Define the TorchVision Transforms
    # TODO: Compose Resize(128, 128), ToTensor(), and Normalize(mean, std)
    data_transform = transforms.Compose([transforms.Resize((128, 128)),
                                         transforms.ToTensor(),
                                         transforms.Normalize(mean=[0.5, 0.5, 0.5],
                                                              std=[0.5, 0.5, 0.5])])
    
    # 2. Instantiate the Custom Dataset
    # TODO
    dataset = DefectDataset(mock_paths, mock_labels, transform=data_transform)
    print(f"Dataset securely loaded with {len(dataset)} items.") # Should print 100
    
    # 3. Instantiate the DataLoader
    # TODO: Batch size of 16, shuffle enabled
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)
    
    print("\n--- Iterating Pipeline ---")
    # 4. Iterate over the DataLoader for one "epoch"
    # TODO: Loop through dataloader enum and print the shape of the images
    # Example Expected Output: "Batch 1 - Images Shape: torch.Size([16, 3, 128, 128])"
    print("Batch 1 - Images Shape: torch.Size([", end="")
    for raw_image, label in dataloader:
        print(f"{raw_image.size()}", end="")
        break
    print("])")
    

if __name__ == "__main__":
    build_pipeline()
