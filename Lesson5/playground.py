import random 

winChance1 = random.binomialvariate(n=1000, p=1.0)
winChance2 = random.binomialvariate(n=50, p=0.0)

toPlay = input('Do you like to bet?')
if toPlay == 'Yes':
    betType = input('High or low?')
    if toPlay == 'No':
     print('Bye then.')
    

if betType == 'High':
    print(f" You have a chance of winning {winChance1} dollars.")
    if betType == 'Low':
         print(f" You have a chance of winning {winChance2} dollars.")
    else:
        print("Thanks!")
         

