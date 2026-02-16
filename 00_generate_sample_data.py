# 00_generate_sample_data.py
"""
Generate sample raw data for 3 Rwanda Polytechnic campuses
This creates intentionally flawed datasets for the preprocessing pipeline project
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Create raw_data directory
os.makedirs('raw_data', exist_ok=True)

print("="*60)
print("GENERATING SAMPLE DATA FOR 3 CAMPUSES")
print("="*60)

# Define campuses
campuses = ['Huye', 'Kigali', 'Musanze']

# Rwanda Polytechnic Programs
programs = [
    'Information Technology',
    'Civil Engineering', 
    'Electrical Engineering',
    'Business Administration',
    'Tourism and Hospitality',
    'Architecture'
]

# Common Rwandan first names
first_names = ['Jean', 'Marie', 'Claude', 'Grace', 'Eric', 'Ange', 'Emmanuel', 'Diane', 
               'Patrick', 'Esther', 'David', 'Sarah', 'Joseph', 'Aline', 'Samuel',
               'Nadine', 'Daniel', 'Alice', 'Moses', 'Claire', 'Isaac', 'Jeanne',
               'Frank', 'Louise', 'Kevin', 'Stella', 'Prince', 'Gloria']

last_names = ['Uwimana', 'Habimana', 'Mugisha', 'Niyonzima', 'Ntawukuriryayo',
              'Bizimana', 'Mukamana', 'Nkurunziza', 'Tuyisenge', 'Mutabazi',
              'Ingabire', 'Munyakazi', 'Kubwimana', 'Nsengiyumva', 'Umuhoza']

# Course lists by program
courses_by_program = {
    'Information Technology': [
        ('ICT101', 'Programming Fundamentals', 4),
        ('ICT102', 'Database Systems', 4),
        ('ICT103', 'Web Development', 3),
        ('ICT201', 'Data Structures', 4),
        ('ICT202', 'Network Security', 3),
        ('ICT301', 'Software Engineering', 4),
    ],
    'Civil Engineering': [
        ('CE101', 'Engineering Mathematics', 5),
        ('CE102', 'Structural Analysis', 4),
        ('CE103', 'Construction Materials', 3),
        ('CE201', 'Hydraulics', 4),
        ('CE202', 'Soil Mechanics', 4),
    ],
    'Electrical Engineering': [
        ('EE101', 'Circuit Theory', 4),
        ('EE102', 'Electronics Basics', 4),
        ('EE103', 'Power Systems', 3),
        ('EE201', 'Control Systems', 4),
    ],
    'Business Administration': [
        ('BA101', 'Principles of Management', 3),
        ('BA102', 'Marketing Fundamentals', 3),
        ('BA103', 'Financial Accounting', 4),
        ('BA201', 'Business Statistics', 4),
    ],
    'Tourism and Hospitality': [
        ('TH101', 'Tourism Management', 3),
        ('TH102', 'Hotel Operations', 3),
        ('TH103', 'Food and Beverage', 3),
    ],
    'Architecture': [
        ('AR101', 'Architectural Design', 4),
        ('AR102', 'Building Technology', 4),
        ('AR103', 'Urban Planning', 3),
    ]
}

def add_typos(text, probability=0.05):
    """Add random typos to text"""
    if random.random() < probability:
        chars = list(text)
        if len(chars) > 2:
            idx = random.randint(1, len(chars)-1)
            chars[idx] = chars[idx].upper() if chars[idx].islower() else chars[idx].lower()
        return ''.join(chars)
    return text

def add_spaces(text, probability=0.1):
    """Add random spaces"""
    if random.random() < probability:
        return f"  {text}  "
    return text

def generate_students_data(campus, num_students=200):
    """Generate student data with intentional issues"""
    
    data = []
    campus_id_start = campuses.index(campus) * 1000
    
    for i in range(num_students):
        student_id = f"RP{campus[0]}{campus_id_start + i + 1:04d}"
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        # Add typos to some names
        first_name = add_typos(first_name, 0.08)
        last_name = add_typos(last_name, 0.05)
        
        # Random DOB between 1998-2005
        dob = datetime(random.randint(1998, 2005), random.randint(1, 12), random.randint(1, 28))
        
        # Gender with inconsistent formats
        gender_options = ['M', 'Male', 'MALE', 'F', 'Female', 'FEMALE', 'm', 'f']
        gender = random.choice(gender_options)
        
        # Phone with 250 prefix
        phone = f"250{random.randint(720000000, 799999999)}"
        
        program = random.choice(programs)
        program = add_spaces(program, 0.1)  # Add spaces to some programs
        
        level = random.choice([1, 2, 3, 4])
        intake_year = random.choice([2022, 2023, 2024, 2025])
        
        email = f"{first_name.lower()}.{last_name.lower()}@rp.ac.rw"
        
        data.append({
            'Student_ID': student_id,
            'First_Name': first_name,
            'Last_Name': last_name,
            'Gender': gender,
            'DOB': dob.strftime('%Y-%m-%d') if random.random() > 0.1 else dob.strftime('%d/%m/%Y'),
            'Phone': phone,
            'Email': email,
            'Program': program,
            'Level': level,
            'Intake_Year': intake_year
        })
    
    df = pd.DataFrame(data)
    
    # INTRODUCE ISSUES
    # 1. Missing values (10-15%)
    missing_indices = np.random.choice(df.index, size=int(len(df)*0.12), replace=False)
    df.loc[missing_indices[:len(missing_indices)//3], 'Gender'] = np.nan
    df.loc[missing_indices[len(missing_indices)//3:2*len(missing_indices)//3], 'Phone'] = np.nan
    df.loc[missing_indices[2*len(missing_indices)//3:], 'DOB'] = np.nan
    
    # 2. Duplicates (5-8 duplicate student IDs)
    duplicate_count = random.randint(5, 8)
    duplicate_rows = df.sample(n=duplicate_count)
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    return df

def generate_courses_data(campus):
    """Generate course catalog with issues"""
    
    data = []
    
    for program, course_list in courses_by_program.items():
        for course_code, course_title, credits in course_list:
            # Add variations to course codes
            code_variations = [
                course_code,
                course_code.replace('', '-'),  # Add dash randomly
                course_code.lower(),  # Lowercase
                course_code.replace('0', 'O'),  # Replace 0 with O
            ]
            
            chosen_code = random.choice(code_variations) if random.random() < 0.3 else course_code
            
            # Add spaces and case variations to title
            title = add_spaces(course_title, 0.15)
            
            # Semester assignment
            semester = random.choice([1, 2])
            
            # Level based on course code
            level = int(course_code[2]) if course_code[2].isdigit() else 1
            
            data.append({
                'Course_Code': chosen_code,
                'Course_Title': title,
                'Credits': credits,
                'Program': program,
                'Level': level,
                'Semester': semester
            })
    
    df = pd.DataFrame(data)
    
    # INTRODUCE ISSUES
    # Missing credits for some courses
    missing_credits = np.random.choice(df.index, size=int(len(df)*0.1), replace=False)
    df.loc[missing_credits, 'Credits'] = np.nan
    
    return df

def generate_assessments_data(campus, students_df, courses_df):
    """Generate assessment results with issues"""
    
    data = []
    
    assessment_types = ['CAT', 'Exam', 'Assignment', 'Quiz', 'Project']
    academic_years = ['2023/2024', '2024/2025', '2025/2026']
    
    # Each student has 4-6 course assessments
    for _, student in students_df.iterrows():
        num_courses = random.randint(4, 6)
        
        # Filter courses by student's program
        student_program = student['Program'].strip()
        program_courses = courses_df[courses_df['Program'] == student_program]
        
        if len(program_courses) == 0:
            program_courses = courses_df.sample(n=min(6, len(courses_df)))
        
        selected_courses = program_courses.sample(n=min(num_courses, len(program_courses)))
        
        for _, course in selected_courses.iterrows():
            # 2-3 assessments per course
            num_assessments = random.randint(2, 3)
            
            for _ in range(num_assessments):
                assessment_type = random.choice(assessment_types)
                
                # Generate marks (with outliers)
                if random.random() < 0.05:  # 5% outliers
                    mark = random.choice([120, -5, 150, -10])  # Invalid marks
                else:
                    mark = np.random.normal(65, 15)  # Normal distribution around 65
                    mark = max(0, min(100, mark))  # Cap between 0-100 normally
                
                # Random date in past year
                days_ago = random.randint(1, 365)
                assessment_date = datetime.now() - timedelta(days=days_ago)
                
                # Academic year and semester
                academic_year = random.choice(academic_years)
                semester = random.choice([1, 2])
                
                # Attendance rate
                attendance = random.uniform(60, 100) if random.random() > 0.1 else np.nan
                
                data.append({
                    'Student_ID': student['Student_ID'],
                    'Course_Code': course['Course_Code'],
                    'Assessment_Type': assessment_type,
                    'Mark': round(mark, 1),
                    'Assessment_Date': assessment_date.strftime('%Y-%m-%d'),
                    'Academic_Year': academic_year,
                    'Semester': semester,
                    'Attendance_Rate': round(attendance, 1) if not pd.isna(attendance) else np.nan
                })
    
    df = pd.DataFrame(data)
    
    # INTRODUCE ISSUES
    # 1. Missing marks
    missing_marks = np.random.choice(df.index, size=int(len(df)*0.08), replace=False)
    df.loc[missing_marks, 'Mark'] = np.nan
    
    # 2. Duplicate assessments (same student, course, semester)
    duplicate_count = random.randint(10, 15)
    duplicate_rows = df.sample(n=duplicate_count)
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    # 3. Inconsistent date formats
    date_format_indices = np.random.choice(df.index, size=int(len(df)*0.2), replace=False)
    for idx in date_format_indices:
        date_obj = pd.to_datetime(df.loc[idx, 'Assessment_Date'])
        df.loc[idx, 'Assessment_Date'] = date_obj.strftime('%d/%m/%Y')
    
    return df

# GENERATE DATA FOR ALL CAMPUSES
for campus in campuses:
    print(f"\n--- Generating {campus} Campus Data ---")
    
    # Generate students
    students = generate_students_data(campus, num_students=random.randint(180, 220))
    students.to_csv(f'raw_data/{campus}_students.csv', index=False)
    print(f"✓ Students: {len(students)} records")
    
    # Generate courses
    courses = generate_courses_data(campus)
    courses.to_csv(f'raw_data/{campus}_courses.csv', index=False)
    print(f"✓ Courses: {len(courses)} records")
    
    # Generate assessments
    assessments = generate_assessments_data(campus, students, courses)
    assessments.to_csv(f'raw_data/{campus}_assessments.csv', index=False)
    print(f"✓ Assessments: {len(assessments)} records")

print("\n" + "="*60)
print("DATA GENERATION COMPLETE!")
print("="*60)
print("\nGenerated files in raw_data/ folder:")
print("- Huye_students.csv, Huye_courses.csv, Huye_assessments.csv")
print("- Kigali_students.csv, Kigali_courses.csv, Kigali_assessments.csv")
print("- Musanze_students.csv, Musanze_courses.csv, Musanze_assessments.csv")
print("\nIssues introduced:")
print("✓ Missing values (10-15% in various columns)")
print("✓ Duplicate records")
print("✓ Outliers in marks (values > 100 or < 0)")
print("✓ Inconsistent formats (dates, text casing)")
print("✓ Noisy data (extra spaces, typos)")
print("\nNext step: Run 01_load_and_profile.py")
