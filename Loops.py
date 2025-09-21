'''Problem 1

You work for a bakery that sells two items: muffins and cupcakes.
The number of muffins and cupcakes in your shop at any given time is stored in the
variables muffins and cupcakes which you will define, and the store has 10 muffins
and 10 cupcakes.  Write a program that takes strings from standard input indicating
what your customers are buying ("muffin" for a muffin, "cupcake" for a cupcake). If
they buy a muffin, decrease muffins by one, and if they buy a cupcake, decrease
cupcakes by 1. If there is no more of that baked good left, print ("Out of stock").
Once you are done selling, input "0", and have the program print out the number of
muffins and cupcakes remaining, in the form "muffins: 9 cupcakes: 3"
(if there were 9 muffins and 3 cupcakes left, for example).

'''




#PROBLEM 1

muffins = 10
cupcakes = 10


order = 'idk'

while order != '0':
    order = input('What can I get for you today? - ')
    if order == 'muffin' and muffins > 0:
        muffins -= 1
        print(muffins, 'muffins left.')
    elif muffins == 0:
        print('Out of stock, sorry!')
    elif order == 'cupcake' and cupcakes > 0:
        cupcakes -= 1
        print(cupcakes, 'cupcakes left.')
    elif cupcakes == 0:
        print('Out of stock, sorry!')

print('muffins:', muffins, 'cupcakes:', cupcakes)







    
