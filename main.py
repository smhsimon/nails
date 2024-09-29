import os
import pandas as pd

import settings
import handle_input
import initialize
import archive

initialize.initialize(True)
archive.create_archive()

# $env:FLASK_APP = "interface.py"
# flask run --debug