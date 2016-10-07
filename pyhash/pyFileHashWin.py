# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from Ui_pyFileHashWin import Ui_MainWindow
from PyQt4 import QtGui,QtCore
import os
import time
import hashlib
import zlib

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_openfile_clicked(self):
        self.chose_file_calc_mode()

    @pyqtSignature("")
    def on_pushButton_clear_clicked(self):
        self.textBrowser.clear()

    @pyqtSignature("")
    def on_pushButton_save_clicked(self):
        self.save_file()

    @pyqtSignature("")
    def on_action_openfile_triggered(self):
        self.chose_file_calc_mode()

    @pyqtSignature("")
    def on_action_save_triggered(self):
        self.save_file()
    
    @pyqtSignature("")
    def on_action_close_triggered(self):
        sys.exit()

    def chose_file_calc_mode(self):
        self.textBrowser.clear()
        f_path = QtGui.QFileDialog.getOpenFileName(self, u"打开文件","./")
        self.textBrowser.append("Open File:"+f_path)
        f_stat = os.stat(f_path)
        if self.checkBox_atime.isChecked():
            a_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_stat.st_atime))  # 上次访问的时间。
            self.textBrowser.append(u"a_time:"+a_time)
        if self.checkBox_mtime.isChecked():
            m_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_stat.st_mtime))  # 最后一次修改的时间。
            self.textBrowser.append(u"m_time:"+m_time)
        if self.checkBox_ctime.isChecked():
            c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_stat.st_ctime))  ##文件创建时间
            self.textBrowser.append(u"c_time:"+c_time)
        if self.checkBox_size.isChecked():
            self.textBrowser.append(u"size:"+str(f_stat.st_size)+u"个字节")
        self.textBrowser.append(u"---------------------------------------------------------------------------------------")
        with open(f_path, "rb") as open_f:
            f_data = open_f.read()
            if self.checkBox_md5.isChecked():
                self.textBrowser.append(u"md5："+hashlib.md5(f_data).hexdigest())
            if self.checkBox_sha1.isChecked():
                self.textBrowser.append(u"sha1："+hashlib.sha1(f_data).hexdigest())
            if self.checkBox_sha224.isChecked():
                self.textBrowser.append(u"sha224："+hashlib.sha224(f_data).hexdigest())
            if self.checkBox_sha256.isChecked():
                self.textBrowser.append(u"sha256："+hashlib.sha256(f_data).hexdigest())
            if self.checkBox_sha384.isChecked():
                self.textBrowser.append(u"sha384："+hashlib.sha384(f_data).hexdigest())
            if self.checkBox_sha512.isChecked():
                self.textBrowser.append(u"sha512："+hashlib.sha512(f_data).hexdigest())
            if self.checkBox_crc32.isChecked():
                self.textBrowser.append(u"crc32："+str(zlib.crc32(f_data, 0)))
            if self.checkBox_adler32.isChecked():
                self.textBrowser.append(u"adler32："+str(zlib.adler32(f_data)))

    def save_file(self):
        save_f_path = QtGui.QFileDialog.getSaveFileName(self, "文件信息另存为", "./", ".txt")
        with open(save_f_path, 'wb') as save_f_open:
            save_f_open.write(unicode(self.textBrowser.toPlainText()).encode("utf-8"))
        QtGui.QMessageBox.information(self, u"提示", u"文件信息保存成功!")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    splash = QtGui.QSplashScreen(QtGui.QPixmap(":/photo/starting_up.png"))
    app.processEvents()
    splash.show()
    splash.showMessage(u"正在加载...")
    time.sleep(1.5)
    splash.showMessage(u"加载完成...",QtCore.Qt.LeftToRight,QtCore.Qt.red)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

