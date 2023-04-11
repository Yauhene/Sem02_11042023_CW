# 1. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
i = 1
n = int(input("Введите число n:"))
result = 1

while i <= n:
    result *= i 
    i+=1
    
print(result)

# 2. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

A = 8

i1 = 0
i2 = 1
print(i1)
print(i2)
i = 3

while i <= A:
    i3 = i1 + i2
    #temp = i3
    i+=1
    print(f'i3 = {i3} i = {i}')
    i1 = i2
    i2 = i3
else:
    print('данное число не входит в последовательность Фибоначчи')

#============================
a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 2
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)  