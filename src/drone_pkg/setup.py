from setuptools import find_packages, setup

package_name = 'drone_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='subhalaxmi',
    maintainer_email='mtg6375@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['simple_node = drone_pkg.__init__:main',
                            'altitude_publisher = drone_pkg.drone_altitude:main',
                            'altitude_subscriber = drone_pkg.target_altitude:main',
                            'arm_server = drone_pkg.arm_server:main',
                            'arm_client = drone_pkg.arm_client:main',
        ],
    },
)
