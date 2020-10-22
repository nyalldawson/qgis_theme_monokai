# -----------------------------------------------------------
# Copyright (C) 2020 Nyall Dawson
# -----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# ---------------------------------------------------------------------

from qgis.gui import (
    QgsGui,
    QgsCodeEditorColorScheme,
)

from qgis.PyQt.QtGui import QColor


def classFactory(iface):
    return MonokaiSchemePlugin(iface)


class MonokaiColorScheme(QgsCodeEditorColorScheme):
    COLORS = {
        QgsCodeEditorColorScheme.ColorRole.Default: QColor(248,248,242),
        QgsCodeEditorColorScheme.ColorRole.Keyword: QColor(249,38,114 ),
        QgsCodeEditorColorScheme.ColorRole.Class: QColor(102,217,239 ),
        QgsCodeEditorColorScheme.ColorRole.Method: QColor(166,226,46),
        QgsCodeEditorColorScheme.ColorRole.Decoration: QColor(254,151,31),
        QgsCodeEditorColorScheme.ColorRole.Number: QColor(174,129,255),
        QgsCodeEditorColorScheme.ColorRole.Comment: QColor(120,117,111),
        QgsCodeEditorColorScheme.ColorRole.CommentLine: QColor(120,117,111),
        QgsCodeEditorColorScheme.ColorRole.CommentBlock: QColor(120,117,111),
        QgsCodeEditorColorScheme.ColorRole.Background: QColor(39,40,34),
        QgsCodeEditorColorScheme.ColorRole.Cursor: QColor(248,248,240),
        QgsCodeEditorColorScheme.ColorRole.CaretLine: QColor(62,61,50),
        QgsCodeEditorColorScheme.ColorRole.Operator: QColor(249,38,114),
        QgsCodeEditorColorScheme.ColorRole.QuotedOperator: QColor(249,38,114),
        QgsCodeEditorColorScheme.ColorRole.Identifier: QColor(248,248,242),
        QgsCodeEditorColorScheme.ColorRole.QuotedIdentifier: QColor(248,248,242),
        QgsCodeEditorColorScheme.ColorRole.Tag: QColor(102,217,239),
        QgsCodeEditorColorScheme.ColorRole.UnknownTag: QColor(102,217,239),
        QgsCodeEditorColorScheme.ColorRole.SingleQuote: QColor(230,219,116),
        QgsCodeEditorColorScheme.ColorRole.DoubleQuote: QColor(230,219,116),
        QgsCodeEditorColorScheme.ColorRole.TripleSingleQuote: QColor(120,117,111),
        QgsCodeEditorColorScheme.ColorRole.TripleDoubleQuote: QColor(120,117,111),
        QgsCodeEditorColorScheme.ColorRole.MarginBackground: QColor(47,49,41),
        QgsCodeEditorColorScheme.ColorRole.MarginForeground: QColor(143,144,138),
        QgsCodeEditorColorScheme.ColorRole.SelectionBackground: QColor(85,84,70),
        QgsCodeEditorColorScheme.ColorRole.SelectionForeground: QColor(248,248,242),
        QgsCodeEditorColorScheme.ColorRole.MatchedBraceBackground: QColor(179,179,179),
        QgsCodeEditorColorScheme.ColorRole.MatchedBraceForeground: QColor(48,48,48),
        QgsCodeEditorColorScheme.ColorRole.Edge: QColor(70,71,65),
        QgsCodeEditorColorScheme.ColorRole.Fold: QColor(47,49,41),
        QgsCodeEditorColorScheme.ColorRole.Error: QColor("#fe4450"),
        QgsCodeEditorColorScheme.ColorRole.FoldIconForeground: QColor(143,144,138),
        QgsCodeEditorColorScheme.ColorRole.FoldIconHalo: QColor(47,49,41),
        QgsCodeEditorColorScheme.ColorRole.IndentationGuide: QColor(70,71,65),
        QgsCodeEditorColorScheme.ColorRole.ErrorBackground: QColor(255,255,255),
    }

    def __init__(self):
        super().__init__('monokai', 'Monokai')

        for role, color in self.COLORS.items():
            self.setColor(role, color)


class MonokaiSchemePlugin:
    def __init__(self, _):
        QgsGui.codeEditorColorSchemeRegistry().addColorScheme(MonokaiColorScheme())

    def initGui(self):
        pass

    def unload(self):
        QgsGui.codeEditorColorSchemeRegistry().removeColorScheme('monokai')
