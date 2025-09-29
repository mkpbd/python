## for loop with range function and give explanation of code 

for j in range(100):
    print(j, end=",")


for row in range(5):
    for col in range(row+1):
        print('*', end=" ")
    
    print()



for row in range(5):
    for col in range(row+1):
        print(chr(97+row), end=" ")
    
    print()



list_items = [['kamal', 'jamal'], [1,2], [True, False]]

for item in list_items:
    print(item);

for items in list_items:
    for item in items:
        print(item)