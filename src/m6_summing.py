"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Stephen Acomb.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    # Test 1:
    cosExpected1 = 0.13416
    cosAnswer1 = sum_cosines(3)
    print('Test 1 expected:', cosExpected1)
    print('       actual:  ', cosAnswer1)

    # Test 2:
    cosExpected2 = -0.23582
    cosAnswer2 = sum_cosines(5)
    print('Test 2 expected:', cosExpected2)
    print('       actual:  ', cosAnswer2)

    # Test 3:
    cosExpected3 = 1.47825
    cosAnswer3 = sum_cosines(7)
    print('Test 3 expected:', cosExpected3)
    print('       actual:  ', cosAnswer3)

def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------
    cosSum = 0
    for k in range(n+1):
        cosSum += math.cos(k)
    return cosSum

def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    # Test 1:
    sqrExpected1 = 1.4142135
    sqrAnswer1 = sum_square_roots(1)
    print('Test 1 expected:', sqrExpected1)
    print('       actual:  ', sqrAnswer1)

    # Test 2:
    sqrExpected2 = 3.4142135
    sqrAnswer2 = sum_square_roots(2)
    print('Test 2 expected:', sqrExpected2)
    print('       actual:  ', sqrAnswer2)

    # Test 3:
    sqrExpected3 = 11.854408
    sqrAnswer3 = sum_square_roots(5)
    print('Test 3 expected:', sqrExpected3)
    print('       actual:  ', sqrAnswer3)

def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------
    sumSqr = 0
    for k in range(n+1):
        sumSqr += math.sqrt(2*k)
    return sumSqr

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
