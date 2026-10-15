# Project Documentation — Student Performance Analytics System

## 1. Project Title and Student Details
- **Project:** Student Performance Analytics System
- **Student Name:** Sumit Jadhav
- **Technology:** Python, NumPy, Pandas

## 2. Objective
The objective is to read student records and turn the raw dataset into understandable performance summaries. The program calculates assessment averages, grades, pass/fail results, attendance labels, department-level statistics and top performers.

## 3. Technologies Used
- Python for program logic, functions, loops and conditions.
- Pandas for loading CSV data, DataFrame operations, grouping, sorting and exporting results.
- NumPy for numerical calculations and conditional pass/fail labels.
- VS Code as the suggested editor.

## 4. Dataset Description
The supplied Excel workbook's `Student Performance` sheet was used. It contains 100 records and 10 columns: Student_ID, Gender, Age, Department, Attendance_Percentage, Study_Hours_Per_Week, Assignment_Score, Midterm_Score, Final_Exam_Score and Overall_Performance. The sheet was exported to `data/students.csv` for simple CSV loading.

## 5. Implementation
1. `load_data()` reads the CSV using `pandas.read_csv()` and validates required columns.
2. `assign_grade()` assigns a letter grade using conditional statements.
3. `add_analytics()` calculates the average of the three assessment scores and adds Grade, Result and Attendance_Status columns. NumPy is used for pass/fail labels and numerical summary calculations.
4. A loop iterates through assessment columns to calculate each assessment's average, highest and lowest scores.
5. `print_report()` displays class-level, assessment-level and department-level analysis, plus the top five performers.
6. `save_outputs()` exports student-level analysis and summary tables to CSV files in `output/`.

## 6. Key Features
- Dataset loading and basic validation.
- Per-student calculated average.
- Grade and pass/fail classification.
- Overall class average, highest and lowest performance.
- Assessment-wise and department-wise analysis.
- Top five performers.
- CSV output files for later review.

## 7. Output / Screenshots
Run `python main.py` in the VS Code terminal. The terminal displays the summary and the program creates three CSV output files. Add a screenshot of your actual terminal output here before submission.

## 8. Final Outcome
The project provides a simple, repeatable way to inspect student performance and export results for further review. It demonstrates core Python programming alongside NumPy and Pandas without using machine learning.

## 9. Challenges and Learning
The dataset was supplied as an Excel workbook, so it was converted into CSV to make the project easy to run. The project also demonstrates why the existing `Overall_Performance` value should be preserved separately from a newly calculated average of the three assessment scores. The grading and pass threshold are explicitly defined in the project and should be changed only if the trainer provides different rules.

## 10. GitHub Repository
Repository URL: **Add your GitHub repository URL after you create and upload the project.**

## Grading Rules Used
- 90+: A+
- 80–89.99: A
- 70–79.99: B
- 60–69.99: C
- 50–59.99: D
- 40–49.99: E
- Below 40: F
- Pass if Overall_Performance is at least 40; otherwise Fail.
- Attendance at least 75% is labelled `Eligible (75%+)` for reporting purposes only, not as an official policy.
