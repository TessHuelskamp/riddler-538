# Problem

> Given a two-character, seven-segment display, like you might find on a microwave clock, how many numbers can you make that are not ambiguous if the display happens to be upside down?

# Solution

1. Mapped each digit to it's updside down counterpart (e.g., `1->1`, `6->9`, `7->X`)
1. Ran through 00->99 to see what it's upside down counterpart was.
1. A number was counted as good if it was either: an invalid number or the same number.
1. There were 58 "good" upsidedown numbers.
