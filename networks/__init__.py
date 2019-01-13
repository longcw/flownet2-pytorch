import sys
import os


this_dir = os.path.abspath(os.path.dirname(__file__))
for pkg_name in ['channelnorm_package', 'correlation_package', 'resample2d_package']:
    sys.path.insert(0, os.path.join(this_dir, pkg_name))