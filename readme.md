**Note on Data Availability**:  
Due to the proprietary nature of the datasets used in this project, I am unable to share the raw data publicly. I appreciate your understanding.

### Data Preparation and Analysis

**Project Overview**:  
In this project, I prepared and transformed data to facilitate analysis. My objectives included cleaning data, selecting features, and performing data transformations to create a dataset suitable for analysis.

**Implementation Details**:  
**Files**:  
- `data/processed/beetloader_processed.csv` - A dataset I curated from raw data sources.  
- `src/transform_raw_data_beetloader.py (--input raw_data_beetloader.csv)` - A Python script I developed to transform the raw data.

**Project Description**:  
The transformed dataset includes features necessary for analysis, with attributes to provide insights. I designed the features to be modifiable. For example, the script allows for toggling the inclusion or exclusion of records with missing values (lines 96 and 98), depending on analytical needs.

---

### Data Exploration and Comparative Analysis

**Project Overview**:  
I conducted an exploratory data analysis (EDA) to uncover insights from the `beetloader_processed.csv` and `trucks.csv` datasets. I compared these datasets to assess their compatibility and the potential for integrated analysis.

**Implementation Details**:  
**File**:  
- `notebooks/eda v1.ipynb` - Details the EDA process I executed.

**Project Description**:  
The EDA was crucial for understanding the datasets and preparing them for further comparative studies. I outlined the main steps in the EDA process in this notebook.

---

### Comparative Analysis and Model Evaluation

**Project Overview**:  
This part of my project involved comparing two datasets: the beet loader and trucks datasets. I developed a methodology to combine and analyze them, evaluating the potential for creating a unified model.

**Implementation Details**:  
**File**:  
- `notebooks/model_evaluation.ipynb`

**Project Description**:  
I assessed the latest version of the model against the trucks dataset. The notebook is structured to facilitate conversion into a Python script for broader use.

---

### Stakeholder Presentation - Model Evaluation and Next Steps

**Project Overview**:  
I presented my findings to a group of peers and advisors, simulating a stakeholder presentation to discuss the potential of rolling out the proof of concept (PoC) company-wide and the necessary steps based on the model's performance.

**Implementation Details**:  
**Files**:  
- `conclusions/conclusions.ipynb` - Analysis and conclusions drawn from the raw data.  
- `conclusions/model_evaluation.csv` - Contains comparison results between the model and the trucks dataset data.

**Project Description**:  
Based on specific analytical assumptions, I formulated conclusions regarding the model's effectiveness. These were supplemented by additional considerations and proposed next steps for potential real-world application.
