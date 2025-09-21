'''
Assume each pizza has 8 slices.
Assume that there is a family of 4.
Ask how many slices each person in the family eats.
Then calculate how many whole pizzas you need to order and
how many pizza slices are leftover after everyone is done eating.
So if everyone is eating 3 slices you need 2 pizzas with 4 leftover slices.
Do not use loops or lists or functions. You can use the modulo operator %
Submit a document that specifies the following
Input: What are the inputs?
Processing: What is the processing you are doing?
Output: What is the output?
Assumptions: What are the assumptions you are making or the problem statement is making?
What will happen when you change the assumptions?
Give 2 examples
Test cases: Test the program with these 4 test cases 1.
Everyone eats the same number of slices. 2.
Everyone eats 2 slices of pizza .3 Everyone eat 3 slices of pizza 4.
The number of slices each family member eats is 1, 2, 3, 3 so that the total slices is 9
'''



pizza_slices = 8
#slices_per_person = int(input('How may slices for each member? '))

#total_slices = slices_per_person * 4

#print(total_slices)

#total_pizzas = total_slices / pizza_slices

#extra_slices = total_slices % pizza_slices

#print(f'The total amount of whole pizzas needed is {total_pizzas:1.0f}.')
#print('There are', extra_slices, 'leftover slices.')

fam1 = 1
fam2 = 2
fam3 = 3
fam4 = 3

total_slices = fam1 + fam2 + fam3 + fam4


print(total_slices)

if total_slices > 8:
    total_pizzas = total_slices // pizza_slices + 1

leftover_slices = total_pizzas * 8 - 9

    

print(total_pizzas)

print(leftover_slices)

print('The total number of pizzas needed is', total_pizzas)
print('There are', leftover_slices, 'slices left.')


