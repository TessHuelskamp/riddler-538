# Inspired by this tweet from TheOnion: https://twitter.com/TheOnion/status/1350155959684001798?s=20

# To see how adding a sevent cent coin would ruin
# the "picking the largest value" algo we use to make change,
# I knapsacked picking coins to see what the difference is between the two

# Requires python 3.2
import functools

WITH_SEVEN_CENTS = (1, 5, 7, 10, 25, 50)
WITHOUT_SEVEN_CENTS = (1, 5, 10, 25, 50)

def min_num_of_coins(amount, store):
    if amount ==0:
        return []

    possible_results=[]
    for coin in store:
        if coin > amount:
            continue

        intermediate=[]
        intermediate=min_num_of_coins(amount-coin, store)
        intermediate.append(coin)
        possible_results.append(intermediate)

    return min(possible_results, key=len)


assert min_num_of_coins(1, WITH_SEVEN_CENTS) ==  [1]
assert min_num_of_coins(1, WITHOUT_SEVEN_CENTS) ==  [1]
assert min_num_of_coins(5, WITH_SEVEN_CENTS) ==  [5]
assert min_num_of_coins(5, WITHOUT_SEVEN_CENTS) ==  [5]

assert min_num_of_coins(7, WITH_SEVEN_CENTS) ==  [7]
assert sorted(min_num_of_coins(7, WITHOUT_SEVEN_CENTS), reverse=True) ==  [5, 1, 1]

# Exponetial runtime rn :(
#assert sorted(min_num_of_coins(49, WITH_SEVEN_CENTS), reverse=True) ==  [7]
#assert sorted(min_num_of_coins(49, WITHOUT_SEVEN_CENTS), reverse=True) ==  [25, 10, 10, 1, 1, 1, 1]


#print(min_num_of_coins(49, WITH_SEVEN_CENTS))
#print(min_num_of_coins(49, WITHOUT_SEVEN_CENTS))


for amount in range(1,99+1):

    # It's easier to see differences with the larger coins at the front

    smallest_with_seven=min_num_of_coins(amount, WITH_SEVEN_CENTS)
    smallest_without_seven=min_num_of_coins(amount, WITHOUT_SEVEN_CENTS)

    if len(smallest_without_seven) == len(smallest_with_seven):
        print("no difference for {}".format(amount))
    elif len(smallest_without_seven) < len(smallest_with_seven):
        # There shouldn't be any cases when adding a coin would need more coins to make change but...
        string="{} cents was easier to make with our normal coins.\nWith 7:{}\nWithout:{}"
        print(string.format(amount, sorted(smallest_with_seven, reverse=True), sorted(smallest_without_seven, reverse=True)))

    elif len(smallest_without_seven) > len(smallest_with_seven):
        # Seven wins!
        string="{} cents was easier to make with the seven coin variant.\nWith 7:{}\nWithout:{}"
        print(string.format(amount, sorted(smallest_with_seven, reverse=True), sorted(smallest_without_seven, reverse=True)))

