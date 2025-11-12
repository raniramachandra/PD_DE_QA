#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[22]:


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame.
    
    Args:
    - file_path: Path to the CSV file.
    
    Returns:
    - A DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"File '{file_path}' loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading file '{file_path}': {e}")
        return None

# Example usage:
# file_path = 'path_to_file.csv'
# df = load_csv(file_path)


# In[23]:


file_path = '03_Library Systembook.csv'
df = load_csv(file_path)

if df is not None:
    print(df.head())  # Display the first few rows of the loaded CSV


# In[24]:


file_path2 = '03_Library SystemCustomers.csv'
df2 = load_csv(file_path2)

if df2 is not None:
    print(df2.head())  # Display the first few rows of the loaded CSV


# In[33]:


def drop_na_and_log(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Drops rows with NaN values in a specific column, logs the number of rows dropped and the total number of records, 
    and returns a log DataFrame for auditing.
    
    Args:
    - data: The DataFrame to clean.
    - column_name: The column name to check for NaN values.
    
    Returns:
    - A tuple containing the cleaned DataFrame and a DataFrame containing the audit log of dropped records.
    """
    # Record the number of rows before dropping NaN
    initial_row_count = len(data)
    
    # Drop rows where the specified column has NaN values
    data_cleaned = data.dropna(subset=[column_name])
    
    # Record the number of rows after dropping NaN
    final_row_count = len(data_cleaned)
    
    # Log the number of records dropped and total records before and after
    dropped_records = initial_row_count - final_row_count
    log_data = {
        'Column Name': [column_name],
        'Records Before Drop': [initial_row_count],
        'Records Dropped': [dropped_records],
        'Records After Drop': [final_row_count]
    }
    
    # Create the log DataFrame
    log_df = pd.DataFrame(log_data)
    
    return data_cleaned, log_df

# Example usage:
# Assuming 'Book checkout' is the column where you want to drop NaN values
# cleaned_data, audit_log = drop_na_and_log(cleaned_data, 'Book checkout')

# Print cleaned data and audit log
# print(cleaned_data)
# print(audit_log)


# In[34]:


# Applying the function
cleaned_data_customer, audit_log_customer = drop_na_and_log(df2, 'Customer ID')

# Print cleaned data and audit log
print(cleaned_data_customer)
print(audit_log_customer)


# In[25]:


def clean_and_format_data(data: pd.DataFrame, date_columns: list, string_columns: list, drop_na: bool = True) -> pd.DataFrame:
    """
    Cleans and formats the dataset by:
    - Stripping unwanted characters from string columns.
    - Converting specified columns to datetime format.
    - Optionally dropping rows with NaN values.

    Args:
    - data: The DataFrame to clean.
    - date_columns: List of column names to convert to datetime.
    - string_columns: List of column names to clean (remove unwanted characters).
    - drop_na: Whether to drop rows with NaN values (default is True).

    Returns:
    - A cleaned and formatted DataFrame.
    """
    # Clean string columns by removing unwanted characters (like quotes)
    for column in string_columns:
        data[column] = data[column].str.replace('"', "", regex=True)
    
    # Convert specified columns to datetime format
    for column in date_columns:
        data[column] = pd.to_datetime(data[column], errors='coerce')  # Use 'coerce' to handle invalid formats

    # Drop rows with NaN values if specified
    if drop_na:
        data = data.dropna()

    return data

# Example usage:
# Assuming 'Book checkout' and 'Book Returned' are the columns to clean and format
# data = pd.DataFrame({
#     'Book checkout': ['"2023-01-01"', '"2023-02-01"', None],
#     'Book Returned': ['"2023-01-10"', '"2023-02-15"', '"Invalid Date"']
# })

# Clean and format the data
cleaned_data = clean_and_format_data(df, date_columns=['Book checkout', 'Book Returned'], string_columns=['Book checkout', 'Book Returned'])

print(cleaned_data)


# In[26]:


def calculate_day_diff(data: pd.DataFrame, checkout_column: str, return_column: str) -> pd.DataFrame:
    """
    Calculates the number of days between two date columns and adds a new column 'day_diff'.
    
    Args:
    - data: The DataFrame containing the date columns.
    - checkout_column: The name of the 'Book checkout' column.
    - return_column: The name of the 'Book Returned' column.
    
    Returns:
    - The DataFrame with a new column 'day_diff' showing the number of days between the two dates.
    """
    # Calculate the difference in days between the two date columns
    data['day_diff'] = (data[return_column] - data[checkout_column]).dt.days
    
    return data


# In[28]:


# Assuming 'Book checkout' and 'Book Returned' are the columns in the DataFrame
cleaned_data = calculate_day_diff(cleaned_data, 'Book checkout', 'Book Returned')

print(cleaned_data)


# LOADING SQL server

# In[ ]:


#!pip install pandas sqlalchemy pyodbc


# In[ ]:


# Checking the ODBC Driver for SQL Server
# import pyodbc

# # List all ODBC drivers installed on the system
# drivers = [driver for driver in pyodbc.drivers()]
# print("ODBC Drivers available:")
# for driver in drivers:
#     print(driver)


# In[ ]:


# from sqlalchemy import create_engine

# # Define the connection string to your MS SQL Server
# server = 'localhost'  
# database = 'QAETLStagingDB'
# username = 'python_app'
# password = 'password'

# # Create the connection string with Windows Authentication
# connection_string = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'


# # Create the SQLAlchemy engine
# engine = create_engine(connection_string)


# In[ ]:


# # Write the DataFrame to SQL Server
# cleaned_data.to_sql('book_library', con=engine, if_exists='replace', index=False)
# cleaned_data_customer.to_sql('customer_library', con=engine, if_exists='replace', index=False)
# audit_log_customer.to_sql('audit_log_customer', con=engine, if_exists='replace', index=False)


# CONVERTING to .PY file

# In[ ]:


# Open your terminal (either in VS Code or elsewhere).

# Run the following command to convert your notebook to a .py file:

# jupyter nbconvert --to script your_notebook.ipynb


# This will generate a Python script (your_notebook.py) in the same folder as the .ipynb file, containing only the code cells.

