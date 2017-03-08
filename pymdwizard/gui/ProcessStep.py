#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a Process Step <procstep> section


SCRIPT DEPENDENCIES
------------------------------------------------------------------------------
    None


U.S. GEOLOGICAL SURVEY DISCLAIMER
------------------------------------------------------------------------------
Any use of trade, product or firm names is for descriptive purposes only and
does not imply endorsement by the U.S. Geological Survey.

Although this information product, for the most part, is in the public domain,
it also contains copyrighted material as noted in the text. Permission to
reproduce copyrighted items for other than personal use must be secured from
the copyright owner.

Although these data have been processed successfully on a computer system at
the U.S. Geological Survey, no warranty, expressed or implied is made
regarding the display or utility of the data on any other system, or for
general or scientific purposes, nor shall the act of distribution constitute
any such warranty. The U.S. Geological Survey shall not be held liable for
improper or incorrect use of the data described and/or contained herein.

Although this program has been used by the U.S. Geological Survey (USGS), no
warranty, expressed or implied, is made by the USGS or the U.S. Government as
to the accuracy and functioning of the program and related program material
nor shall the fact of distribution constitute any such warranty, and no
responsibility is assumed by the USGS in connection therewith.
------------------------------------------------------------------------------
"""

from lxml import etree

from PyQt5.QtGui import QPainter, QFont, QPalette, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QComboBox, QTableView
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPlainTextEdit
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint



from pymdwizard.core import utils
from pymdwizard.core import xml_utils

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_ProcessStep
from pymdwizard.gui.single_date import SingleDate


class ProcessStep(WizardWidget): #

    drag_label = "Process Step <procstep>"


    def build_ui(self):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_ProcessStep.Ui_Form()#.Ui_USGSContactInfoWidgetMain()
        self.ui.setupUi(self)
        self.setup_dragdrop(self)

        self.single_date = SingleDate()
        self.single_date.ui.lbl_format.deleteLater()
        self.single_date.ui.label.deleteLater()

        self.ui.fgdc_procdate.setLayout(QVBoxLayout(self))
        self.ui.fgdc_procdate.layout().insertWidget(0, self.single_date)



    def dragEnterEvent(self, e):
        """
        Only accept Dragged items that can be converted to an xml object with
        a root tag called 'procstep'
        Parameters
        ----------
        e : qt event

        Returns
        -------
        None

        """
        print("pc drag enter")
        mime_data = e.mimeData()
        if e.mimeData().hasFormat('text/plain'):
            parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            element = etree.fromstring(mime_data.text(), parser=parser)
            if element.tag == 'procstep':
                e.accept()
        else:
            e.ignore()


         
                
    def _to_xml(self):
        """
        encapsulates the QPlainTextEdit text in an element tag

        Returns
        -------
        procstep element tag in xml tree
        """
        procstep = etree.Element('procstep')
        procdesc = etree.Element('procdesc')
        procdesc.text = self.findChild(QPlainTextEdit, "fgdc_procdesc").toPlainText()
        procstep.append(procdesc)

        procdate = etree.Element('procdate')
        date_var = self.single_date.findChild(QLineEdit, "lineEdit").text()
        procdate.text = date_var
        procstep.append(procdate)

        return procstep

    def _from_xml(self, xml_processstep):
        """
        parses the xml code into the relevant procstep elements

        Parameters
        ----------
        process_step - the xml element status and its contents

        Returns
        -------
        None
        """
        try:
            if xml_processstep.tag == 'procstep':
                #print xml_processstep.text[0]
                procdesc = xml_processstep.xpath('procdesc/text()')
                pd_text = str(procdesc[0])
                self.findChild(QPlainTextEdit, "fgdc_procdesc").setPlainText(pd_text)

                procdate = xml_processstep.xpath('procdate/text()')
                date_text = str(procdate[0])
                date_edit = self.single_date.findChild(QLineEdit, "lineEdit")
                date_edit.setText(date_text)
            else:
                print ("The tag is not procstep")
        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(ProcessStep,
                        "Process Step testing")

