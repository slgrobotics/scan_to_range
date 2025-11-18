from setuptools import setup

package_name = 'scan_to_range'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='LaserScan → Range converter node',
    license='MIT',
    entry_points={
        'console_scripts': [
            'scan_to_range = scan_to_range.scan_to_range_node:main',
        ],
    },
)
