#  Open terminal #2 (run one of below commands at a time)
#  ros2 topic pub -1 /ctrl_pamis interfaces_cdf/msg/PAMI "{num_pamis: 1, type: 1, arg1: 90}"
#  ros2 topic pub -1 /ctrl_pamis interfaces_cdf/msg/PAMI "{num_pamis: 1, type: 2, arg1: 100}"
#  ros2 topic pub -1 /ctrl_pamis interfaces_cdf/msg/PAMI "{num_pamis: 1, type: 3, arg1: 450, arg2: 450, arg3: 90}"
#  ros2 topic pub -1 /ctrl_pamis interfaces_cdf/msg/PAMI "{num_pamis: 1, type: 4, arg1: 1000, arg2: -1}"
# 
#  $ ros2 service call /name_example name_project/srv/srv_msg_exemples "data : x"


import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from .ui_mainwindow import Ui_MainWindow #ne pas oublier de faire 'pyside6-uic mainwindow.ui -o ui_mainwindow.py' à chaque modif du .ui

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from interfaces_cdf.msg import PAMI
from threading import Thread

from flask import Flask

flsk = Flask(__name__)
ros_message = "Aucun message reçu"

# Protocol de com ----------------------------------------------------
class Message():
    def __init__(self):
        #Sur la page web : 
        #[num_msg_int],[num_pamis],[order],[arg1],[arg2],[arg3]
        self.num_msg_int = 0
        self.num_msg_str = str(self.num_msg_int)  #numero du msg, le pamis l'utilisera pour savoir si un nv msg à spawn ou non
        self.num_pamis = "0"
        self.order = "0"
        self.arg1 = "0"
        self.arg2 = "0"
        self.arg3 = "0"
    # fin de la classe

msg_pamis = Message() #structure mise en global
# Protocol de com ----------------------------------------------------

# ROS 2 --------------------------------------------------------------
class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('controle_pamis_web')

        self.pami_ = self.create_subscription(
            PAMI, 
            'ctrl_pamis',
            self.pami_callback,
            10)
        self.pami_ # prevent unused variable warning

    def pami_callback(self, msg):
        msg_pamis.num_msg_int +=1
        msg_pamis.num_msg_str = str(msg_pamis.num_msg_int)
        msg_pamis.num_pamis = str(msg.num_pamis)
        msg_pamis.order = str(msg.type)
        msg_pamis.arg1 = str(msg.arg1)
        msg_pamis.arg2 = str(msg.arg2)
        msg_pamis.arg3 = str(msg.arg3)
        self.get_logger().info('I heard from /ctrl_pamis, order : %d' % msg.type)

    # fin de la classe

def run_ros_node():
    ros_node = MinimalSubscriber()
    rclpy.spin(ros_node)
    rclpy.shutdown()
# ROS 2 --------------------------------------------------------------





# MainWindow ---------------------------------------------------------
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sendButton_rotation.clicked.connect(self.rotation)#activation des callback
        self.ui.sendButton_translation.clicked.connect(self.translation)
        self.ui.sendButton_XYT.clicked.connect(self.XYT)
        self.ui.sendButton_recalage.clicked.connect(self.recalage)
        self.ui.sendButton_XYT_2.clicked.connect(self.changementPosition)
        self.ui.sendButton_jack.clicked.connect(self.departMatch)

    def departMatch(self):#callback function
        msg_pamis.num_msg_int +=1
        msg_pamis.num_msg_str = str(msg_pamis.num_msg_int)
        msg_pamis.num_pamis = self.ui.comboBox.currentText()
        msg_pamis.order = "6"
        msg_pamis.arg1 = "1"
        msg_pamis.arg2 = "0"
        msg_pamis.arg3 = "0"    

    def rotation(self):
        msg_pamis.num_msg_int +=1
        msg_pamis.num_msg_str = str(msg_pamis.num_msg_int)
        msg_pamis.num_pamis = self.ui.comboBox.currentText()
        msg_pamis.order = "1"
        degree = int(self.ui.lineEdit_rotation.text())
        degree *= 10 #dizieme de degree
        msg_pamis.arg1 = str(int(degree))
        msg_pamis.arg2 = "0"
        msg_pamis.arg3 = "0"

    def translation(self):
        msg_pamis.num_msg_int +=1
        msg_pamis.num_msg_str = str(msg_pamis.num_msg_int)
        msg_pamis.num_pamis = self.ui.comboBox.currentText()
        msg_pamis.order = "2"
        distance = int(self.ui.lineEdit_translation.text())
        msg_pamis.arg1 = str(distance)
        msg_pamis.arg2 = "0"
        msg_pamis.arg3 = "0"

    def XYT(self):
        msg_pamis.num_msg_int +=1
        msg_pamis.num_msg_str = str(msg_pamis.num_msg_int)
        msg_pamis.num_pamis = self.ui.comboBox.currentText()
        msg_pamis.order = "3"
        x = int(self.ui.lineEdit_XYT_x.text())
        y = int(self.ui.lineEdit_XYT_y.text())
        theta = int(self.ui.lineEdit_XYT_theta.text()) * 10 #dizieme de degree

        msg_pamis.arg1 = str(x)
        msg_pamis.arg2 = str(y)
        msg_pamis.arg3 = str(theta)

    def recalage(self):
        msg_pamis.num_msg_int +=1
        msg_pamis.num_msg_str = str(msg_pamis.num_msg_int)
        msg_pamis.num_pamis = self.ui.comboBox.currentText()
        msg_pamis.order = "4"
        distance = int(self.ui.lineEdit_recalage_distance.text())
        coordonnee = 1 if self.ui.comboBox_recalage.currentText()=="x" else -1

        msg_pamis.arg1 = str(distance)
        msg_pamis.arg2 = str(coordonnee)
        msg_pamis.arg3 = "0"
    
    def changementPosition(self):
        msg_pamis.num_msg_int +=1
        msg_pamis.num_msg_str = str(msg_pamis.num_msg_int)
        msg_pamis.num_pamis = self.ui.comboBox.currentText()
        msg_pamis.order = "5"
        x = int(self.ui.lineEdit_XYT_x_2.text())
        y = int(self.ui.lineEdit_XYT_y_2.text())
        theta = int(self.ui.lineEdit_XYT_theta_2.text()) * 10 #dizieme de degree

        msg_pamis.arg1 = str(x)
        msg_pamis.arg2 = str(y)
        msg_pamis.arg3 = str(theta)

    def closeEvent(self, event):
        print("Au revoir")
        rclpy.shutdown()
        event.accept()

    # fin de la classe
# MainWindow ---------------------------------------------------------





def run_flask():
    flsk.run(host='192.168.188.129', port=8080, debug=False) #si debug mis à true, cela ne marchera plus car flask est dans une thread

@flsk.route('/')
def home():
    return f'Hello, World! ROS control pamis :> Go to /pamis'

@flsk.route('/pamis')
def pamis():
    return f'{msg_pamis.num_msg_str},{msg_pamis.num_pamis},{msg_pamis.order},{msg_pamis.arg1},{msg_pamis.arg2},{msg_pamis.arg3}'

def window_show():
    window = MainWindow()
    window.show()

def main(args=None):
    app = QApplication([])
    # run_ros_node()
    rclpy.init(args=args)
    ros_thread = Thread(target=run_ros_node)
    ros_thread.start()

    # run_flask()
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    window = MainWindow()
    window.show()


    sys.exit(app.exec())

if __name__ == "__main__":
    main()
