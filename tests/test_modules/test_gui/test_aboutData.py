# Add root folder to python paths
# This must be done on every test in order to pass in Travis
import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

from gui.aboutData import versionString, licenses, developers, credits as pyfa_credits, description  # noqa: E402, E401


def test_aboutData():
    """
    Simple test to validate all about data exists
    """
    assert versionString.__len__() > 0
    assert licenses.__len__() > 0
    assert developers.__len__() > 0
    assert pyfa_credits.__len__() > 0
    assert description.__len__() > 0
