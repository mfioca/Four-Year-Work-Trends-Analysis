# Data Science Portfolio Project
## Analyzing 3 Years of Work Data

### Overview
This project showcases my data cleaning, analysis, and visualization skills using data gathered from [RescueTime](https://www.rescuetime.com), a productivity tracking tool used during my work hours over a three-year period. The dataset includes detailed time logs of every application and webpage accessed, which were cleaned, analyzed, and visualized to highlight trends in focus work, application usage, and productivity patterns.

### Key Steps

1. **Data Cleaning:**
   - Inspected and standardized the dataset by correcting header names, timestamps, and null values.
   - Removed duplicates and cleaned up application names using custom Python functions such as `standardize_app_names` and `find_apps_with_multiple_types_or_subtypes`.
   - Categorized activities using the `assign_activity_subtype` and `assign_activity_type` functions, ensuring consistency in activity subtypes.

2. **Data Analysis and Visualization:**
   - Visualized trends in the data using both Jupyter Notebook and Tableau.
   - In Jupyter Notebook, created initial graphs and explored patterns in focus and non-focus work activities.
   - In Tableau, developed interactive dashboards to highlight trends in activity categories, application usage, and time-based patterns across the dataset.

### Files in the Repository

- **user_history.csv**: Original dataset downloaded from RescueTime.com.
- **cleaning_csv.ipynb**: Jupyter Notebook for data cleaning and preparation.
- **cleaned_data_1.csv**: Final cleaned dataset.
- **look_at_data.ipynb**: Jupyter Notebook used for data analysis and graphing.
- **tableau_data.csv**: Final cleaned dataset prepared for import into Tableau.
- **three_year_work_data_analysis.twbx**: Tableau workbook file containing graphs and dashboards.
- **python_code_for_reference.py**: Python file with custom functions used for data processing.
- **Tableau_Dashboard.png**: Screenshot of the final Tableau dashboard (when ready).
