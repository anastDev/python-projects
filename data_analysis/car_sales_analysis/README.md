# 🚗 Car Sales Data Loader

A small Python project that demonstrates **safe CSV loading**, **structured logging**, and basic dataset inspection using pandas.

The goal of this project is to build a **clean foundation for data analysis workflows** before adding more advanced analysis.

---

## ✨ Features

* 📂 CSV file loading with error handling
* 🪵 Structured logging to both console and file
* 🔎 Dataset preview using pandas
* 🧩 Modular structure separating utilities and execution logic

---

## 📁 Project Structure

```
car_sales_analysis/
│
├── data/
│   └── car_sales_small.csv
│
├── scripts/
│   ├── logger_config.py
│   └── file_reader.py
│
├── main.py
└── README.md
```

---

## 🧠 How It Works

### 🪵 logger_config.py

Configures a reusable Python logger with:

* file logging
* console logging
* formatted log messages

### 📂 file_reader.py

Handles safe CSV file loading using pandas with error handling for:

* missing files
* permission errors
* empty datasets
* unexpected exceptions

### ▶️ main.py

Entry point of the program. It:

1. Loads the dataset
2. Displays the first rows of the dataset
3. Displays the last rows of the dataset

---

## 🛠 Technologies Used

* 🐍 Python
* 🐼 pandas
* 🪵 logging

---

## 🎯 Purpose

This project is part of a collection of small Python experiments used to practice:

* clean project structure
* logging configuration
* data loading workflows
* error handling in data pipelines

Future versions may include actual analysis such as:

* 📊 sales trends
* 🚘 revenue by car model
* 🌍 regional sales comparisons
