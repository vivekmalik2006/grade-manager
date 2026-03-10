# Simple Grade Manager

A basic grade management system created for B.Tech First Year project.

## What it does
- Add students with roll number and name
- Add marks for different subjects
- Calculate percentage and grade automatically
- View individual student details
- See list of all students
- Generate class report with statistics
- Delete students if needed
- Saves all data automatically

## How to Run
1. Save the `grade_manager.py` file
2. Open terminal/command prompt
3. Run: `python grade_manager.py`

## Features Explained Simply

### 1. Student Class
- Stores student info (roll no, name, marks)
- Calculates percentage from marks
- Converts percentage to letter grade (A+, A, B, C, D, F)

### 2. GradeManager Class
- Manages all students
- Saves/loads data from JSON file
- Provides menu options for all operations

### 3. Data Storage
- Uses JSON file to save data
- Data persists even after closing program
- No database needed - simple file storage

## Sample Usage