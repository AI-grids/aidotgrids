"""Tests loading of standardized tasks for OPFData.


Example usage:
--------------
    $ python tests/test_opfdata.py

"""

import sys
sys.path.append("src/aidotgrids")
import load

root_path = "<Provide your path to data root repo>"
(
    train_data, 
    val_data, 
    test_data
) = load.load_task(
    "OPFData", 
    "train_medium_test_small", 
    root_path,
    data_frac = 0.01,
    train_frac = 0.1
)

print("Successfully executed 'test_opfdata.py'!")