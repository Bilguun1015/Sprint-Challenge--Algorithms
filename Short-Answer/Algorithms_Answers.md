#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3)
first line equals to O(1) because it is constant
second line we have a loop that has n^3 so it is O(n^3)
and third line is also constant even though is n^2 it will be constant 0(1)
biggest 

b) O(n^2)
first line = 0(1)
second line equals O(n) because n is the range of the for loop
third line is constant 0(1)
fourth line is another loop dependent on n so O(n)
since the loops are inside each other multiply together to get O(n^2)

c) O(n)
if we give 1 bunny as an argument it is going to get called once because when it hits 0 it stops
so the function is getting called however times that the bunnies number


## Exercise II

def finding_f_floor(n):
    base cases:
    if n equals highest possible floor
    then
    it returns n
    if n equals nth floor
    it returns n
    
    x equals n divided by 2
    thrown = throw_egg(x)
        if thrown is broken
        then
            return finding_f_floor(x)
        else
            x = x + x/2
            return finding_f_floor(x)


