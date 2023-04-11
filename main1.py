for i in range(0, 5, 2):
    print(i)

stroka = "qwerty"
for el in stroka:
    print(el)


i = 0
while (i < 5):
    n = int(input("Ввод: "))
    if n == 0:
        break
    i+=1
else:
    print("Конец")
#
stroka = "qwerty"
for el in stroka:
    print(el, end=" ")
print("qqqq")
print("qqqq")
#
num = input("Введите ваше число: ")

print(int(num[0]) + int(num[1]) + int(num[2]))