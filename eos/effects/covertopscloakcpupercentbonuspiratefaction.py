# covertOpsCloakCPUPercentBonusPirateFaction
#
# Used by:
# Ships from group: Expedition Frigate (2 of 2)
# Ship: Astero
# Ship: Victorieux Luxury Yacht
type = "passive"
runTime = "early"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Cloaking"),
                                  "cpu", ship.getModifiedItemAttr("shipBonusPirateFaction"))
