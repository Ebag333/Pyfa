# ===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
# ===============================================================================

from gui.graph import Graph
import service
from gui.bitmapLoader import BitmapLoader
from eos.graph import Data
import gui.mainFrame
from gnosis.gnosis import GnosisSimulation


class armorRepsGraph(Graph):
    def __init__(self):
        Graph.__init__(self)
        # self.defaults["time"] = "0-300"
        self.name = "Armor Repairs"
        self.armorReps = None
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()

    def getFields(self):
        # return self.defaults
        return None

    @staticmethod
    def getLabels():
        # return self.propertyLabelMap
        return None

    def getIcons(self):
        """
        icons = {}
        sAttr = service.Attribute.getInstance()
        for key, attrName in self.propertyAttributeMap.iteritems():
            iconFile = sAttr.getAttributeInfo(attrName).icon.iconFile
            bitmap = BitmapLoader.getBitmap(iconFile, "icons")
            if bitmap:
                icons[key] = bitmap

        return icons
        """
        return None

    def getPoints(self, fit, fields):
        capacitor_amount = fit.ship.getModifiedItemAttr("capacitorCapacity")
        capacitor_recharge = fit.ship.getModifiedItemAttr("rechargeRate")
        projected = []

        return_matrix = GnosisSimulation.capacitor_simulation(fit, projected, capacitor_amount,
                                                              capacitor_recharge)

        x = []
        y = []
        for tick in return_matrix['Matrix']['Cached Runs']:
            x.append(tick['Current Time'] / 1000)  # Divide by 1000 to give seconds
            y.append(tick['Armor Reps'])

        return x, y


armorRepsGraph.register()
