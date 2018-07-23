# riddler express for 07/20/2018

>  if riddler nation needed to make change (anywhere from 0.01 to 0.99) and was establishing its own mint, what values of coins would be ideal to yield the smallest number of coins in any transaction? when picking values, let’s say we’re ditching the europeans and limiting our mint to four different coin denominations — replacing the current common american ones of penny, nickel, dime and quarter.

# Answer

These mints make change for 1 through 99 cents with 6 or less coins.

([1, 4, 13, 29], [24, 1, 4, 15], [1, 39, 4, 15], [16, 1, 27, 4], [16, 1, 4, 29], [17, 4, 29, 1], [1, 18, 4, 30], [1, 18, 4, 31], [24, 1, 19, 4], [1, 19, 4, 29], [32, 1, 19, 4], [33, 19, 4, 1], [28, 12, 5, 1], [1, 12, 5, 39], [1, 28, 5, 13], [16, 1, 28, 5], [16, 40, 5, 1], [17, 20, 5, 1], [24, 17, 5, 1], [25, 18, 5, 1], [1, 18, 5, 29], [1, 19, 5, 30], [1, 28, 13, 6], [1, 26, 6, 15], [32, 1, 6, 15], [40, 1, 6, 15], [41, 1, 6, 15], [16, 25, 6, 1], [17, 21, 6, 1], [24, 17, 6, 1], [1, 11, 38, 7])

# Disclaimer

* I spent a lot of time getting this to work in the car but luckily made it home in time to fix the rest of the solution on a real computer before the 9pm (12pm est) deadline.
* I wanted to write better explanations but won't have time before this answer is due.
* Thank you @cnmcgrath for helping me debug syntax errors remotely :D

# Thought process

* Assuming we're minimizing the smallest number of coins needed for a particular transaction and NOT the average (which would have to be weighted towards certain numbers anyways).
* We're limited to using 4 coins.
* We _need_ to have a penny (1 cent coin) because we need to be able to make change for a penny
  * This saves a little bit of computation.
* Then we have `99c3` mints (`~100**3`) to try (which isn't too bad)
* Then from there we need to calculate the number of coins each change between 1 and 99 needs.
  * Start with changes you can make with one coin... and then with two coins... and so on...
  * ... until we've made change for everything between 1 and 99 cents.
* And after that we'll have our answer
