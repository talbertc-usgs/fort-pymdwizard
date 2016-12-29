# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ITISSearchSimple.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ItisSearchWidget(object):
    def setupUi(self, ItisSearchWidget):
        ItisSearchWidget.setObjectName("ItisSearchWidget")
        ItisSearchWidget.resize(543, 351)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ItisSearchWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(ItisSearchWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 5, 5, 7)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_search_term = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_search_term.setFont(font)
        self.label_search_term.setObjectName("label_search_term")
        self.horizontalLayout.addWidget(self.label_search_term)
        self.search_term = QtWidgets.QLineEdit(self.layoutWidget)
        self.search_term.setObjectName("search_term")
        self.horizontalLayout.addWidget(self.search_term)
        self.button_search = QtWidgets.QPushButton(self.layoutWidget)
        self.button_search.setObjectName("button_search")
        self.horizontalLayout.addWidget(self.button_search)
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_search_type = QtWidgets.QLabel(self.layoutWidget)
        self.label_search_type.setAccessibleName("")
        self.label_search_type.setObjectName("label_search_type")
        self.horizontalLayout.addWidget(self.label_search_type)
        self.combo_search_type = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_search_type.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.combo_search_type.setObjectName("combo_search_type")
        self.combo_search_type.addItem("")
        self.combo_search_type.addItem("")
        self.horizontalLayout.addWidget(self.combo_search_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_search_results = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_search_results.setFont(font)
        self.label_search_results.setObjectName("label_search_results")
        self.horizontalLayout_6.addWidget(self.label_search_results)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.table_results = QtWidgets.QTableView(self.layoutWidget)
        self.table_results.setLineWidth(1)
        self.table_results.setAlternatingRowColors(True)
        self.table_results.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table_results.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_results.setSortingEnabled(True)
        self.table_results.setObjectName("table_results")
        self.table_results.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_results)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_add_taxon = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_add_taxon.setObjectName("btn_add_taxon")
        self.horizontalLayout_2.addWidget(self.btn_add_taxon)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btn_close = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(ItisSearchWidget)
        self.combo_search_type.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ItisSearchWidget)

    def retranslateUi(self, ItisSearchWidget):
        _translate = QtCore.QCoreApplication.translate
        ItisSearchWidget.setWindowTitle(_translate("ItisSearchWidget", "ITIS Search"))
        self.label_search_term.setText(_translate("ItisSearchWidget", "Search Term:"))
        self.search_term.setToolTip(_translate("ItisSearchWidget", "terms to search ITIS for"))
        self.button_search.setToolTip(_translate("ItisSearchWidget", "Perform search of ITIS"))
        self.button_search.setText(_translate("ItisSearchWidget", "Seach ITIS"))
        self.label_search_type.setToolTip(_translate("ItisSearchWidget", "The type of ITIS search to perform (Scientific or Common name)"))
        self.label_search_type.setText(_translate("ItisSearchWidget", "Search Type:"))
        self.combo_search_type.setToolTip(_translate("ItisSearchWidget", "Search ITIS on common or scientific name"))
        self.combo_search_type.setItemText(0, _translate("ItisSearchWidget", "Common name"))
        self.combo_search_type.setItemText(1, _translate("ItisSearchWidget", "Scientific name"))
        self.label_search_results.setToolTip(_translate("ItisSearchWidget", "Results from the ITIS common or scientific name search"))
        self.label_search_results.setText(_translate("ItisSearchWidget", "Search Results:"))
        self.btn_add_taxon.setToolTip(_translate("ItisSearchWidget", "Add the selected item above to the list of include species (right)"))
        self.btn_add_taxon.setText(_translate("ItisSearchWidget", "Add Selection"))
        self.btn_close.setText(_translate("ItisSearchWidget", "Close"))

