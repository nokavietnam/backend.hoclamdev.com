# import imp
# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))

# wsgi = imp.load_source('wsgi', 'app.py')
# application = wsgi.app

import importlib.util
import sys

spec = importlib.util.spec_from_file_location("app", "app.py")
module = importlib.util.module_from_spec(spec)
sys.modules["app"] = module
spec.loader.exec_module(module)
application = module.application
