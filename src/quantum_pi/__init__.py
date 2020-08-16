#!/usr/bin/env python

# * -------------------------- * #
# * src/quantum_pi/__init__.py * #
# * -------------------------- * #

from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = 'quantum-pi'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = '0.0.0'
finally:
    del get_distribution, DistributionNotFound

# EOF #
