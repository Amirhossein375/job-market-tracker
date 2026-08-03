import torch
import torch.nn as nn
import torch.optim as optim

class_0 = torch.randn(50 , 2)+1.0
class_1 = torch.randn(50 , 2)+5.0
X = torch.cat((class_0 , class_1) , dim=0)
y = torch.cat((torch.zeros(50 , 1),torch.ones(50 , 1)),dim=0 )

model = nn.Sequential(
    nn.Linear(2,5),
    nn.ReLU(),
    nn.Linear(5,1),
    nn.Sigmoid()
)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters() , lr=0.01)
print("=== Neural Network Training Begins ===")

for epoch in range(100):
    optimizer.zero_grad()
    predictions = model(X)
    loss = criterion(predictions , y)
    loss.backward()
    optimizer.step()
 
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/100], Loss: {loss.item():.4f}")

test_point_0 = torch.tensor([[1.2 , 0.9]])
test_point_1 = torch.tensor([[4.8 , 5.2]])

with torch.no_grad():
    pred_0 = model(test_point_0).item()
    pred_1 = model(test_point_1).item()

print("=== Test results on new points === \n")
print(f"Point [1.2, 0.9] -> Prob of Class 1: {pred_0:.4f}(Predicted Class: {0 if pred_0 < 0.5 else 1})")
print(f"Point [4.8, 5.2] -> Prob of Class 1: {pred_1:.4f}(Predicted Class: {0 if pred_1 < 0.5 else 1})")