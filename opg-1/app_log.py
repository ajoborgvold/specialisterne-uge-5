import os

def create_log_detail_files(file_path, keywords):
    """Create new separate files for each selected log keyword and place the files in a log_details folder in the current directory."""
    
    try:
        current_directory = os.getcwd()
        log_details_path = os.path.join(current_directory, "log_details")
        os.makedirs(log_details_path, exist_ok=True)

        file_handles = {keyword: open(os.path.join(log_details_path, f"{keyword.lower()}.txt"), "a") for keyword in keywords}

        with open(file_path) as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word in keywords:
                        file_handles[word].write(line)
                        break

        for file_handle in file_handles.values():
            file_handle.close()
            
        print(f"Created {len(keywords)} log file(s) for your selected keyword(s) {keywords} and placed the file(s) in the log_details folder in the current directory.")
    # except FileNotFoundError:
    #     print(f"Error: The log file {file_path} was not found.")
    except Exception as e:
        print(f"An error occured: {str(e)}")

def get_log_search_keywords(file_path):
    """
    Let the user select one or more keywords from the keywords_dict. Search for the keywords in the log file and pass the selected keywords to the create_log_detail_files function.
    """
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}. Check the provided file path.")
        
        keywords_dict = {"e": "ERROR", "w": "WARNING", "i": "INFO", "s": "SUCCESS"}
        is_add_new_keyword_on = True
        keywords_list = []

        while is_add_new_keyword_on:
            print("Select a keyword to search for in the log file.")
            keyword_input = input("Press e for 'error', w for 'warning', i for 'info' or s for 'success'\n").strip().lower()
            if keyword_input in keywords_dict:
                keywords_list.append(keywords_dict[keyword_input])
            else:
                print("Invalid keyword input. Please try again.")
                continue
            
            print("Your selected keywords:", keywords_list)

            if len(keywords_list):
                add_new_keyword = input("Would like to add another keyword? Press y for 'yes', n for 'no'\n").strip().lower()
                if add_new_keyword.lower() == "y":
                    is_add_new_keyword_on = True
                elif add_new_keyword.lower() == "n":
                    is_add_new_keyword_on = False
                else:
                    print("Invalid input. Exiting loop.")
                    break
        
        create_log_detail_files(file_path, keywords_list)
    except FileNotFoundError as e:
        print(str(e))

get_log_search_keywords("app_log.txt")