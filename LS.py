# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LiveStats
                                 A QGIS plugin
 Display live statistics about vector selections
                              -------------------
        begin                : 2012-12-30
        copyright            : (C) 2012 by Olivier Dalang
        email                : olivier.dalang@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import resources

from LSstat import LSstat


class LS:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        self.stats = []

    def initGui(self):        
        self.createStat()

    def unload(self):
        for stat in self.stats:
            stat.setParent(None)

    def createStat(self):
        self.stats.append( LSstat(self.iface) )

    """
    def getStat(self, name):
        for stat in self.stats:
            if stat.name == name:
                return stat.result
        return None"""