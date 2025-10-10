# # Tuples 
# import builtins
# print(__builtins__ is builtins)
# n_input = int(input())
# # t_tuple = tuple(int(x) for x in input().split())

# t_list = []

# x = 1; 

# while x <= n_input:
#     t_list.add(x)
#     x = x+1

# t_tuple = tuple(t_list)

# print(t_tuple)

# hash_value =  hash(t_tuple)

# print(hash_value)



if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))