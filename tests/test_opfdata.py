"""Tests loading of standardized tasks for OPFData.


Example usage:
--------------
    $ python tests/test_opfdata.py

or
    $ pytest

"""
import string
import random

from aidotgrids import load

# create a random root path name
root_path = "~/AI-grid/test_opfdata_".join(
    random.choice(string.ascii_letters) for _ in range(7)
)


dataset = load.load_task(
    "OPFData", 
    "train_medium_test_small", 
    root_path,
    data_frac = 0.01,
    train_frac = 0.1
)

print("Successfully executed 'test_opfdata.py'!")