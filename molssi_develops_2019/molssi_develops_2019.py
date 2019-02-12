"""
molssi_develops_2019.py
A short description of the project.

Handles the primary functions
"""
import numpy as np

def mean(num_list):
    """
    Computes the mean of a list of numbers
    Parameters
    ----------
    num_list: list of numbers

    Returns
    -------
    res: float
         Mean of the numbers in num_list
    """
    if not isinstance(num_list, list):
        raise TypeError('Invalid input %s Input must be a list' % (num_list))

    if len(num_list) < 1:
        raise ZeroDivisionError('Cannot calculate mean of an empty list')
    res = sum([ float(x) for x in num_list]) / len(num_list)

    return res


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
