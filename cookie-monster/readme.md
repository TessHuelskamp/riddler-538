# cookie monster problem

What is the highest spelled out number that you can tweet (now in 280 chars)

> Cookie monster alwaus ends his counting with an "!" at the end of the number

# plan to solve this

For now, I'm just going to brute force the solution (It's 7
am at an airport and this is the best I've got). Later, I could search for the
number more efficiently by caching 1-999 and finding (as you go up from 1) which
strings are the longest we've seen so far (if spelledOut(17) > spelledOut(x<17),
there's no reason to check 1-16 after we add the next 1000)

# examples for testing
> I mostly want to make sure I have the syntax for this right

* "Five hundred thirty eight!"
* "One trillion one hundred eleven billion three hundred seventy three million
  three hundred seventy three thousand three hundred seventy two!"
1 111 373 373 372
//373 broke things one we find the number that busts 140, step down until you're below things
  * That was the answer to the last problem (when twitter only allowed you to
    tweet 280 chars).
  * For testing, I'll set the limit to be 140 characters and make sure I arive at this answer.

# what comes after a trillion

Quadrillion Quintillion Sextillion Septillion Octillion Nonillion Decillion
Undecillion
