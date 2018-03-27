# Riddler Classic from Fri Mar 23

The text of the riddler itself:

> Imagine taking a number and moving its last digit to the front. For example,
> 1,234 would become 4,123. What is the smallest positive integer such that when
> you do this, the result is exactly double the original number? (For bonus
> points, solve this one without a computer.)

# Notes on submission time

I didn't finish this on time but wanted to write down half of my thoguht process
before the answer comes out to confirm that I was on the right track to finding
the answer.

# Working out the problem

1. Separate the number into the two parts. The digit on the end that is being
   rotated, and the rest of the number.
  * `123456 -> 612345`
  * `xxxxxy -> yxxxxx`
1. I realized that you can write each number in terms of x and y in the
   following way.
  * `x + y` for the first number.
    * > `123450+6`
  * `y*10^floor(log10(x))+x/10`
    * > `6*10^floor(log10(123450)) +123450/10`
    * > `6*10^5 +12345`
    * > `600000+12345`
    * > `612345`
1. Then, what we want to find is x and y such that one is twice the other.
  * So, `2x + 2y = y*10^floorlog10(x)+x/10`
1. Reducing things down we get
  * `2x + 2y = y*10^floor(log10(x))+x/10`
  * `19x + 20y = 10y*10^floor(log10(x))`
1. And that's where I'm stuck.
