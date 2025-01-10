# SPDX-FileCopyrightText: 2025 Sou Kawamoto <s23c1040mc@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'countup', 10)
        self.timer = self.create_timer(0.5, self.publish_message)
        self.count = 0

    def publish_message(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"Count: {self.count}, Time: {now}"
        self.pub.publish(String(data=message))
        self.get_logger().info(f"Publishing: {message}")
        self.count += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

