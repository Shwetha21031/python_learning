# tdd (Test driven development) = set of programs and software design principles based on
# fail test -> fix code -> pass test -> fail new test

# 1. you may not write production code unless you've first written a failing unit test
# 2. you may not write more of a unit test than is sufficient to fail
# 3 . you may not write more production code than is sufficient to make the failing unit test pass


# import builtin python module 
# import unittest

# encapsulate all the future test in this class , must inherit unittest class
# class testing (unittest.TestCase):
#  It allows you to create test cases by defining methods within a subclass of unittest.TestCase
# body will consist of all the tests
# in general we initialize inside __init__ method , in testcase class we initialize inside setUp method

# first portion of test method must be "test_"
# so that the testing framework can identify and execute them as part of the test suite. 

# assertions 
# Assertions are statements that check if a given condition is true during the execution of a program. 
# When an assert statement is encountered, it evaluates the accompanying expression, which is expected to be true. If the expression is false, Python raises an AssertionError exception.

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug


# to run a test in cmd
#  python -m unittest test_calc.py
#   or 
# if __name__  == '__main__':
    # unittest.main()
# in terminal
#  py test_calc.py



# setUp():
# this code runs before every other tests

# tesrDown(): 
# executes after werun everysingle test
# - eg created a file during testing and want to remove them in the end


# test dosent run in order


# setUp class - runs once before everything
# teardown class - runs once after everything
# eg setup database


# setup class called
# setup called
# terdown called
# .setup called
# terdown called
# .setup called
# terdown called
# .teardown class called

# mocking
# from unittest.mock import patch