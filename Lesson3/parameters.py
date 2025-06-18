#You want the function below to print a greeting message to the screen.
# This code will not be executed until it is 'called'.
def say_hello(name):
    print(f'Hello {name},')
def say_welcome(city):
    print(f'welcome to {city}.')
def say_all(name, city):
    print(f'Hello {name}, welcome to {city}.')
# Our function is defined above, so now we can 'call' it
say_hello('Bob')
say_welcome('San Diego')
say_all('Bob', 'San Diego')