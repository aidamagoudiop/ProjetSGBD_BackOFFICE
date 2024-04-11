import ttconv

input_ui_file = "dashboard.ui"
output_py_file = "ui_dashboard.py"
backend = "tk"

# Convert UI file to Python code
ttconv.convert_ui(input_ui_file, output_py_file, backend)
