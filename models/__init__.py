#!/usr/bin/python3
"""
The __init__ dunder method for the models
Makes the models directory become a package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
