import numpy as np
from random import randint

def random_predict(number:int=1)-> int:
    """ Guess a rand number

    Args:
        number (int, optional): [description]. Defaults to 1.

    Returns:
        int: [description]
    """

    #setting the boundaries for search and initial guess
    count=0 
    low=1
    high=100
    guess = (low+high)//2

    #binary search algorithm slices the range in a half on each step until it finds the result
    while guess != number:
        count+=1
        guess = (low+high)//2
        #predict_num = randint(1,101)
        if guess > number:
            high = guess
        elif guess < number:
            low = guess + 1
    return(count, number)


def score_game(random_predict) -> int:
    """mean guessing score

    Args:
        random_predict ([type]): [description]

    Returns:
        int: [description]
    """
    count_ls=[]
    np.random.seed(1)
    random_array = np.random.randint(1,101,size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number)[0])
    score = int(np.mean(count_ls))
    #print (count_ls)
    print(f"Угадываем в среднем за {score} попыток")
    return score

if __name__ == "__main__":
    score_game(random_predict)
    print(f"Загаданное число: {random_predict(randint(1,101))[1]}")
