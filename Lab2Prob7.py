numbers=[i for i in range (1,1001) if i%8==0]
divisor = [number for number in numbers if True in [True for divisor in range(2,10) if number % divisor == 0]]
print(divisor)