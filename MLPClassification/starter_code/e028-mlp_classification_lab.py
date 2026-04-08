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
        self.fcl1 = nn.Linear(20, 64)
        # TODO: Define ReLU and Dropout (p=0.3)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.3)
        # TODO: Define Layer 2 (64 -> 32)
        self.fcl2 = nn.Linear(64, 32)
        # TODO: Define output Layer 3 (32 -> 4 classes)
        self.output = nn.Linear(32, 4)

    def forward(self, x):
        # TODO: Route the data: Linear -> ReLU -> Dropout -> Linear -> ReLU -> Dropout -> Output
        x = self.relu(self.fcl1(x))
        x = self.dropout(x)
        x = self.output(self.fcl2(x))
        return x


def train_and_validate():
    """
    Task 2: Build the Full Training/Validation Loop
    """
    model = SensorMLP()
    
    # TODO: Define CrossEntropyLoss and Adam optimizer (lr=0.01)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    epochs = 100
    best_val_loss = float('inf')
    
    print("--- Starting Hybrid Sensor Training ---")
    
    for epoch in range(epochs):
        
        # =======================
        #      TRAINING PHASE
        # =======================
        # TODO: Set model to training mode
        model.train()
        # TODO: Execute forward pass, loss computation, and backprop
        x, y = X_train.to(device), y_train.to(device)

        optimizer.zero_grad()
        pred = model(x)
        loss = criterion(pred, y)        
        loss.backward()
        optimizer.step()

        train_loss = loss.item() # Replace with actual loss

        
        # =======================
        #     VALIDATION PHASE
        # =======================
        # TODO: Set model to evaluation mode
        model.eval()
        # TODO: Disable autograd (torch.no_grad())
        with torch.no_grad(): # Use 'with' statement
            x_v, y_v = X_val.to(device), y_val.to(device)
            val_pred = model(x_v)
            val_loss = criterion(val_pred, y_v).item()
        
        # TODO: Execute forward pass and calculate validation loss
        
        print(f"Epoch {epoch+1:02d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f}")
        
        # =======================
        #     CHECKPOINTING
        # =======================
        # TODO: If val_loss is better than best_val_loss, save the state_dict
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), "best_model.pth")

    print("\n--- Training Complete ---")

if __name__ == "__main__":
    train_and_validate()
