# TimeSeries-Anomaly-Detection
TimeSeries Anomaly Detection is a machine learning project focused on detecting anomalies in synthetic multivariate time series data. The project generates a large dataset (over 1 GB) of system metrics, applies a simple anomaly detection algorithm, and visualizes both the detected anomalies and their distribution across different features.

# TimeSeries Anomaly Detection

## 🚀 Overview
**TimeSeries Anomaly Detection** is a project that demonstrates the generation, analysis, and visualization of anomalies in synthetic multivariate time series data. The workflow involves:
1. Generating synthetic time series data of system metrics (e.g., CPU temperature, memory usage).
2. Detecting anomalies using a basic unsupervised anomaly detection algorithm.
3. Visualizing the results through time-series plots and summary statistics.

This project can serve as a foundation for developing and testing advanced anomaly detection algorithms or for understanding data preprocessing, anomaly detection, and visualization techniques.

---


---

## 📋 Features
- **Synthetic Data Generation**: Creates a large (1+ GB) dataset of system metrics.
- **Anomaly Detection**: Uses the Isolation Forest algorithm to identify anomalies in multivariate time series data.
- **Visualization**:
  - Time series plots highlighting anomalies.
  - Bar charts summarizing anomaly counts across features.

---

## ⚙️ Installation
### Prerequisites:
- Python 3.7 or above
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

### Install Required Libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

🛠️ Usage
Step 1: Generate Synthetic Data
Run the generate_data.py script to create the synthetic multivariate time series dataset:
```
python generate_data.py
```
Step 2: Apply Anomaly Detection
Run the anomaly_detection.py script to detect anomalies in the dataset:
```
python anomaly_detection.py
```

Step 3: Visualize the Results
Run the visualization.py script to generate visualizations for the detected anomalies:
```
python visualization.py
```
📊 Results
1. Time Series Visualization
Time-series data with anomalies highlighted:

2. Anomaly Counts per Feature
Bar chart summarizing the count of anomalies for each feature:

💡 Key Concepts
Multivariate Time Series Data: Represents multiple system metrics (e.g., CPU temperature, memory usage) over time.
Anomaly Detection: Identifies outliers or unusual patterns in data that deviate significantly from the norm.
Isolation Forest Algorithm: An unsupervised algorithm used to detect anomalies in high-dimensional datasets.

✨ Future Improvements
Implement advanced anomaly detection techniques (e.g., LSTM Autoencoders or Variational Autoencoders).
Add support for real-time anomaly detection.
Extend visualization to include heatmaps or correlation analysis

🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to open a PR or raise an issue.
