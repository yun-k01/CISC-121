def bisection_zero(f_x, a_0, b_0):
    """
    -------------------------------------------------------
    Finds one zero of the polynomial by using the bisection method.
    Use: zero_f = bisection_zero(f_x,a_0,b_0)
    -------------------------------------------------------
    Parameters:
        f_x - a polynomial function (list)
        a_0 - a test point with f(a_0) < 0 (float)
        b_0 - a test point with f(b_0) > 0 (float)
    Returns:
        zero_f - a zero of the polynomial f(zero_f) = 0 (float)
    -------------------------------------------------------
    """
    
    m_0 = (a_0 + b_0)/2  # this represents the initial midpoint of the function given by a_0 and b_0
    m_i = m_0  # this represents future midpoints of the function 
    
    loop = 1
    while loop != 0:

        n = len(f_x)-1 #this is the degree of the polynomial
        f_val = f_x[0]*m_i**(n) #initialize
        
        
        for i in range(1,n+1): #watch indices
            f_val += f_x[i]*(m_i**(n-i)) #sum each remaining term
        
        if round(f_val, 3) == 0:
            zero_f = m_i
            loop = 0
            
        elif f_val < 0:
            if n % 2 == 0:  # if the highest degree of the polynomial is even, m_i will decrease 
                m_i -= 0.01
            else:           # if the highest degree of the polynomial is odd, m_i will increase 
                m_i += 0.01
            
        else: 
            if n % 2 == 0:  # if the highest degree of the polynomial is even, m_i will increase 
                m_i += 0.01
            else:           # if the highest degree of the polynomial is odd, m_i will decrease 
                m_i -= 0.01
            
    return(format(zero_f,',.3f'))
    
    
    