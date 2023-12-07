import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from interfaces_cdf.msg import PAMI
from threading import Thread

from flask import Flask

flsk = Flask(__name__)
ros_message = "Aucun message reçu"

num_msg = "0"  #numero du msg, le pamis l'utilisera pour savoir si un nv msg à spawn ou non
num_pamis = "0"
order = "0"
arg1 = "0"
arg2 = "0"
arg3 = "0"


# ROS 2 --------------------------------------------------------------
class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('controle_pamis_web')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription # prevent unused variable warning

        self.pami_ = self.create_subscription(
            PAMI, 
            'ctrl_pamis',
            self.pami_callback,
            10)
        self.pami_ # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        global ros_message
        ros_message = msg.data

    def pami_callback(self, msg):
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

#        self.ui.sendButton.clicked.connect(self.doSomething)
#        self.i = 0
#        self.node_ = MinimalPublisher()

#    def doSomething(self):
#        msg = String()
#        msg.data = self.ui.lineEdit_1.text()
#        self.node_.publish_string(msg)

    def closeEvent(self, event):
        print("Au revoir")
        rclpy.shutdown()
        event.accept()

    # fin de la classe
# MainWindow ---------------------------------------------------------





def run_flask():
    flsk.run(host='192.168.188.129', port=8080, debug=False)

@flsk.route('/')
def home():
    return f'Hello, World! ROS Message: {ros_message}'

@flsk.route('/pamis')
def pamis():
    return f'{num_pamis},{order},{arg1},{arg2},{arg3}'

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
