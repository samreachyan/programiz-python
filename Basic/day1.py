import constant

def double(num):
    '''double any value and return'''
    # this is comment will be not display on screen
    return 2 * num

print(constant.PI)
print(constant.GRAVITY)

print(double.__doc__)

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


def my_sum(*args):
    '''Total param array'''
    return sum(args)

print(my_sum(1,2,3,4))
print(my_sum.__doc__)