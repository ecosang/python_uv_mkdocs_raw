# Python UV MkDocs Raw

A demo Python package showcasing API documentation generation using MkDocs and mkdocstrings.

## Overview

This package provides utility functions and arithmetic calculations with comprehensive documentation. It serves as an example of how to generate beautiful API documentation from Python docstrings using MkDocs.

## Quick Start

### Installation

```bash
# Using uv (recommended)
uv add https://github.com/ecosang/python_uv_mkdocs_raw.git

# Or using pip
pip install python-uv-mkdocs-raw
```

### Basic Usage

```python
from demoprogram import utility, calc

# Utility functions
text = "Hello, World!"
reversed_text = utility.reverse_string(text)
word_count = utility.count_words(text)
is_palindrome = utility.is_palindrome("racecar")

# Arithmetic functions
result = calc.add(5, 3)
power_result = calc.power(2, 8)
factorial_result = calc.factorial(5)
```

## Features

### Utility Functions (`demoprogram.utility`)

- **String manipulation**: Reverse strings, check palindromes, count words
- **File operations**: Get file sizes, format bytes
- **System information**: Get platform and Python version info

### Arithmetic Functions (`demoprogram.calc`)

- **Basic arithmetic**: Addition, subtraction, multiplication, division
- **Advanced math**: Power, square root, factorial
- **Number theory**: GCD, LCM
- **Statistics**: Average, percentage calculations
- **Utilities**: Rounding to decimal places

## Documentation

This documentation is automatically generated from the source code docstrings using:

- **MkDocs**: Static site generator
- **Material for MkDocs**: Beautiful theme
- **mkdocstrings**: Python docstring parser
- **mkdocstrings-python**: Python handler for mkdocstrings

## Development

### Building Documentation Locally

```bash
# Install development dependencies
uv sync --group dev

# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

### Project Structure

```
python_uv_mkdocs_raw/
├── demoprogram/
│   ├── __init__.py
│   ├── utility.py      # Utility functions
│   └── calc.py         # Arithmetic functions
├── docs/
│   ├── index.md        # This file
│   ├── examples.md     # Usage examples
│   └── api/            # Auto-generated API docs
├── mkdocs.yml          # MkDocs configuration
└── pyproject.toml      # Project configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add or update docstrings
5. Test the documentation build
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 