from itertools import product
import numpy as np
from collections import Counter
from math import sqrt

def coin_toss(flips): #function that calculates every single possible outcome of a fair coin flip
    possible_outcomes = 'H', 'T'
    sample_space = np.array(sorted(product(possible_outcomes, repeat=flips))) #cartestian product
    num_of_tails = [] #shows me a list of how many tells tails occurs in the sample space
    n = len(possible_outcomes) ** flips
    tail_outcomes = [] #removes duplicate values from num of tails to create probability distribution table for RV column
    count_tails = [] #occurence of tails from the RV column (in decimal form)
    mean_before_sum = []
    mean = []

    for tail in sample_space: #iterate each row in sample space
        tail_tracker = np.where(tail == 'T') #find every value where there is a tails
        #create a list that tells me amount of tails in each specific row
        cord_ofTails, occurCount = np.unique(tail_tracker, return_counts=True)
        num_of_tails.append(len(occurCount))

    #create a dictionary (learn more about them in crash course)
    dictOfTails = dict(Counter(num_of_tails))
    dictOfTails = {key: value for key, value in dictOfTails.items()} #dict comprehension

    for key, value in dictOfTails.items(): #create a seperate list I can call on for value and key
        p_of_x = value / n #create decimal form of value
        calc_mean = p_of_x * key
        mean_before_sum.append(calc_mean)
        count_tails.append(p_of_x)
        tail_outcomes.append(key)

    mean.append(sum(mean_before_sum)) #create list with just the sum (can create np array)
    var = sum(((np.array(tail_outcomes) - np.array(mean)) ** 2) * count_tails)
    std = sqrt(var)

    return f'Sample space of {n} possible outcomes for tossing a coin ' \
           f'{flips}x: \n{sample_space}\n\n X:    {tail_outcomes} \n P(X): {count_tails}\n Mean: {mean}\n' \
           f' Variance: {var}\n Standard Deviation: {std}\n'

run = True
while run:
    print("~~~~~~~~~~~Statistics Calculator~~~~~~~~~~~"
          "\n---probability distribution of a coin toss---")
    coin_flip = int(input('\nHow many times would like to flip a coin?: '))
    print(coin_toss(coin_flip))