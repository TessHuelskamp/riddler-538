# 538 Riddler Express Jan  5
These were both straightforward to solve but I thought I'd write up a solution
here to be thorough.

## Area of a kite

![kite drawing](https://espnfivethirtyeight.files.wordpress.com/2018/01/roeder-riddler-0104-2.png)

If you notice that the edge of the kite that intersects the circle is a right
angle, due to some cool fact about circles, you notice that we need to find the
area of two right triangles with bases and heights of 5 and 8 respectively.
Then, the area of both of the right triangles is `2*(1/2*5*8)=40`.

## Area of a rectangle inside a quarter circle

![rectangle inside square](https://espnfivethirtyeight.files.wordpress.com/2018/01/roeder-riddler-0104-1.png)

This one was cute in that you need to recognize that the radius will go through
the top right corner of the rectangle. Since the radius is 13 (`5+8`) and the
base of the rectangle is 5, we can find the size of the long end of the
rectangle noticing that those two edges are 2 out of 3 of the edges in a 5-12-13
right triangle. Once we know that the longer side of the rectangle is 12, the
area is then 60 (`5*12`).
