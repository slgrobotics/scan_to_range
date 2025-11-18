#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan, Range


class ScanToRangeNode(Node):

    def __init__(self):
        super().__init__('scan_to_range')

        # Declare parameters
        self.declare_parameter('input_topic', '/scan')
        self.declare_parameter('output_topic', '/range')

        input_topic = self.get_parameter('input_topic').value
        output_topic = self.get_parameter('output_topic').value

        self.get_logger().info(f"Listening on:   {input_topic}")
        self.get_logger().info(f"Publishing to:  {output_topic}")

        self.pub_ = self.create_publisher(Range, output_topic, 10)
        self.sub_ = self.create_subscription(
            LaserScan, input_topic, self.scan_callback, 10
        )

    def scan_callback(self, scan_msg: LaserScan):

        if not scan_msg.ranges:
            return

        # Choose what you want here:
        # value = min(scan_msg.ranges)  # shortest
        # value = max(scan_msg.ranges)  # longest
        value = scan_msg.ranges[len(scan_msg.ranges)//2]  # center ray

        msg = Range()
        msg.header = scan_msg.header
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = scan_msg.angle_increment
        msg.min_range = scan_msg.range_min
        msg.max_range = scan_msg.range_max
        msg.field_of_view = 0.1 # good for typical "Ping" sonar
        msg.variance = 0.01
        msg.range = float(value)

        self.pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ScanToRangeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
