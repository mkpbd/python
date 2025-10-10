get_input = input().strip()

split_input = get_input.split()

print(split_input)
brightness = float(split_input[0])
threshold = float(split_input[1])

if brightness >= threshold :
    print('ON')
else :
    print('OFF')



# brightness, threshold = map(int, input().split())

# if brightness >= threshold:
#     print("ON")
# else:
#     print("OFF")
