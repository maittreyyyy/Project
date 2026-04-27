# Medicaid Drug Reimbursement Analysis  
**CAP5771 – Milestone 1, Milestone 2 & Milestone 3**

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

Milestone 3 focuses on deployment and reproducibility:

- **Model saving and serialization**
- **Independent model testing**
- **Reproducibility across notebooks**
- **Deployment workflow validation**

The goal is to build a reproducible, end-to-end pipeline from raw administrative data to interpretable modeling results and deployment-ready decision support.

---

## **Research Question**

**Do states systematically pay different reimbursement prices for the same drug, and do those differences persist over time?**

To answer this, the project calculates **cost per unit reimbursement** and evaluates cross-state and quarterly variation.

The final business-facing question becomes:

**If I select a drug, a state, and the next quarter, what cost per unit reimbursement should I expect?**

---

## **Data Source**

- **Dataset:** State Drug Utilization Data (2025)  
- **Publisher:** Centers for Medicare & Medicaid Services (CMS)  
- **Accessed via:** Data.gov  
- **License:** Public Domain  

Source:  
https://healthdata.gov/CMS/State-Drug-Utilization-Data-2024/atef-9yh4/about_data

The dataset contains **state-level quarterly Medicaid reimbursement records**, including prescription counts, reimbursement totals, utilization behavior, and payment variation across time.

---

## **Database Design**

Database Google Drive Link:  
https://drive.google.com/file/d/1D5Cmnq3bE4PUHxkN5pDmSrNs9Wnfalho/view?usp=drive_link

(You can directly download the database here)

The SQLite database is named **`medicaid_drugs.db`** and contains two relational tables.

---

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

## **Feature Engineering**

Several domain-driven features were created to improve predictive modeling:

- `cost_per_unit`
- `units_per_prescription`
- `FDA_ProductID`
- `Therapeutic_Class`
- `EPC_Class`
- `MoA_Class`
- `ROUTENAME`
- `LABELERNAME`
- `MARKETINGCATEGORYNAME`
- `is_expansion_state`

These features help capture reimbursement intensity, utilization behavior, therapeutic grouping, manufacturer influence, and Medicaid expansion policy differences across states.

---

## **Modeling**

This project is treated as a **regression problem** because the goal is to predict a continuous value:

```python
cost_per_unit = medicaid_amount_reimbursed / units_reimbursed
```

## **Models Compared**

- **Linear Regression** *(baseline model)*
- **XGBoost**
- **LightGBM** *(final selected model)*

---

## **Final Model**

The final deployed model is:

```txt
LightGBM Regressor
```

## **Models Compared**

- **Linear Regression** — baseline model  
- **XGBoost** — comparison model  
- **LightGBM** — final selected model  

---

## **Final Model**

The final deployed model is:

### **LightGBM Regressor**

It was trained using:

- **log transformation on target**
- **categorical feature handling**
- **outlier trimming**
- **train / test split**
- **feature selection based on domain relevance**

---

## **Final Performance**

- **R²:** 0.8562  
- **RMSE:** 46.8734  
- **MAE:** 6.3614  

This showed strong predictive performance and better generalization compared to baseline models.

---

## **Visualization / Dashboard**

A customer-focused interactive dashboard was built using **ipywidgets** and visualization tools.

Instead of a general exploratory dashboard, the final design focused on **decision support**.

### **Main Dashboard Questions**

- Which states show the highest reimbursement pressure?
- Which therapeutic classes drive the highest cost?
- Which manufacturers dominate reimbursement totals?
- What is the expected next-quarter cost per unit for a selected drug?

### **The Dashboard Includes**

- cost distribution analysis  
- reimbursement trends over time  
- state comparison views  
- therapeutic class drivers  
- supplier concentration  
- next-quarter prediction widget using the trained LightGBM model  

---

## **Milestone 3 – Model Deployment**

Milestone 3 focused on making the final model portable, reproducible, and usable outside the original training notebook.

The final LightGBM model was saved using **joblib** as:

```txt
lgbm_medicaid_model.pkl
```
## Repository structure
```
Project/
│
├── data/
│   └── medicaid_data.csv
│
├── database/
│   └── medicaid_drugs.db
│
├── diary/
│   ├── problem_formulation.txt
│   ├── data_acquisition.txt
│   ├── data_exploration.txt
│   ├── DataWrangling.txt
│   ├── DataWrangling2.txt
│   ├── DataModelling.txt
│   ├── DataModelling2.txt
│   ├── DataVisualisation.txt
│   └── Data_Model_Testing.txt
│
├── notebooks/
│   ├── 01_data_acquistion_exploration.ipynb
│   ├── 02_data_modeling_packaging.ipynb
│   ├── 03_database.ipynb
│   ├── 04_data_visualisation.ipynb
│   └── model_testing.py
│
├── lgbm_medicaid_model.pkl
├── df_model.csv
├── schema.png
├── data_dictionary.pdf
├── requirements.txt
└── README.md
```
## **Technical Stack**

- Python 3.11  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- SQLite3  
- scikit-learn  
- LightGBM  
- XGBoost  
- joblib  
- plotly  
- ipywidgets  

---

## **Author**

**Maitrey Phatak**  
Master’s Student – Applied Data Science
