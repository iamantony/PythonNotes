__author__ = 'Antony Cherepanov'

print("Names at the top level of a file are global to code within that " +
      "single file only")
print("If we want use them in other modules, than we should import them")

glob_str = "i'm global"
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