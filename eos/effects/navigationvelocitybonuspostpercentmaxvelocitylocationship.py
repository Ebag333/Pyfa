# navigationVelocityBonusPostPercentMaxVelocityLocationShip
#
# Used by:
# Implant: Low-grade Snake Alpha
# Implant: Mid-grade Snake Alpha
type = "passive"


def handler(fit, implant, context):
    fit.ship.boostItemAttr("maxVelocity", implant.getModifiedItemAttr("velocityBonus"))
