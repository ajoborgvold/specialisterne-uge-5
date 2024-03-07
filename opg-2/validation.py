import re
from email_validator import validate_email, EmailNotValidError
import phonenumbers

#======================#
# Validation functions
#======================#
def check_id_validity(customer_id, row_id, pattern):
    """Use a regular expression to check that the customer id consists of exactly 4 digits."""
    
    if customer_id is None:
        print(f"Anomaly detected in row: {row_id}. Customer id is missing.")
        return
    
    try:
        if not (re.match(pattern, customer_id)):
            raise ValueError(f"Invalid customer id format: {customer_id}.")
    except ValueError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_name_validity(name, row_id, pattern):
    """Use a regular expression to check that the name contains only alphabetic characters and that it consists of at least two parts, representing a first and a last name with optional middle name(s)."""
    
    if name is None:
        print(f"Anomaly detected in row: {row_id}. Name is missing.")
        return
    
    try:
        if not (re.match(pattern, name)):
            raise ValueError(f"Invalid name format: {name}.")
    except ValueError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_email_validity(email, row_id):
    """Use the email_validator package to check if the email is valid. The check_deliverability is set to false to allow email addresses with the domain 'example.com'."""
    
    if email is None:
        print(f"Anomaly detected in row: {row_id}. Email is missing.")
        return
    
    try:
        validate_email(email, check_deliverability=False)
    except EmailNotValidError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_amount_validity(amount, row_id, pattern):
    """Use a regular expression to check that the amount consists of one or more digits followed by a dot and two decimal places."""
    
    if amount is None:
        print(f"Anomaly detected in row: {row_id}. Purchase amount is missing.")
        return

    try:
        if not (re.match(pattern, amount)):
            raise ValueError(f"Invalid amount format: {amount}.")
    except ValueError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_phone_number_validity(phone_number, row_id):
    if phone_number is None:
        print(f"Anomaly detected in row: {row_id}. Phone number is missing.")
        return
    
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_possible_number(parsed_number):
            raise ValueError(f"Invalid phone number format: {phone_number}")
    except (phonenumbers.phonenumberutil.NumberParseException, ValueError) as e:
        print(f"Anomaly detected in row: {row_id}. Error parsing phone number: {str(e)}")


#==========================#
# Dictionaries:
# a. data patterns
# b. validation functions
#==========================#
patterns = {
    "customer_id": r'^\d{4}$',
    "name": r'^[A-Za-z]+(\s[A-Za-z]+)+$',
    "purchase_amount": r'^\d+\.\d{2}$'
}

validation_functions = {
    "customer_id": check_id_validity,
    "name": check_name_validity,
    "email": check_email_validity,
    "purchase_amount": check_amount_validity,
    "phone_number": check_phone_number_validity,
}