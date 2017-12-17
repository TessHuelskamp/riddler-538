# Cookie monster problem

What is the highest spelled out number that you can tweet (now in 280 chars).

# Answer
chars: 279

spelled out: one hundred three sextillion three hundred twenty three qintillion three hundred seventy three quadrillion three hundred seventy three trillion three hundred seventy three billion three hundred seventy three million three hundred seventy three thousand three hundred seventy two!

as int: 103323373373373373373372

# Notes
* The git repo is a mess (I started coding this at 7am after waking up at 4 to
  drive a few hours to the airport).
  * I decided to brute force this (before checking if the 140 char's solution
    was near max Uint64...)
  * Then I decided to brute force using the powers of 1000 slice (before I
    realized that was a stupid idea too :D)
* Finally I relized I didn't have to check all of the numbers and checked the
  transition points (explanation in code)
* This worked fine for 140 characters but took about 2.5 hours for 280.
* I didn't have time to implement a possible better search strategy but think
  it could've sped things up considerably.
  * The thought there was to add the largest string for each power of 1000
    until I went over and then search there.
  * Pseudo code/execution
```
check largest*1000^1
check largest*1000^1 + largest*1000^2
check largest*1000^1 + largest*1000^2 + largest*1000^3
...
at power 5 we go over?
start checking from (largest*1000^1 + largest*1000^2 + largest*1000^3 +largest*1000^4) on
```
* I also wanted to put all of the number functions in their own class/module
  but am new to go and ran out of time for that.
  * I also should've written my error codes like you're supposed to in go _shrug_

