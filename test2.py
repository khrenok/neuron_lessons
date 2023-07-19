def simple_perseptron(Sensors):

    b = 7    
    s = sum([int(Sensors[1] * weights[i]) for i in range(len(Sensors))])

    if s >= b:

        return True
    
    else:
        return False



num1 = list('001001001001001')
num2 = list('111001111100111')

weights = [1 for i in range(15)]

print(simple_perseptron(num1))
print(simple_perseptron(num2))
