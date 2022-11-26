#!/usr/bin/env python3
"""
Helps to treat the models directory as a package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
