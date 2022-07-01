Task 1 - Interpreter for Operations
We need our programming language to support integers. 
Our interpreter will need to take terms and interpret them into integer values. 
For that reason we will define the value VALint( i ):

def VALint(i: int) -> int:
    return i

Let’s define a term called “TMOpr” that can be interpreted into a value. TMOpr applies an operator (opr) to values v1 and v2. 
For example, let’s say we want our programming language to support adding values v1 and v2, we could write:

def TMOpr(opr: str, v1, v2):
    if opr == “+”:
        return VALint(v1 + v2)

And in order for someone using this language to do 2 + 3 they would have to call:

TMOpr(“+”, VALint(2), VALint(3)) or TMOpr(“+”, VALint(3), VALint(2))

Why is it operating on values and not terms? Terms need to be interpreted into values before they can be operated on! 
For example if we have “x + y” we first need to figure out what x and y are before we can add them up.

Using the above code as an example, add the following features to TMOpr:

Subtraction
Division
Multiplication
Greater or equal
Greater
Less than or equal to
Less than
Equal
Not Equal

For booleans, you can either create a new value called VALbool or you can use VALint(0) for False and VALint(1) for True.
