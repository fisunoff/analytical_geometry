# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(1064, 639)
        font = QtGui.QFont()
        font.setPointSize(11)
        DockWidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DockWidget.setWindowIcon(icon)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1041, 591))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.value_Bx = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Bx.setMinimum(-999.0)
        self.value_Bx.setMaximum(999.0)
        self.value_Bx.setObjectName("value_Bx")
        self.gridLayout_2.addWidget(self.value_Bx, 1, 1, 1, 1)
        self.value_Dz = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Dz.setMinimum(-999.0)
        self.value_Dz.setMaximum(999.0)
        self.value_Dz.setObjectName("value_Dz")
        self.gridLayout_2.addWidget(self.value_Dz, 3, 3, 1, 1)
        self.value_Cz = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Cz.setMinimum(-999.0)
        self.value_Cz.setMaximum(999.0)
        self.value_Cz.setObjectName("value_Cz")
        self.gridLayout_2.addWidget(self.value_Cz, 2, 3, 1, 1)
        self.label_A = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_A.setObjectName("label_A")
        self.gridLayout_2.addWidget(self.label_A, 0, 0, 1, 1)
        self.value_Ax = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Ax.setMinimum(-999.0)
        self.value_Ax.setMaximum(999.0)
        self.value_Ax.setProperty("value", 0.0)
        self.value_Ax.setObjectName("value_Ax")
        self.gridLayout_2.addWidget(self.value_Ax, 0, 1, 1, 1)
        self.label_D = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_D.setObjectName("label_D")
        self.gridLayout_2.addWidget(self.label_D, 3, 0, 1, 1)
        self.value_Dx = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Dx.setMinimum(-999.0)
        self.value_Dx.setMaximum(999.0)
        self.value_Dx.setObjectName("value_Dx")
        self.gridLayout_2.addWidget(self.value_Dx, 3, 1, 1, 1)
        self.value_Cx = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Cx.setMinimum(-999.0)
        self.value_Cx.setMaximum(999.0)
        self.value_Cx.setObjectName("value_Cx")
        self.gridLayout_2.addWidget(self.value_Cx, 2, 1, 1, 1)
        self.value_Ay = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Ay.setMinimum(-999.0)
        self.value_Ay.setMaximum(999.0)
        self.value_Ay.setObjectName("value_Ay")
        self.gridLayout_2.addWidget(self.value_Ay, 0, 2, 1, 1)
        self.value_By = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_By.setMinimum(-999.0)
        self.value_By.setMaximum(999.0)
        self.value_By.setObjectName("value_By")
        self.gridLayout_2.addWidget(self.value_By, 1, 2, 1, 1)
        self.value_Dy = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Dy.setMinimum(-999.0)
        self.value_Dy.setMaximum(999.0)
        self.value_Dy.setObjectName("value_Dy")
        self.gridLayout_2.addWidget(self.value_Dy, 3, 2, 1, 1)
        self.label_B = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_B.setObjectName("label_B")
        self.gridLayout_2.addWidget(self.label_B, 1, 0, 1, 1)
        self.value_Az = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Az.setMinimum(-999.0)
        self.value_Az.setMaximum(999.0)
        self.value_Az.setObjectName("value_Az")
        self.gridLayout_2.addWidget(self.value_Az, 0, 3, 1, 1)
        self.value_Bz = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Bz.setMinimum(-999.0)
        self.value_Bz.setMaximum(999.0)
        self.value_Bz.setObjectName("value_Bz")
        self.gridLayout_2.addWidget(self.value_Bz, 1, 3, 1, 1)
        self.label_C = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_C.setObjectName("label_C")
        self.gridLayout_2.addWidget(self.label_C, 2, 0, 1, 1)
        self.value_Cy = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.value_Cy.setMinimum(-999.0)
        self.value_Cy.setMaximum(999.0)
        self.value_Cy.setObjectName("value_Cy")
        self.gridLayout_2.addWidget(self.value_Cy, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.metrics_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.metrics_line.setObjectName("metrics_line")
        self.gridLayout.addWidget(self.metrics_line, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.result_name = QtWidgets.QLabel(self.layoutWidget)
        self.result_name.setText("")
        self.result_name.setObjectName("result_name")
        self.gridLayout.addWidget(self.result_name, 1, 0, 1, 1)
        self.result_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.result_line.setObjectName("result_line")
        self.gridLayout.addWidget(self.result_line, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_6)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 291, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.result_name_angle = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.result_name_angle.setText("")
        self.result_name_angle.setObjectName("result_name_angle")
        self.gridLayout_3.addWidget(self.result_name_angle, 1, 0, 1, 1)
        self.pushButton_angle = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_angle.setObjectName("pushButton_angle")
        self.gridLayout_3.addWidget(self.pushButton_angle, 0, 2, 1, 1)
        self.result_line_angle = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.result_line_angle.setObjectName("result_line_angle")
        self.gridLayout_3.addWidget(self.result_line_angle, 1, 2, 1, 1)
        self.angle_line_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.angle_line_1.setObjectName("angle_line_1")
        self.gridLayout_3.addWidget(self.angle_line_1, 0, 0, 1, 1)
        self.angle_line_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.angle_line_2.setObjectName("angle_line_2")
        self.gridLayout_3.addWidget(self.angle_line_2, 0, 1, 1, 1)
        self.result_line_angle_cos = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.result_line_angle_cos.setObjectName("result_line_angle_cos")
        self.gridLayout_3.addWidget(self.result_line_angle_cos, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)
        DockWidget.setTabOrder(self.value_Ax, self.value_Ay)
        DockWidget.setTabOrder(self.value_Ay, self.value_Az)
        DockWidget.setTabOrder(self.value_Az, self.value_Bx)
        DockWidget.setTabOrder(self.value_Bx, self.value_By)
        DockWidget.setTabOrder(self.value_By, self.value_Bz)
        DockWidget.setTabOrder(self.value_Bz, self.value_Cx)
        DockWidget.setTabOrder(self.value_Cx, self.value_Cy)
        DockWidget.setTabOrder(self.value_Cy, self.value_Cz)
        DockWidget.setTabOrder(self.value_Cz, self.value_Dx)
        DockWidget.setTabOrder(self.value_Dx, self.value_Dy)
        DockWidget.setTabOrder(self.value_Dy, self.value_Dz)
        DockWidget.setTabOrder(self.value_Dz, self.tabWidget)
        DockWidget.setTabOrder(self.tabWidget, self.metrics_line)
        DockWidget.setTabOrder(self.metrics_line, self.pushButton)
        DockWidget.setTabOrder(self.pushButton, self.angle_line_1)
        DockWidget.setTabOrder(self.angle_line_1, self.angle_line_2)
        DockWidget.setTabOrder(self.angle_line_2, self.pushButton_angle)
        DockWidget.setTabOrder(self.pushButton_angle, self.result_line)
        DockWidget.setTabOrder(self.result_line, self.result_line_angle_cos)
        DockWidget.setTabOrder(self.result_line_angle_cos, self.result_line_angle)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "Аналитическая геометрия: тетраэдр"))
        self.label_A.setText(_translate("DockWidget", "A"))
        self.label_D.setText(_translate("DockWidget", "D"))
        self.label_B.setText(_translate("DockWidget", "B"))
        self.label_C.setText(_translate("DockWidget", "C"))
        self.pushButton.setText(_translate("DockWidget", "Go"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("DockWidget", "Метрические"))
        self.pushButton_angle.setText(_translate("DockWidget", "Go"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("DockWidget", "Углы"))
