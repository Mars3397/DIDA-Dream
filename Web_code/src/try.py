import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open('gift1.PNG')

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((395, 1390), 375, 100, linewidth=1, edgecolor='r', facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)

plt.show()