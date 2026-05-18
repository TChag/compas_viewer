from PySide6.QtWidgets import QLabel

from compas_viewer.components.component import Component

from .mainwindow import MainWindow


class StatusBar(Component):
    def __init__(self, window: MainWindow) -> None:
        super().__init__()
        self.widget = window.widget.statusBar()
        self.status_label = QLabel(text="Ready...")
        self.widget.addWidget(self.status_label)

    def set_status(self, text: str):
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.setText(text)
