# Prompt:

> The year is 2000, and an arithmetical anarchist group has an idea. For the
> next 100 years, it will vandalize a famous landmark whenever the year (in
> two-digit form, for example this year is “18”) is the product of the month
> and date (i.e. month × date = year, in the MM/DD/YY format).

> A few questions about the lawless ensuing century: How many attacks will
> happen between the beginning of 2001 and the end of 2099? What year will see
> the most vandalism? The least? What will be the longest gap between attacks?

# Explanation

* Used python to run through all of the dates in 2001 and 2099.
* Using the datetime class meant I didn't have to deal with leap years myself. :)
* Printed relevant stats at the end.
* Usage is `python3 attacks.py`.

# Results

There were 212 total attacks.

Years with the least (0) numbers of attacks:
[2000, 2037, 2041, 2043, 2047, 2053, 2058, 2059, 2061, 2062, 2067, 2071, 2073, 2074, 2079, 2082, 2083, 2086, 2089, 2094, 2097]

Years with the most (7) numbers of attacks:
[2024]

They happened on the following dates:
2024-01-24 2024-02-12 2024-03-08 2024-04-06 2024-06-04 2024-08-03 2024-12-02 

The longest gap between attacks was 1097 days. It started on 2057-03-19 and ended on 2060-03-20.
