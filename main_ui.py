# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 401, 428))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLineEdit(self.widget)
        self.fileName.setReadOnly(True)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        self.addFileButton = QtWidgets.QPushButton(self.widget)
        self.addFileButton.setObjectName("addFileButton")
        self.horizontalLayout.addWidget(self.addFileButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listColumns = QtWidgets.QListView(self.widget)
        self.listColumns.setEnabled(True)
        self.listColumns.setAutoFillBackground(False)
        self.listColumns.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        # self.listColumns.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listColumns.setObjectName("listColumns")
        self.horizontalLayout_2.addWidget(self.listColumns)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_3.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(self.widget)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_3.addWidget(self.removeButton)
        self.clearButton = QtWidgets.QPushButton(self.widget)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_3.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.listColumns_2 = QtWidgets.QListView(self.widget)
        self.listColumns_2.setEnabled(True)
        self.listColumns_2.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        # self.listColumns_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listColumns_2.setObjectName("listColumns_2")
        self.horizontalLayout_2.addWidget(self.listColumns_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelXAxis = QtWidgets.QLabel(self.widget)
        self.labelXAxis.setObjectName("labelXAxis")
        self.verticalLayout_2.addWidget(self.labelXAxis)
        self.dropdownXAxis = QtWidgets.QComboBox(self.widget)
        self.dropdownXAxis.setEditable(False)
        self.dropdownXAxis.setObjectName("dropdownXAxis")
        self.verticalLayout_2.addWidget(self.dropdownXAxis)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelXTitle = QtWidgets.QLabel(self.widget)
        self.labelXTitle.setObjectName("labelXTitle")
        self.verticalLayout.addWidget(self.labelXTitle)
        self.lineXTitle = QtWidgets.QLineEdit(self.widget)
        self.lineXTitle.setObjectName("lineXTitle")
        self.verticalLayout.addWidget(self.lineXTitle)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelYTitle = QtWidgets.QLabel(self.widget)
        self.labelYTitle.setObjectName("labelYTitle")
        self.verticalLayout_5.addWidget(self.labelYTitle)
        self.lineYTitle = QtWidgets.QLineEdit(self.widget)
        self.lineYTitle.setObjectName("lineYTitle")
        self.verticalLayout_5.addWidget(self.lineYTitle)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.plotButton = QtWidgets.QPushButton(self.widget)
        self.plotButton.setObjectName("plotButton")
        self.verticalLayout_4.addWidget(self.plotButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAdd_Datasheet = QtWidgets.QAction(MainWindow)
        self.actionAdd_Datasheet.setObjectName("actionAdd_Datasheet")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileName.setText(_translate("MainWindow", "No File Selected"))
        self.addFileButton.setText(_translate("MainWindow", "Add File"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.labelXAxis.setText(_translate("MainWindow", "X-Axis"))
        self.labelXTitle.setText(_translate("MainWindow", "X-Axis"))
        self.lineXTitle.setText(_translate("MainWindow", "X Axis Title"))
        self.labelYTitle.setText(_translate("MainWindow", "Y-Axis"))
        self.lineYTitle.setText(_translate("MainWindow", "Y Axis Title"))
        self.plotButton.setText(_translate("MainWindow", "PLOT!"))
        self.actionAdd_Datasheet.setText(_translate("MainWindow", "Add Datasheet"))
