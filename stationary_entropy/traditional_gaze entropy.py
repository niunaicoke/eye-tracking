import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy


# Define grid size
grid_size = 1080

x_grid_size = 1088
y_grid_size = 1080
def get_grid_index(value, grid_size):
    return min(int(value * grid_size), grid_size - 1)  # Ensure values are within bounds


"""easy"""
path = "/Users/scottliu/Desktop/1+2_aoi/gaze/easy_gaze.csv"
df = pd.read_csv(path)
df = df.dropna(subset=['fixation id'])
df = df[df['gaze detected on surface'] == True]
x = df["gaze position on surface x [normalized]"]
y = df["gaze position on surface y [normalized]"]



df['x_idx'] = x.apply(lambda v: get_grid_index(v, x_grid_size))
df['y_idx'] = y.apply(lambda v: get_grid_index(v, y_grid_size))
heatmap, _, _ = np.histogram2d(df['x_idx'], df['y_idx'], bins=(1088, 1080), range=[[0, x_grid_size], [0, y_grid_size]])
prob_dist = heatmap.flatten() / np.sum(heatmap)
prob_dist = prob_dist[prob_dist > 0]

# Compute gaze entropy
gaze_entropy = entropy(prob_dist, base=2)

# Compute max entropy
max_entropy = np.log2(x_grid_size * y_grid_size)

plt.figure(figsize=(8, 6))
plt.imshow(heatmap.T, origin='lower', cmap='hot', interpolation='nearest')
plt.colorbar(label='Gaze Count')
plt.xlabel('X Grid Index')
plt.ylabel('Y Grid Index')
plt.title('easy Gaze Heatmap')
plt.show()

print(f"Max Possible Gaze Entropy: {max_entropy:.4f}")
print(f"Easy Gaze Entropy: {gaze_entropy:.4f} ")
print(f"Easy normalized Gaze Entropy respect to max entropy: {gaze_entropy/max_entropy:.4f}")


"""medium"""
path = "/Users/scottliu/Desktop/1+2_aoi/gaze/medium_gaze.csv"
df = pd.read_csv(path)
df = df.dropna(subset=['fixation id'])
df = df[df['gaze detected on surface'] == True]
x = df["gaze position on surface x [normalized]"]
y = df["gaze position on surface y [normalized]"]

df['x_idx'] = x.apply(lambda v: get_grid_index(v, x_grid_size))
df['y_idx'] = y.apply(lambda v: get_grid_index(v, y_grid_size))
heatmap, _, _ = np.histogram2d(df['x_idx'], df['y_idx'], bins=(1088, 1080), range=[[0, x_grid_size], [0, y_grid_size]])
prob_dist = heatmap.flatten() / np.sum(heatmap)
prob_dist = prob_dist[prob_dist > 0]

# Compute gaze entropy
gaze_entropy = entropy(prob_dist, base=2)



plt.figure(figsize=(8, 6))
plt.imshow(heatmap.T, origin='lower', cmap='hot', interpolation='nearest')
plt.colorbar(label='Gaze Count')
plt.xlabel('X Grid Index')
plt.ylabel('Y Grid Index')
plt.title('medium Gaze Heatmap')
plt.show()

print(f"medium Gaze Entropy: {gaze_entropy:.4f} ")
print(f"medium normalized Gaze Entropy respect to max entropy: {gaze_entropy/max_entropy:.4f}")



"""hard"""
path = "/Users/scottliu/Desktop/1+2_aoi/gaze/hard_gaze.csv"
df = pd.read_csv(path)
df = df.dropna(subset=['fixation id'])
df = df[df['gaze detected on surface'] == True]
x = df["gaze position on surface x [normalized]"]
y = df["gaze position on surface y [normalized]"]

df['x_idx'] = x.apply(lambda v: get_grid_index(v, x_grid_size))
df['y_idx'] = y.apply(lambda v: get_grid_index(v, y_grid_size))
heatmap, _, _ = np.histogram2d(df['x_idx'], df['y_idx'], bins=(1088, 1080), range=[[0, x_grid_size], [0, y_grid_size]])
prob_dist = heatmap.flatten() / np.sum(heatmap)
prob_dist = prob_dist[prob_dist > 0]

# Compute gaze entropy
gaze_entropy = entropy(prob_dist, base=2)

plt.figure(figsize=(8, 6))
plt.imshow(heatmap.T, origin='lower', cmap='hot', interpolation='nearest')
plt.colorbar(label='Gaze Count')
plt.xlabel('X Grid Index')
plt.ylabel('Y Grid Index')
plt.title('hard Gaze Heatmap')
plt.show()
print(f"hard Gaze Entropy: {gaze_entropy:.4f} ")
print(f"hard normalized Gaze Entropy respect to max entropy: {gaze_entropy/max_entropy:.4f}")


print(df[["gaze position on surface x [normalized]", "gaze position on surface y [normalized]"]].describe())