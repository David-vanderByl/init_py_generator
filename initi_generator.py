import os
import ast

def get_symbols_to_include(file_path):
    with open(file_path) as f:
        file_content = f.read()

    module = ast.parse(file_content)

    # Get all top-level function and class names
    top_level_class_names = [node.name for node in module.body if isinstance(node, ast.ClassDef) and node.name != '__init__']
    top_level_function_names = [node.name for node in module.body if isinstance(node, ast.FunctionDef) and node.name != '__init__']

    # Now find all function calls in the code
    all_calls = [node.func.id for node in ast.walk(module) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)]

    # Top-level functions to include are those which are NOT called somewhere in the script
    functions_to_include = [fn for fn in top_level_function_names if fn not in all_calls]

    # Return a combined list of class names and function names to include
    return top_level_class_names + functions_to_include

def create_init_file(directory):
    if not os.path.exists(directory):
        print(f"Directory: {directory} does not exist.")
        return

    py_files = [f for f in os.listdir(directory) if f.endswith('.py') and f != '__init__.py']

    init_file = os.path.join(directory, '__init__.py')
    with open(init_file, 'w') as f:
        f.write("# This file makes the directory a Python package\n\n")

        all_symbols = []

        for py_file in py_files:
            symbols = get_symbols_to_include(os.path.join(directory, py_file))
            if symbols:
                base_name = py_file[:-3]
                for symbol in symbols:
                    f.write(f"from .{base_name} import {symbol}\n")
                    all_symbols.append(f'"{symbol}"')

        f.write("\n__all__ = [\n")
        f.write(',\n'.join(all_symbols))
        f.write("\n]\n")

    print(f"__init__.py file has been created in {directory}.")

# Use the function
create_init_file('./example')
