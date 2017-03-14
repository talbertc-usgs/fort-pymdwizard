# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Citation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fgdc_citation(object):
    def setupUi(self, fgdc_citation):
        fgdc_citation.setObjectName("fgdc_citation")
        fgdc_citation.resize(1154, 360)
        fgdc_citation.setStyleSheet("")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(fgdc_citation)
        self.horizontalLayout_13.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.fgdc_citeinfo = QtWidgets.QGroupBox(fgdc_citation)
        self.fgdc_citeinfo.setMinimumSize(QtCore.QSize(1000, 360))
        self.fgdc_citeinfo.setObjectName("fgdc_citeinfo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fgdc_citeinfo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.first_hbox = QtWidgets.QHBoxLayout()
        self.first_hbox.setObjectName("first_hbox")
        self.groupBox = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setStyleSheet("font: italic;")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_10.addWidget(self.label_34)
        self.fgdc_title = QtWidgets.QLineEdit(self.groupBox)
        self.fgdc_title.setObjectName("fgdc_title")
        self.verticalLayout_10.addWidget(self.fgdc_title)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.first_hbox.addWidget(self.groupBox)
        self.fgdc_pubdate = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_pubdate.sizePolicy().hasHeightForWidth())
        self.fgdc_pubdate.setSizePolicy(sizePolicy)
        self.fgdc_pubdate.setObjectName("fgdc_pubdate")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fgdc_pubdate)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_38 = QtWidgets.QLabel(self.fgdc_pubdate)
        self.label_38.setStyleSheet("font: italic;")
        self.label_38.setObjectName("label_38")
        self.verticalLayout_2.addWidget(self.label_38)
        self.pubdate_layout = QtWidgets.QHBoxLayout()
        self.pubdate_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.pubdate_layout.setObjectName("pubdate_layout")
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.pubdate_layout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.pubdate_layout)
        self.first_hbox.addWidget(self.fgdc_pubdate)
        self.verticalLayout_4.addLayout(self.first_hbox)
        self.second_hbox = QtWidgets.QHBoxLayout()
        self.second_hbox.setSpacing(10)
        self.second_hbox.setObjectName("second_hbox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setStyleSheet("font: italic;")
        self.label_35.setObjectName("label_35")
        self.verticalLayout_13.addWidget(self.label_35)
        self.originator_layout = QtWidgets.QVBoxLayout()
        self.originator_layout.setObjectName("originator_layout")
        self.verticalLayout_13.addLayout(self.originator_layout)
        self.second_hbox.addWidget(self.groupBox_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.geoform_groupbox = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        self.geoform_groupbox.setObjectName("geoform_groupbox")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.geoform_groupbox)
        self.verticalLayout_14.setContentsMargins(6, 3, 6, 3)
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_geoform = QtWidgets.QComboBox(self.geoform_groupbox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_geoform.setFont(font)
        self.fgdc_geoform.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fgdc_geoform.setEditable(True)
        self.fgdc_geoform.setObjectName("fgdc_geoform")
        self.fgdc_geoform.addItem("")
        self.fgdc_geoform.addItem("")
        self.fgdc_geoform.addItem("")
        self.fgdc_geoform.addItem("")
        self.fgdc_geoform.addItem("")
        self.fgdc_geoform.addItem("")
        self.fgdc_geoform.addItem("")
        self.horizontalLayout.addWidget(self.fgdc_geoform)
        self.verticalLayout_14.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addWidget(self.geoform_groupbox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.second_hbox.addLayout(self.verticalLayout_6)
        self.groupBox_6 = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_39 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setStyleSheet("font: italic;")
        self.label_39.setObjectName("label_39")
        self.verticalLayout_17.addWidget(self.label_39)
        self.onlink_layout = QtWidgets.QVBoxLayout()
        self.onlink_layout.setObjectName("onlink_layout")
        self.verticalLayout_17.addLayout(self.onlink_layout)
        self.second_hbox.addWidget(self.groupBox_6)
        self.verticalLayout_4.addLayout(self.second_hbox)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.fgdc_serinfo = QtWidgets.QFrame(self.fgdc_citeinfo)
        self.fgdc_serinfo.setObjectName("fgdc_serinfo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_serinfo)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_43 = QtWidgets.QLabel(self.fgdc_serinfo)
        self.label_43.setStyleSheet("font: bold;")
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_6.addWidget(self.label_43)
        spacerItem2 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.radio_seriesyes = QtWidgets.QRadioButton(self.fgdc_serinfo)
        self.radio_seriesyes.setObjectName("radio_seriesyes")
        self.horizontalLayout_6.addWidget(self.radio_seriesyes)
        self.radioButton_4 = QtWidgets.QRadioButton(self.fgdc_serinfo)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_6.addWidget(self.radioButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_44 = QtWidgets.QLabel(self.fgdc_serinfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setStyleSheet("font: italic;")
        self.label_44.setObjectName("label_44")
        self.verticalLayout.addWidget(self.label_44)
        self.series_ext = QtWidgets.QWidget(self.fgdc_serinfo)
        self.series_ext.setObjectName("series_ext")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.series_ext)
        self.horizontalLayout_10.setContentsMargins(3, 6, 3, 3)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setSpacing(3)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_42 = QtWidgets.QLabel(self.series_ext)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_21.addWidget(self.label_42)
        self.fgdc_sername = QtWidgets.QLineEdit(self.series_ext)
        self.fgdc_sername.setObjectName("fgdc_sername")
        self.verticalLayout_21.addWidget(self.fgdc_sername)
        self.horizontalLayout_9.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setSpacing(3)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_41 = QtWidgets.QLabel(self.series_ext)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_22.addWidget(self.label_41)
        self.fgdc_issue = QtWidgets.QLineEdit(self.series_ext)
        self.fgdc_issue.setObjectName("fgdc_issue")
        self.verticalLayout_22.addWidget(self.fgdc_issue)
        self.horizontalLayout_9.addLayout(self.verticalLayout_22)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addWidget(self.series_ext)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_15.addWidget(self.fgdc_serinfo)
        self.fgdc_pubinfo = QtWidgets.QFrame(self.fgdc_citeinfo)
        self.fgdc_pubinfo.setObjectName("fgdc_pubinfo")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.fgdc_pubinfo)
        self.verticalLayout_24.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_24.setSpacing(3)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_49 = QtWidgets.QLabel(self.fgdc_pubinfo)
        self.label_49.setStyleSheet("font: bold;")
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_8.addWidget(self.label_49)
        spacerItem4 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.radio_pubinfoyes = QtWidgets.QRadioButton(self.fgdc_pubinfo)
        self.radio_pubinfoyes.setObjectName("radio_pubinfoyes")
        self.horizontalLayout_8.addWidget(self.radio_pubinfoyes)
        self.radioButton_8 = QtWidgets.QRadioButton(self.fgdc_pubinfo)
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout_8.addWidget(self.radioButton_8)
        self.verticalLayout_24.addLayout(self.horizontalLayout_8)
        self.label_50 = QtWidgets.QLabel(self.fgdc_pubinfo)
        self.label_50.setStyleSheet("font: italic;")
        self.label_50.setObjectName("label_50")
        self.verticalLayout_24.addWidget(self.label_50)
        self.pub_ext = QtWidgets.QWidget(self.fgdc_pubinfo)
        self.pub_ext.setObjectName("pub_ext")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pub_ext)
        self.verticalLayout_3.setContentsMargins(3, 6, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setSpacing(3)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_51 = QtWidgets.QLabel(self.pub_ext)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_30.addWidget(self.label_51)
        self.fgdc_pubplace = QtWidgets.QLineEdit(self.pub_ext)
        self.fgdc_pubplace.setObjectName("fgdc_pubplace")
        self.verticalLayout_30.addWidget(self.fgdc_pubplace)
        self.horizontalLayout_12.addLayout(self.verticalLayout_30)
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setSpacing(3)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_52 = QtWidgets.QLabel(self.pub_ext)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_31.addWidget(self.label_52)
        self.fgdc_publish = QtWidgets.QLineEdit(self.pub_ext)
        self.fgdc_publish.setObjectName("fgdc_publish")
        self.verticalLayout_31.addWidget(self.fgdc_publish)
        self.horizontalLayout_12.addLayout(self.verticalLayout_31)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.verticalLayout_24.addWidget(self.pub_ext)
        spacerItem5 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_24.addItem(spacerItem5)
        self.horizontalLayout_15.addWidget(self.fgdc_pubinfo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.fgdc_lworkcit = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        self.fgdc_lworkcit.setObjectName("fgdc_lworkcit")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fgdc_lworkcit)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_65 = QtWidgets.QLabel(self.fgdc_lworkcit)
        self.label_65.setStyleSheet("font: bold;")
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_28.addWidget(self.label_65)
        spacerItem6 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem6)
        self.radio_lworkyes = QtWidgets.QRadioButton(self.fgdc_lworkcit)
        self.radio_lworkyes.setObjectName("radio_lworkyes")
        self.horizontalLayout_28.addWidget(self.radio_lworkyes)
        self.radio_lworkno = QtWidgets.QRadioButton(self.fgdc_lworkcit)
        self.radio_lworkno.setChecked(True)
        self.radio_lworkno.setObjectName("radio_lworkno")
        self.horizontalLayout_28.addWidget(self.radio_lworkno)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem7)
        self.label_66 = QtWidgets.QLabel(self.fgdc_lworkcit)
        self.label_66.setStyleSheet("font: italic;")
        self.label_66.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_28.addWidget(self.label_66)
        self.verticalLayout_5.addLayout(self.horizontalLayout_28)
        self.lworkcite_widget = QtWidgets.QWidget(self.fgdc_lworkcit)
        self.lworkcite_widget.setObjectName("lworkcite_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.lworkcite_widget)
        self.horizontalLayout_5.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5.addWidget(self.lworkcite_widget)
        self.verticalLayout_4.addWidget(self.fgdc_lworkcit)
        self.horizontalLayout_13.addWidget(self.fgdc_citeinfo)

        self.retranslateUi(fgdc_citation)
        QtCore.QMetaObject.connectSlotsByName(fgdc_citation)

    def retranslateUi(self, fgdc_citation):
        _translate = QtCore.QCoreApplication.translate
        fgdc_citation.setWindowTitle(_translate("fgdc_citation", "Form"))
        self.fgdc_citeinfo.setTitle(_translate("fgdc_citation", "Citation"))
        self.groupBox.setTitle(_translate("fgdc_citation", "Dataset Title"))
        self.label_34.setText(_translate("fgdc_citation", "A good title includes \'What\', \'Where\', and \'When\'.  (Example: Point Locations of Wind Turbines in Colorado, Derived from 2010 NAIP Imagery)"))
        self.fgdc_pubdate.setTitle(_translate("fgdc_citation", "Publication Date "))
        self.label_38.setText(_translate("fgdc_citation", "When was the data set published or finalized?"))
        self.groupBox_3.setTitle(_translate("fgdc_citation", "Dataset Author/ Originator"))
        self.label_35.setText(_translate("fgdc_citation", "Who created the data set? List the organization and/or person(s)"))
        self.geoform_groupbox.setTitle(_translate("fgdc_citation", "Dataset Format"))
        self.fgdc_geoform.setCurrentText(_translate("fgdc_citation", "tabular digital data"))
        self.fgdc_geoform.setItemText(0, _translate("fgdc_citation", "tabular digital data"))
        self.fgdc_geoform.setItemText(1, _translate("fgdc_citation", "vector digital data"))
        self.fgdc_geoform.setItemText(2, _translate("fgdc_citation", "raster digital data"))
        self.fgdc_geoform.setItemText(3, _translate("fgdc_citation", "spreadsheet"))
        self.fgdc_geoform.setItemText(4, _translate("fgdc_citation", "remote-sensing image"))
        self.fgdc_geoform.setItemText(5, _translate("fgdc_citation", "spreadsheet"))
        self.fgdc_geoform.setItemText(6, _translate("fgdc_citation", "application/service"))
        self.groupBox_6.setTitle(_translate("fgdc_citation", "Online Link to the Dataset"))
        self.label_39.setText(_translate("fgdc_citation", "Is there a link to the data or the agency that produced it? if so, provide the URL(s) "))
        self.label_43.setText(_translate("fgdc_citation", "Is this data set part of a series?"))
        self.radio_seriesyes.setText(_translate("fgdc_citation", "Yes"))
        self.radioButton_4.setText(_translate("fgdc_citation", "No"))
        self.label_44.setText(_translate("fgdc_citation", " Is it a release with an assigned issue number (e.g. USGS Data Series)"))
        self.label_42.setText(_translate("fgdc_citation", "Series Name"))
        self.label_41.setText(_translate("fgdc_citation", "Issue Name / Number within Series"))
        self.label_49.setText(_translate("fgdc_citation", "Can you provide more publication information about this data set?"))
        self.radio_pubinfoyes.setText(_translate("fgdc_citation", "Yes"))
        self.radioButton_8.setText(_translate("fgdc_citation", "No"))
        self.label_50.setText(_translate("fgdc_citation", "More details are always helpful for finding and properly referencing data."))
        self.label_51.setText(_translate("fgdc_citation", "Publication Place"))
        self.label_52.setText(_translate("fgdc_citation", "Publisher"))
        self.fgdc_lworkcit.setTitle(_translate("fgdc_citation", "Larger Work"))
        self.label_65.setText(_translate("fgdc_citation", "Is this data set associated with a larger work?"))
        self.radio_lworkyes.setText(_translate("fgdc_citation", "Yes"))
        self.radio_lworkno.setText(_translate("fgdc_citation", "No"))
        self.label_66.setText(_translate("fgdc_citation", "If the citation of a larger project is relevant, you may optionally cite it here."))

