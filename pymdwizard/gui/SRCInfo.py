#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a SRCInfo <srcinfo> section


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
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QComboBox, QTableView, QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPlainTextEdit, QRadioButton, QFrame
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle, QScrollArea, QGroupBox
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint



from pymdwizard.core import utils
from pymdwizard.core import xml_utils

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_SRCInfo #
from pymdwizard.gui.single_date import SingleDate
from pymdwizard.gui.multiple_instances import Multi_Instance


class SRCInfo(WizardWidget): #

    drag_label = "SRCInfo <srcinfo>"


    def build_ui(self):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_SRCInfo.Ui_Form()
        self.ui.setupUi(self)
        self.setup_dragdrop(self)
        self.single_date = SingleDate()
        self.single_date.ui.lbl_format.deleteLater()
        self.single_date.ui.label.deleteLater()
        self.beg_date = SingleDate()
        self.beg_date.ui.lbl_format.deleteLater()
        self.beg_date.ui.label.deleteLater()
        self.end_date = SingleDate()
        self.end_date.ui.lbl_format.deleteLater()
        self.end_date.ui.label.deleteLater()

        self.ui.fgdc_pubdate.setLayout(QVBoxLayout(self))
        self.ui.fgdc_pubdate.layout().insertWidget(0, self.single_date)

        self.ui.fgdc_begdate.setLayout(QVBoxLayout(self))
        self.ui.fgdc_begdate.layout().insertWidget(0, self.beg_date)

        self.ui.fgdc_enddate.setLayout(QVBoxLayout(self))
        self.ui.fgdc_enddate.layout().insertWidget(0, self.end_date)

        #Multi_Inst onlink
        olParams = {'Title':'Online Link for the Data Set',
                  'Italic Text':'Is there a link to the data?',
                  'Label': 'Link',
                  'Add text':'+',
                  'Remove text': '-'}
                  #'widget':SingleDate}
        self.multi_instance = Multi_Instance(params=olParams)
        self.ui.fg_dc_onlink.layout().insertWidget(0, self.multi_instance)




    def connect_events(self):
        """
        Connect the appropriate GUI components with the corresponding functions

        Returns
        -------
        None
        """
        #self.ui.radioButton.toggled.connect(self.include_lworkext_change)



    def dragEnterEvent(self, e):
        """
        Only accept Dragged items that can be converted to an xml object with
        a root tag called 'srcinfo'

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
            if element.tag == 'srcinfo':
                e.accept()
        else:
            e.ignore()


         
                
    def _to_xml(self):
        """
        encapsulates the QLineEdit text in an element tag

        Returns
        -------
        srcinfo element tag in xml tree
        """
        #lineage = etree.Element('lineage')
        srcinfo = etree.Element('srcinfo')
        srccite = etree.Element('srccite')
        citeinfo = etree.Element('citeinfo')


        origin = etree.Element("origin")
        pubdate = etree.Element("pubdate")
        geoform = etree.Element("geoform")
        title = etree.Element("title")
        citeinfo.append(origin)

        date_var = self.single_date.findChild(QLineEdit, "lineEdit").text()
        pubdate.text = date_var

        origin.text = self.findChild(QLineEdit, "fgdc_origin").text()
        title.text = self.findChild(QLineEdit, "fgdc_title").text()
        geoform.text = self.findChild(QComboBox, "fgdc_geoform").currentText()

        citeinfo.append(origin)
        citeinfo.append(pubdate)
        citeinfo.append(title)
        citeinfo.append(geoform)


        pubinfo = etree.Element("pubinfo")
        pubplace = etree.Element("pubplace")
        pubplace.text = self.findChild(QLineEdit, "fgdc_pubplace").text()
        publish = etree.Element("publish")
        publish.text = self.findChild(QLineEdit, "fgdc_publish").text()
        pubinfo.append(pubplace)
        pubinfo.append(publish)
        citeinfo.append(pubinfo)

        cnt = 0
        len_listonlink = len(self.multi_instance.widget_instances)
        while cnt < len_listonlink:
            linEdit1 = self.multi_instance.widget_instances[cnt].findChildren(QLineEdit)
            ol_text = linEdit1[0].text()
            str_ol = str(ol_text)
            onlink = etree.Element("onlink")
            onlink.text = str_ol
            cnt +=1
            citeinfo.append(onlink)
        else:
            pass

        srccite.append(citeinfo)

        srcscale = etree.Element("srcscale")
        srcscale.text = self.findChild(QLineEdit, "fgdc_srcscale").text()

        typesrc = etree.Element("typesrc")
        typesrc.text = self.findChild(QComboBox, "fgdc_typesrc").currentText()

        srcinfo.append(srccite)
        srcinfo.append(srcscale)
        srcinfo.append(typesrc)

        srctime = etree.Element("srctime")
        timeinfo = etree.Element("timeinfo")
        begdate = etree.Element("begdate")
        enddate = etree.Element("enddate")

        beg_var = self.beg_date.findChild(QLineEdit, "lineEdit").text()
        begdate.text = beg_var
        timeinfo.append(begdate)
        end_var = self.end_date.findChild(QLineEdit, "lineEdit").text()
        enddate.text = end_var
        timeinfo.append(enddate)
        srctime.append(timeinfo)

        srccurr = etree.Element("srccurr")
        srccurr.text = self.findChild(QComboBox, "fgdc_srccurr").currentText()
        srctime.append(srccurr)

        srccitea = etree.Element("srccitea")
        srccontr = etree.Element("srccontr")
        srccitea.text = self.findChild(QLineEdit, "fgdc_srccitea").text()
        srccontr.text = self.findChild(QLineEdit, "fgdc_srccontr").text()

        srcinfo.append(srctime)
        srcinfo.append(srccitea)
        srcinfo.append(srccontr)

        return srcinfo

    def _from_xml(self, xml_srcinfo):
        """
        parses the xml code into the relevant srcinfo elements

        Parameters
        ----------
        srcinfo - the xml element status and its contents

        Returns
        -------
        None
        """
        try:
            if xml_srcinfo.tag == "srcinfo":
                origin = xml_srcinfo.xpath('srccite/citeinfo/origin/text()')
                og_text = str(origin[0])
                self.findChild(QLineEdit, "fgdc_origin").setText(og_text)

                pubdate = xml_srcinfo.xpath('srccite/citeinfo/pubdate/text()')
                date_text = str(pubdate[0])
                self.single_date.findChild(QLineEdit, "lineEdit").setText(date_text)

                title = xml_srcinfo.xpath('srccite/citeinfo/title/text()')
                title_text = str(title[0])
                self.findChild(QLineEdit, "fgdc_title").setText(title_text)

                geoform = xml_srcinfo.xpath('srccite/citeinfo/geoform/text()')
                geoform_text = str(geoform[0])
                self.findChild(QComboBox, "fgdc_geoform").setCurrentText(geoform_text)


                place = xml_srcinfo.xpath('srccite/citeinfo/pubinfo/pubplace/text()')
                place_text = str(place[0])
                self.findChild(QLineEdit, "fgdc_pubplace").setText(place_text)

                lish = xml_srcinfo.xpath('srccite/citeinfo/pubinfo/publish/text()')
                lish_text = str(lish[0])
                self.findChild(QLineEdit, "fgdc_publish").setText(lish_text)

                scale = xml_srcinfo.xpath('srcscale/text()')
                scale_text = str(scale[0])
                self.findChild(QLineEdit, "fgdc_srcscale").setText(scale_text)

                typesrc = xml_srcinfo.xpath('typesrc/text()')
                typesrc_text = str(typesrc[0])
                self.findChild(QComboBox, "fgdc_typesrc").setCurrentText(typesrc_text)

                srccitea = xml_srcinfo.xpath('srccitea/text()')
                srccitea_text = str(srccitea[0])
                self.findChild(QLineEdit, "fgdc_srccitea").setText(srccitea_text)

                srccontr = xml_srcinfo.xpath('srccontr/text()')
                srccontr_text = str(srccontr[0])
                self.findChild(QLineEdit, "fgdc_srccontr").setText(srccontr_text)

                begdate = xml_srcinfo.xpath('srctime/timeinfo/begdate/text()')
                begdate_text = str(begdate[0])
                self.beg_date.findChild(QLineEdit, "lineEdit").setText(begdate_text)

                enddate = xml_srcinfo.xpath('srctime/timeinfo/enddate/text()')
                enddate_text = str(enddate[0])
                self.end_date.findChild(QLineEdit, "lineEdit").setText(enddate_text)

                srccurr = xml_srcinfo.xpath('srctime/srccurr/text()')
                srccurr_text = str(srccurr[0])
                self.findChild(QComboBox, "fgdc_srccurr").setCurrentText(srccurr_text)

                list_onlink = [b.text for b in xml_srcinfo.iterfind("srccite/citeinfo/onlink")]
                lenOL = len(list_onlink)
                cnt = 0
                for lw in list_onlink[:1]:
                    line_edit = self.multi_instance.findChild(QLineEdit)
                    print list_onlink[cnt]
                    line_edit.setText(list_onlink[cnt])
                cnt =+ 1
                for lw in list_onlink[2:]:
                    self.multi_instance.add_another()
                    scroll = self.multi_instance.findChild(QScrollArea, 'scrollArea')
                    line_edit = scroll.findChild(QLineEdit)
                    line_edits = scroll.findChildren(QLineEdit)
                    print line_edits
                    print lw
                    line_edit(cnt).setText(lw)
                    print line_edit[cnt]
                    cnt += 1


                #
                # if srcinfo.findall("citeinfo/title"):
                #     title_text = srcinfo.findtext("citeinfo/title")
                #
                #     title_box = self.findChild(QLineEdit, 'fgdc_title')
                #     title_box.setText(title_text)
                # else:
                #     print ("No title tag")
                #
                # if srcinfo.findall("citeinfo/edition"):
                #     edition_text = srcinfo.findtext("citeinfo/edition")
                #
                #     edition_box = self.findChild(QLineEdit, 'fgdc_edition')
                #     edition_box.setText(edition_text)
                # else:
                #     print ("No onlink tag")
                #
                # if srcinfo.findall("citeinfo/geoform"):
                #     geoform_text = srcinfo.findtext("citeinfo/geoform")
                #
                #     geoform_box = self.findChild(QComboBox, 'fgdc_geoform')
                #     geoform_box.setCurrentText(geoform_text)
                # else:
                #     print ("No onlink tag")
                #
                # if srcinfo.findall("citeinfo/onlink"):
                #     onlink_text = srcinfo.findtext("citeinfo/onlink")
                #
                #     onlink_box = self.findChild(QLineEdit, 'fgdc_onlink')
                #     onlink_box.setText(onlink_text)
                # else:
                #     print ("No onlink tag")
                #
                # if srcinfo.findall("citeinfo/serinfo"):
                #     self.ui.radioButton_3.setChecked(True)
                #     sername_text = srcinfo.findtext("citeinfo/serinfo/sername")
                #
                #     sername_box = self.findChild(QLineEdit, 'fgdc_sername')
                #     sername_box.setText(sername_text)
                #
                #     issue_text = srcinfo.findtext("citeinfo/serinfo/issue")
                #
                #     issue_box = self.findChild(QLineEdit, 'fgdc_issue')
                #     issue_box.setText(issue_text)
                #
                # else:
                #     print ("No series name tag")
                #
                # if srcinfo.findall("citeinfo/pubinfo"):
                #     self.ui.radioButton_5.setChecked(True)
                #     pubplace_text = srcinfo.findtext("citeinfo/pubinfo/pubplace")
                #
                #     pub_box = self.findChild(QLineEdit, 'fgdc_pubplace')
                #     pub_box.setText(pubplace_text)
                #
                #     publish_text = srcinfo.findtext("citeinfo/pubinfo/publish")
                #
                #     publish_box = self.findChild(QLineEdit, 'fgdc_publish')
                #     publish_box.setText(publish_text)
                #
                # else:
                #     print ("No pub tag")

            else:
                print ("The tag is not srcinfo")



        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(SRCInfo,
                        "SRCInfo testing")

