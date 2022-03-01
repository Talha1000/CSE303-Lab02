numbers=[i for i in range (1,1001)]
divisor = {number:max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in numbers}
print(divisor)