this is read me file


# **Power BI Data Engineering – QAETLStagingDB Project**

## 🗂️ Overview

This project demonstrates the end-to-end data engineering flow for managing book and customer datasets.
It uses **Python**, **GitLab version control**, **SQL Server (QAETLStagingDB)**, and **Power BI** for data visualization.

---

## ⚙️ Data Flow Summary

### 1. **Source Data**

* **Raw CSV files:**

  * `customer.csv`
  * `books.csv`
* All files are version-controlled under the folder:

  ```
  PD_DE_QA/
  ```

---

### 2. **Data Loading & Cleaning (Python)**

Python scripts handle:

* Reading raw CSV files.
* Cleaning operations:

  * Removing rows with missing (`NaN`) values.
  * Removing unwanted characters (e.g., quotes `" "`).
* Data enrichment:

  * Calculating **Total Days Borrowed** between `Book checkout` and `Book Returned` columns.

**Key Functionality:**

* Each load generates a **log DataFrame** capturing:

  * Total records before cleaning
  * Records dropped due to missing values
  * Records after cleaning

---

### 3. **Audit & Logging**

Audit logs are maintained to ensure data quality:

* **Initial Load Log** → records row counts at first ingestion.
* **Post-Cleaning Log** → captures row counts after cleaning and transformation.

All logs are stored in SQL tables such as:

```
dbo.audit_log_book
dbo.audit_log_customer
```

---

### 4. **Data Storage (SQL Server)**

Cleaned and enriched datasets are loaded into **SQL Server (QAETLStagingDB)** under staging tables:

```
dbo.book_library
dbo.customer_library
```

---

### 5. **Visualization (Power BI)**

Power BI connects to:

```
Server: localhost
Database: QAETLStagingDB
```

**Reports include:**

* Data load summary and quality metrics (records before/after cleaning).
* Book borrowing analysis (e.g., average days borrowed, active customers).
* Audit dashboards showing ETL success and failure counts.

---

## 🧰 Technologies Used

| Component                       | Purpose                                       |
| ------------------------------- | --------------------------------------------- |
| **Python (pandas)**             | Data loading, cleaning, enrichment            |
| **SQL Server (QAETLStagingDB)** | Staging database for cleaned data             |
| **GitLab**                      | Version control for all scripts and CSV files |
| **Power BI**                    | Visualization and ETL monitoring              |

---

## ✅ Example Workflow

1. **Python Script Run**

   * Loads raw CSVs from `PD_DE_QA/`
   * Cleans data → removes `NaN` values
   * Computes `Days Taken = Book Returned – Book checkout`
   * Generates audit log

2. **Load to SQL Server**

   * Data and logs are inserted into `QAETLStagingDB` tables

3. **Power BI Dashboard**

   * Connects to SQL Server (`localhost`)
   * Displays summary of:

     * Rows loaded
     * Rows dropped
     * Total records processed

---

Further ref :
https://github.com/jamurkin/DE5-M5
https://github.com/niroshsuthagar-QA/DE5-M5-20251110
https://realpython.com/python-classes/


