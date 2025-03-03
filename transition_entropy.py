import pandas as pd
import numpy as np
from collections import Counter

aoi_list = ["Guide", "OR ", "Progbars", "Combined total screen"]

"""easy"""
file_path = "/Users/scottliu/Desktop/2+3_aoi/fixations/easy_aoi.csv"
df = pd.read_csv(file_path)
aoi_sequence = df["aoi name"].tolist()
transitions = list(zip(aoi_sequence[:-1], aoi_sequence[1:]))

# Count transition occurrences
transition_counts = Counter(transitions)
transition_matrix = pd.DataFrame(0, index=aoi_list, columns=aoi_list)

# transition matrix with counts
for (src, dst), count in transition_counts.items():
    if src in aoi_list and dst in aoi_list:
        transition_matrix.at[src, dst] = count

# count to probabiltiy
transition_matrix_prob = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)

# Replace na transitions with 0
transition_matrix_prob = transition_matrix_prob.fillna(0)

# Compute gaze transition entropy
p_values = transition_matrix_prob.values.flatten()
p_values = p_values[p_values > 0]  # Avoid log(0)
gaze_transition_entropy = -np.sum(p_values * np.log2(p_values))

print("easy Transition Matrix (Probabilities) (left prior state, top destination state):")
print(transition_matrix_prob)

max_entropy = np.log2(len(aoi_list)*len(aoi_list))  # Maximum entropy
print(f"Maximum Possible Entropy: {max_entropy:.4f} bits")


print(f"\neasy Gaze Transition Entropy: {gaze_transition_entropy:.4f} bits")
print(f"easy Normalized Entropy with respect to Max entropy: {gaze_transition_entropy/max_entropy:.4f} bits")





"""medium"""
file_path = "/Users/scottliu/Desktop/2+3_aoi/fixations/medium_aoi.csv"
df = pd.read_csv(file_path)
aoi_sequence = df["aoi name"].tolist()
transitions = list(zip(aoi_sequence[:-1], aoi_sequence[1:]))

# Count transition occurrences
transition_counts = Counter(transitions)
transition_matrix = pd.DataFrame(0, index=aoi_list, columns=aoi_list)

# transition matrix with counts
for (src, dst), count in transition_counts.items():
    if src in aoi_list and dst in aoi_list:
        transition_matrix.at[src, dst] = count

# count to probabiltiy
transition_matrix_prob = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)

# Replace na transitions with 0
transition_matrix_prob = transition_matrix_prob.fillna(0)

# Compute gaze transition entropy
p_values = transition_matrix_prob.values.flatten()
p_values = p_values[p_values > 0]  # Avoid log(0)
gaze_transition_entropy = -np.sum(p_values * np.log2(p_values))

print("\nmedium Transition Matrix (Probabilities) (left prior state, top destination state):")
print(transition_matrix_prob)



print(f"\nmeiudm Gaze Transition Entropy: {gaze_transition_entropy:.4f} bits")
print(f"meiudm normalized entropy with respect to Max entropy: {gaze_transition_entropy/max_entropy:.4f} bits")






"""hard"""
file_path = "/Users/scottliu/Desktop/2+3_aoi/fixations/hard_aoi.csv"
df = pd.read_csv(file_path)
aoi_sequence = df["aoi name"].tolist()
transitions = list(zip(aoi_sequence[:-1], aoi_sequence[1:]))

# Count transition occurrences
transition_counts = Counter(transitions)
transition_matrix = pd.DataFrame(0, index=aoi_list, columns=aoi_list)

# transition matrix with counts
for (src, dst), count in transition_counts.items():
    if src in aoi_list and dst in aoi_list:
        transition_matrix.at[src, dst] = count

# count to probabiltiy
transition_matrix_prob = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)

# Replace na transitions with 0
transition_matrix_prob = transition_matrix_prob.fillna(0)

# Compute gaze transition entropy
p_values = transition_matrix_prob.values.flatten()
p_values = p_values[p_values > 0]  # Avoid log(0)
gaze_transition_entropy = -np.sum(p_values * np.log2(p_values))

print("\nhard Transition Matrix (Probabilities) (left prior state, top destination state):")
print(transition_matrix_prob)



print(f"\nhard Gaze Transition Entropy: {gaze_transition_entropy:.4f} bits")
print(f"hard normalized entropy with respect to Max entropy: {gaze_transition_entropy/max_entropy:.4f} bits")