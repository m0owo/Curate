import sys
import os
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QPainterPath, QPainter, QColor
from datetime import datetime
current_directory = os.getcwd()
sys.path.append(current_directory)

class CountdownWidget(QWidget):
    def __init__(self, target_datetime):
        super().__init__()
        self.target_datetime = target_datetime
        self.remaining_time = 0
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.setAlignment(Qt.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
        self.update_timer()
        self.label.setStyleSheet("QLabel {font:600 11pt Manrope;color:rgb(137, 153, 211);"
                                 "text-align: center; background-color: #E8F3F2;"
                                 "border-radius: 5px; padding:5px}")

    def update_timer(self):
        current_datetime = datetime.now()
        time_difference = self.target_datetime - current_datetime
        self.remaining_time = max(0, time_difference.total_seconds())
        days, remainder = divmod(self.remaining_time, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        if self.remaining_time == 0:
            self.label.setText("Live Now")
        elif days > 1:
            self.label.setText(self.target_datetime.strftime("%d/%m/%Y @ %H:%M"))
        else:
            self.label.setText("{:02d} days {:02d}:{:02d}".format(int(days), int(hours), int(minutes)))
            QTimer.singleShot(1000, self.update_timer)

class ClickablePost(QFrame):
    clicked = Signal(object)
    def __init__(self, container, details, home_ui):
        super().__init__(container)
        self.details = details
        self.clicked.connect(home_ui.handle_post_click)
    def get_product(self):
        return self.details.get('product')
    def get_details(self):
        return self.details
    def mousePressEvent(self, event):
        print("Mouse pressed on post")
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.details)

class TagButton():
    def __init__(self, tag, container = None):
        self.temp_text = tag.get('tag_text').lower()
        self.container = container
        if container:
            self.tag_button = QPushButton()
            self.container.layout().addWidget(self.tag_button)
        else:
            self.tag_button = QPushButton()
        self.tag_button.setText(self.temp_text)
        tag_button_stylesheet = ("QPushButton {"  # Change QLabel to QPushButton
        "    font: 600 14pt Manrope;"
        "    color: rgb(137, 153, 211);"
        "    text-align: center;"
        "    background-color: #E8F3F2;"
        "    border-radius: 20px;"
        "}"
        "QPushButton:hover{background-color:rgb(201, 212, 249); color:rgb(238, 248, 255);}")
        self.tag_button.setStyleSheet(tag_button_stylesheet)
        set_preferred_size(self.tag_button, 100)
    def get_tag_button(self):
        return self.tag_button
    
class BigPostTagButton(TagButton):
    def __init__(self, tag, container = None):
        super().__init__(tag, container)
        self.tag_button.setStyleSheet("QPushButton {font:600 16pt Manrope;color:rgb(137, 153, 211);"
                                      "text-align: center; background-color: #E8F3F2;"
                                      "border-radius: 5px;}QPushButton:hover{background-color:rgb(201, 212, 249); color:rgb(238, 248, 255);}")
        set_preferred_size(self.tag_button, 60, 40)

class PostTagButton(TagButton):
    def __init__(self, tag, container = None):
        super().__init__(tag, container)
        self.tag_button.setStyleSheet("QPushButton {font:600 11pt Manrope;color:rgb(137, 153, 211);"
                                      "text-align: center; background-color: #E8F3F2;"
                                      "border-radius: 5px;}QPushButton:hover{background-color:rgb(201, 212, 249); color:rgb(238, 248, 255);}")
        set_preferred_size(self.tag_button, 10)

class SaleTypeTagButton():
    def __init__(self, text, container = None):
        self.temp_text = text
        self.container = container

        if container:
            self.tag_button = QPushButton()
            self.container.layout().addWidget(self.tag_button)
        else:
            self.tag_button = QPushButton()

        self.tag_button.setText(self.temp_text)
        self.tag_button.setStyleSheet("QPushButton {font:600 11pt Manrope;text-align:center;"
                                      "background-color: rgb(250, 234, 225);color:rgb(176, 98, 106);"
                                      "border-radius: 5px;}QPushButton:hover{background-color:rgb(242, 207, 199); color:rgb(179, 85, 82);}")
        
        set_preferred_size(self.tag_button, 20)
    def get_tag_button(self):
        return self.tag_button

class ProductTypeTagButton(SaleTypeTagButton):
    def __init__(self, text, container = None):
        super().__init__(text, container)
        self.tag_button.setStyleSheet("QPushButton {font:600 11pt Manrope;text-align:center;"
                                      "background-color:#feecc7;color:#fba224;"
                                      "border-radius: 5px;}QPushButton:hover{background-color:#fdd78a; color:#fff5e1;}")
        
def clear_frame(frame):
    for widget in frame.findChildren(QPushButton):
        frame.layout().removeWidget(widget)

def remove_children(frame):
    layout = frame.layout()  # Get the layout managing the frame
    if layout:
        while layout.count():  # Remove all widgets from the layout
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()  # Delete the widget if needed
            else:
                sublayout = item.layout()
                if sublayout:
                    remove_children(sublayout.parentWidget())  # Recursively remove children

# def clear_widget(widget):
#     for i in reversed(range(widget.layout().count())):
#         widget.layout().itemAt(i).widget().setParent(None)

def clear_widget(widget):
    # If widget is a layout, clear its contents
    if hasattr(widget, "count"):
        for i in reversed(range(widget.count())):
            item = widget.itemAt(i)
            if item is not None:
                widget.removeItem(item)
    # If widget is a container, clear its child widgets
    elif hasattr(widget, "layout"):
        layout = widget.layout()
        if layout is not None:
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item is not None and item.widget() is not None:
                    item.widget().setParent(None)
    # If widget is a single widget, set its parent to None
    elif isinstance(widget, QWidget):
        widget.setParent(None)


def remove_cur_layout(label):
    current_layout = label.layout()
    if current_layout:
        # Remove the layout from the label
        while current_layout.count():
            item = current_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                layout = item.layout()
                if layout is not None:
                    while layout.count():
                        inner_item = layout.takeAt(0)
                        inner_widget = inner_item.widget()
                        if inner_widget is not None:
                            inner_widget.deleteLater()
                    layout.deleteLater()
        del current_layout


def border_radius(pixmap, radius):
    mask = QPixmap(pixmap.size())
    mask.fill(Qt.transparent)
    painter = QPainter(mask)
    painter.setRenderHint(QPainter.Antialiasing)
    path = QPainterPath()
    path.addRoundedRect(pixmap.rect(), radius, radius)
    painter.fillPath(path, QColor(Qt.white))
    painter.end()
    pixmap.setMask(mask)

def set_preferred_size(w, padding = 20, hpadding = 8):
    preferred_size = w.sizeHint()
    preferred_width = preferred_size.width()
    preferred_height = preferred_size.height()
    text_width = w.fontMetrics().boundingRect(w.text()).width() + padding
    w.setMinimumWidth(text_width)
    min_height = w.fontMetrics().boundingRect(w.text()).height() + hpadding
    w.setMinimumHeight(min_height)
    w.setFixedSize(QSize(max(preferred_width, text_width), max(preferred_height, min_height)))
    return w

class Spacer():
    def __init__(self):
        self.spacer = QWidget()
        self.spacer.setFixedSize(QSize(230, 300))
    def get_spacer(self):
        return self.spacer

def get_button_content_width(button):
    font_metrics = button.fontMetrics()
    text_width = font_metrics.horizontalAdvance(button.text())
    return text_width    

class PathDivider(QLabel):
    def __init__(self):
        super().__init__()
        self.setText('>')
    def get_divider(self):
        return self

class PathSource(QLabel):
    clicked = Signal(object)
    def __init__(self, source_name, stack, stack_index, product_ui):
        super().__init__()
        self.setText(source_name)
        self.stack_index = stack_index
        self.stack = stack
        self.clicked.connect(product_ui.handle_path_click)
    def mousePressEvent(self, event):
        print("Mouse pressed on path")
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self)
    def get_path_source(self):
        return self
    def get_stack_index(self):
        return self.stack_index
    def get_name(self):
        return self.text()
    def get_stacked_widget(self):
        return self.stack
    def get_stacked_index(self):
        return self.stack_index
