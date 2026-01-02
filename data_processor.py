"""
Pipeline Data Processor
A simple script that processes sensor data from pipelines.
"""

import csv
from datetime import datetime


def load_sensor_data(filepath):
    """Load sensor readings from a CSV file."""
    data = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'sensor_id': row['sensor_id'],
                'timestamp': row['timestamp'],
                'pressure_psi': float(row['pressure_psi']),
                'flow_rate': float(row['flow_rate']),
                'temperature_f': float(row['temperature_f'])
            })
    return data


def calculate_daily_averages(data):
    """Calculate daily averages for each sensor."""
    daily_totals = {}
    
    for reading in data:
        date = reading['timestamp'].split(' ')[0]
        sensor = reading['sensor_id']
        key = (date, sensor)
        
        if key not in daily_totals:
            daily_totals[key] = {
                'pressure_sum': 0,
                'flow_sum': 0,
                'temp_sum': 0,
                'count': 0
            }
        
        daily_totals[key]['pressure_sum'] += reading['pressure_psi']
        daily_totals[key]['flow_sum'] += reading['flow_rate']
        daily_totals[key]['temp_sum'] += reading['temperature_f']
        daily_totals[key]['count'] += 1
    
    averages = []
    for (date, sensor), totals in daily_totals.items():
        averages.append({
            'date': date,
            'sensor_id': sensor,
            'avg_pressure': totals['pressure_sum'] / totals['count'],
            'avg_flow': totals['flow_sum'] / totals['count'],
            'avg_temp': totals['temp_sum'] / totals['count']
        })
    
    return averages


def detect_anomalies(data, pressure_threshold=1500, temp_threshold=200):
    """Detect readings that exceed safety thresholds."""
    anomalies = []
    
    for reading in data:
        if reading['pressure_psi'] > pressure_threshold:
            anomalies.append({
                'type': 'HIGH_PRESSURE',
                'sensor_id': reading['sensor_id'],
                'timestamp': reading['timestamp'],
                'value': reading['pressure_psi'],
                'threshold': pressure_threshold
            })
        
        if reading['temperature_f'] > temp_threshold:
            anomalies.append({
                'type': 'HIGH_TEMPERATURE',
                'sensor_id': reading['sensor_id'],
                'timestamp': reading['timestamp'],
                'value': reading['temperature_f'],
                'threshold': temp_threshold
            })
    
    return anomalies

def send_alert(anomaly):
    """Send an alert for critical anomalies."""
    if anomaly is None:
        return None
    message = f"ALERT: {anomaly['type']} detected at sensor {anomaly['sensor_id']}"
    print(message)
    return message
if __name__ == "__main__":
    print("Pipeline Data Processor v1.0")
