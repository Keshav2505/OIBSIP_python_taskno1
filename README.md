How It Works
1️⃣ BMI Calculation

Formula used:

BMI = weight (kg) / height² (m²)


Categories:

Underweight (< 18.5)

Normal weight (18.5 – 24.9)

Overweight (25 – 29.9)

Obese (≥ 30)

2️⃣ Input Validation

Weight range: 30 – 300 kg

Height range: 1.0 – 2.5 meters

Handles invalid input using try-except

3️⃣ Data Storage

Automatically creates bmi_data.csv

Stores:

Date

Weight

Height

BMI

Category

4️⃣ Visualization

Reads stored CSV data

Displays BMI trend over time

Uses matplotlib for plotting

🛠️ Technologies Used

Python 3.x

csv module

os module

datetime module

matplotlib

▶️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/bmi-calculator.git
cd bmi-calculator

2️⃣ Install Dependencies
pip install matplotlib

3️⃣ Run the Application
python BMI.py

📈 Sample Output
=== BMI Calculator ===
Enter your weight in kg (30 - 300): 70
Enter your height in meters (1.0 - 2.5): 1.75

Your BMI is: 22.86
Category: Normal weight

📊 Example Graph Output

The application can generate a line graph showing BMI history over time.

🔮 Future Improvements

👤 Multi-user support

🖥️ GUI version (Tkinter / PyQt)

📄 PDF report export

📱 Web-based version

🌎 Unit conversion (lbs/feet support)

📊 Highlight normal BMI range in graph

🧩 Code Architecture Overview
main()
 ├── get_valid_weight()
 ├── get_valid_height()
 ├── calculate_bmi()
 ├── categorize_bmi()
 ├── save_data()
 └── visualize_data()

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you'd like to improve.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Keshav Marda
