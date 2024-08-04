from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,QLineEdit, QLabel, QDialog
from PyQt6 import uic
from PyQt6.QtCore import QDate, QDateTime
import sys

from model.movies import Movie, ListMovie
from model.accounts import Account, ListAccounts
from ui_py.ui_homedashboardform import Ui_MainWindow

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/adddialog.ui", self)
        self.btnBox.accepted.connect(self.addMovie)
    def addMovie(self):
        self.l = ListMovie()
        self.l.add_movie(Movie("Null", self.txtName.text(), self.txtDate.text(), self.txtScore.text(), self.txtUrl.text()))
        home.callAfterInit()
        self.close()

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.oldMovie = None
        uic.loadUi("./ui/editdialog.ui",self)
        self.btnBox.accepted.connect(self.setNewMovie)

    def setOldMovie(self, movie:Movie):
        # Dat Ten Objects cho dung
        self.oldMovie = movie
        self.txtName.setText(movie.getName())
        date_str = movie.getDate()
        date = QDate.fromString(date_str, "yyyy-MM-dd")
        self.txtDate.setDate(date)
        self.txtScore.setText(movie.getScore())
        self.txtUrl.setText(movie.getLink())

    def setNewMovie(self):
        # Xoa Movie cu
        self.l = ListMovie()
        self.l.delete_movies_by_name(self.oldMovie.getName())
        # Them Movie Moi
        self.l.add_movie(Movie("Null", self.txtName.text(), self.txtDate.text(), self.txtScore.text(), self.txtUrl.text()))
        home.callAfterInit()
        self.close()

    def exit(self):
        self.close()

class HomeMenuDashboard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.callAfterInit()
        self.btnDelete.clicked.connect(self.deleteMovie)
        self.btnEditDialog.clicked.connect(self.showEditDialog)
        self.btnAddDialog.clicked.connect(self.showAddDialog)
    def deleteMovie(self):
        nameMovieDetete = self.test.currentItem().text()
        self.test.takeItem(self.test.currentRow())
        self.l.delete_movies_by_name(nameMovieDetete)
        self.callAfterInit()
    def showAddDialog(self):
        add.show()
    def showEditDialog(self):
        if self.test.currentRow():
            edit.show()
            edit.setOldMovie(self.l.getMovieByName(self.test.currentItem().text()))
        
    def callAfterInit(self):
        self.l = ListMovie()
        # thêm tất cả tên của đối tương Movie vào List
        self.test.clear()
        for mov in self.l.getAllMovies():
            self.test.addItem(mov.getName())
        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = HomeMenuDashboard()
    add = AddDialog()
    edit = EditDialog()
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