from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from frontend.widgets.ai_orb import AIOrb


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("JARVIS X")
        self.resize(1600, 900)
        self.setMinimumSize(1400, 800)

        self.build_ui()

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ==========================
        # Top Bar
        # ==========================

        top_bar = QFrame()
        top_bar.setFixedHeight(45)
        top_bar.setStyleSheet("""
            background:#111827;
            color:white;
        """)

        top_layout = QHBoxLayout(top_bar)

        title = QLabel("J.A.R.V.I.S.")
        title.setStyleSheet("font-size:18px;font-weight:bold;")

        top_layout.addWidget(title)
        top_layout.addStretch()

        status = QLabel("● ONLINE")
        status.setStyleSheet("color:#22C55E;font-size:14px;")

        top_layout.addWidget(status)

        main_layout.addWidget(top_bar)

        # ==========================
        # Body
        # ==========================

        body = QFrame()

        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar

        sidebar = QFrame()
        sidebar.setFixedWidth(80)

        sidebar.setStyleSheet("""
            background:#111827;
        """)

        body_layout.addWidget(sidebar)

        # Main Area

        content = QWidget()

        content.setStyleSheet("""
            background:#0B0F19;
        """)

        content_layout = QVBoxLayout(content)

        content_layout.addStretch()

        self.orb = AIOrb()

        content_layout.addWidget(
            self.orb,
            alignment=Qt.AlignCenter
        )

        text = QLabel("Awaiting your command...")

        text.setStyleSheet("""
            color:white;
            font-size:18px;
        """)

        content_layout.addWidget(
            text,
            alignment=Qt.AlignCenter
        )

        content_layout.addStretch()

        body_layout.addWidget(content)

        main_layout.addWidget(body)

        # ==========================
        # Bottom Status Bar
        # ==========================

        bottom = QFrame()

        bottom.setFixedHeight(35)

        bottom.setStyleSheet("""
            background:#111827;
            color:white;
        """)

        bottom_layout = QHBoxLayout(bottom)

        bottom_layout.addWidget(QLabel("Status : Ready"))

        bottom_layout.addStretch()

        bottom_layout.addWidget(QLabel("Gemini Connected"))

        main_layout.addWidget(bottom)