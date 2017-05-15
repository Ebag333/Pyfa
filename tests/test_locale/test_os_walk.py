import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

from _development.helpers_locale import GetPath  # noqa: E402


def test_os_walk():
    current_directory = os.path.dirname(os.path.abspath(unicode(__file__)))
    subfolders = os.listdir(current_directory)
    subfolders = [e for e in subfolders if not (e.endswith(".py") or e.endswith(".pyc") or e.endswith(".md"))]

    subfolder_count = 0
    for subfolder in subfolders:
        subdir = GetPath(current_directory, subfolder)
        testfile = GetPath(subdir, "testcodec")

        if "__pycache__" in testfile:
            # Grabbed a Travis temp folder, skip any assertions, but count it.
            subfolder_count += 1
            continue

        # noinspection PyBroadException
        try:
            with open(testfile, 'r') as f:
                read_data = f.read()
            # noinspection PyStatementEffect
            f.closed
        except:
            print("Test File:")
            print(testfile)
            assert False, "Failed to read file."

        read_data = read_data.replace("\n", "")
        assert read_data == "True"
        subfolder_count += 1

    assert len(subfolders) == subfolder_count
