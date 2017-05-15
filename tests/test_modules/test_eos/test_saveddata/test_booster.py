# Add root folder to python paths
# This must be done on every test in order to pass in Travis
import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

# noinspection PyPackageRequirements
from _development.helpers import DBInMemory as DB, Gamedata, Saveddata  # noqa: E402, E401
from _development.helpers_fits import RifterFit, KeepstarFit  # noqa: E402, E401
from _development.helpers_items import StrongBluePillBooster  # noqa: E402, E401


def test_itemModifiedAttributes(DB, StrongBluePillBooster):  # noqa: F811
    assert StrongBluePillBooster.itemModifiedAttributes is not None


def test_isInvalid(DB, StrongBluePillBooster):  # noqa: F811
    assert StrongBluePillBooster.isInvalid is False


def test_slot(DB, StrongBluePillBooster):  # noqa: F811
    assert StrongBluePillBooster.slot == 1


def test_item(DB, Gamedata, StrongBluePillBooster):  # noqa: F811
    assert isinstance(StrongBluePillBooster.item, Gamedata['Item'])


def test_clear(DB, StrongBluePillBooster):  # noqa: F811
    try:
        StrongBluePillBooster.clear()
        assert True
    except:
        assert False
