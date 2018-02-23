# Desert Riddler from Fri Feb 23

> During their descent, three paratroopers were blown off course and
> crash-landed in the desert — an infinite, uniform, two-dimensional plane.
> They come to at a random time after the crash and must find a way to meet up.
> The only tool they each have is a device that displays a snapshot of the
> positions (but not the velocities) of all three of them in the desert. They
> can each use this tool only once. To make things more annoying, they’ve all
> been nearly blinded by sandstorms and won’t be able to physically see the
> others until they’ve all arrived at the same point.

> Can you devise a strategy that they can agree upon beforehand and that will
> guarantee they will meet up? (Note that the snapshot does not indicate the
> specific identities of the other paratroopers, so a strategy like “let’s
> agree that A stands still and B and C walk to him” will not work.)

> Extra credit: Is there a strategy that would work for any number of paratroopers?

# Disclaimer

I wrote this up on another travel day (I was up at 2am to catch a 5am flight :(
). The last time I tried to solve things on that much sleep I forgot to check
`INT_MAX` limits and wrote the mess of the code that's in the cookie monster
dir (TODO: fix that).

# My interpretation of the rules

* Each paratrooper lands somewhere in the desert.
* Each has a device that can show the locations of everyone once (but doesn't
  label who is who).
  *  I'm not exactly sure what it means that the velocity isn't displayed.
    * I'm assuming that that means you get x,y coordinates of everyone (but
      again not which x, y coordinate you are).
* The _each_ have the device so they don't have to query the map at the same
  time.
  * I.e., the map can change states and a later query would reflect with that.
* The problem says they won't see each other until they all arrive at the same
  point.
  * I'm assuming the wording's wrong here (if it isn't then I'll have to modify
    things; this soln could be adapted) and that if 2 or more people bump into
    each other they will see each other.

# Plan of attack
1. Agree beforehand that person A will start the finding of people. Everyone
   else will stay put until they are found.
1. Person A queries their map.
1. Person A assumes that they are at point in the lower left hand corner of the
   map.
  * The lower left hand corner of the map doesn't matter, this is how I'm going
    to order the points.
1. Person A then tries to get to the nearest person from the lower left hand
   corner of the map (go up/down (y-y0) left/right (x-x0)).
1. If at that point there is _not_ a trooper there, person A will go back to
   where they started.
1. Then, Person A would assume they were the next lower left hand spot (?; TODO
   define ordering) person and then try to go to the spot closest to that.
1. Eventually, through checking all of the spots A could have landed, A will
   eventually run into someone.
1. Then, whoever A runs into will check their map. Since A will be with the
   person A found (lets call the found person B), the map will show where A
   started (this is important for cases like one I'll draw below) and A and B
   will then know where both of them currently are.
1. Once A and B know where they are, they can jut around the desert and pick up
   the rest of the troops one by one. (whoever they run into will have to join
   the pack) and then they will all eventually be found.
1. At the end they've all found each other but they don't seem any closer to
   getting out of the desert. At least they have friends.

# Why B needs to check their map

Let's say the map looks like what I drew below. The dots are people and the
lines are drawn to show distance.

The `+`, `@`, `&`, and `*` call out specific spots that I'll talk about later.

```
  . _ . _ . _ . _ .
   \ / \ / \ / \ / \
    @ _ & _ . _ . _ .
   / \ / \ / \ / \ /
  + _ * _ . _ . _ .

```

Let's say A lands at the spot marked with a `@`. Due to how we told A to check
for points, A will assume that he is at the point marked with a `+` and will
head right. Heading right one space, A _will_ hit a person. However it will be
person `&` and not person `*` like A had thought. That's why B needs to check
their map so that A and B can see where A actually was (one dot will be
"missing" now that A and B are at the same location).

