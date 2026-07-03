import json

# ────────────────────────────────────────────────────────────────────────
# EXERCISE 1: Read and count
# ────────────────────────────────────────────────────────────────────────
def count_lines_in_file(filepath: str) -> int:
    """
    Given a filepath, open the file, read its contents, and return
    the number of lines in it.
    
    If the file does not exist, you must catch the FileNotFoundError
    and return -1.
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement count_lines_in_file")

# ────────────────────────────────────────────────────────────────────────
# EXERCISE 2: Safe Division
# ────────────────────────────────────────────────────────────────────────
def safe_divide(a: float, b: float):
    """
    Divide 'a' by 'b' and return the result.
    
    If 'b' is 0, catch the ZeroDivisionError and return the string:
    "Cannot divide by zero"
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement safe_divide")

# ────────────────────────────────────────────────────────────────────────
# EXERCISE 3: JSON Export
# ────────────────────────────────────────────────────────────────────────
def save_dict_to_json(data: dict, filepath: str) -> bool:
    """
    Save the given dictionary 'data' to the specified 'filepath' as a JSON file.
    Use the 'json' module.
    
    Return True if successful.
    """
    # TODO: Implement this function
    raise NotImplementedError("TODO: Implement save_dict_to_json")
