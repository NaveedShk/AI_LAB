import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Importing the dataset
df = pd.read_csv(r'E:\4th semester\AI Lab\lab 10\customer_data.csv')

# Dropping the customer_id as it's not a feature we want to use for clustering
df = df.drop('customer_id', axis=1)

# Extracting all features for clustering except 'age'
X = df[['age', 'annual_income', 'spending_score']].values

# K-Means without scaling
wcss_list = []  # Initializing the list for WCSS (Within-cluster sum of squares)
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss_list.append(kmeans.inertia_)

# Plotting the Elbow Method graph for the non-scaled data
plt.plot(range(1, 11), wcss_list)
plt.title('Elbow Method for K-Means (Without Scaling)')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS')
plt.show()

# We will use K=5 based on the Elbow method from the previous code
kmeans_no_scale = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict_no_scale = kmeans_no_scale.fit_predict(X)

# Visualizing the clusters (without scaling)
plt.scatter(X[y_predict_no_scale == 0, 0], X[y_predict_no_scale == 0, 1], s=100, c='blue', label='Cluster 1')
plt.scatter(X[y_predict_no_scale == 1, 0], X[y_predict_no_scale == 1, 1], s=100, c='green', label='Cluster 2')
plt.scatter(X[y_predict_no_scale == 2, 0], X[y_predict_no_scale == 2, 1], s=100, c='red', label='Cluster 3')
plt.scatter(X[y_predict_no_scale == 3, 0], X[y_predict_no_scale == 3, 1], s=100, c='black', label='Cluster 4')
plt.scatter(X[y_predict_no_scale == 4, 0], X[y_predict_no_scale == 4, 1], s=100, c='purple', label='Cluster 5')

# Plotting the centroids
plt.scatter(kmeans_no_scale.cluster_centers_[:, 0], kmeans_no_scale.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Customers (Without Scaling)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

# Now we apply feature scaling (excluding the 'age' column)
scaler = StandardScaler()
df_scaled = df[['annual_income', 'spending_score']]  # Exclude 'age' column
X_scaled = np.hstack((df[['age']].values, scaler.fit_transform(df_scaled)))  # Recombine 'age' with scaled values

# K-Means with scaling
wcss_list_scaled = []  # Initializing the list for WCSS (Within-cluster sum of squares)
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss_list_scaled.append(kmeans.inertia_)

# Plotting the Elbow Method graph for the scaled data
plt.plot(range(1, 11), wcss_list_scaled)
plt.title('Elbow Method for K-Means (With Scaling)')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS')
plt.show()

# K-Means with scaling
kmeans_scaled = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict_scaled = kmeans_scaled.fit_predict(X_scaled)

# Visualizing the clusters (with scaling)
plt.scatter(X_scaled[y_predict_scaled == 0, 0], X_scaled[y_predict_scaled == 0, 1], s=100, c='blue', label='Cluster 1')
plt.scatter(X_scaled[y_predict_scaled == 1, 0], X_scaled[y_predict_scaled == 1, 1], s=100, c='green', label='Cluster 2')
plt.scatter(X_scaled[y_predict_scaled == 2, 0], X_scaled[y_predict_scaled == 2, 1], s=100, c='red', label='Cluster 3')
plt.scatter(X_scaled[y_predict_scaled == 3, 0], X_scaled[y_predict_scaled == 3, 1], s=100, c='black', label='Cluster 4')
plt.scatter(X_scaled[y_predict_scaled == 4, 0], X_scaled[y_predict_scaled == 4, 1], s=100, c='purple', label='Cluster 5')

# Plotting the centroids
plt.scatter(kmeans_scaled.cluster_centers_[:, 0], kmeans_scaled.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Customers (With Scaling)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

# Displaying the final dataset with cluster labels
df['cluster_no_scale'] = y_predict_no_scale
df['cluster_scaled'] = y_predict_scaled
print(df.head())
