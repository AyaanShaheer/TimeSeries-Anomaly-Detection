import pandas as pd
import numpy as np

# File paths
input_file = "synthetic_timeseries_data.csv"
output_file = "anomaly_detected_data.csv"

# Threshold for Z-score
z_threshold = 3

# Function to calculate Z-scores
def detect_anomalies(data_chunk):
    # Identify numeric columns
    numeric_columns = data_chunk.select_dtypes(include=[np.number]).columns
    
    # Calculate Z-scores
    z_scores = (data_chunk[numeric_columns] - data_chunk[numeric_columns].mean()) / data_chunk[numeric_columns].std()
    
    # Flag rows with any Z-score > threshold as anomalies
    data_chunk['anomaly'] = (z_scores.abs() > z_threshold).any(axis=1)
    return data_chunk

# Read the large file in chunks and process
chunk_size = 100000
chunks = pd.read_csv(input_file, chunksize=chunk_size)
processed_chunks = []

for chunk in chunks:
    processed_chunk = detect_anomalies(chunk)
    processed_chunks.append(processed_chunk)

    # Save the processed chunk to output file
    if not processed_chunks[0].index[0]:  # First chunk
        processed_chunk.to_csv(output_file, mode='w', index=False)
    else:
        processed_chunk.to_csv(output_file, mode='a', index=False, header=False)

print(f"Anomaly detection complete! Results saved to {output_file}")
