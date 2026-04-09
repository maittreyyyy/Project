# Medicaid Drug Reimbursement Analysis  
**CAP5771 – Milestone 1**

---

## **Project Overview**

This project analyzes **State Drug Utilization Data** published by the **Centers for Medicare & Medicaid Services (CMS)**. The objective is to examine whether reimbursement prices for identical drugs vary systematically across U.S. states and whether those differences persist over time.

Milestone 1 focuses on the early stages of the data science workflow:

- **Problem formulation**
- **Data acquisition**
- **Database schema design**
- **Initial data exploration**

Milestone 2 extends the project beyond exploration into a full data science pipeline:

- **Data Cleaning (Wrangling Part I)**
- **Feature Engineering (Wrangling Part II)**
- **Modeling (Foundations + Evaluation)**
- **Visualization / Dashboard**

The goal is to build a reproducible, end-to-end pipeline from raw administrative data to interpretable modeling results.
The goal is to build a clean, reproducible pipeline from raw administrative data to structured economic analysis.

---

## **Research Question**

**Do states systematically pay different reimbursement prices for the same drug, and do those differences persist over time?**

To answer this, the project calculates **price per prescription** and evaluates cross-state and quarterly variation.

---

## **Data Source**

- **Dataset:** State Drug Utilization Data (2025)  
- **Publisher:** Centers for Medicare & Medicaid Services (CMS)  
- **Accessed via:** Data.gov  
- **License:** Public Domain  

Source: https://healthdata.gov/CMS/State-Drug-Utilization-Data-2024/atef-9yh4/about_data

The dataset contains **state-level quarterly Medicaid reimbursement records**, including prescription counts and reimbursement totals.

---

## **Database Design**

Database Google Drive Link: https://drive.google.com/file/d/1D5Cmnq3bE4PUHxkN5pDmSrNs9Wnfalho/view?usp=drive_link
(You can directly download the database here)

The SQLite database is named **`medicaid_drugs.db`** and contains two relational tables.

### **Table 1: drug (Reference Table)**

**Primary Key:** `ndc`

Columns:
- `ndc`
- `labeler_code`
- `product_code`
- `package_size`
- `product_name`

This table stores **static drug identity information**.

---

### **Table 2: utilization (Fact Table)**

**Primary Key:** `utilization_id`  
**Foreign Key:** `ndc → drug.ndc`

Columns:
- `utilization_id`
- `ndc`
- `utilization_type`
- `state`
- `year`
- `quarter`
- `suppression_used`
- `units_reimbursed`
- `number_of_prescriptions`
- `total_amount_reimbursed`
- `medicaid_amount_reimbursed`
- `non_medicaid_amount_reimbursed`

This table stores **state-level quarterly utilization and reimbursement outcomes**.

The relationship between tables is **one-to-many**, where each drug can appear in multiple state-quarter records.

---

## **Repository Structure**
```
Project/
│
├── data/
│ └── medicaid_data.csv
│
├── database/
│ └── medicaid_drugs.db
│
├── diary/
│ ├── problem_formulation.txt
│ ├── data_acquisition.txt
│ ├── data_acquisition_database.txt
│ ├── data_exploration.txt
   ├── DataWrangling.txt
│  ├── DataWrangling2.txt
│  ├── DataModelling.txt
│  ├── DataModelling2.txt
│  ├── DataVisualisation.txt
│ └── reflection_future_work.txt
│
├── notebooks/
│ ├── 01_problem_formulation.ipynb
│ ├── 02_data_acquisition.ipynb
│ ├── 03_database_schema.ipynb
│ ├── 04_data_exploration.ipynb
│ ├── 05_data_wrangling.ipynb 
│ ├── 06_new_data_wrangling.ipynb
│ ├── 07_app.py

├── schema.png
├── data_dictionary.pdf
├── requirements.txt
└── README.md


```

## **How to Reproduce the Project**

### **1. Clone the Repository**
```
git clone <repository-url>
cd <repository-folder>
```

### **2. Create and Activate Environment**

if using conda
```
conda create -n dataScience_MedProject python=3.11
conda activate dataScience_MedProject
```
if using venv
```
python -m venv venv
source venv/bin/activate

```

### **3. Install Dependencies**
```
pip install -r requirements.txt

```

### **4. For creating database**
Open and run:
database.ipynb



### **5. Run Data Exploration**
Open and run:
main.ipynb

### **6. Run Data Wrangling**
Open and run:
data_wrangling.ipynb

### **7. Run Data Modeling**
Open and run:
data_modelling.ipynb


### **8. Run Data Visualisation**
Open and run:
app.py




## **Technical Stack**

Python 3.11

pandas

numpy

matplotlib

seaborn

SQLite3

LightGBM

streamlit
## **Author**

Maitrey Phatak
Master’s Student – Applied Data Science




















