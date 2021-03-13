print("Я колобок")
repeat = 1
while repeat == 1:
    print("Выберите действие")
    print ("1.Я убежал")
    print ("2.Я остался дома")

    a = int(input())

    if a == 1:
        print("Я убежал")
        repeat = 0
    elif a == 2:
        print("Я остался дома")
        repeat = 0
    else :
        print("Я тебя не понял")

print("Выберите действие")
print ("1.Я встретил медведя  и побежал дальше.")
print ("2.Я спал")
a = int(input())
if a == 1:
    print("Я встретил медведя  и побежал дальше.")
    print("Я встретил лису")
    print("Меня съели")
if a == 2:
    print("Я спал")
    print("Я проснулся")
    print("Я убежал от бабушки")


