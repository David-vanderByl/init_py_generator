# Generate `_init_.py` files automatically

This script generates an `__init__.py` file for a directory containing .py files. The generated `__init__.py` file is used to make the directory a Python package.

## Usage

```python
import os


def generate_init_file(directory_path: str):
    # Get the list of .py files in the directory
    py_files = [file for file in os.listdir(directory_path) if file.endswith('.py') and file != '__init__.py']

    # Create the content for the __init__.py file
    init_content = "# This file makes the directory a Python package\n\n"
    for py_file in py_files:
        module_name = os.path.splitext(py_file)[0]
        import_statement = f"from . import {module_name}\n"
        init_content += import_statement

    # Generate the __all__ list
    all_list = [f"'{py_file}'" for py_file in py_files]
    all_statement = ",\n".join(all_list)

    init_content += f"\n__all__ = [\n    {all_statement}\n]"

    # Write the content to the __init__.py file
    init_file_path = os.path.join(directory_path, '__init__.py')
    with open(init_file_path, 'w') as f:
        f.write(init_content)

    print(f"Generated __init__.py file in: {init_file_path}")


# Example usage
directory_path = './example_directory'  # Replace with your desired directory path
generate_init_file(directory_path)
