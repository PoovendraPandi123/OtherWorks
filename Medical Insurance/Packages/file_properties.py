import logging
import os
import json

class FileProperties:

    _property_file = ''
    _file_properties = ''

    def __init__(self, property_folder, property_file):
        if os.path.exists(property_folder):
            self._property_file = property_file
            self.load_properties()
        else:
            print("File Property Folder Not Found!!!")
            logging.info("File Properties Not Found!!!")

    def load_properties(self):
        try:
            with open(self._property_file, "r") as f:
                self._file_properties = json.load(f)
        except Exception as e:
            print(e)
            logging.error("Error in Load File Properties JSON!!!", exc_info=True)

    def get_file_properties(self):
        return self._file_properties