import random

name = input('What is your name? ')

names = ['tracker', 'ribbon', 'corkscrew', 'sawhorse', 'tranquility', 'hyacinth']
true_password = random.choice(names)
for word in names:
        if word == true_password:
            print(word.upper())
        else:
            print(word)
   

