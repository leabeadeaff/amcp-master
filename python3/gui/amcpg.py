# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'amcp_test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_recompute = QtWidgets.QPushButton(self.tab)
        self.btn_recompute.setObjectName("btn_recompute")
        self.gridLayout_2.addWidget(self.btn_recompute, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.logfile_small = QtWidgets.QTextEdit(self.tab)
        self.logfile_small.setMinimumSize(QtCore.QSize(300, 300))
        self.logfile_small.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.logfile_small.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.logfile_small.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logfile_small.setObjectName("logfile_small")
        self.gridLayout_2.addWidget(self.logfile_small, 4, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 170))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.model = QtWidgets.QLabel(self.groupBox_3)
        self.model.setMinimumSize(QtCore.QSize(0, 0))
        self.model.setStyleSheet("")
        self.model.setScaledContents(True)
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName("model")
        self.verticalLayout_2.addWidget(self.model, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.btn_disconnect = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.gridLayout_8.addWidget(self.btn_disconnect, 1, 1, 1, 1)
        self.btn_connect = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout_8.addWidget(self.btn_connect, 1, 0, 1, 1)
        self.select_vna = QtWidgets.QComboBox(self.groupBox_6)
        self.select_vna.setObjectName("select_vna")
        self.select_vna.addItem("")
        self.select_vna.addItem("")
        self.gridLayout_8.addWidget(self.select_vna, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_6, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.f_center = QtWidgets.QLineEdit(self.groupBox)
        self.f_center.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.f_center.setObjectName("f_center")
        self.gridLayout_4.addWidget(self.f_center, 1, 1, 1, 4)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 7, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 5, 0, 1, 1)
        self.sel_method = QtWidgets.QComboBox(self.groupBox)
        self.sel_method.setObjectName("sel_method")
        self.sel_method.addItem("")
        self.sel_method.addItem("")
        self.gridLayout_4.addWidget(self.sel_method, 5, 1, 1, 4)
        self.ext_cl = QtWidgets.QLineEdit(self.groupBox)
        self.ext_cl.setObjectName("ext_cl")
        self.gridLayout_4.addWidget(self.ext_cl, 8, 4, 1, 1)
        self.r_setup = QtWidgets.QLineEdit(self.groupBox)
        self.r_setup.setObjectName("r_setup")
        self.gridLayout_4.addWidget(self.r_setup, 7, 4, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 8, 5, 1, 1)
        self.f_max = QtWidgets.QLineEdit(self.groupBox)
        self.f_max.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.f_max.setObjectName("f_max")
        self.gridLayout_4.addWidget(self.f_max, 4, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 4, 3, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 8, 0, 1, 4)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 4, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 5, 1, 1)
        self.averaging = QtWidgets.QLineEdit(self.groupBox)
        self.averaging.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.averaging.setObjectName("averaging")
        self.gridLayout_4.addWidget(self.averaging, 7, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 7, 5, 1, 1)
        self.f_min = QtWidgets.QLineEdit(self.groupBox)
        self.f_min.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.f_min.setObjectName("f_min")
        self.gridLayout_4.addWidget(self.f_min, 4, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphWidget = PlotWidget(self.groupBox_8)
        self.graphWidget.setObjectName("graphWidget")
        self.verticalLayout_4.addWidget(self.graphWidget)
        self.gridLayout_2.addWidget(self.groupBox_8, 1, 2, 7, 3)
        self.btn_run_measurement = QtWidgets.QPushButton(self.tab)
        self.btn_run_measurement.setObjectName("btn_run_measurement")
        self.gridLayout_2.addWidget(self.btn_run_measurement, 6, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.fp_res = QtWidgets.QLabel(self.groupBox_2)
        self.fp_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fp_res.setObjectName("fp_res")
        self.gridLayout.addWidget(self.fp_res, 1, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.L1_res = QtWidgets.QLabel(self.groupBox_2)
        self.L1_res.setMinimumSize(QtCore.QSize(50, 0))
        self.L1_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.L1_res.setObjectName("L1_res")
        self.gridLayout.addWidget(self.L1_res, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.C0_res = QtWidgets.QLabel(self.groupBox_2)
        self.C0_res.setMinimumSize(QtCore.QSize(50, 0))
        self.C0_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.C0_res.setObjectName("C0_res")
        self.gridLayout.addWidget(self.C0_res, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.R1_res = QtWidgets.QLabel(self.groupBox_2)
        self.R1_res.setMinimumSize(QtCore.QSize(50, 0))
        self.R1_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.R1_res.setObjectName("R1_res")
        self.gridLayout.addWidget(self.R1_res, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.C1_res = QtWidgets.QLabel(self.groupBox_2)
        self.C1_res.setMinimumSize(QtCore.QSize(50, 0))
        self.C1_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.C1_res.setObjectName("C1_res")
        self.gridLayout.addWidget(self.C1_res, 1, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 0, 6, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 1, 4, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 1, 6, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 0, 4, 1, 1)
        self.Q_res = QtWidgets.QLabel(self.groupBox_2)
        self.Q_res.setMinimumSize(QtCore.QSize(50, 0))
        self.Q_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Q_res.setObjectName("Q_res")
        self.gridLayout.addWidget(self.Q_res, 4, 1, 1, 1)
        self.fs_res = QtWidgets.QLabel(self.groupBox_2)
        self.fs_res.setMinimumSize(QtCore.QSize(50, 0))
        self.fs_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fs_res.setObjectName("fs_res")
        self.gridLayout.addWidget(self.fs_res, 0, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 3, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 3, 6, 1, 1)
        self.esr_res = QtWidgets.QLabel(self.groupBox_2)
        self.esr_res.setObjectName("esr_res")
        self.gridLayout.addWidget(self.esr_res, 3, 5, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem2, 4, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.nanovna_wrapper_loc = QtWidgets.QLineEdit(self.groupBox_5)
        self.nanovna_wrapper_loc.setObjectName("nanovna_wrapper_loc")
        self.gridLayout_6.addWidget(self.nanovna_wrapper_loc, 2, 1, 1, 2)
        self.btn_nanovna_cal_loc = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_nanovna_cal_loc.setObjectName("btn_nanovna_cal_loc")
        self.gridLayout_6.addWidget(self.btn_nanovna_cal_loc, 4, 3, 1, 1)
        self.btn_nanovna_wrapper_loc = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_nanovna_wrapper_loc.setObjectName("btn_nanovna_wrapper_loc")
        self.gridLayout_6.addWidget(self.btn_nanovna_wrapper_loc, 2, 3, 1, 1)
        self.nanovna_calfile_loc = QtWidgets.QLineEdit(self.groupBox_5)
        self.nanovna_calfile_loc.setObjectName("nanovna_calfile_loc")
        self.gridLayout_6.addWidget(self.nanovna_calfile_loc, 4, 1, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setMinimumSize(QtCore.QSize(200, 0))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 5, 2, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_5, 2, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.vnaj_loc = QtWidgets.QLineEdit(self.groupBox_4)
        self.vnaj_loc.setObjectName("vnaj_loc")
        self.gridLayout_5.addWidget(self.vnaj_loc, 1, 1, 1, 3)
        self.sel_minivna_port = QtWidgets.QComboBox(self.groupBox_4)
        self.sel_minivna_port.setMinimumSize(QtCore.QSize(200, 0))
        self.sel_minivna_port.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sel_minivna_port.setObjectName("sel_minivna_port")
        self.sel_minivna_port.addItem("")
        self.gridLayout_5.addWidget(self.sel_minivna_port, 5, 1, 1, 2)
        self.minivna_calfile_loc = QtWidgets.QLineEdit(self.groupBox_4)
        self.minivna_calfile_loc.setObjectName("minivna_calfile_loc")
        self.gridLayout_5.addWidget(self.minivna_calfile_loc, 4, 1, 1, 3)
        self.btn_vnaj_loc = QtWidgets.QToolButton(self.groupBox_4)
        self.btn_vnaj_loc.setObjectName("btn_vnaj_loc")
        self.gridLayout_5.addWidget(self.btn_vnaj_loc, 1, 4, 1, 1)
        self.vnajhl_loc = QtWidgets.QLineEdit(self.groupBox_4)
        self.vnajhl_loc.setObjectName("vnajhl_loc")
        self.gridLayout_5.addWidget(self.vnajhl_loc, 2, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 6, 1, 1, 1)
        self.btn_vnaj = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_vnaj.setObjectName("btn_vnaj")
        self.gridLayout_5.addWidget(self.btn_vnaj, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_vnajhl_loc = QtWidgets.QToolButton(self.groupBox_4)
        self.btn_vnajhl_loc.setObjectName("btn_vnajhl_loc")
        self.gridLayout_5.addWidget(self.btn_vnajhl_loc, 2, 4, 1, 1)
        self.btn_minivna_cal_loc = QtWidgets.QToolButton(self.groupBox_4)
        self.btn_minivna_cal_loc.setObjectName("btn_minivna_cal_loc")
        self.gridLayout_5.addWidget(self.btn_minivna_cal_loc, 4, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setMinimumSize(QtCore.QSize(200, 0))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_10.addWidget(self.groupBox_4, 1, 0, 1, 2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.java_loc = QtWidgets.QLineEdit(self.groupBox_7)
        self.java_loc.setObjectName("java_loc")
        self.gridLayout_7.addWidget(self.java_loc, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_7)
        self.label_24.setMinimumSize(QtCore.QSize(200, 0))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_java_loc = QtWidgets.QToolButton(self.groupBox_7)
        self.btn_java_loc.setObjectName("btn_java_loc")
        self.gridLayout_7.addWidget(self.btn_java_loc, 1, 2, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_7, 0, 0, 1, 2)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_25 = QtWidgets.QLabel(self.groupBox_9)
        self.label_25.setMinimumSize(QtCore.QSize(150, 0))
        self.label_25.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_9.addWidget(self.label_25, 0, 0, 1, 1)
        self.btn_refresh_ports = QtWidgets.QPushButton(self.groupBox_9)
        self.btn_refresh_ports.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_refresh_ports.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_refresh_ports.setObjectName("btn_refresh_ports")
        self.gridLayout_9.addWidget(self.btn_refresh_ports, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 0, 2, 1, 2)
        self.gridLayout_10.addWidget(self.groupBox_9, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.command_input = QtWidgets.QLineEdit(self.tab_2)
        self.command_input.setObjectName("command_input")
        self.gridLayout_3.addWidget(self.command_input, 1, 1, 1, 1)
        self.btn_send = QtWidgets.QPushButton(self.tab_2)
        self.btn_send.setObjectName("btn_send")
        self.gridLayout_3.addWidget(self.btn_send, 1, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)
        self.logfile = QtWidgets.QPlainTextEdit(self.tab_2)
        self.logfile.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logfile.setObjectName("logfile")
        self.gridLayout_3.addWidget(self.logfile, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(1)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.progressBar.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1152, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExport_Spectre = QtWidgets.QAction(MainWindow)
        self.actionExport_Spectre.setObjectName("actionExport_Spectre")
        self.actionas_SPICE_model = QtWidgets.QAction(MainWindow)
        self.actionas_SPICE_model.setObjectName("actionas_SPICE_model")
        self.actionas_Spectre_model = QtWidgets.QAction(MainWindow)
        self.actionas_Spectre_model.setObjectName("actionas_Spectre_model")
        self.menuExport.addAction(self.actionas_SPICE_model)
        self.menuExport.addAction(self.actionas_Spectre_model)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btn_run_measurement.clicked.connect(MainWindow.run_measurement)
        self.btn_recompute.clicked.connect(MainWindow.recompute)
        self.sel_minivna_port.activated['QString'].connect(MainWindow.update_comports)
        self.btn_connect.clicked.connect(MainWindow.connect_vna)
        self.btn_disconnect.clicked.connect(MainWindow.disconnect_vna)
        self.select_vna.currentTextChanged['QString'].connect(MainWindow.update_vna)
        self.btn_vnaj.clicked.connect(MainWindow.run_vnaj)
        self.btn_refresh_ports.clicked.connect(MainWindow.refresh_comports)
        self.btn_java_loc.clicked.connect(MainWindow.open_javaloc)
        self.btn_vnaj_loc.clicked.connect(MainWindow.open_vnaj_loc)
        self.btn_vnajhl_loc.clicked.connect(MainWindow.open_vnajhl_loc)
        self.btn_minivna_cal_loc.clicked.connect(MainWindow.open_minivna_cal_loc)
        self.btn_nanovna_wrapper_loc.clicked.connect(MainWindow.open_nanovna_wrapper_loc)
        self.btn_nanovna_cal_loc.clicked.connect(MainWindow.open_nanovna_cal_loc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMCP - Automated Measurement of Crystal Parameters"))
        self.btn_recompute.setText(_translate("MainWindow", "Re-Compute Values"))
        self.logfile_small.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt;\">Welcome to AMCP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:10pt;\">----------------------------</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">* make sure the calibration files are up to date</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">* use F</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; vertical-align:sub;\">min</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> and F</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; vertical-align:sub;\">max</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> narrow in so both seriel and parallel resonance frequencies are in view</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">* use F</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; vertical-align:sub;\">center</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> and &quot;Run Estimation&quot; to automatically zoom (experimental)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Crystal Model"))
        self.model.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/crystal/images/xtal_model.png\"/></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Select VNA"))
        self.btn_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.select_vna.setItemText(0, _translate("MainWindow", "MiniVNA"))
        self.select_vna.setItemText(1, _translate("MainWindow", "NanoVNA"))
        self.groupBox.setTitle(_translate("MainWindow", "Measurement Setup"))
        self.f_center.setText(_translate("MainWindow", "26E6"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">R<span style=\" vertical-align:sub;\">setup</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Method:</p></body></html>"))
        self.sel_method.setItemText(0, _translate("MainWindow", "Phase-Shift Method"))
        self.sel_method.setItemText(1, _translate("MainWindow", "-3dB Method"))
        self.ext_cl.setText(_translate("MainWindow", "0"))
        self.r_setup.setText(_translate("MainWindow", "12.5"))
        self.label_35.setText(_translate("MainWindow", "pF"))
        self.f_max.setText(_translate("MainWindow", "26050000"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">F<span style=\" vertical-align:sub;\">max</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">External Load-Capacitance:</p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hz</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Averaging:</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hz</p></body></html>"))
        self.averaging.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">F<span style=\" vertical-align:sub;\">center</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Ω</p></body></html>"))
        self.f_min.setText(_translate("MainWindow", "25990000"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">F<span style=\" vertical-align:sub;\">min</span></p></body></html>"))
        self.btn_run_measurement.setText(_translate("MainWindow", "Run Measurement"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Results"))
        self.fp_res.setText(_translate("MainWindow", "-"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>L<span style=\" vertical-align:sub;\">1</span>:</p></body></html>"))
        self.L1_res.setText(_translate("MainWindow", "-"))
        self.label_15.setText(_translate("MainWindow", "mH"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>R<span style=\" vertical-align:sub;\">1</span>:</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "Ω"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>C<span style=\" vertical-align:sub;\">0</span>:</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "fF"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>C<span style=\" vertical-align:sub;\">1</span>:</p></body></html>"))
        self.C0_res.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "fF"))
        self.R1_res.setText(_translate("MainWindow", "-"))
        self.C1_res.setText(_translate("MainWindow", "-"))
        self.label_27.setText(_translate("MainWindow", "kHz"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p>F<span style=\" vertical-align:sub;\">P</span>:</p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "kHz"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p>F<span style=\" vertical-align:sub;\">S</span>:</p></body></html>"))
        self.Q_res.setText(_translate("MainWindow", "-"))
        self.fs_res.setText(_translate("MainWindow", "-"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">ESR:</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Q:"))
        self.label_31.setText(_translate("MainWindow", "Ω"))
        self.esr_res.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">-</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Overview"))
        self.groupBox_5.setTitle(_translate("MainWindow", "NanoVNA"))
        self.label_23.setText(_translate("MainWindow", "Calibration File:"))
        self.nanovna_wrapper_loc.setText(_translate("MainWindow", "devices/nanovna/nanovna_wrapper.py"))
        self.btn_nanovna_cal_loc.setText(_translate("MainWindow", "..."))
        self.btn_nanovna_wrapper_loc.setText(_translate("MainWindow", "..."))
        self.label_22.setText(_translate("MainWindow", "NanoVNA wrapper:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "MiniVNA"))
        self.vnaj_loc.setText(_translate("MainWindow", "../vnaJ/vnaJ.3.3.3.jar"))
        self.sel_minivna_port.setItemText(0, _translate("MainWindow", "-"))
        self.minivna_calfile_loc.setText(_translate("MainWindow", "../vnaJ/vnaJ.3.3/calibration/TRAN_miniVNA_26M.cal"))
        self.btn_vnaj_loc.setText(_translate("MainWindow", "..."))
        self.vnajhl_loc.setText(_translate("MainWindow", "../vnaJ/vnaJ-hl.3.3.3.jar"))
        self.label_6.setText(_translate("MainWindow", "COM Port:"))
        self.btn_vnaj.setText(_translate("MainWindow", "VnaJ"))
        self.label_13.setText(_translate("MainWindow", "VnaJ-headless"))
        self.btn_vnajhl_loc.setText(_translate("MainWindow", "..."))
        self.btn_minivna_cal_loc.setText(_translate("MainWindow", "..."))
        self.label_20.setText(_translate("MainWindow", "Calibration File:"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Java"))
        self.java_loc.setText(_translate("MainWindow", "../oracle_java/jre1.8.0_221/bin/java"))
        self.label_24.setText(_translate("MainWindow", "Java location"))
        self.btn_java_loc.setText(_translate("MainWindow", "..."))
        self.groupBox_9.setTitle(_translate("MainWindow", "Miscellaneous"))
        self.label_25.setText(_translate("MainWindow", "Refresh COM Ports:"))
        self.btn_refresh_ports.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Setup"))
        self.btn_send.setText(_translate("MainWindow", "Send"))
        self.label_21.setText(_translate("MainWindow", "Console:"))
        self.logfile.setPlainText(_translate("MainWindow", "start log:\n"
"--------------------\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Log"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export "))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionClose.setText(_translate("MainWindow", "Exit"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExport_Spectre.setText(_translate("MainWindow", "Export Spectre"))
        self.actionas_SPICE_model.setText(_translate("MainWindow", "as SPICE model"))
        self.actionas_Spectre_model.setText(_translate("MainWindow", "as Spectre model"))
from pyqtgraph import PlotWidget
import gui.resource_rc
