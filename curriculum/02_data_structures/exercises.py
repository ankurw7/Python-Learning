"""
Module: 02_data_structures
Topic: Exercises
Description: Practice problems for lists, dictionaries, and sets.
"""

def exercise_filter_long_strings(strings: list[str], min_length: int) -> list[str]:
    """
    TODO: Implement this function.
    
    Return a new list containing only the strings from the input list
    that have a length greater than or equal to min_length.
    
    Args:
        strings (list[str]): List of strings to filter.
        min_length (int): Minimum length required.
        
    Returns:
        list[str]: Filtered list.
    """
    return [s for s in strings if len(s) >= min_length]


def exercise_count_word_frequencies(words: list[str]) -> dict[str, int]:
    """
    TODO: Implement this function.
    
    Count the frequency of each word in the input list.
    
    Args:
        words (list[str]): List of words.
        
    Returns:
        dict[str, int]: Dictionary where keys are words and values are counts.
    """
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def exercise_unique_elements_sorted(numbers: list[int]) -> list[int]:
    """
    TODO: Implement this function.
    
    Return a sorted list of unique elements from the input list.
    Hint: Use a set to get unique elements, then sort.
    
    Args:
        numbers (list[int]): List of numbers (potentially with duplicates).
        
    Returns:
        list[int]: Sorted list of unique numbers.
    """
    return sorted(set(numbers))
