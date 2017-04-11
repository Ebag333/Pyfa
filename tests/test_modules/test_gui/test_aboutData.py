# Add root folder to python paths
# This must be done on every test in order to pass in Travis
import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

from gui.aboutData import versionString, licenses, developers, credits, description


def test_aboutData():
    """
    Simple test to validate all about data exists
    """
    assert versionString.__len__() > 0
    assert licenses.__len__() > 0
    assert developers.__len__() > 0
    assert credits.__len__() > 0
    assert description.__len__() > 0
