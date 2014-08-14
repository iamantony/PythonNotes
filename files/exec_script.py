__author__ = 'Antony Cherepanov'

# Quick way to execute some code in other module:
# open file -> read its' content -> execute code
print("1:")
exec(open('../imports/several_variables.py').read())
print()


# But if you have a variable that also defined in file, that you are going to
# execute, then your local variable will get value from executed script.
# Because exec() execute code in local scope.
print("2:")
first = 1024
print("Before:", first)
exec(open('../imports/several_variables.py').read())
print("After:", first)