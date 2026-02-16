import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt


# -----------------------
# BMI Calculation
# -----------------------
def calculate_bmi(weight, height):
    return weight / (height ** 2)


def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# -----------------------
# Input Validation
# -----------------------
def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kg (30 - 300): "))
            if 30 <= weight <= 300:
                return weight
            else:
                print("Weight must be between 30 and 300 kg.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_height():
    while True:
        try:
            height = float(input("Enter your height in meters (1.0 - 2.5): "))
            if 1.0 <= height <= 2.5:
                return height
            else:
                print("Height must be between 1.0 and 2.5 meters.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# -----------------------
# Save Data to CSV
# -----------------------
def save_data(date, weight, height, bmi, category):
    file_exists = os.path.isfile("bmi_data.csv")

    with open("bmi_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Weight", "Height", "BMI", "Category"])

        writer.writerow([date, weight, height, round(bmi, 2), category])


# -----------------------
# Visualize Data
# -----------------------
def visualize_data():
    dates = []
    bmi_values = []

    if not os.path.isfile("bmi_data.csv"):
        print("No historical data found.")
        return

    with open("bmi_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row["Date"])
            bmi_values.append(float(row["BMI"]))

    if bmi_values:
        plt.plot(dates, bmi_values, marker='o')
        plt.title("BMI History")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No data available for visualization.")


# -----------------------
# Main Program
# -----------------------
def main():
    print("=== BMI Calculator ===")

    weight = get_valid_weight()
    height = get_valid_height()

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(date, weight, height, bmi, category)

    choice = input("\nWould you like to see your BMI history graph? (y/n): ")
    if choice.lower() == 'y':
        visualize_data()


if __name__ == "__main__":
    main()
