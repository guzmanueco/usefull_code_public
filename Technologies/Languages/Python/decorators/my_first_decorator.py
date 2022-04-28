from functools import wraps

def multiply_elements_by_two(func):
    """
    Multiplies every numeric argument in a function by 2.
    Parameters:
    -----------
    func : python function
    Returns:
    --------
    The input function will now multiply by two its arguments before running
    """
    @wraps(func)
    def wrapper(*args):
        ls = [*args]
        for i,e in enumerate(ls):
            ls[i]*=2
        return func(*ls)
    return wrapper

@multiply_elements_by_two
def multiply(*ls):
    """
    Multiplies every element in the input ls
    Parameters:
    ------------
    ls : list
        list of numeric values
    
    Returns:
    --------
    the result of multiplying every element in the list
    """
    result=0
    for i, e in enumerate(ls):
        if i == 0:
            result=ls[i]
        else:
             result*=ls[i]
    return result

def multiply_by_n_elements(n):
    """
    Multiplies every numeric argument in a function by n.
    Parameters:
    -----------
    func : python function
    Returns:
    --------
    The input function will now multiply by n its arguments before running
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            ls = [*args]
            for i,e in enumerate(ls):
                ls[i]*=n
            return func(*ls)
        return wrapper
    return decorator

@multiply_by_n_elements(5)
def multiply_2_el(*ls):
    """
    Returns the product of the two elements of the input list
    Parameters:
    -----------
    ls : list
        list with two numeric values
    
    Returns:
    ---------
    The prodcut of the two elements of ls
    """
    result=0
    for i, e in enumerate(ls):
        if i == 0:
            result=ls[i]
        else:
            result*=ls[i]
    return result