import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shaggy/paper_implementation/agv_localisation_implementation/install/localization'
