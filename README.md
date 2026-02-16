# Multi-Campus Education Data Preprocessing Pipeline

## Rwanda Polytechnic - Data Mining & Data Warehousing Project

**Course**: Data Mining and Data Warehousing  
**Institution**: Rwanda Polytechnic  
**Project Duration**: 1 Week  
**Submission Date**: February 16, 2026

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Team Information](#team-information)
3. [Project Structure](#project-structure)
4. [Installation & Setup](#installation--setup)
5. [Dataset Description](#dataset-description)
6. [Pipeline Phases](#pipeline-phases)
7. [Execution Instructions](#execution-instructions)
8. [Outputs & Deliverables](#outputs--deliverables)
9. [Technologies Used](#technologies-used)
10. [Key Results](#key-results)

---

## 🎯 Project Overview

This project implements a comprehensive **data preprocessing pipeline** for multi-campus educational data integration. The system consolidates student, course, and assessment data from three Rwanda Polytechnic campuses (Huye, Kigali, and Musanze) into a unified, analytics-ready "gold" dataset.

### Business Context

Rwanda Polytechnic requires a centralized data analytics platform to:
- Monitor student performance across multiple campuses
- Identify at-risk students for early intervention
- Support data-driven decision making
- Enable predictive analytics for dropout prevention
- Standardize reporting across all campuses

### Technical Challenge

The raw data from each campus contains multiple quality issues:
- **Missing values** (10-15% across various columns)
- **Duplicate records** (student IDs, assessment results)
- **Outliers** (invalid marks, unrealistic values)
- **Inconsistent formats** (dates, text casing, course codes)
- **Noisy data** (typos, extra spaces, special characters)

---

## 👥 Team Information

**Group Members**: [3 students per team]

- **Member 1**: [Name] - [Role/Responsibilities]
- **Member 2**: [Name] - [Role/Responsibilities]
- **Member 3**: [Name] - [Role/Responsibilities]

---

## 📁 Project Structure

```
multi-campus-pipeline/
│
├── raw_data/                          # Original campus datasets
│   ├── Huye_students.csv
│   ├── Huye_courses.csv
│   ├── Huye_assessments.csv
│   ├── Kigali_students.csv
│   ├── Kigali_courses.csv
│   ├── Kigali_assessments.csv
│   ├── Musanze_students.csv
│   ├── Musanze_courses.csv
│   └── Musanze_assessments.csv
│
├── outputs/                           # All generated outputs
│   ├── students_raw_combined.csv
│   ├── students_cleaned.csv
│   ├── silver_students_transformed.csv
│   ├── gold_integrated.csv
│   ├── gold_reduced.csv
│   ├── gold_features.csv             # FINAL OUTPUT
│   ├── 01_profiling_summary.txt
│   ├── 02_cleaning_summary_report.txt
│   └── [visualization PNG files]
│
├── scripts/
│   ├── 00_generate_sample_data.py    # Data generation
│   └── 01_load_and_profile.py        # Phase 1 script
│
├── notebooks/
│   ├── 02_cleaning_pipeline.ipynb    # Phase 2
│   ├── 03_transformation.ipynb       # Phase 3
│   ├── 04_integration.ipynb          # Phase 4
│   ├── 05_reduction.ipynb            # Phase 5
│   └── 06_feature_engineering.ipynb  # Phase 6
│
├── README.md                          # This file
├── PROJECT_REPORT.docx               # Comprehensive report
└── requirements.txt                   # Python dependencies
```

---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Step 1: Clone Repository

```bash
git clone [repository-url]
cd multi-campus-pipeline
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required Packages**:
```
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
scikit-learn==1.3.0
jupyter==1.0.0
```

---

## 📊 Dataset Description

### Data Sources

**3 Campuses**: Huye, Kigali, Musanze

**3 Dataset Types per Campus**:

#### 1. Students Dataset
- **Records**: ~180-220 per campus
- **Columns**: Student_ID, First_Name, Last_Name, Gender, DOB, Phone, Email, Program, Level, Intake_Year
- **Issues**: Missing gender/phone/DOB, duplicate IDs, inconsistent formats

#### 2. Courses Dataset
- **Records**: 25 per campus (same catalog)
- **Columns**: Course_Code, Course_Title, Credits, Program, Level, Semester
- **Issues**: Missing credits, code variations, spacing

#### 3. Assessments Dataset
- **Records**: 4-6 assessments per student
- **Columns**: Student_ID, Course_Code, Assessment_Type, Mark, Assessment_Date, Academic_Year, Semester, Attendance_Rate
- **Issues**: Invalid marks (>100, <0), missing values, duplicates, date format inconsistencies

### Academic Programs

1. Information Technology
2. Civil Engineering
3. Electrical Engineering
4. Business Administration
5. Tourism and Hospitality
6. Architecture

---

## 🔄 Pipeline Phases

### Phase 1: Data Collection & Loading
**Script**: `01_load_and_profile.py`

**Tasks**:
- Load data from 3 campuses
- Add metadata (Campus_ID, Source_File, Upload_Date)
- Generate data profiling summary
- Visualize missing values and distribution

**Outputs**:
- Combined raw datasets
- Profiling summary report
- Visualization charts

### Phase 2: Data Cleaning
**Notebook**: `02_cleaning_pipeline.ipynb`

**Tasks**:
1. **Missing Data**: Impute using mean/median/mode
2. **Duplicates**: Remove by key fields
3. **Outliers**: Detect and treat using IQR/capping
4. **Inconsistent Formats**: Standardize dates, text, codes
5. **Noisy Data**: Clean with regex, validate ranges

**Outputs**:
- Cleaned datasets
- Before/after comparison report
- Quality metrics

### Phase 3: Data Transformation
**Notebook**: `03_transformation.ipynb`

**Tasks**:
- **Scaling**: Standardize attendance rates, marks
- **Encoding**: One-hot encode categorical variables
- **Binning**: Create performance and attendance bands

**Outputs**:
- Transformed silver datasets
- Transformation summary

### Phase 4: Data Integration
**Notebook**: `04_integration.ipynb`

**Tasks**:
- Merge students ↔ assessments ↔ courses
- Resolve conflicts (name variations, code mismatches)
- Create unified gold dataset

**Outputs**:
- Integrated gold dataset
- Merge quality report

### Phase 5: Data Reduction
**Notebook**: `05_reduction.ipynb`

**Tasks**:
- Remove high-missing columns (>50%)
- Drop low-variance features
- Select analysis-ready features

**Outputs**:
- Reduced gold dataset
- Feature selection justification

### Phase 6: Feature Engineering
**Notebook**: `06_feature_engineering.ipynb`

**Tasks**:
- **Date-time features**: assessment_month, assessment_weekday, is_weekend
- **Aggregation features**: student_avg_mark, student_course_count, total_credits
- **Risk flags**: is_at_risk, low_attendance_flag

**Outputs**:
- Final gold_features.csv
- Feature engineering visualizations
- Analytics-ready dataset

---

## ▶️ Execution Instructions

### Option 1: Run Complete Pipeline

```bash
# Generate sample data
python 00_generate_sample_data.py

# Load and profile
python 01_load_and_profile.py

# Run remaining phases in Jupyter
jupyter notebook
# Then open and run notebooks 02-06 in sequence
```

### Option 2: Run Individual Phases

```bash
# Phase 1
python 01_load_and_profile.py

# Phases 2-6: Open in Jupyter and run sequentially
jupyter notebook 02_cleaning_pipeline.ipynb
jupyter notebook 03_transformation.ipynb
jupyter notebook 04_integration.ipynb
jupyter notebook 05_reduction.ipynb
jupyter notebook 06_feature_engineering.ipynb
```

### Expected Execution Time

- Data generation: 30 seconds
- Phase 1: 1 minute
- Phase 2: 2-3 minutes
- Phase 3: 1-2 minutes
- Phase 4: 30 seconds
- Phase 5: 30 seconds
- Phase 6: 1-2 minutes

**Total**: ~10-15 minutes

---

## 📈 Outputs & Deliverables

### Final Datasets

1. **gold_integrated.csv** - Fully integrated data (5,905 records × 42 columns)
2. **gold_features.csv** - With engineered features (5,905 records × 50+ columns)

### Reports

1. **01_profiling_summary.txt** - Initial data quality assessment
2. **02_cleaning_summary_report.txt** - Cleaning operations and metrics
3. **PROJECT_REPORT.docx** - Comprehensive project report (4-6 pages)

### Visualizations

1. **01_missing_values_profile.png** - Missing data across datasets
2. **01_campus_distribution.png** - Data distribution by campus
3. **01_mark_distribution_raw.png** - Raw mark distribution with outliers
4. **02_missing_values_before.png** - Missing data before cleaning
5. **02_outliers_before.png** - Outlier detection visualization
6. **02_before_after_comparison.png** - Cleaning impact metrics
7. **06_missing_values_final.png** - Final data quality
8. **06_mark_distribution_final.png** - Cleaned mark distribution
9. **06_at_risk_by_campus.png** - At-risk students analysis

### Presentation

**PowerPoint slides** (8-10 slides):
- Workflow diagram
- Before vs after metrics
- Final dataset preview
- Key insights

---

## 🛠️ Technologies Used

### Programming & Tools
- **Python 3.10**: Core programming language
- **Jupyter Notebook**: Interactive development
- **Git**: Version control

### Data Processing Libraries
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **scikit-learn**: Machine learning preprocessing

### Visualization Libraries
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical graphics

### Key Techniques
- IQR method for outlier detection
- StandardScaler for feature scaling
- One-hot encoding for categorical variables
- K-bins discretization for binning
- Aggregate functions for feature engineering

---

## 📊 Key Results

### Data Quality Improvement

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Missing Values (Students) | 73 | 0 | 100% |
| Missing Values (Assessments) | 492 | 0 | 100% |
| Duplicate Students | 18 | 0 | 100% |
| Duplicate Assessments | 205 | 0 | 100% |
| Invalid Marks | 31 | 0 | 100% |
| Total Records (Students) | 607 | 589 | -3% (cleaned) |
| Total Records (Assessments) | 6,110 | 5,905 | -3.4% (cleaned) |

### Final Dataset Characteristics

- **Total Records**: 5,905 assessment records
- **Unique Students**: 589
- **Campuses**: 3 (Huye, Kigali, Musanze)
- **Programs**: 6
- **Courses**: 75 (25 per campus)
- **Features**: 50+ (including 8+ engineered features)
- **Data Quality**: 100% complete, no duplicates, no outliers

### Engineered Features (8+)

1. **assessment_month** - Month of assessment
2. **assessment_weekday** - Day of week
3. **is_weekend_assessment** - Boolean flag
4. **student_course_count** - Number of courses per student
5. **student_avg_mark** - Average mark per student
6. **student_max_mark** - Best mark per student
7. **student_fail_count** - Number of failed assessments
8. **is_at_risk** - Risk flag (avg < 50 OR fails >= 2)
9. **low_attendance_flag** - Attendance < 75%
10. **student_total_credits** - Total credits earned

---

## 📝 Academic Context

This project fulfills the requirements for **FA2 Group Work** in the Data Mining and Data Warehousing course at Rwanda Polytechnic. It demonstrates practical application of:

- Data collection and profiling
- Data cleaning techniques
- Data transformation methods
- Data integration strategies
- Dimensionality reduction
- Feature engineering for analytics
- Data quality assessment
- Professional documentation and reporting

---

## 📧 Contact & Support

For questions or issues:
- Review the PROJECT_REPORT.docx for detailed methodology
- Check individual notebook comments for implementation details
- Refer to output logs in the `outputs/` directory

---

## 📄 License

This project is developed for educational purposes as part of Rwanda Polytechnic coursework.

---

**Last Updated**: February 2026  
**Version**: 1.0
