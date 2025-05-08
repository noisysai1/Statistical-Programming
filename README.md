# Statistical-Programming
Statistical Programming


# 📊 Statistical Programming – Assignment 1

**Course:** DATA 51100
**Student:** Sai Kumar Murarishetti  
**Lewis ID:** L30079224  

---

## 📝 Assignment Overview

This is the first programming assignment for the Statistical Programming course. The objective of this assignment is to implement a Python program that calculates the **mean** and **variance** of a sequence of numbers using an **online algorithm** (incremental approach), without storing the entire dataset.

The user is prompted to enter a number `n`, and the program calculates the mean and variance for all integers from 1 to `n` using a numerically stable method. The loop continues until the user enters a negative number.

---

## 🔢 Key Concepts

- **Mean (Average)**: Sum of numbers divided by the count.
- **Variance**: Measures the spread of the numbers from the mean.
- **Online Algorithm**: Allows updating statistics incrementally as new data comes in, efficient for large data or streams.

---

## 🧮 How the Program Works

1. Prompts the user for an integer input.
2. For values ≥ 0:
   - Uses a `while` loop to iteratively compute:
     - Mean: updated at each step using `xn = xn + (i - xn)/i`
     - Variance: updated using a formula derived from Welford’s method.
3. Stops when a negative number is entered.
4. Displays the final computed **mean** and **variance** for each valid input.

---

## 🚀 How to Run

Make sure you have Python installed (version 3.x). Run the script in your terminal or any Python environment:
python OnlineStats.py
