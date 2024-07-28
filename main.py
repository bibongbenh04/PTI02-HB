from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6 import uic
import sys

from model.movies import Movie, ListMovie
from model.accounts import Account, ListAccounts
from ui_py.ui_homedashboardform import Ui_MainWindow

class HomeMenuDashboard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.callAfterInit()
        
    def callAfterInit(self):
        self.l = ListMovie()
        # thêm tất cả tên của đối tương Movie vào List
        for mov in self.l.getAllMovies():
            self.test.addItem(mov.getName())
        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = HomeMenuDashboard()
    home.show()
    app.exec()
    














# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
# from PyQt6 import uic
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("ui/main_window.ui", self)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())