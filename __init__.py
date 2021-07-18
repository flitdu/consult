# -*- coding: utf-8 -*-


def datapath(fname):
    """Get full path for file `fname` in test data directory placed in this module directory.
    Usually used to place corpus to test_data directory.

    """
    return os.path.join(module_path, fname)
