import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Load the data
path = "/Users/scottliu/Desktop/1+2_aoi/gaze/easy_gaze.csv"
df = pd.read_csv(path)
df = df.dropna(subset=['fixation id'])
df = df[df['gaze detected on surface'] == True]
x = df["gaze position on surface x [normalized]"]
y = df["gaze position on surface y [normalized]"]

# Load the image
image_path = "/Users/scottliu/Desktop/image.png"
image = Image.open(image_path)
image_width, image_height = image.size

# Normalize x and y to image dimensions
x_pixels = x * image_width +100
y_pixels = y * image_height

# # Clip out-of-bounds points (optional, if needed)
# x_pixels = np.clip(x_pixels, 0, image_width)
# y_pixels = np.clip(y_pixels, 0, image_height)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Display the image
ax.imshow(image, alpha=1.0, extent=[0, image_width, 0, image_height])

# Create the KDE plot (heatmap) with Seaborn
sns.kdeplot(
    x=x_pixels,
    y=y_pixels,
    cmap=plt.cm.jet,  # Use the 'jet' colormap
    fill=True,        # Fill the contours
    alpha=0.5,        # Set transparency
    levels=100,       # Number of contour levels
    ax=ax             # Plot on the same axis as the image
)

# # Set axis limits to match the image dimensions
# ax.set_xlim(0, image_width)
# ax.set_ylim(0, image_height)

# Remove axis labels
ax.axis('off')

# Save or show the plot
plt.savefig("/Users/scottliu/Desktop/kde_heatmap_overlay_fixed.png", bbox_inches='tight', pad_inches=0)
plt.show()