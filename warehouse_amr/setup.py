from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'warehouse_amr'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
         (os.path.join('share', package_name, 'launch'), glob('launch/*')),
         (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
         (os.path.join('share', package_name, 'config'), glob('config/*')),
         (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
         (os.path.join('share', package_name, 'maps'), glob('maps/*')),	
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sushama',
    maintainer_email='sushama@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [ 'amr_intro_node = warehouse_amr.amr_intro_node:main',
        'moving_obstacle_node = warehouse_amr.moving_obstacle_node:main',
        'pickup_drop_task_node = warehouse_amr.pickup_drop_task_node:main',
        ],
    },
)
