import torch
import torch.nn as nn
import matplotlib.pyplot as plt

image = torch.zeros(100 , 100)
image[30:70 ,30:70] = 1.0
image_tensor = image.unsqueeze(0).unsqueeze(0)

sobel_filter = torch.tensor([
    [-1.0, 0.0, 1.0],
    [-2.0, 0.0, 2.0],
    [-1.0, 0.0, 1.0]
])

filter_weight = sobel_filter.unsqueeze(0).unsqueeze(0)

conv_layer = nn.Conv2d(in_channels=1 ,out_channels=1 , kernel_size=3 , bias=False)
with torch.no_grad():
    conv_layer.weight = nn.Parameter(filter_weight)

output_tensor = conv_layer(image_tensor)
output_image = output_tensor.squeeze().detach().numpy()

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image.numpy(), cmap='gray')
axes[0].set_title("Original Image (Square)")
axes[0].axis('off')

axes[1].imshow(output_image, cmap='gray')
axes[1].set_title("Edge Detected (Sobel Filter)")
axes[1].axis('off')

plt.savefig("edge_detection_result.png")
print("✅")
