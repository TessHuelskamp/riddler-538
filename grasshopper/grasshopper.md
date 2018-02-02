# Problem Description
> A grasshopper lands somewhere randomly on your lawn, which has an area of 1
> square meter. As soon as it lands, it jumps 30 centimeters. What shape should
> your lawn be to maximize the chances that the grasshopper will still be on
> the lawn after the 30-centimeter jump?

# First Thought
The grasshopper landed on my land (somehow) that just happens to be a sphere.
With area = `1m**2` (radius ~=28cms). Then, anywhere that the grasshopper can
jump will have to be on my lawn because there's nowhere else for it to go. The
grass hopper will land on my land 100% of the time :)

# Second Thought
Since I know the first option isn't possible, let's say I've build a 31 cm tall
~wall~ fence that surrounds my property. Let's say my property is a meter long
(ignoring the surface area here) and is a giant long line. When the grasshopper
lands between section 0-0.3cm or 0.7-1.0cm of the land _half_ of that time the
grass hopper will escape (the other time the grasshopper will jump back towards
the middle). So in total, 70 percent of the time (`.3/2+.4+.3/2=.7`) the grass
hopper will land on my lawn. Here's an ascii diagram:

```
______|________|______
 1/2  .3   1   .7 1/2

```

## Second thought version 2
The issue with the last section is that there's a good portion of the lawn that
the grass hopper can jump off. Obviously, we want to minimize that. So, this
time I built a longer lawn that's split into 100 sections (I could only by
grass in centimeter units) that are 29 cm apart. Essentially, if the grasshopper
lands on any section of my lawn except (for the two end pieces), the grasshopper
will have no choice but to stay on my lawn }:). For lawn pieces 0 and 99, half
of the time the grass hopper will stay on my lawn, the other half the
grasshopper will leave.

So (`98+(1/2*2)`) 99% of the time the grasshopper will stay on my lawn.

Diagram:
```
_        _         _        _ ... _        _
^1cm lawn           ^29cm space
```
## Second thought version 3
Same thing as above but this time I'm going to build my lawn on a ring (sort of
like my lawn was on a really big headband). This time the grasshopper will never
be able to leave as there are no endpoints!

# Two/Three dimensions!
Now that I thought about how I'd maximize the grasshopper staying on my lawn I
thought I'd apply that thought to two dimensions.

## A really long ring (without a fence)
Same approach as the second version of my second thought but this time I won't
cheat and build a fence. I'm going to assume that the grasshopper can only
rotate in 1 degree units; if the grasshopper jumps at 0 degrees or 180 degrees
the grasshopper will stay on my lawn.

This means that 0.55 percent of the time (`99*2/360`) the grass hopper will land
on my land (which isn't very good).

## TESSellations
 The headband approach worked in one(?) dimension because all of the spots the
grasshopper could jump to were 30 cm away. I tried to make this work in 2
dimensions with tessellations. There were two[1][2] version of tessellations we could
go with where all of the sections of my lawn are the same 30cm apart: simple
squares and simple triangles.

> [1]I didn't include hexagons because they're basically triangles.

> [2]I also didn't include the
> [semi-regular](http://mathforum.org/sum95/suzanne/whattess.html) tessellations
> because the triangles were obviously more efficient.

Diagrams. Here the dots(`.`) are where I'd put little specs of my land. The other
characters (`|-/\`) just show how the dots would connect.

Tessellation of squares
```
  . _ . _ . _ . _ .
  |   |   |   |   |
  . _ . _ . _ . _ .
  |   |   |   |   |
  . _ . _ . _ . _ .
  |   |   |   |   |
  . _ . _ . _ . _ .

```


Tessellation of triangles
```
  . _ . _ . _ . _ .
 / \ / \ / \ / \ / \
. _ . _ . _ . _ . _ .
 \ / \ / \ / \ / \ /
  . _ . _ . _ . _ .
 / \ / \ / \ / \ / \
. _ . _ . _ . _ . _ .
 \ / \ / \ / \ / \ /
  . _ . _ . _ . _ .
```

When the grasshopper lands on a portion of my lawn in the square-tessellated
version, 1.11 percent of the time (4/360) the grass hopper will return to my land.

When the grasshopper lands on a portion of my lawn in the triangle-tessellated
version, 1.67 percent of the time (6/360) the grass hopper will return to my land.

Both of these calculations assume that there are suffitiently enough portions of
my lawn to negate the edge effect (my lawn manufacture got really good and can
now manufacture picometer circles o grass instead of centimeter circles of
grass).

If we were allowed to use 3dshapes ([we're not
;(](https://twitter.com/ollie/status/959493842738319360)), I'd build a giant one of these
![jungle gym](https://thumbs.dreamstime.com/z/gimnasio-de-la-selva-del-patio-28769128.jpg)
to negate the edge effects. (NB: This percentage would be slightly
smaller than the 1.67 percent from the triangle tesselation since there are a
few five spoked nodes).

# Final thoughts
Given that the extra credit question asked us how we'd change our answer
depending on how far the grasshopper can jump, I'm assuming there's a better
answer I haven't come up with yet. I'm going to sleep on this but this is where
I'm at for now.
