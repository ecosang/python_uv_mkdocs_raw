# Python UV MkDocs Raw

A demo Python package showcasing API documentation generation using MkDocs and mkdocstrings.

## Features

- **Utility Functions**: String manipulation, file operations, system information
- **Arithmetic Functions**: Basic and advanced mathematical operations
- **Comprehensive Documentation**: Auto-generated from docstrings using MkDocs
- **Modern UI**: Beautiful documentation with Material for MkDocs theme

## Quick Start

### Installation

```bash
# Using uv (recommended)
uv add python-uv-mkdocs-raw

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

## Documentation

📖 **Live Documentation**: [https://ecosang.github.io/python_uv_mkdocs_raw/](https://ecosang.github.io/python_uv_mkdocs_raw/)

The documentation is automatically generated from the source code docstrings and includes:

- **API Reference**: Complete function documentation with parameters, return types, and examples
- **Examples**: Practical usage examples and real-world scenarios
- **Interactive Features**: Search, dark/light mode, code copying

### Building Documentation Locally

```bash
# Install development dependencies
uv sync --group dev

# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Project Structure

```
python_uv_mkdocs_raw/
├── demoprogram/
│   ├── __init__.py
│   ├── utility.py      # Utility functions
│   └── calc.py         # Arithmetic functions
├── docs/
│   ├── index.md        # Main documentation
│   ├── examples.md     # Usage examples
│   ├── api/            # Auto-generated API docs
│   └── stylesheets/    # Custom CSS
├── mkdocs.yml          # MkDocs configuration
├── .github/workflows/  # GitHub Actions for deployment
└── pyproject.toml      # Project configuration
```

## Available Functions

### Utility Functions (`demoprogram.utility`)

- `reverse_string(text)`: Reverse a string
- `is_palindrome(text)`: Check if a string is a palindrome
- `count_words(text)`: Count words in a string
- `get_file_size(file_path)`: Get file size in bytes
- `format_bytes(bytes_size)`: Format bytes to human-readable format
- `get_system_info()`: Get system information

### Arithmetic Functions (`demoprogram.calc`)

- **Basic**: `add()`, `subtract()`, `multiply()`, `divide()`, `power()`
- **Advanced**: `square_root()`, `factorial()`, `gcd()`, `lcm()`
- **Statistics**: `average()`, `percentage()`
- **Utilities**: `round_to_decimal()`

## Development

### Prerequisites

- Python 3.10+
- uv (recommended) or pip

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/ecosang/python_uv_mkdocs_raw.git
cd python_uv_mkdocs_raw

# Install dependencies
uv sync --group dev

# Run tests (if available)
python -m pytest

# Build documentation
mkdocs build
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add or update docstrings following Google style
5. Test the documentation build: `mkdocs build`
6. Submit a pull request

## Documentation Stack

This project uses the following tools for documentation:

- **[MkDocs](https://www.mkdocs.org/)**: Static site generator
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)**: Beautiful theme
- **[mkdocstrings](https://mkdocstrings.github.io/)**: Python docstring parser
- **[mkdocstrings-python](https://mkdocstrings.github.io/python/)**: Python handler

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## GitHub Pages

The documentation is automatically deployed to GitHub Pages when changes are pushed to the main branch. The site is available at:

**https://ecosang.github.io/python_uv_mkdocs_raw/**

The deployment is handled by GitHub Actions (see `.github/workflows/docs.yml`).