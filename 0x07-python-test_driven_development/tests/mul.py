# Trying out relative imports
# using sys module
import sys
sys.path.append("..")

# using __import__
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[3, 6, 9],[12, 15, 18]]
print(matrix_divided(matrix, 3))