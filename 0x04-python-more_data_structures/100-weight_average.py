#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    result = 0
    score_2 = 0
    for score1, score2 in my_list:
        result += (score1 * score2)
        score_2 += score2
    return (result/score_2)
