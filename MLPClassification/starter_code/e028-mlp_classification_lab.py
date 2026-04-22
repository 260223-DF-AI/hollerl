import torch
import torch.nn as nn
import torch.optim as optim

# Simulated IoT Sensor Dataset (4 categories)
X_train = torch.randn(200, 20) # 200 samples, 20 features
y_train = torch.randint(0, 4, (200,)) # 4 classes
X_val = torch.randn(50, 20)
y_val = torch.randint(0, 4, (50,))

class SensorMLP(nn.Module):
    """
    Task 1: Build the MLP Architecture
    """
    def __init__(self):
        super(SensorMLP, self).__init__()
        # TODO: Define Layer 1 (20 -> 64)
        self.layer1 = nn.Linear(20, 64)
        
        # TODO: Define ReLU and Dropout (p=0.3)
        self.ReLu = nn.ReLU()
        self.Dropout = nn.Dropout(p=0.3)
        
        # TODO: Define Layer 2 (64 -> 32)
        self.layer2 = nn.Linear(64, 32)
        
        # TODO: Define output Layer 3 (32 -> 4 classes)
        self.layer3 = nn.Linear(32, 4)

    def forward(self, x):
        # TODO: Route the data: Linear -> ReLU -> Dropout -> Linear -> ReLU -> Dropout -> Output
        x = self.layer1(x)
        x = self.ReLu(x)
        x = self.Dropout(x)
        x = self.layer2(x)
        x = self.ReLu(x)
        x = self.Dropout(x)
        x = self.layer3(x)
        return x


def train_and_validate():
    """
    Task 2: Build the Full Training/Validation Loop
    """
    model = SensorMLP()
    
    # TODO: Define CrossEntropyLoss and Adam optimizer (lr=0.01)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    epochs = 50
    best_val_loss = float('inf')
    
    print("--- Starting Hybrid Sensor Training ---")
    
    for epoch in range(epochs):
        
        # =======================
        #      TRAINING PHASE
        # =======================
        # TODO: Set model to training mode
        model.train()
        optimizer.zero_grad()
        
        # TODO: Execute forward pass, loss computation, and backprop
        outputs = model(X_train)
        train_loss = criterion(outputs, y_train)
        train_loss.backward()
        optimizer.step()

        
        # =======================
        #     VALIDATION PHASE
        # =======================
        # TODO: Set model to evaluation mode
        model.eval()
        
        # TODO: Disable autograd (torch.no_grad())
        val_loss = 0.0
        
        # TODO: Execute forward pass and calculate validation loss
        with torch.no_grad():  # Disable autograd for validation
            val_outputs = model(X_val)  # Forward pass
            val_loss = criterion(val_outputs, y_val)
        
        print(f"Epoch {epoch+1:02d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f}")
        
        # =======================
        #     CHECKPOINTING
        # =======================
        # TODO: If val_loss is better than best_val_loss, save the state_dict
        if val_loss.item() < best_val_loss:  # Save best model
            best_val_loss = val_loss.item()
            best_model_state = model.state_dict()
            torch.save(best_model_state, "best_sensor_model.pth")  # Save to file
            print(f"New best model saved with Val Loss: {best_val_loss:.4f}")

    print("\n--- Training Complete ---")

if __name__ == "__main__":
    train_and_validate()
