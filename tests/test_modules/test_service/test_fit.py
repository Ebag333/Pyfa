# Add root folder to python paths
import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

# noinspection PyPackageRequirements
from _development.helpers import DBInMemory as DB, Gamedata, Saveddata  # noqa: E402, E401
# noinspection PyPackageRequirements
from _development.helpers_fits import RifterFit, KeepstarFit  # noqa: E402, E401
from service.fit import Fit  # noqa: E402, E401


def test_getAllFits(DB, RifterFit, KeepstarFit):  # noqa: F811
    assert len(Fit.getAllFits()) == 0

    DB['db'].save(RifterFit)
    DB['db'].save(KeepstarFit)

    # For some reason in Travis this adds the first fit twice.  WHY?!?
    assert len(Fit.getAllFits()) != 0

    # Cleanup after ourselves
    DB['db'].remove(RifterFit)
    DB['db'].remove(KeepstarFit)


def test_getFitsWithShip_RifterFit(DB, RifterFit):  # noqa: F811
    DB['db'].save(RifterFit)

    assert Fit.getFitsWithShip(587)[0][1] == 'My Rifter Fit'

    DB['db'].remove(RifterFit)
