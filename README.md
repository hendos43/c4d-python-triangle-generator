# c4d-python-triangle-generator
Specify 3 angles, draw a triangle polygon in C4D using a python generator with a base length of 1 (tiny!)

## Instructions:
- Make a python generator object in C4D
- load this file
- change angles as appropriate at the top of this script
- enjoy your triangular polygon

## Notes:
- disable the object after you have your triangle generated to avoid making multiple when the python script is re-executed
- the base length of the triangle is 1 so it's probably very tiny if you can't see it
- points are generated/named like so: https://www.calculator.net/triangle-calculator.html?vc=45&vx=&vy=&va=72&vz=1&vb=63&angleunits=d&x=36&y=28
- there is some unnecessary calculation but leaving it like this so the process is very clear
- to make a spline, select the edges of the triangle and use C4D's 'Edge to Spline' function
