## Exercise: Numbers in python
#1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
l= 92
w= 48.8
area = l*w
print("area of field : " ,area)


##2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
pack_cost = 1.49
t_packets= 9
total_cost = pack_cost*t_packets
amount_given = 20
return_amt = amount_given-total_cost
print("the shopkeeper going to give you back is :", return_amt)

'''3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
is its length. If tiles cost 500 rs per square feet, how much will be the total
cost to replace all tiles. Calculate and print the cost using python
(Hint: Use power operator ** to find area of a square)'''
sq_area=5.5*5.5
total_cost = 500*sq_area
print(total_cost)

'4. Print binary representation of number 17'
binary=bin(17)
print(binary)
'''or use format(binary,'b')      '''







#[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/3_numbers/3_numbers_exercise.py)