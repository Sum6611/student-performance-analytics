"""
Student Performance Analytics System
Student: Sumit Jadhav
Technology: Python, NumPy, Pandas
"""

from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
OUTPUT_DIR = BASE_DIR / "output"

SCORE_COLUMNS = ["Assignment_Score", "Midterm_Score", "Final_Exam_Score"]
PASS_MARK = 40
TOP_STUDENT_COUNT = 5


def load_data(file_path):
    """Load the student CSV file into a Pandas DataFrame."""
    data = pd.read_csv(file_path)
    required = ["Student_ID", "Department", "Attendance_Percentage",
                "Study_Hours_Per_Week", "Overall_Performance"] + SCORE_COLUMNS
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing)}")
    return data


def assign_grade(score):
    """Assign a letter grade using the project's stated grading rule."""
    if pd.isna(score):
        return "N/A"
    if score >= 90:
        return "A+"
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    if score >= PASS_MARK:
        return "E"
    return "F"


def add_analytics(data):
    """Create calculated columns using Pandas, NumPy, functions and a loop."""
    result = data.copy()
    result["Calculated_Average"] = result[SCORE_COLUMNS].mean(axis=1)
    # The supplied dataset already contains Overall_Performance. We preserve it
    # and use it as the main score for grades/pass-fail, as documented below.
    result["Grade"] = result["Overall_Performance"].apply(assign_grade)
    result["Result"] = np.where(
        result["Overall_Performance"] >= PASS_MARK, "Pass", "Fail"
    )
    result["Attendance_Status"] = np.where(
        result["Attendance_Percentage"] >= 75, "Eligible (75%+)", "Low Attendance"
    )

    # Demonstrate a loop by printing the summary for every subject score column.
    subject_summary = []
    for column in SCORE_COLUMNS:
        values = result[column].dropna().to_numpy()
        subject_summary.append({
            "Assessment": column.replace("_Score", "").replace("_", " "),
            "Average": round(float(np.mean(values)), 2) if len(values) else np.nan,
            "Highest": round(float(np.max(values)), 2) if len(values) else np.nan,
            "Lowest": round(float(np.min(values)), 2) if len(values) else np.nan,
        })
    return result, pd.DataFrame(subject_summary)


def print_report(data, subject_summary):
    """Display readable analysis results in the terminal."""
    scores = data["Overall_Performance"].dropna().to_numpy()
    if len(scores) == 0:
        print("No valid Overall_Performance scores are available.")
        return

    print("\n" + "=" * 68)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("                 Student: Sumit Jadhav")
    print("=" * 68)
    print(f"Total student records : {len(data)}")
    print(f"Overall class average : {np.mean(scores):.2f}")
    print(f"Highest performance  : {np.max(scores):.2f}")
    print(f"Lowest performance   : {np.min(scores):.2f}")
    print(f"Students passed       : {(data['Result'] == 'Pass').sum()}")
    print(f"Students failed       : {(data['Result'] == 'Fail').sum()}")
    print(f"Pass percentage       : {(data['Result'].eq('Pass').mean() * 100):.2f}%")

    print("\n--- Assessment-wise Analysis ---")
    print(subject_summary.to_string(index=False))

    print("\n--- Department-wise Average Performance ---")
    department_summary = (
        data.groupby("Department", dropna=False)["Overall_Performance"]
        .agg(["count", "mean", "min", "max"])
        .rename(columns={"count": "Students", "mean": "Average", "min": "Lowest", "max": "Highest"})
        .round(2)
        .sort_values("Average", ascending=False)
    )
    print(department_summary.to_string())

    print("\n--- Top Performing Students ---")
    display_columns = ["Student_ID", "Department", "Overall_Performance", "Grade", "Result"]
    print(data.nlargest(TOP_STUDENT_COUNT, "Overall_Performance")[display_columns].to_string(index=False))

    print("\n--- Student Results (first 15 records) ---")
    display_columns = ["Student_ID", "Department", "Attendance_Percentage",
                       "Overall_Performance", "Grade", "Result"]
    print(data[display_columns].head(15).round(2).to_string(index=False))


def save_outputs(data, subject_summary):
    """Save detailed student results and summaries as CSV files."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    data.to_csv(OUTPUT_DIR / "student_analysis_results.csv", index=False)
    subject_summary.to_csv(OUTPUT_DIR / "assessment_summary.csv", index=False)
    department_summary = (
        data.groupby("Department", dropna=False)["Overall_Performance"]
        .agg(Student_Count="count", Average_Performance="mean",
             Highest_Performance="max", Lowest_Performance="min")
        .round(2).reset_index()
    )
    department_summary.to_csv(OUTPUT_DIR / "department_summary.csv", index=False)
    print(f"\nOutput files saved in: {OUTPUT_DIR}")


def main():
    try:
        data = load_data(DATA_FILE)
        analysed_data, subject_summary = add_analytics(data)
        print_report(analysed_data, subject_summary)
        save_outputs(analysed_data, subject_summary)
    except FileNotFoundError:
        print(f"Dataset not found: {DATA_FILE}")
        print("Keep students.csv inside the data folder.")
    except (ValueError, KeyError) as error:
        print(f"Could not process dataset: {error}")


if __name__ == "__main__":
    main()
