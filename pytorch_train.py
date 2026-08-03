import torch
import torch.nn as nn
import torch.optim as optim

x = torch.tensor([[1.0] , [2.0] , [3.0] , [4.0]])
y = torch.tensor([[3.0] , [5.0],[7.0],[9.0]])

model = nn.Linear(1,1)
criterion = nn.MSELoss()

optimizer = optim.SGD(model.parameters() , lr=0.01)

print("=== Neural Network Training Begins ===")
for epoch in range(500):
    optimizer.zero_grad()
    predictions = model(x)
    loss = criterion(predictions , y)
    loss.backward()
    optimizer.step()

    if(epoch+1)%10 ==0:
        print(f"Epoch [{epoch+1}/500], Loss: {loss.item():.4f}")

print("\n === Training complete! ===")
print("Learned Weight (W):" , model.weight.item())
print("Learned Bias (B):" , model.bias.item())