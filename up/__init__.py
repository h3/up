import logging

__version__ = '0.0.1+git'  # keep in sync with ../setup.py

log = logging.getLogger('up')
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
