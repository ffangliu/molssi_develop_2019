"""
molssi_develops_2019
A short description of the project.
"""

# Make Python 2 and 3 imports work the same
# Safe to remove with Python 3-only code
from __future__ import absolute_import

# Add imports here
from .molssi_develops_2019 import *
from .molssi_math import canvas, mean
from .string_util import title_case

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
