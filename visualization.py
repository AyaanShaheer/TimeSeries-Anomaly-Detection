import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

# File with anomalies
input_file = "anomaly_detected_data.csv"

# Load data
df = pd.read_csv(input_file)

# Filter anomalies
anomalies = df[df['anomaly'] == True]

# Set up plotting style
sns.set(style="whitegrid")

# Plot: Time Series with Anomalies
def plot_time_series_with_anomalies(df, anomalies, feature, title):
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df[feature], label=f'{feature} (normal)', alpha=0.8)
    plt.scatter(anomalies['timestamp'], anomalies[feature], color='red', label='Anomaly', s=10)
    
    # Formatting X-axis for better readability
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(MaxNLocator(10))  # Limit to 10 labels
    
    plt.title(title)
    plt.xlabel('Timestamp')
    plt.ylabel(feature)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example: Plot CPU Temperature with anomalies
plot_time_series_with_anomalies(df, anomalies, 'cpu_temperature', 'CPU Temperature Over Time')

# Plot: Summary of Anomalies
def plot_anomaly_summary(df, numeric_features):
    # Count anomalies per feature
    anomaly_counts = anomalies[numeric_features].count()

    # Check if any anomalies are detected in features
    if anomaly_counts.sum() == 0:
        print("No anomalies detected.")
    else:
        anomaly_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
        plt.title('Anomaly Counts per Feature')
        plt.ylabel('Count')
        plt.xlabel('Feature')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# List of numeric features to summarize anomalies
numeric_features = ['cpu_temperature', 'cpu_usage', 'cpu_load', 'memory_usage', 'battery_level', 'cpu_power']

# Call the anomaly count plot
plot_anomaly_summary(df, numeric_features)

# Check the anomaly detection count (debugging step)
print("Anomaly detection count per feature:")
print(df['anomaly'].value_counts())
