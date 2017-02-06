# shipShieldThermalResistanceCF2
#
# Used by:
# Variations of ship: Merlin (3 of 4)
# Ship: Cambion
# Ship: Whiptail
type = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("shieldThermalDamageResonance", ship.getModifiedItemAttr("shipBonusCF"),
                           skill="Caldari Frigate")
