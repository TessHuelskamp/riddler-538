# coding: utf-8

from random import randint
def rng(): return randint(0,9)

def get_game():
    # returns: list of rolls [5 4 2 2 1]
    rolls_we_care_about = list()

    roll=rng()
    largest=10

    while roll > 0:
        if roll <=largest:
            largest=roll
            rolls_we_care_about.append(roll)

        roll=rng()

    return rolls_we_care_about


# If there are more than 5 rolls, the fractions are marginally off (floats, ¯\_(ツ)_/¯)
# this is good enough for the riddler since we don't need to be super precise :)
def calculate_score(rolls):
    result=sum([ roll * .1**int(1+idx) for idx, roll in enumerate(rolls)])

    # sometimes the sum is 0 (as an int)
    return float(result)

num_games = 10000
total=sum([calculate_score(get_game()) for _ in range(num_games)])

avg = float(total)/float(num_games)

print(avg)


