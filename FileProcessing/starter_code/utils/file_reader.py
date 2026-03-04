from starter_code.expections import FileProcessingError, InvalidDataError, MissingFieldError

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    records = []

    try:
        with open(f"{filepath}", "r") as f:
            for i, line in enumerate(f):
                if i == 0:
                    continue # we would need to do 
    # something here to read the column names from the first line
            entry = line.split(",")[:-1]
            records.append({
                "date": entry[0],
                "store_id": entry[1],
                "quantity": entry[2],
                "price": entry[3],
            })
    except FileNotFoundError:
        raise FileProcessingError("File does not exist")
    except Exception as e:
        raise FileProcessingError(f"Something went wrong: {e}")

    return records