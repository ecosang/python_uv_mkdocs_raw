# Examples

This page provides practical examples of how to use the functions in the `demoprogram` package.

## Utility Functions Examples

### String Manipulation

```python
from demoprogram import utility

# Reverse a string
text = "Hello, World!"
reversed_text = utility.reverse_string(text)
print(reversed_text)  # Output: !dlroW ,olleH

# Check if a string is a palindrome
print(utility.is_palindrome("racecar"))  # Output: True
print(utility.is_palindrome("hello"))    # Output: False
print(utility.is_palindrome("A man a plan a canal Panama"))  # Output: True

# Count words in a string
sentence = "The quick brown fox jumps over the lazy dog"
word_count = utility.count_words(sentence)
print(word_count)  # Output: 9
```

### File Operations

```python
from demoprogram import utility

# Get file size
file_size = utility.get_file_size("example.txt")
if file_size >= 0:
    formatted_size = utility.format_bytes(file_size)
    print(f"File size: {formatted_size}")
else:
    print("Could not get file size")

# Format bytes
sizes = [1024, 1048576, 1073741824]  # 1KB, 1MB, 1GB
for size in sizes:
    print(f"{size} bytes = {utility.format_bytes(size)}")
# Output:
# 1024 bytes = 1.0 KB
# 1048576 bytes = 1.0 MB
# 1073741824 bytes = 1.0 GB
```

### System Information

```python
from demoprogram import utility

# Get system information
sys_info = utility.get_system_info()
print(f"Platform: {sys_info['platform']}")
print(f"Python version: {sys_info['python_version']}")
print(f"Python executable: {sys_info['executable']}")
```

## Arithmetic Functions Examples

### Basic Arithmetic

```python
from demoprogram import calc

# Basic operations
a, b = 10, 3
print(f"{a} + {b} = {calc.add(a, b)}")           # Output: 10 + 3 = 13
print(f"{a} - {b} = {calc.subtract(a, b)}")      # Output: 10 - 3 = 7
print(f"{a} * {b} = {calc.multiply(a, b)}")      # Output: 10 * 3 = 30
print(f"{a} / {b} = {calc.divide(a, b):.2f}")    # Output: 10 / 3 = 3.33
print(f"{a} ^ {b} = {calc.power(a, b)}")         # Output: 10 ^ 3 = 1000
```

### Advanced Mathematics

```python
from demoprogram import calc

# Square root
print(f"√16 = {calc.square_root(16)}")           # Output: √16 = 4.0
print(f"√2 = {calc.square_root(2):.4f}")         # Output: √2 = 1.4142

# Factorial
print(f"5! = {calc.factorial(5)}")               # Output: 5! = 120
print(f"0! = {calc.factorial(0)}")               # Output: 0! = 1

# GCD and LCM
print(f"GCD(48, 18) = {calc.gcd(48, 18)}")      # Output: GCD(48, 18) = 6
print(f"LCM(12, 18) = {calc.lcm(12, 18)}")      # Output: LCM(12, 18) = 36
```

### Statistics and Utilities

```python
from demoprogram import calc

# Average calculation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avg = calc.average(numbers)
print(f"Average of {numbers} = {avg}")           # Output: Average of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] = 5.5

# Percentage calculation
part, total = 25, 100
percentage = calc.percentage(part, total)
print(f"{part} is {percentage * 100:.1f}% of {total}")  # Output: 25 is 25.0% of 100

# Rounding
pi = 3.14159265359
print(f"π rounded to 2 decimals: {calc.round_to_decimal(pi, 2)}")    # Output: π rounded to 2 decimals: 3.14
print(f"π rounded to 4 decimals: {calc.round_to_decimal(pi, 4)}")    # Output: π rounded to 4 decimals: 3.1416
```

## Error Handling Examples

```python
from demoprogram import calc

# Division by zero
try:
    result = calc.divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero

# Square root of negative number
try:
    result = calc.square_root(-4)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot calculate square root of negative number

# Factorial of negative number
try:
    result = calc.factorial(-1)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Factorial is not defined for negative numbers

# Average of empty list
try:
    result = calc.average([])
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot calculate average of empty list
```

## Real-World Example: Grade Calculator

```python
from demoprogram import calc, utility

def calculate_grade_percentage(scores):
    """Calculate the percentage grade from a list of scores."""
    if not scores:
        return 0
    
    total_possible = len(scores) * 100  # Assuming each score is out of 100
    total_earned = sum(scores)
    
    return calc.percentage(total_earned, total_possible) * 100

def format_grade_report(student_name, scores):
    """Format a grade report for a student."""
    if not scores:
        return f"No scores available for {student_name}"
    
    percentage = calculate_grade_percentage(scores)
    average_score = calc.average(scores)
    
    report = f"""
Grade Report for {student_name}
{'=' * 30}
Scores: {scores}
Number of assignments: {len(scores)}
Average score: {calc.round_to_decimal(average_score, 1)}%
Overall percentage: {calc.round_to_decimal(percentage, 1)}%
"""
    return report

# Example usage
student_scores = [85, 92, 78, 95, 88]
report = format_grade_report("Alice", student_scores)
print(report)
```

## Performance Example: Benchmarking

```python
import time
from demoprogram import calc

def benchmark_function(func, *args, iterations=10000):
    """Benchmark a function's performance."""
    start_time = time.time()
    
    for _ in range(iterations):
        result = func(*args)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return result, execution_time

# Benchmark different operations
operations = [
    (calc.add, 5, 3),
    (calc.multiply, 5, 3),
    (calc.power, 2, 10),
    (calc.factorial, 10),
    (calc.gcd, 48, 18),
]

print("Performance Benchmark (10,000 iterations each):")
print("-" * 50)

for func, *args in operations:
    result, execution_time = benchmark_function(func, *args)
    print(f"{func.__name__}{args} = {result}")
    print(f"Time: {execution_time:.6f} seconds")
    print()
``` 