import os
import csv
from validation import *

def validate_data(file_path):
    """
    Preliminary data handling and validation:
        1. Open file using the with keyword, ensuring that it is also closed correctly.
        2. Read the rows:
            - Filter out rows with no valid data.
            - Check if there is a row_id in the data and if not, use the row_number as row_id. Ensure that rows that are filtered out are also counted when calculating row_numbers, so that the row_numbers passed on as row_id's match the actual row number in the data file.
        3. Invoke the validate_row function.
    """
    
    try:
        with open(file_path) as file:
            reader = csv.DictReader(file)
            row_number = 2
            for row in reader:
                if all(value == '' for value in row.values()):
                    row_number += 1
                    continue
                
                row_id = row.get("row_id", row_number)
                validate_row(row, row_id, validation_functions, patterns)
                row_number += 1
    except Exception as e:
        print(f"An error occured while processing the file: {str(e)}")
    finally:
        print()
        print("Finished validating all fields in all rows.")

def validate_row(row, row_id, validation_functions, patterns):
    """
    Validate all fields in each row:
        1. Use the field names fetched from the data heading to look up and call the appropriate validation functions, passing the corresponding validation patterns.
        2. If no appropriate validation function is found due to data anomalies, print a message pointing to the row, field name and field value in question.
    """
    
    for field_name, field_value in row.items():
        if field_name == "row_id":
            continue
        validation_function = validation_functions.get(field_name)
        if validation_function:
            pattern = patterns.get(field_name)
            if pattern:
                validation_function(field_value, row_id, pattern)
            else:
                validation_function(field_value, row_id)
        else:
            print(f"No appropriate validation function was found. No validation will be performed for the data entry: {field_name}: {field_value}, in row {row_id}")

def check_file_permissions(file_path):
    """
    Permission check:
        1. Check if the file exist; if not, raise an exception.
        2. Check if there are read, write and execute permissions for the data file.
        3. Print the permissions status.
        4. If read permissions are granted, call the validate_data function; if not, print a message.
    """
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}. Check the provided file path.")
        
        if os.access(file_path, os.R_OK):
            print(f"Read permissions granted for the file: {file_path}.")
        
            if os.access(file_path, os.W_OK):
                print(f"Write permissions granted for the file: {file_path}.")
            else:
                print(f"Write permissions not granted for the file: {file_path}.")
            
            if os.access(file_path, os.X_OK):
                print(f"Execute permissions granted for the file: {file_path}.")
            else:
                print(f"Execute permissions not granted for the file: {file_path}.")
            
            print()
            print("Data validation is now in progress.")
            print()
            validate_data(file_path)
            
        else:
            print(f"Read permissions not granted for the file: {file_path}.")
            print()
            print("Data validation cannot be performed without read permissions.")
            
    except FileNotFoundError as e:
        print(str(e))

check_file_permissions("test_data_1.csv")