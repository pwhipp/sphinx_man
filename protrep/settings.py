import os
import logging

_dirs = os.path.abspath(__file__).split('/')
BASE_DIR = '/'.join(_dirs[0:-2])
PROJECT_DIR = os.path.dirname(BASE_DIR)

LOGGING = {
    'filename': f"{PROJECT_DIR}/sphinx_man.log",
    'format': '%(asctime)s :%(levelname)s: %(message)s',
    'datefmt': '%Y/%m/%d %H:%M:%S',
    'level': logging.DEBUG}

SIGNING_RULES_FILENAME = '.signing_rules.yaml'
