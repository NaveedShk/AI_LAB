import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Sample student data (you can replace this with real data)
data = {
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'GPA': [3.4, 3.8, 2.9, 3.0, 3.7, 3.5, 3.2, 3.6, 2.5, 3.1],
    'study_hours': [12, 8, 15, 10, 14, 7, 11, 13, 6, 9],
    'attendance_rate': [85, 90, 80, 88, 92, 85, 87, 89, 76, 84]
}

# Create DataFrame
df = pd.DataFrame(data)

# Selecting relevant features
features = df[['GPA', 'study_hours', 'attendance_rate']]

# Scaling the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Elbow Method to determine optimal K (clusters)
inertia = []
silhouette_scores = []

# Try different values of K (from 2 to 6)
for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_features, kmeans.labels_))

# Plot the Elbow Method (inertia vs K)
plt.figure(figsize=(8, 5))
plt.plot(range(2, 7), inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.show()

# Elbow Method visualization ends here. Now let's pick the optimal K.

# Based on the elbow plot, let's assume K=3 is the optimal number of clusters.
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_features)

# Show final dataset with cluster labels
print("Final Dataset with Clusters:")
print(df[['student_id', 'GPA', 'study_hours', 'attendance_rate', 'cluster']])

# Visualization: Scatter plot of study_hours vs GPA with cluster labels
plt.figure(figsize=(8, 6))
plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'], cmap='viridis')
plt.title('K-Means Clustering: Students Based on GPA and Study Hours')
plt.xlabel('Study Hours')
plt.ylabel('GPA')
plt.colorbar(label='Cluster')
plt.show()
