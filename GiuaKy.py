import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QVBoxLayout,QWidget, QLabel,QDialog
class WidgetPropertiesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game")
        self.setGeometry(100,100,400,200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        dialog_button = QPushButton("Bắt Đầu Game")
        dialog_button.clicked.connect(self.show_dialog)
        dialog_button1 = QPushButton("Thoát Game")
        dialog_button1.clicked.connect(self.show_dialog1)
        layout = QVBoxLayout()

        layout.addWidget(dialog_button)
        layout.addWidget(dialog_button1)
        central_widget.setLayout(layout)

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Thông Báo")
        label = QLabel("Chương Trình Đã Bắt Đầu")
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)
        dialog.setLayout(dialog_layout)
        dialog.exec_()
    def show_dialog1(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Thông Báo")
        label = QLabel("Bạn Đã Thoát Game")
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)
        dialog.setLayout(dialog_layout)
        dialog.exec_()
        dialog.exec_(exit())

def main():
    app = QApplication(sys.argv)
    window = WidgetPropertiesApp()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()

