
# Integer number revers 
def integer_revers(number):
    reves_a =0;
    while  number > 0:
         a = number%10
         reves_a = reves_a*10 + a
         number //= 10
    print(reves_a)
    
# integer_revers(12345)



list = [10, 20, 30, 40, 'kamal']

# access in  list item use in  indexing 
print(list[1])

## update list item using  index 
list[0] = 'jamal'

# print(list)

## list traversing list item using  loop 

# for item in list:
#     print(item)


# for i in range(len(list)):
#     print(list[i])

# for i in range(-1, -len(list)-1, -1):
#     print(list[i])


nest_list = [[3,4], [6,7], [9,10]]

nest_list[1][0] = 400

print(nest_list)