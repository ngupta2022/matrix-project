import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for col in range(width)] for row in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
        """
        Calculates dot product
        """
        result = 0
        for i in range(len(vector_one)):
            result += vector_one[i] * vector_two[i]
        return result

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        deter = 0
        
        if self.h == 1:
            deter = self.g[0][0]
        elif self.h == 2 & self.w ==2: 
            deter = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        return deter

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        sum = 0
        for i in range(self.h):
            sum += self.g[i][i]
        return sum
                    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
            
        # TODO - your code here 
        inverse = zeroes(self.h, self.w)
        
        factor = 1 / (self.determinant())
        
        if self.h == 1:
            inverse[0][0] = factor
        elif self.h == 2:
            if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                raise ValueError('The matrix must be invertible.')
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]

                inverse = [[d, -b],[-c, a]]

                for i in range(inverse.h):
                    for j in range(inverse.w):
                        inverse[i][j] = factor * inverse[i][j]

        return Matrix(inverse)
     
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrixTranspose = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row_var = self.g[j][i]
                row.append(row_var)
            matrixTranspose.append(row)
        return Matrix(matrixTranspose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added when their dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                #mA = self[i][j]
                #mB = other[i][j]
                #mSum = mA + mB
                #row.append(mSum)
                row.append(self[i][j] + other[i][j])
            matrixSum.append(row)
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negative = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-1.0 * self.g[i][j])
            negative.append(row)
        return Matrix(negative)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices must have the same dimensions to be subtracted")
        
        subtraction = []
    
        for i in range(self.h):
            row = []
            for j in range(self.w):
                mSub = self.g[i][j] - other.g[i][j]
                row.append(mSub)
            subtraction.append(row)
        return Matrix(subtraction)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #

        product = []
        matrixB_T = other.T()
        
        for i in range(self.h):
            row = []
            for ii in range(other.w):
                productAB = dot_product(self.g[i], matrixB_T.g[ii])
                row.append(productAB)
            product.append(row)
            
        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            # pass
            #   
            # TODO - your code here
            #
            product = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    rmul = other * self.g[i][j]
                    row.append(rmul)
                product.append(row)
            return Matrix(product)
        
        else: 
            raise(ValueError, "Must be a number multiplied by a mnatrix")