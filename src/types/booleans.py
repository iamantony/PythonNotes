__author__ = 'Antony Cherepanov'


def comparisons():
    print("\ncomparisons()")

    print("When we compare objects, as a result we get boolean value")
    print("2 < 3: ", 2 < 3)
    print("str(one) > str(one plus): " + "one" > "one plus")
    print("[1] < [1, 2]: " + str([1] < [1, 2]))


def boolean_expressions():
    print("\nboolean_expressions()")

    print("When we use logical expression (and, or) as a result we get object!")
    print("AND: Python evaluate objects from left to right and stops if left operand is false")
    print("Else it will return right operand")
    print("2 and 3: " + str(2 and 3))
    print("[] and [1, 2]: " + str([] and [1, 2]))
    print("[42] and {}: " + str([42] and {}))

    print("\nOR: Python evaluate objects from left to right and return first one that is true")
    print("2 or 3: " + str(2 or 3))
    print("[] or [1, 2]: " + str([] or [1, 2]))
    print("[42] or {}: " + str([42] or {}))
    print("[] or {}: " + str([] or {}))

    print("So when we use boolean expression in 'if' statement, it returns us not a boolean value, but object!")
    print("Then Python checks whether object if False (empty) or True and after this decide which brunch to go")


comparisons()
boolean_expressions()