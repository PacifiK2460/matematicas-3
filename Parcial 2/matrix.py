import numpy as np
import sympy as sp

def gauss_jordan(a, b):
    # Convert the matrices to sympy.Matrix for pretty printing and LaTeX conversion
    a = sp.Matrix(a)
    b = sp.Matrix(b)
    
    # Augment the two matrices
    ab = a.row_join(b)
    
    print("Initial augmented matrix:")
    print(sp.latex(ab))
    
    # Perform Gauss-Jordan elimination
    rows, cols = ab.shape
    for i in range(rows):
        # Find maximum in this column
        max_el = abs(ab[i,i])
        max_row = i
        for k in range(i+1, rows):
            if abs(ab[k,i]) > max_el:
                max_el = abs(ab[k,i])
                max_row = k

        # Swap maximum row with current row (column by column)
        for k in range(i, cols):
            tmp = ab[max_row,k]
            ab[max_row,k] = ab[i,k]
            ab[i,k] = tmp

        #print(f"Step {i+1}: Swap row {max_row+1} with row {i+1}")
        print(f"\\underrightarrow{{ R_{{{max_row+1}}} \\leftrightarrow R_{{{i+1}}} }}")
        print(sp.latex(ab))

        # Make all rows below this one 0 in current column
        for k in range(i+1, rows):
            c = -ab[k,i]/ab[i,i]
            for j in range(i, cols):
                if i == j:
                    ab[k,j] = 0
                else:
                    ab[k,j] += c * ab[i,j]

            print(f"\\underrightarrow{{ R_{k+1} + ({sp.latex(c)})R_{i+1} }}")
            if k%2 == 0:
              print(f"\\\\")
            print(sp.latex(ab))

    # Make diagonal elements 1 and all elements above diagonal 0
    for i in range(rows-1, -1, -1):
        divisor = ab[i,i]
        for j in range(cols-1, -1, -1):
            ab[i,j] /= divisor

        print(f"\\underrightarrow{{ \\frac{{R_{i+1}}}{{{sp.latex(divisor)}}} }}")
        print(sp.latex(ab))

        # Make all rows above this one 0 in current column
        for k in range(i-1, -1, -1):
            c = -ab[k,i]/ab[i,i]
            for j in range(cols-1, -1, -1):
                if i == j:
                    ab[k,j] = 0
                else:
                    ab[k,j] += c * ab[i,j]

            print(f"\\underrightarrow{{ R_{k+1} + ({sp.latex(c)})R_{i+1} }}")
            if k%2 == 0:
              print(f"\\\\")
            print(sp.latex(ab))

# Define your matrices here
a = np.array([ [1/2,-1/3,0] , [-7, 0,-7], [0,2,1/5] ])
b = np.array([ [0] , [0], [0] ])

gauss_jordan(a, b)
