# Problem A6, 2001 Putnam Competition

Can the arc length of a parabola inside a circle of radius 1 have arc length
greater than 4?

Using python and matplotlib, this little project makes a dumb plot of the unit
circle and the kind of parabola of interest for this problem.

We then embed this plot in a writeup to the the solution of the problem. The
writeup was produced by the LyX and LaTeX in the TeX application stack
came very close to finding this solution on my own back in 2002 or so and
later found it somewhere on the web. I can't find it now. I'd like to do
proper attribution of this solution, so drop me a line if you know where to
find it.

Other solutions to this problem found by Google search are either not as
complete or not as elegant as this one.  All mildly interesting, but the point
for me was to use this problem as a laboratory for making simple plots of
the sort you'd include in a math text. Fiddling was required in the following
areas:

* python/matplotlb: axis positioning, image dimensions, tick label positioning
* LyX/LaTeX: TeX "figure wrap float" parameters, equation spacing, inline display fractions , spacing after the radical sign

I'll be sticking in some specific notes about this fiddling in the near future.
