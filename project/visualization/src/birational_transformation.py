def quadratic_transform(expr, iterations=1, x='(y*z)', y='(x*z)', z='(x*y)'):
    """
    Maps (x, y, z) to (yz, xz, xy)
    Optional argument, number of iterations of map
    """
    if iterations == 0:
        return expr

    for i in range(iterations):
        new_string = ""
        for char in expr:
            if char == 'x':
                new_string += x
            elif char == 'y':
                new_string += y
            elif char == 'z':
                new_string += z
            else:
                new_string += char
            expr = new_string
        
    return new_string
