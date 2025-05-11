import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# Sample vehicle data
data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

# Create DataFrame
df = pd.DataFrame(data)

# Separate categorical and numerical columns
categorical_cols = ['vehicle_type']
numerical_cols = ['mileage', 'fuel_efficiency', 'maintenance_cost']

# Function to perform clustering
def perform_clustering(df, scale=False, n_clusters=3):
    # Separate categorical and numerical columns
    X = df[numerical_cols]
    y = df[categorical_cols]

    if scale:
        # Scaling numerical features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = X  # No scaling

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)

    # Add cluster labels to DataFrame
    df['cluster'] = clusters
    
    return df, kmeans

# Perform clustering without scaling
df_no_scaling, kmeans_no_scaling = perform_clustering(df, scale=False)

# Perform clustering with scaling
df_scaled, kmeans_scaled = perform_clustering(df, scale=True)

# Display results
print("Clustering Results Without Scaling:")
print(df_no_scaling[['vehicle_serial_no', 'cluster']])

print("\nClustering Results With Scaling:")
print(df_scaled[['vehicle_serial_no', 'cluster']])

# Evaluate clustering quality using silhouette score (higher is better)
silhouette_no_scaling = silhouette_score(df[numerical_cols], kmeans_no_scaling.labels_)
silhouette_scaled = silhouette_score(df[numerical_cols], kmeans_scaled.labels_)

print(f"\nSilhouette Score Without Scaling: {silhouette_no_scaling:.2f}")
print(f"Silhouette Score With Scaling: {silhouette_scaled:.2f}")

# Analyze cluster centroids for both cases
print("\nCluster Centroids Without Scaling:")
print(kmeans_no_scaling.cluster_centers_)

print("\nCluster Centroids With Scaling:")
print(kmeans_scaled.cluster_centers_)
