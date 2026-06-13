def is_armstrong_number(number):
    

    number = format(number, 'd')
    number_split = [0] * len(number)
    for i in range(len(number)):
        number_split[i] = int(number[i])
    
    
    length = len(number_split)

    sum = 0
    for i in range(length):
        sum = sum + int(number_split[i]) ** length

    return sum == int(number)

print(is_armstrong_number(153))