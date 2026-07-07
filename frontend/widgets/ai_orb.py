from enum import Enum

from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget


class OrbState(Enum):
    IDLE = 0
    LISTENING = 1
    THINKING = 2
    SPEAKING = 3
    EXECUTING = 4
    ERROR = 5


class AIOrb(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedSize(320, 320)

        self.state = OrbState.IDLE

        self.radius = 90
        self.direction = 1

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):

        if self.state == OrbState.IDLE:

            self.radius += self.direction * 0.25

            if self.radius > 95:
                self.direction = -1

            if self.radius < 90:
                self.direction = 1

        self.update()

    def set_state(self, state):

        self.state = state

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        center = self.rect().center()

        glow = QColor(0, 212, 255, 30)

        if self.state == OrbState.ERROR:
            glow = QColor(255, 0, 0, 50)

        painter.setBrush(glow)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(center, self.radius + 20, self.radius + 20)

        pen = QPen(QColor("#00D4FF"))
        pen.setWidth(3)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(center, self.radius + 8, self.radius + 8)

        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawEllipse(center, self.radius, self.radius)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#00D4FF"))
        painter.drawEllipse(center, 65, 65)

        painter.setPen(QColor("white"))
        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            "J.A.R.V.I.S."
        )