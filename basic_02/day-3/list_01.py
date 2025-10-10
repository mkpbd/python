
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
# print(list[1])

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

# print(nest_list)

## slicing  index 

new_list = [3,4,5,6,7,8,9]

# print(new_list[1:6])
# print(new_list[1::2])

# print(new_list[-1:-4:-1])
# print(new_list[-1::-2])

## list append 

a = [2,3,4,5]
b =[6,7,8,9]
c = a+b
# print(c)

# d = b.__add__(a)
d = b.insert("a")
print(d)

