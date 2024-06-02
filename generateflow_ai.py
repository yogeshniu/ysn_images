import random
import csv
import math

# Define year
year = 2024

# Monthly mean flow values (replace with actual values from Nepal data)
monthly_means = [59.55, 49.19, 48.23, 71.52, 155.77, 416.99, 821.46, 895.23, 648.87, 299.44, 134.71, 82.50]  # Example values

# Amplitude scaling factor (adjust for desired range of daily variations)
amplitude_factor = 0.2

# Define offset adjustment function (modify for different seasonal patterns)
def get_offset(month):
  # Adjust this function to match the seasonal variations in the Nepal data
  # Here's a simple example with higher values in monsoon months (Jun-Sep)
  if month in (6, 7, 8, 9):
    return 0.1
  else:
    return 0

# Open CSV file for writing
with open('discharge_ai.csv', 'w', newline='') as csvfile:
  # Create CSV writer object
  writer = csv.writer(csvfile)
  # Write header row
  writer.writerow(['Date', 'Discharge'])

  # Loop through each day of the year
  for month in range(1, 13):
    # Get number of days in the month (considering leap year)
    if month in (4, 6, 9, 11):
      days_in_month = 30
    elif month == 2:
      if year % 4 == 0:  # Check for leap year
        days_in_month = 29
      else:
        days_in_month = 28
    else:
      days_in_month = 31

    # Monthly mean for the current month
    monthly_mean = monthly_means[month - 1]
    # Offset adjustment for the month
    offset = get_offset(month)

    # Loop through each day in the month
    for day in range(1, days_in_month + 1):
      # Generate random angle for sine function (0 to 2*pi)
      angle = random.uniform(0, 2*math.pi)
      # Calculate daily fluctuation based on sine function
      daily_variation = amplitude_factor * math.sin(angle)
      # Adjust discharge value with monthly mean, offset, and variation
      discharge = monthly_mean + offset + daily_variation
      # Create date string in YYYY-MM-DD format
      date_string = f"{year:04d}-{month:02d}-{day:02d}"
      # Write date and discharge to CSV file
      writer.writerow([date_string, discharge])

print(f"Random discharge data for year {year} with seasonal variations saved to river_discharge.csv")
