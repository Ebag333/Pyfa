# Add root folder to python paths
# This must be done on every test in order to pass in Travis
import math
import os
import sys

sys.path.append(os.path.realpath(os.getcwd()))

# noinspection PyPackageRequirements
from _development.helpers import DBInMemory as DB, Gamedata, Saveddata  # noqa: E402, E401
from _development.helpers_fits import RifterFit  # noqa: E402, E401


def test_multiply_stacking_penalties(DB, Saveddata, RifterFit):  # noqa: F811
    """
    Tests the stacking penalties under multiply
    """
    char0 = Saveddata['Character'].getAll0()

    RifterFit.character = char0
    em_resist = RifterFit.ship.getModifiedItemAttr("shieldEmDamageResonance")

    mod = Saveddata['Module'](DB['db'].getItem("EM Ward Amplifier II"))
    item_modifer = mod.item.getAttribute("emDamageResistanceBonus")

    RifterFit.calculateFitAttributes()

    for _ in range(10):
        if _ == 0:
            # First run we have no modules, se don't try and calculate them.
            calculated_resist = RifterFit.ship.getModifiedItemAttr("shieldEmDamageResonance")
        else:
            # Calculate what our next resist should be
            # Denominator: [math.exp((i / 2.67) ** 2.0) for i in xrange(8)]
            current_effectiveness = 1 / math.exp(((_ - 1) / 2.67) ** 2.0)
            new_item_modifier = 1 + ((item_modifer * current_effectiveness) / 100)
            calculated_resist = (em_resist * new_item_modifier)

            # Add another resist module to our fit.
            RifterFit.modules.append(mod)

        # Modify our fit so that Eos generates new numbers for us.
        RifterFit.clear()
        RifterFit.calculateFitAttributes()

        em_resist = RifterFit.ship.getModifiedItemAttr("shieldEmDamageResonance")

        assert em_resist == calculated_resist
        # print(str(em_resist) + "==" + str(calculated_resist))
