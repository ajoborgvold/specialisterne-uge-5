import re
from email_validator import validate_email, EmailNotValidError
import phonenumbers

def check_id_validity(customer_id, row_id, pattern):
    if customer_id is None:
        print(f"Anomaly detected in row: {row_id}. Customer id is missing.")
        return
    
    try:
        if not (re.match(pattern, customer_id)):
            raise ValueError(f"Invalid customer id format: {customer_id}. Customer id must be exactly 4 digits.")
    except ValueError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_name_validity(name, row_id, pattern):
    if name is None:
        print(f"Anomaly detected in row: {row_id}. Name is missing.")
        return
    
    try:
        if not (re.match(pattern, name)):
            raise ValueError(f"Invalid name format: {name}. Name can only contain alphabetical characters and must consist of at least 1 first and 1 last name.")
    except ValueError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_email_validity(email, row_id):
    """Use the email_validator package to check if the email address is valid. The check_deliverability is set to false to allow email addresses with a fake domain, e.g. 'example.com'."""
    
    if email is None:
        print(f"Anomaly detected in row: {row_id}. Email is missing.")
        return
    
    try:
        validate_email(email, check_deliverability=False)
    except EmailNotValidError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_amount_validity(amount, row_id, pattern):
    if amount is None:
        print(f"Anomaly detected in row: {row_id}. Purchase amount is missing.")
        return

    try:
        if not (re.match(pattern, amount)):
            raise ValueError(f"Invalid amount format: {amount}. Amount must consist of 1 or more digits followed by a dot as the decimal point and exactly 2 decimal places.")
    except ValueError as e:
        print(f"Anomaly detected in row: {row_id}. {str(e)}")

def check_phone_number_validity(phone_number, row_id):
    """
    Use the phonenumber package to check if the phone number is valid.
    - The is_valid_number is used to run a full validation of length, prefix and region.
    - To improve speed, is_valid_number can be replaced with is_possible_number. This method checks the length only and makes a guess on the numbers validity. Thus, it is faster but also less accurate.
    """
    
    if phone_number is None:
        print(f"Anomaly detected in row: {row_id}. Phone number is missing.")
        return
    
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValueError(f"Invalid phone number format: {phone_number}")
    except (phonenumbers.phonenumberutil.NumberParseException, ValueError) as e:
        print(f"Anomaly detected in row: {row_id}. Error parsing phone number: {str(e)}")

patterns = {
    "customer_id": r'^\d{4}$', # Exactly 4 digits
    "name": r'^[A-Za-z]+(\s[A-Za-z]+)+$', # Only alphabetical characters; at least 1 first and 1 last name; optional middle name(s)
    "purchase_amount": r'^\d+\.\d{2}$' # One or more digits; dot as decimal point; exactly two decimal places (digits)
}

validation_functions = {
    "customer_id": check_id_validity,
    "name": check_name_validity,
    "email": check_email_validity,
    "purchase_amount": check_amount_validity,
    "phone_number": check_phone_number_validity,
}