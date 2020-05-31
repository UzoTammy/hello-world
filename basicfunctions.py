"""Basic functions as tools for programming"""

# Function to convert number to currency format.
def currency_format(num, x):
    if type(num) == float or type(num) == int:
        print(f'{num:,.{x}f}')
    else:
        if type(num) == str:
            print("expecting a float or integer type but string type supplied")

# Function to convert numeric string to currency format
def string_to_currency(text):
    if type(text) == str:
        if text.isdigit():
            currency_format(float(text), 2)
        else:
            remove_comma = ''.join(text.split(','))
            remove_space = ''.join(remove_comma.split(' '))
            try:
                currency_format(float(remove_space), 2)
            except ValueError:
                msg = "Expecting digits only, check your entry"
                print(msg)

# Say hello
def say_hello(self):
    firstname = self.name.split(' ')
    'Hello'.__add__(f' {firstname[0]},')

# divide function
def divide(x, y):
    return x/y

ans = divide(2.8,3.9)
print(ans)
