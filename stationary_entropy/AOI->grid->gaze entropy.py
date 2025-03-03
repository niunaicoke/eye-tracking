import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy


path = "/Users/scottliu/Desktop/2+3_aoi/gaze/easy_gaze.csv"
df = pd.read_csv(path)
df = df.dropna(subset=['fixation id'])
df = df[df['gaze detected on surface'] == True]
x = df["gaze position on surface x [normalized]"]
y = df["gaze position on surface y [normalized]"]


grid_size = 50


def get_grid_index(value, grid_size):
    return min(int(value * grid_size), grid_size - 1)


# Define AOIs ( x_min, x_max, y_min, y_max)
aois = {
    "Guide": (0.0, 0.29, 0.0, 1.0),
    "OR": (0.29, 0.77, 0.0, 1.0),
    "Progbars": (0.77, 1.0, 0.0, 1.0)
}

gaze_entropies = {}

for aoi_name, (x_min, x_max, y_min, y_max) in aois.items():
    # Filter data within AOI
    aoi_df = df.loc[(x >= x_min) & (x <= x_max) & (y >= y_min) & (y <= y_max)].copy()

    #  grid indices
    aoi_df.loc[:, 'x_idx'] = aoi_df['gaze position on surface x [normalized]'].apply(
        lambda v: get_grid_index((v - x_min) / (x_max - x_min), grid_size))
    aoi_df.loc[:, 'y_idx'] = aoi_df['gaze position on surface y [normalized]'].apply(
        lambda v: get_grid_index((v - y_min) / (y_max - y_min), grid_size))

    # Count fixations in each grid
    heatmap, _, _ = np.histogram2d(aoi_df['x_idx'], aoi_df['y_idx'], bins=grid_size,
                                   range=[[0, grid_size], [0, grid_size]])

    # Flatten the heatmap and compute probability distribution
    prob_dist = heatmap.flatten() / np.sum(heatmap)

    # check zero probability
    prob_dist = prob_dist[prob_dist > 0]

    # Compute gaze entropy
    gaze_entropy = entropy(prob_dist, base=2)
    gaze_entropies[aoi_name] = gaze_entropy

    plt.figure(figsize=(8, 6))
    plt.imshow(heatmap.T, origin='lower', cmap='hot', interpolation='nearest')
    plt.colorbar(label='Gaze Count')
    plt.xlabel('X Grid Index')
    plt.ylabel('Y Grid Index')
    plt.title(f'Gaze Heatmap - {aoi_name}')
    plt.show()

# Compute max entropy for each AOI
max_entropy = np.log2(grid_size * grid_size)
print("Max Possible Gaze Entropy:", max_entropy)

# Print entropy values
for aoi_name, entropy_value in gaze_entropies.items():
    print(f"easy_{aoi_name} Gaze Entropy: {entropy_value}")



# AOI bounding box
plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=1, alpha=0.5, label="Gaze Points")
for aoi_name, (x_min, x_max, y_min, y_max) in aois.items():
    plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], label=aoi_name)
plt.xlabel("Gaze Position X [Normalized]")
plt.ylabel("Gaze Position Y [Normalized]")
plt.title("AOI Bounding Boxes")
plt.legend()
plt.show()


print(df[["gaze position on surface x [normalized]", "gaze position on surface y [normalized]"]].describe())

