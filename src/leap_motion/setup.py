from setuptools import setup
import os
from glob import glob

package_name = 'leap_motion'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='federico@cunico.net',
    maintainer_email='federico@cunico.net',
    description='ROS2 package for streaming LeapMotion hand tracking data',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'leap_streamer = leap_motion.leap_motion:main',
        ],
    },
)