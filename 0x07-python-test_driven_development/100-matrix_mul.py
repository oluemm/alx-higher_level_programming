#!/usr/bin/python3
"""Defines a matirx multiplier function"""


def matrix_mul(m_a, m_b):
    """ Multiplies two matrices
    Args:
        m_a(nested list): contains integers / floating point numbers
        m_b(nested list): contains integers / floating point numbers

    Returns: A new matrix of the multiplied result
    """
    # checks m_a & m_b  to determine if they're lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # checks m_a  to determine if it is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # checks m_b to determine if it is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # checks empty list or list of lists
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")

    # checks if individual elements of matrix is an int or float
    if not all(
            (isinstance(elem, int) or isinstance(elem, float))
            for elem in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all(
            (isinstance(elem, int) or isinstance(elem, float))
            for elem in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    # checks matirx row equality
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    # checks matirx multiplication compatibility
    # for 2 matrix to be multiplied, len(m_a[0]) must be == len(m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # invert m_b
    mb_inv = []
    for e in range(len(m_b[0])):
        new_row = []
        for f in range(len(m_b)):
            new_row.append(m_b[f][e])
        mb_inv.append(new_row)

    # compute matrix multiplications
    result_matrix = []
    for row in m_a:
        new_col = []
        for col in mb_inv:
            mult = 0
            for i in range(len(mb_inv[0])):
                mult += row[i] * col[i]
            new_col.append(mult)
        result_matrix.append(new_col)

    return (result_matrix)
