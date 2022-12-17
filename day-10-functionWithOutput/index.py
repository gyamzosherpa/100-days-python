# .......................day-10........................
def my_function(a, b):
    sum = a + b
    return f"the sum of {a} and {b} is {sum}"


print(my_function(20, 30))


def format_name(f_name, l_name):
    full_name = (f_name + " " + l_name).title()
    # ....return means end of execution....
    return full_name


fullName = format_name('gyamzo', 'sherpa')
print(fullName)


# ..........multiple return values.........
def new_name(fname, lname):
    """take a first and last name and format it
    to return the title case version of the name."""
    if fname == "" or lname == "":
        return "You didn't provide valid inputs. "
    full_name = (fname + " " + lname).title()
    return full_name


newfullName = new_name(input("what is ur first name? "), input("what is ur last name? "))
print(newfullName)


