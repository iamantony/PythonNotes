__author__ = 'Anotny Cherepanov'


# If we import whole file (module) "several_variables.py", we will get:
# 1) access to all defined variables
# 2) execute function print
from imports import several_variables

# Also we can import only part of the variables (functions, classes), that
# declared in module. We will not be able to access other variables from module
from imports.several_variables import second
print(second)
# print(first)  # error - variable "first" not imported