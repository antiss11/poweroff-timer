import gui
import sys
from PyQt5 import QtWidgets
import time
import threading
from PyQt5.Qt import QTime, QFocusEvent, QWidget



class Timer(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_sleep.setChecked(True)
        self.radioButton_in.setChecked(True)
        self.centralwidget.setFocus()
        self.pushButton_start.clicked.connect(self.start_button)
        self.time_thread_event = False


            


    def _update(self):
        while self.time_thread_event is False:
            time_now = QTime.currentTime()
            self.timeEdit.setTime(time_now)
            time.sleep(1)
        print('stop')

    def time_thread(self):
        threading.Thread(target=self._update).start()

    def get_timer_type(self):
        if self.radioButton_after.isChecked():
            return "after"
        elif self.radioButton_in.isChecked():
            return "in"

    def get_action_type(self):
        if self.radioButton_off.isChecked():
            return "off"
        elif self.radioButton_restart.isChecked():
            return "restart"
        elif self.radioButton_sleep.isChecked():
            return "sleep"

    def start_action(self, timer_type, action_type):
        pass

    def start_button(self):
        pass




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Timer()
    window.show()
    # window.time_thread()

    app.exec_()

if __name__ == "__main__":
    main()