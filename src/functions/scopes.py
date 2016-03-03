__author__ = 'Antony Cherepanov'

glob_str = "i'm global"

print("Names at the top level of a file are global to code within that " +
      "single file only")
print("If we want use them in other modules, than we should import them")
print("This is global variable: " + glob_str)

glob_list = [1, 2, 3, 4]


def module_func():
    print("\nNow we inside local function. All variables, that we create " +
          "inside this functions are local. We can't access them anywhere else")

    local_str = "this is local variable"
    print("Local variable: " + local_str)

    print("We can use here global variable: " + glob_str)
    print("And we can change them: before - " + str(glob_list))
    glob_list.append(10)
    print("After: " + str(glob_list))

    print("But if we will assign something to global variable, than " +
          "local variable will be created and global variable will now change")

module_func()


def change_global():
    global glob_str

    print("\nchange_global()")

    print("We have global variable: ", glob_str)
    print("To change it's value from local scope of function we should use" +
          "global statement.")

    glob_str = "Change globally"
    print("Changed global variable (inside function): " + str(glob_str))


change_global()
print("Global variable (outside): " + str(glob_str))


def first_way_to_change_global():
    print("\nfirst_way_to_change_global()")
    print("First way to change global variable of another module:")
    print("Import module, declare global variable, change it")

    from functions.another_module import another_module_glob
    global another_module_glob
    print("Before: " + str(another_module_glob))
    another_module_glob += 1
    print("After: " + str(another_module_glob))


def second_way_to_change_global():
    print("\nsecond_way_to_change_global()")
    print("We can find module via sys.module method and get access to " +
          "its' global var.")

    import sys
    an_mod = sys.modules['functions.another_module']
    print("Before: " + str(an_mod.another_module_glob))
    an_mod.another_module_glob += 1
    print("After: " + str(an_mod.another_module_glob))


def nested_functions():
    print("\nnested_functions()")
    print("Within nested function reference to the variable looks first " +
          "in the current local scope.")
    print("Than in the local scope of any enclosing functions from " +
          "inner to outer.")
    print("Then in the current global scope and finally in built-ins.")

    var = 99
    print("In local scope we declared variable: " + str(var))

    def func():
        print("From nested function: " + str(var))

    func()


def closures():
    print("\nclosures()")
    print("Closure - function object that remember values in enclosing " +
          "scopes regardless of whether those scopes are still present " +
          "in memory.")

    def maker(n):
        def action(x):
            return x ** n
        return action

    mk_object = maker(2)
    print("First closure return values powered to 2: " + str(mk_object(4)))

    another_maker = maker(5)
    print("Second closure return values powered to 5: " + str(another_maker(5)))

    def lambda_maker():
        x = 4
        # Pass x manually
        action = (lambda n, x=x: x ** n)
        return action

    print("We can create closures with lambdas.")
    lambda_mk = lambda_maker()
    print("Acts the same: " + str(lambda_mk(3)))


def nonlocal_examples():
    print("\nnonlocal_examples")
    print("We know that in nested function we can reference variables that " +
          "was declared in enclosing function.")
    print("We can use them, but can not change (static variables).")
    print("So if we want more control on variables, we " +
          "should use 'nonlocal' keyword")

    static_var = 64
    mutable_list = [1, 2]

    print("We declare two variables: static and mutable:")
    print(static_var)
    print(mutable_list)

    def nested_func():
        nonlocal static_var

        print("Inside nested function:")
        print("Static variable = " + str(static_var))
        print("We can use it here only because this: 'nonlocal static_var'")
        print("Mutable variable = " + str(mutable_list))

        print("Let's try to change static variable:")
        static_var += 10
        print(static_var)

        print("Let's try to change mutable variable:")
        mutable_list[0] = "changed"
        print(mutable_list)

    nested_func()

    print("Remember:")
    print("- nonlocal variables must have been previously assigned " +
          "in enclosing function")
    print("- nonlocal restricts scope lookup to enclosing defs.")
    print("So you can't use nonlocal keyword with global variable")


def closures_with_nonlocal():
    print("\nclosures_with_nonlocal")
    print("With nonlocal it's easy to create closures that will have")
    print("it's own individual state that can't be changed outside")

    def maker(n):
        degree = n

        def action():
            nonlocal degree
            print("Closure with degree " + str(degree))
            degree += 1

        return action

    print("We have two closures, that have different initial state " +
          "(value of degree). Each call they increment it by one.")
    first = maker(2)
    second = maker(10)

    first()
    second()
    first()
    second()


def function_attributes():
    print("\nfunction_attributes")
    print("Another way to create closures with state retention - " +
          "function attributes")

    def maker(n):
        degree = n

        def action():
            print("Closure with degree " + str(action.degree))
            action.degree += 1

        action.degree = degree
        return action

    print("We have two closures, that have different initial state " +
          "(value of degree). Each call they increment it by one.")
    first = maker(63)
    second = maker(8)

    first()
    second()
    first()
    second()

    print("This method of state retention for closures is portable: " +
          "we can us it with 2.X and 3.X")
    print("Also we have access to closures attributes outside: " +
          str(second.degree))



first_way_to_change_global()
second_way_to_change_global()
nested_functions()
closures()
nonlocal_examples()
closures_with_nonlocal()
function_attributes()

print("\nUpshot\n")
print("global makes scope lookup begin in the enclosing module’s scope and")
print("allows names there to be assigned. Scope lookup continues on to the")
print("built-in scope if the name does not exist in the module, but ")
print("assignments to global names always create or change them in the")
print("module’s scope\n")

print("nonlocal restricts scope lookup to just enclosing defs, requires that")
print("the names already exist there, and allows them to be assigned.")
print("Scope lookup does not continue on to the global or built-in scopes\n")