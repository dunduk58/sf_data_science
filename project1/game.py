import numpy as np

number = np.random.randint(1,101)

#количество попыток
count=0

while True:
    count+=1
    predict_num = int(input("угадай число от 1 до 100: "))
    if predict_num > number:
        print("число должно быть меньше!")
    elif predict_num < number:
        print("число должно быть больше!")
    elif predict_num == number:
        print("вы угадали число Это число = {number},за {count} попыток")
        break