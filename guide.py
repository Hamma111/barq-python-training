# the built-in imports should always be at the top
import os
from datetime import datetime

# third party imports after that with a new line space
import pandas
import selenium

# custom import after that with a new line space
from utils import get_scraped_product, output_csv


def my_strange_function(param1, param2):
    param3 = param1 * param2
    param3 = param1 - 10

    return param3  # there should always be a one line space above return statement


# class names should always be Camel Case like this
class EvenStrangeClass:
    pass


# constant variables should always be upper snake case
EID_DATETIME_STR = datetime(2023, 4, 22, 0, 0)

# normal variables and function names should always be in lower snake case
time_left_in_eid = EID_DATETIME_STR - datetime.now()


# Try to move functions in separate files such as utils.py or helpers.py or scraper.py 
# This will make your code look neater and will be more re-usable


# guid-lines for pull requests
"""
- no useless unwanted files in PR. Delete those, or add those to .gitignore
- no commented or unwanted code in PR
- no incomplete PR
- no spelling mistakes in PR
- always add comments in PR
"""
