from .functions import *

def test_square_positive_integers():
    assert square(1) == 1
    # Note the mistake here! We'll leave this here to
    # show what happens when a test fails.
    assert square(2) == 4
    assert square(4) == 16
    assert square(100) == 10000
