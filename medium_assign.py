'''

This file contains the functions that you need for completing this assignment. 

1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def expression_1(x):
    import math
    var_1= math.pow(x,3)
    var_2= 2*x + math.pow(x,2)
    var_3= 100
    result_1= var_1-var_2-var_3
    print(result_1)


    '''
    
        Write a code that returns value for the following expression: x^3 - (2x + x^2) - 100 
    
    '''

   

def expression_2(x, y):
    import math
    value_1= (math.pow(x,4)) / (2*y)
    value_2= 3*x*y
    value_3= (6*y)/(7*x)
    result_2= value_1 - value_2 + value_3
    print(math.trunc(result_2))


    '''
        Write code that returns only the integer value of the following expression: (x^4 / 2y) - (3xy) + (6y / 7x)
    '''

  


def expression_3(x, y):
    import math
    var_1= math.pow(x,3) + math.pow(y,2)
    var_2= math.pow(x,2) - math.pow(y,3)
    result_3= var_1 / var_2
    print(result_3)

    '''
        Write code that returns the value of the following expression: (x^3 + y^2) / (x^2 - y^3)
    '''

if __name__ == "__main__":
    expression_1(3)
    expression_2(3, 4)
    expression_3(3,4)
