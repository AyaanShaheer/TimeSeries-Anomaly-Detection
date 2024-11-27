import psutil
import pandas as pd
import datetime
import random
import time
import os
import wmi

# Settings for large data generation
duration_minutes = 4500  # ~75 hours
sampling_rate_hz = 25    # Slightly increase sampling rate
num_samples = duration_minutes * 60 * sampling_rate_hz  # Total samples


# File settings
output_file = "synthetic_timeseries_data.csv"
chunk_size = 100000  # Write data in chunks to reduce memory usage

# Start time
start_time = datetime.datetime.now()

# Initialize lists to store data
timestamps = []
cpu_temperatures = []
cpu_usages = []
cpu_loads = []
memory_usages = []
battery_levels = []
cpu_powers = []

# Generate data
for i in range(num_samples):
    try:
        # Get current time
        current_time = datetime.datetime.now()
        timestamps.append(current_time)

        # Generate random CPU temperature
        cpu_temp = random.uniform(30, 85)
        cpu_temperatures.append(cpu_temp)

        # Generate random CPU usage
        cpu_usage = random.uniform(0, 100)
        cpu_usages.append(cpu_usage)

        # Generate random CPU load
        cpu_load = random.uniform(0, 10)
        cpu_loads.append(cpu_load)

        # Generate random memory usage
        memory_usage = random.uniform(0, 100)
        memory_usages.append(memory_usage)

        # Generate random battery level
        battery_level = random.uniform(0, 100)
        battery_levels.append(battery_level)

        # Generate random CPU power consumption
        cpu_power = random.uniform(10, 200)
        cpu_powers.append(cpu_power)

        # Introduce anomalies randomly (e.g., 10% chance)
        if random.random() < 0.1:
            cpu_usages[-1] = random.uniform(90, 100)
        if random.random() < 0.1:
            cpu_temperatures[-1] = random.uniform(85, 105)
        if random.random() < 0.1:
            memory_usages[-1] = random.uniform(95, 100)
        if random.random() < 0.1:
            battery_levels[-1] = random.uniform(0, 10)
        if random.random() < 0.1:
            cpu_powers[-1] = random.uniform(150, 300)

        # Write data in chunks to avoid memory overflow
        if i > 0 and i % chunk_size == 0:
            data_chunk = {
                'timestamp': timestamps,
                'cpu_temperature': cpu_temperatures,
                'cpu_usage': cpu_usages,
                'cpu_load': cpu_loads,
                'memory_usage': memory_usages,
                'battery_level': battery_levels,
                'cpu_power': cpu_powers
            }
            df = pd.DataFrame(data_chunk)
            if not os.path.exists(output_file):
                df.to_csv(output_file, mode='w', index=False)
            else:
                df.to_csv(output_file, mode='a', header=False, index=False)
            
            # Clear lists to free memory
            timestamps.clear()
            cpu_temperatures.clear()
            cpu_usages.clear()
            cpu_loads.clear()
            memory_usages.clear()
            battery_levels.clear()
            cpu_powers.clear()

    except Exception as e:
        print(f"Error: {e}")

# Write the final chunk
data_chunk = {
    'timestamp': timestamps,
    'cpu_temperature': cpu_temperatures,
    'cpu_usage': cpu_usages,
    'cpu_load': cpu_loads,
    'memory_usage': memory_usages,
    'battery_level': battery_levels,
    'cpu_power': cpu_powers
}
df = pd.DataFrame(data_chunk)
if not os.path.exists(output_file):
    df.to_csv(output_file, mode='w', index=False)
else:
    df.to_csv(output_file, mode='a', header=False, index=False)

print(f"Data generation complete! File saved as {output_file}.")
