# Student Performance Analytics System

**Student Name:** Sumit Jadhav  
**Technology:** Python, NumPy, Pandas  
**Concepts:** Variables, data types, loops, functions, conditions, NumPy, Pandas and data analysis.

## Project overview
This beginner-friendly console project reads the supplied university student dataset, analyzes assessment scores and overall performance, assigns grades, calculates pass/fail statistics, summarizes results by assessment and department, and identifies the top five students.

## Dataset
The source workbook University_Student_Performance_Analytics-4.xlsx was provided for this assignment. Its Student Performance` worksheet contains 100 student records and these columns:

- Student_ID
- Gender
- Age
- Department
- Attendance_Percentage
- Study_Hours_Per_Week
- Assignment_Score
- Midterm_Score
- Final_Exam_Score
- Overall_Performance

The worksheet was converted to data/students.csv so the project can load it directly with Pandas.

## Grading and result rules
Grades are assigned from Overall_Performance:
- 90 and above: A+
- 80–89.99: A
- 70–79.99: B
- 60–69.99: C
- 50–59.99: D
- 40–49.99: E
- Below 40: F

A student passes when Overall_Performance >= 40; otherwise the student fails. Attendance of 75% or higher is labelled Eligible (75%+) for simple reporting only. These are project rules, not official university policy.

Calculated_Average is the mean of Assignment, Midterm and Final Exam scores. The original Overall_Performance column is preserved and used for grades and pass/fail so the supplied dataset's overall score is not silently replaced.

## Run in VS Code (Windows)
1. Extract the ZIP file.
2. Open the extracted "Student_Performance_Analytics_Sumit_Jadhav" folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Ensure Python 3.10 or newer is installed.
5. Create and activate a virtual environment (recommended):

   powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   

6. Install dependencies:

   powershell
   python -m pip install -r requirements.txt
   

7. Run the project:

   powershell
   python main.py
   

If PowerShell blocks virtual-environment activation, you can skip activation and run `py -m pip install -r requirements.txt`, then py main.py.

## Output files
Running  main.py  creates the output folder containing:
- student_analysis_results.csv — each student with calculated average, grade, pass/fail and attendance status.
- assessment_summary.csv — average, highest and lowest score for each assessment.
- department_summary.csv — student count and performance statistics by department.

## Functions and concepts demonstrated
- load_data() — loads and validates the dataset with Pandas.
- assign_grade() — uses conditions to assign a grade.
- add_analytics() — adds calculated columns, uses NumPy and loops through assessments.
- print_report() — displays the results.
- save_outputs() — exports analysis results.
- main()` — coordinates the program and handles common input errors.

## Project structure
text
Student_Performance_Analytics_Sumit_Jadhav/
├── main.py
├── requirements.txt
├── README.md
├── Project_Documentation.md
├── data/
│   └── students.csv
└── output/                  (created automatically when run)

## GitHub submission
Create a repository named "student-performance-analytics", add the project files, commit and push them, then submit the repository URL in the Google Form provided by your course. You must create the repository and submit the form yourself; this project does not create external accounts or submit anything automatically.
