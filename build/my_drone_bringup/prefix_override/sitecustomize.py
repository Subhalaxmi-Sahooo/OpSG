import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/subhalaxmi/nidar_ws/install/my_drone_bringup'
