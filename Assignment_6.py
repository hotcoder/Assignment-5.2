'''
Created on Nov 17, 2017

@author: z002krv
'''
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]

print(new_fellowship)

new_dict = {member : len(member) for member in fellowship}

print(new_dict)

list_generator = (number for number in range(5))

for number in list_generator:
    print(number)