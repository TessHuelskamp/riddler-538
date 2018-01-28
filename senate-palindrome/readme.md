# Senate Riddler Express (1-26-18)

Text of the Riddler:

> On Monday, the Senate voted 81-18 to end the government shutdown. This
> naturally grabbed the Riddler’s attention: It’s a palindrome! The vote tally
> reads the same forward and backward. This specific tally was made possible by
> the absence of John McCain. But do senators need to be absent to create
> palindrome tallies? If so, what numbers of absences will do the trick?

# Assumptions

* The dash(-) separating the ayes and the nays isn't part of the vote
  representation.
  * This assumption is necessary to find a palindrome with the entire senate
    present.
* Senators can vote with any number of senators present (I didn't bother looking
  up the quorum/vote abstention rules).
* Any number of senators can vote for or against a bill (this means that votes
  like `0-90` are palindromes).

# Solution

Do senators need to be absent to create tallies? Turns out that they don't need
to be. You can have a palindrome vote of `5-95` and `91-9`. Interestingly, the
opposite of those votes (`95-5` and `9-91`) are not palindromes.

To check this, I just brute forced all possible voting combinations and checked
which ones are palindromes. The 211 palindromes are in the `palindromes.ssv`
file in this directory.
