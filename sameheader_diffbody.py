from PySide6.QtWidgets import *

# Header widget UI
class HeaderWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.button_page1 = QPushButton("Go to Page 1")
        self.button_page2 = QPushButton("Go to Page 2")
        layout.addWidget(self.button_page1)
        layout.addWidget(self.button_page2)
        self.setLayout(layout)

# Page widget 1
class PageWidget1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label1 = QLabel("Page 1")
        layout.addWidget(self.label1)
        self.setLayout(layout)

# Page widget 2
class PageWidget2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label2 = QLabel("Page 2")
        layout.addWidget(self.label2)
        self.setLayout(layout)

# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set header widget
        self.header_widget = HeaderWidget()

        # Create a stacked widget to manage different bodies
        self.stacked_widget = QStackedWidget()

        # Add page bodies to the stacked widget
        self.page1_body = PageWidget1()
        self.stacked_widget.addWidget(self.page1_body)
        self.page2_body = PageWidget2()
        self.stacked_widget.addWidget(self.page2_body)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.header_widget)
        layout.addWidget(self.stacked_widget)

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect buttons to switch pages
        self.header_widget.button_page1.clicked.connect(self.show_page1)
        self.header_widget.button_page2.clicked.connect(self.show_page2)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)  # Show page 1

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)  # Show page 2


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
