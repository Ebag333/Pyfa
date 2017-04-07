# noinspection PyPackageRequirements
import wx

from gui.preferenceView import PreferenceView
from gui.bitmapLoader import BitmapLoader

import gui.mainFrame
import gui.globalEvents as GE
from service.settings import SettingsProvider
from service.settings import GeneralSettings
from service.fit import Fit
from service.price import Price


class PFGeneralPref(PreferenceView):
    title = "General"

    def populatePanel(self, panel):
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.dirtySettings = False
        self.openFitsSettings = SettingsProvider.getInstance().getSettings("pyfaPrevOpenFits",
                                                                           {"enabled": False, "pyfaOpenFits": []})
        self.sFit = Fit.getInstance()
        self.generalSettings = GeneralSettings.getInstance()

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.stTitle = wx.StaticText(panel, wx.ID_ANY, self.title, wx.DefaultPosition, wx.DefaultSize, 0)
        self.stTitle.Wrap(-1)
        self.stTitle.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        mainSizer.Add(self.stTitle, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        mainSizer.Add(self.m_staticline1, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.cbGlobalChar = wx.CheckBox(panel, wx.ID_ANY, u"Use global character", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        mainSizer.Add(self.cbGlobalChar, 0, wx.ALL | wx.EXPAND, 5)

        self.cbGlobalDmgPattern = wx.CheckBox(panel, wx.ID_ANY, u"Use global damage pattern", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        mainSizer.Add(self.cbGlobalDmgPattern, 0, wx.ALL | wx.EXPAND, 5)

        self.cbCompactSkills = wx.CheckBox(panel, wx.ID_ANY, u"Compact skills needed tooltip", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        mainSizer.Add(self.cbCompactSkills, 0, wx.ALL | wx.EXPAND, 5)

        self.cbFitColorSlots = wx.CheckBox(panel, wx.ID_ANY, u"Color fitting view by slot", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        mainSizer.Add(self.cbFitColorSlots, 0, wx.ALL | wx.EXPAND, 5)

        self.cbReopenFits = wx.CheckBox(panel, wx.ID_ANY, u"Reopen previous fits on startup", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        mainSizer.Add(self.cbReopenFits, 0, wx.ALL | wx.EXPAND, 5)

        self.cbRackSlots = wx.CheckBox(panel, wx.ID_ANY, u"Separate Racks", wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbRackSlots, 0, wx.ALL | wx.EXPAND, 5)

        labelSizer = wx.BoxSizer(wx.VERTICAL)
        self.cbRackLabels = wx.CheckBox(panel, wx.ID_ANY, u"Show Rack Labels", wx.DefaultPosition, wx.DefaultSize, 0)
        labelSizer.Add(self.cbRackLabels, 0, wx.ALL | wx.EXPAND, 5)
        mainSizer.Add(labelSizer, 0, wx.LEFT | wx.EXPAND, 30)

        self.cbShowTooltip = wx.CheckBox(panel, wx.ID_ANY, u"Show tab tooltips", wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbShowTooltip, 0, wx.ALL | wx.EXPAND, 5)

        self.cbMarketShortcuts = wx.CheckBox(panel, wx.ID_ANY, u"Show market shortcuts", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        mainSizer.Add(self.cbMarketShortcuts, 0, wx.ALL | wx.EXPAND, 5)

        self.cbGaugeAnimation = wx.CheckBox(panel, wx.ID_ANY, u"Animate gauges", wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbGaugeAnimation, 0, wx.ALL | wx.EXPAND, 5)

        self.cbExportCharges = wx.CheckBox(panel, wx.ID_ANY, u"Export loaded charges", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        mainSizer.Add(self.cbExportCharges, 0, wx.ALL | wx.EXPAND, 5)

        self.cbOpenFitInNew = wx.CheckBox(panel, wx.ID_ANY, u"Open fittings in a new page by default",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbOpenFitInNew, 0, wx.ALL | wx.EXPAND, 5)

        self.cbShowShipBrowserTooltip = wx.CheckBox(panel, wx.ID_ANY, u"Show ship browser tooltip",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        mainSizer.Add(self.cbShowShipBrowserTooltip, 0, wx.ALL | wx.EXPAND, 5)

        priceSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.stDefaultSystem = wx.StaticText(panel, wx.ID_ANY, u"Default Market Prices:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.stDefaultSystem.Wrap(-1)
        priceSizer.Add(self.stDefaultSystem, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.chPriceSystem = wx.Choice(panel, choices=Price.systemsList.keys())
        priceSizer.Add(self.chPriceSystem, 1, wx.ALL | wx.EXPAND, 5)

        mainSizer.Add(priceSizer, 0, wx.ALL | wx.EXPAND, 0)

        # Search Item Limit
        searchLimitSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.chSearchLimitText = wx.StaticText(panel, wx.ID_ANY, u"Item Search Limit:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.chSearchLimitText.Wrap(-1)
        searchLimitSizer.Add(self.chSearchLimitText, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.editSearchLimit = wx.TextCtrl(panel, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0)
        searchLimitSizer.Add(self.editSearchLimit, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        mainSizer.Add(searchLimitSizer, 0, wx.ALL | wx.EXPAND, 0)

        self.cbGlobalChar.SetValue(self.sFit.serviceFittingOptions["useGlobalCharacter"])
        self.cbGlobalDmgPattern.SetValue(self.sFit.serviceFittingOptions["useGlobalDamagePattern"])
        self.cbFitColorSlots.SetValue(self.sFit.serviceFittingOptions["colorFitBySlot"] or False)
        self.cbRackSlots.SetValue(self.sFit.serviceFittingOptions["rackSlots"] or False)
        self.cbRackLabels.SetValue(self.sFit.serviceFittingOptions["rackLabels"] or False)
        self.cbCompactSkills.SetValue(self.sFit.serviceFittingOptions["compactSkills"] or False)
        self.cbReopenFits.SetValue(self.openFitsSettings["enabled"])
        self.cbShowTooltip.SetValue(self.sFit.serviceFittingOptions["showTooltip"] or False)
        self.cbMarketShortcuts.SetValue(self.sFit.serviceFittingOptions["showMarketShortcuts"] or False)
        self.cbGaugeAnimation.SetValue(self.sFit.serviceFittingOptions["enableGaugeAnimation"])
        self.cbExportCharges.SetValue(self.sFit.serviceFittingOptions["exportCharges"])
        self.cbOpenFitInNew.SetValue(self.sFit.serviceFittingOptions["openFitInNew"])
        self.chPriceSystem.SetStringSelection(self.sFit.serviceFittingOptions["priceSystem"])
        self.cbShowShipBrowserTooltip.SetValue(self.sFit.serviceFittingOptions["showShipBrowserTooltip"])
        self.editSearchLimit.SetValue(unicode(self.generalSettings.get("itemSearchLimit")))

        self.cbGlobalChar.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbGlobalDmgPattern.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbFitColorSlots.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbRackSlots.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbRackLabels.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbCompactSkills.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbReopenFits.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbShowTooltip.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbMarketShortcuts.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbGaugeAnimation.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbExportCharges.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.cbOpenFitInNew.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.chPriceSystem.Bind(wx.EVT_CHOICE, self.OnWindowLeave)
        self.cbShowShipBrowserTooltip.Bind(wx.EVT_CHECKBOX, self.OnWindowLeave)
        self.editSearchLimit.Bind(wx.EVT_LEAVE_WINDOW, self.OnWindowLeave)

        self.cbRackLabels.Enable(self.sFit.serviceFittingOptions["rackSlots"] or False)

        panel.SetSizer(mainSizer)
        panel.Layout()

    def getImage(self):
        return BitmapLoader.getBitmap("prefs_settings", "gui")

    def OnWindowLeave(self, event):
        self.sFit.serviceFittingOptions["rackSlots"] = self.cbRackSlots.GetValue()
        self.cbRackLabels.Enable(self.cbRackSlots.GetValue())

        self.sFit.serviceFittingOptions["priceSystem"] = self.chPriceSystem.GetString(self.chPriceSystem.GetSelection())
        self.sFit.serviceFittingOptions["colorFitBySlot"] = self.cbFitColorSlots.GetValue()
        self.sFit.serviceFittingOptions["rackLabels"] = self.cbRackLabels.GetValue()
        self.sFit.serviceFittingOptions["compactSkills"] = self.cbCompactSkills.GetValue()
        self.sFit.serviceFittingOptions["useGlobalCharacter"] = self.cbGlobalChar.GetValue()
        self.sFit.serviceFittingOptions["useGlobalDamagePattern"] = self.cbGlobalDmgPattern.GetValue()
        self.openFitsSettings["enabled"] = self.cbReopenFits.GetValue()
        self.sFit.serviceFittingOptions["showTooltip"] = self.cbShowTooltip.GetValue()
        self.sFit.serviceFittingOptions["showMarketShortcuts"] = self.cbMarketShortcuts.GetValue()
        self.sFit.serviceFittingOptions["enableGaugeAnimation"] = self.cbGaugeAnimation.GetValue()
        self.sFit.serviceFittingOptions["exportCharges"] = self.cbExportCharges.GetValue()
        self.sFit.serviceFittingOptions["openFitInNew"] = self.cbOpenFitInNew.GetValue()
        self.sFit.serviceFittingOptions["showShipBrowserTooltip"] = self.cbShowShipBrowserTooltip.GetValue()
        # Item Search Limit
        self.generalSettings.set('itemSearchLimit', int(self.editSearchLimit.GetValue()))

        fitID = self.mainFrame.getActiveFit()
        if fitID:
            fit = self.sFit.getFit(fitID)
            self.sFit.recalc(fit)
            wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=fitID))
        event.Skip()


PFGeneralPref.register()
