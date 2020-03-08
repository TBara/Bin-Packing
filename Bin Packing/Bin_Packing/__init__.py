"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Bin_Packing.views
