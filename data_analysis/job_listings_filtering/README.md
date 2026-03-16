# 💼 Job Listings Filter

A small Python data analysis tool that filters job postings based on user-defined criteria.

The project demonstrates how **pandas filtering operations** can be used to build flexible data queries similar to SQL.

---

## ✨ Features

Filter job postings using:

* 🧑‍💻 Job title
* 🛠 Required skills
* 📍 Job location
* 💰 Salary range

Multiple filters can be applied simultaneously.

---

## 🔍 Example Search

Example filter:

* Job title: **Software Engineer**
* Skill: **C#**
* Locations: **Los Angeles, New York**
* Salary range: **70k – 90k**

The function returns only the rows matching the specified conditions.

---

## 📊 Dataset

Dataset source: [Kaggle](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

The dataset contains job postings with fields such as:

* job title
* skills or description
* company name
* location
* median salary

Download the dataset and place it inside the `data/` folder.

---

## 🛠 Technologies Used

* 🐍 Python
* 🐼 pandas
* 📄 CSV datasets

---

## 🎯 Purpose

This project explores how pandas can be used to implement **filtering logic similar to database queries**.

The filtering function is designed to be reusable and extendable with additional filters in the future.
