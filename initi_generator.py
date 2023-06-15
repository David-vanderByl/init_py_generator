import os
import ast

# This function takes a path to a python file,
# reads its contents and uses the ast module to parse the file.
# It then walks through the parsed AST to find top-level function and class definitions
# except '__init__' methods or classes.
def get_top_level_symbols(file_path):
    # Open the file and read its contents
    with open(file_path) as f:
        file_content = f.read()

    # Parse the file contents to an AST
    module = ast.parse(file_content)

    # Use ast.walk to find all function definitions in the AST
    # Filter the list to include only top-level definitions and exclude '__init__'
    function_names = [node.name for node in ast.walk(module) if isinstance(node, ast.FunctionDef) and node.name != '__init__']

    # Similarly find all class definitions
    # Filter the list to include only top-level definitions and exclude '__init__'
    class_names = [node.name for node in ast.walk(module) if isinstance(node, ast.ClassDef) and node.name != '__init__']
    
    # Return a combined list of function and class names
    return function_names + class_names

# This function creates a '__init__.py' file in the given directory.
# The '__init__.py' file will have import statements for all top-level symbols (functions, classes) from each python file in the directory.
def create_init_file(directory):
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Directory: {directory} does not exist.")
        return

    # List all python files in the directory, excluding '__init__.py'
    py_files = [f for f in os.listdir(directory) if f.endswith('.py') and f != '__init__.py']

    # Path to the new '__init__.py' file
    init_file = os.path.join(directory, '__init__.py')

    # Open the file in write mode
    with open(init_file, 'w') as f:
        # Write a comment to indicate the purpose of this file
        f.write("# This file makes the directory a Python package\n\n")

        # A list to store names of all top-level symbols for '__all__' variable
        all_symbols = []

        # Iterate over each python file
        for py_file in py_files:
            # Get all top-level symbols from the file
            symbols = get_top_level_symbols(os.path.join(directory, py_file))

            # If the file has any top-level symbols
            if symbols:
                # Get the base name of the file by removing '.py' extension
                base_name = py_file[:-3]

                # Write an import statement for each symbol and add the symbol to 'all_symbols' list
                for symbol in symbols:
                    f.write(f"from .{base_name} import {symbol}\n")
                    all_symbols.append(f'"{symbol}"')

        # Write '__all__' variable to the file
        f.write("\n__all__ = [\n")
        f.write(',\n'.join(all_symbols))
        f.write("\n]\n")

    print(f"__init__.py file has been created in {directory}.")

# Use the function
create_init_file('./example')
