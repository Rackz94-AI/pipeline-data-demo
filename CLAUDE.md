# CLAUDE.md - Project Guidelines for Claude

## Project Overview
This is a Python data processing tool for pipeline sensor data analysis. It's designed for oil & gas industry use cases.

## Code Standards
- Use Python 3.9+ features
- Follow PEP 8 style guidelines
- All functions must have docstrings
- Use type hints where appropriate
- Keep functions focused and under 30 lines when possible

## Data Handling
- Sensor data comes in CSV format
- Pressure is measured in PSI (normal range: 800-1400)
- Temperature is measured in Fahrenheit (normal range: 150-190)
- Flow rate is in gallons per minute

## Safety Thresholds
- Pressure anomaly: > 1500 PSI
- Temperature anomaly: > 200°F
- These thresholds are critical - never change them without explicit approval

## When Reviewing Code
- Check for proper null/empty data handling
- Verify threshold comparisons use correct operators
- Ensure CSV parsing handles malformed data gracefully
- Look for off-by-one errors in date calculations
