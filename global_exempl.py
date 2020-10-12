##spam = 42 #global variable
##
##def eggs():
##    spam = 42 #local variable
##
##print('Some code here.')
##print('Some more here.')


def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You Tried to divide by zero.')
        
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
print(div42by(3))
