Task 2 - Evaluating Functions
In this task we will write code to simplify two polynomial expressions.

First we’ll define a polynomial function in a similar way as above.
A polynomial expression is the successive multiplication, division, addition or subtraction of a variable X and constants. 
For example,

X2 + 1 is a second degree polynomial and can be decomposed into:

Add( Mul( X() , X() ), Int(1) )

We can write the following code to define expressions:

https://github.com/KrishNath2010/Making-a-Programming-Language-From-Scratch/pull/1 

Finish the above implementation to support all operations (division and subtraction). 
Print the following polynomial to the command line: (7X3 + 2X5 + 3X - 4) / (2X2).
