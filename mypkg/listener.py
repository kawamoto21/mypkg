# SPDX-FileCopyrightText: 2025 Sou Kawamoto <s23c1040mc@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.create_subscription(String, 'countup', self.callback, 10)

    def callback(self, msg):
        # メッセージを受信して解析
        message = msg.data
        self.get_logger().info(f"Received: {message}")

        # 解析処理: カウント値を抽出して条件に応じて反応
        if "Count" in message:
            count = int(message.split(",")[0].split(":")[1].strip())
            if count % 5 == 0:  # カウントが5の倍数なら通知
                self.get_logger().warn(f"Count {count} is a multiple of 5!")

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

