# Senate Riddler Express (1-26-18)

Text of the Riddler:

> On Monday, the Senate voted 81-18 to end the government shutdown. This
> naturally grabbed the Riddler’s attention: It’s a palindrome! The vote tally
> reads the same forward and backward. This specific tally was made possible by
> the absence of John McCain. But do senators need to be absent to create
> palindrome tallies? If so, what numbers of absences will do the trick?

# Assumptions

* The hyphen(-) separating the yeas and the nays isn't part of the vote
  representation.
  * This assumption is necessary to find a palindrome with the entire senate
    present.
* Senators can vote with any number of senators present (I didn't bother looking
  up the quorum/vote abstention rules).
* Any number of senators can vote for or against a bill (this means that votes
  like `0-90` are palindromes).
* I don't count the leading 0 in numbers less than 10; e.g., the vote is
  `90-9` not `90-09`. I don't think this makes a difference in the total number
  of palindromes though.

# Solution

Do senators need to be absent to create tallies? Turns out that they don't need
to be. You can have a palindrome vote of `5-95` and `91-9`. Interestingly, the
opposite of those votes (`95-5` and `9-91`) are not palindromes.

To check this, I just brute forced all possible voting combinations and checked
which ones are palindromes. The 211 palindromes are in the `palindromes.ssv`
file in this directory.

# EXTRA CREDIT
The extra credit question asked how many times the senate had voted in a
palindrome in the last three decades. I've never messed with webscraping before
and thought it would be fun to write something up.

The base of the data is stored [here](https://www.senate.gov/legislative/votes.htm)


## Notes
* I used the `html.parser` library
  * I didn't use the `beautiful_soup` library because I couldn't get it
    installed correctly and got tired of messing around with my system.
  * I would've preferred to use that library (instead of writing a class to
    extend the `HTMLParser` class) but here we are.
  * To run this code, you'll need to install the `html` python library (`pip
    install html`) if you haven't already.
* For the ordering of the votes (matters for votes like `90-9` vs. `9-90`) I
  used the yea nay order listed on [senate.gov](https://www.senate.gov/legislative/votes.htm) itself.
* Like before, I assumed that the hyphen isn't part of the string we consider for
  palindrome checking.

## Results
The senate had a vote that resulted in a palindrome *247* times in the last
three decades. All of the votes are listed in the `all-palindromes-extra-credit.txt` file.
