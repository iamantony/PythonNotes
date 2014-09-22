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


first_way_to_change_global()
second_way_to_change_global()
nested_functions()
closures()