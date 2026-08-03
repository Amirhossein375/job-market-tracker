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
print(f"Output of Neural Network Layer: {output.item():.4f}")

print("\n=== Section 3: Multi-Layer Neural Network ===")

multi_layer_model = nn.Sequential(nn.Linear(in_features=3 , out_features=5),nn.ReLU(),nn.Linear(in_features=5 , out_features=1))

multi_layer_output = multi_layer_model(sample_input)

print("Model Structure: \n", multi_layer_model)
print(f"\nInput: {sample_input.tolist()}")
print(f"Output of Multi-Layer Network: {multi_layer_output.item():.4f}")