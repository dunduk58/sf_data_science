import numpy as np

def random_predict(number:int=1)-> int:
    """ Guess a rand number

    Args:
        number (int, optional): [description]. Defaults to 1.

    Returns:
        int: [description]
    """

    count=0

    while True:
        count+=1
        predict_num = np.random.randint(1,101)
        if number == predict_num:
            break
    return(count)
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
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"угадываем в среднем за {score} попыток")
    return score

if __name__ == "__main__":
    score_game(random_predict)
