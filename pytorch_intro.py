import torch
from torch import nn
x = torch.tensor(3.0 , requires_grad=True)
y = x**2

y.backward()

print(f"Value of x: {x.item()}")
print(f"Value of y: {y.item()}")
print(f"Derivative (dy/dx) at x=3: {x.grad}")

neural_layer = nn.Linear(in_features=3 , out_features=1)
print("Initial Weights (W) :" , neural_layer.weight)
print("Initial Bias (B):" , neural_layer.bias)
print("-"*50)

sample_input = torch.tensor([1.0 , 2.0 , 3.0])
output = neural_layer(sample_input)

print(f"Input: {sample_input.tolist()}")
print(f"Output of Neural Network Layer: {output.item():.2f}")