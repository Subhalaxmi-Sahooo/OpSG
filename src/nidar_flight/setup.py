from setuptools import find_packages, setup

package_name = 'nidar_flight'

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
        'console_scripts': ["takeoff_node = nidar_flight.takeoff_node:main",
                            "square_path_node = nidar_flight.square_path:main"
        ],
    },
)
