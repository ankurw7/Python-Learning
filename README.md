# Python Learning Program for AI Use

This project is designed to be a structured resource for learning Python, optimized for AI interaction and usage.

## Structure

The project is organized into modules covering different aspects of Python programming, from basics to advanced AI-related topics.

- **01_basics**: Variables, Data Types, Conditionals, Loops.
- **02_data_structures**: Lists, Dictionaries, Sets, Tuples, Comprehensions.
- **03_ai_concepts**: Vectors, Dot Product, MSE, Tokenization (Pure Python).
- **04_file_handling_exceptions**: Reading/Writing Files, JSON processing, Exception Handling.


## Usage

Each module contains:
1. `lesson_info.json`: Metadata about the module.
2. `examples.py`: Clear, documented examples of concepts.
3. `exercises.py`: Problems to solve (look for `TODO` comments).
4. `tests.py`: Unit tests to verify solutions.

### Running Examples
```bash
python curriculum/01_basics/examples.py
```

### Running Tests
To check your progress on exercises:
```bash
python curriculum/01_basics/tests.py
```

## Teacher Agent

You can use the interactive Teacher Agent to navigate the curriculum:

```bash
python teacher.py
```
This script will scan the modules and guide you through learning (examples) and verification (tests).

## Goal

To provide a comprehensive, machine-readable, and verifiable Python learning path.
