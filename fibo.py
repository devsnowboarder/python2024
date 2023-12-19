def fiboNumber(count):
    num1 =0
    num2=1
    for  x  in range(1,count):
        print(num1)
        fibo = num1 + num2
        num1=num2
        num2=fibo

fiboNumber(20)