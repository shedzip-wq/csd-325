# Sheridan Dela Cruz
# April 18, 2026
# Module 4.2

"""
Revised version of sitka_highs.py with the following changes:
- Added a user menu (Highs, Lows, Exit)
- Program loops until user selects Exit
- User can choose to view high temperatures (red) or low temperatures (blue)
- Added low‑temperature extraction from CSV
- Added exit message
- Added documentation throughout
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Load the data once so the menu can reuse it
filename = 'sitka_weather_2018_simple.csv'

dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)


def show_highs():
    """Plot high temperatures in red."""
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def show_lows():
    """Plot low temperatures in blue."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# -----------------------------
# Main Program Loop
# -----------------------------
while True:
    print("\nWeather Data Viewer")
    print("-------------------")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        show_highs()

    elif choice == "2":
        show_lows()

    elif choice == "3":
        print("\nExiting program. Have a great day!")
        sys.exit()

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
