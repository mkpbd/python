#function to calculation speed 

def cal_speed(distance, time):
    print("Distance (KM):", distance)
    print("Time (hr):", time)
    speed = distance / time
    return speed

result = cal_speed(100, 2)
print("Speed (KM/hr):", result)

#function to calculation  distance traveled
def cal_distance(speed, time):
    print("Speed (KM/hr):", speed)
    print("Time (hr):", time)
    distance = speed * time
    return distance

result = cal_distance(50, 2)
print("Distance (KM):", result)

#function to calculation time taken
def cal_time(distance, speed):
    print("Distance (KM):", distance)
    print("Speed (KM/hr):", speed)
    time = distance / speed
    return time

result = cal_time(100, 50)
print("Time (hr):", result)

#function to calculation average speed