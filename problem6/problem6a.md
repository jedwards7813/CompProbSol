# Problem 6a "Writing Function Files in Python"
## Outcomes
- Use the function syntax in Python
- Import and execute functions from a package you create
 
## Problem 

Now it's time to learn to write and call functions in Python. The syntax/structure is not the same as MATLAB, so it might be a good idea to make a list of the differences. 

- a file can hold any number of functions
- the file containing the functions can itself be called a `package`
- you must load the file/`package` or specific functions with in the file in order to call them in Python

Okay let's make a package! Open the python file `motion.py` in the problem6 folder on CompProbSol. This is the starting point for the assignment. There should already be 2 function definitions in the file:

```python
def projectile(v,ang,h,g):
    
    return r,tf,hmax    
    
def freefall(h,v,g):
    
    return vf,tf
```

`projectile` should take a launch velocity, launch angle, initial height, and acceleration due to gravity and return range, time of flight, and maximum height. `freefall` should be a 1D projectile calculator that takes initial height, initial velocity, and acceleration due to gravity and returns final velocity and time of flight (to return to "ground" h=0). **(Please note that you already have much of this code in MATLAB, this should be an exercise of comparing and contrasting syntax amongst different languages).** You should set default values for all these quantities. In addition, I would like you to create 3 additional functions that convert units: 
1. meters to feet and vice versa
1. amongst meters per second, miles per hour, and ft/s
1. degrees to radians and vice versa

and 1 function that graphs the trajectory of the particle; this function should be called in your `projectile` function - so that it returns a graph of the trajectory (*y* vs *x*)

When you are done with these functions and you have checked that they work (**oooo, come up with some good test cases and check with an online calculator**), I want you to open a Jupyter Notebook, call it `motiontest.ipynb`, import your package, and call your function with inputs and without inputs (show off your default values). Push `motion.py` and your notebook up to github.
