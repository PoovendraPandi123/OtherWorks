from datetime import datetime
import pandas as pd
import numpy as np
import re
import logging

from Packages import read_file as rf
from Packages import  file_properties as fp

def get_data(**kwargs):
    try:

        read_data = rf.get_data_from_file(
            file_path = kwargs["file_path"],
            sheet_name = kwargs["sheet_name"],
            source_extension = kwargs["source_extension"],
            attribute_list = kwargs["attribute_list"],
            column_start_row = kwargs["column_start_row"],
            password_protected = '',
            source_password = '',
            attribute_data_types_list = kwargs["attribute_data_types_list"],
            unique_list = kwargs["unique_list"],
            date_key_word = ''
        )

        print("read_data")
        print(read_data)

        if read_data["Status"] == "Success":
            return read_data["data"]
        else:
            return None
    except Exception as e:
        print(e)
        logging.error("Error in Get Data Function!!!", exc_info=True)
        return None

def get_read_proper_data(file_location):
    try:

        data = pd.read_excel(file_location)
        # Making all the column names to string
        data_column_converter = {}
        for name in data.columns:
            data_column_converter[name] = str

        data_frame = pd.read_excel(file_location, converters=data_column_converter)

        return data_frame
    except Exception as e:
        print(e)
        logging.error("Error in Get Read Proper Data Function!!!", exc_info=True)
        return ''

def get_file_properties_data():
    try:
        config_folder = "G:/AdventsProduct/Others/Medical Insurance/conf"
        config_file = config_folder + "/" + "source_properties.json"

        file_properties = fp.FileProperties(property_folder=config_folder, property_file=config_file)
        file_properties_data = file_properties.get_file_properties()

        return file_properties_data
    except Exception as e:
        print(e)
        logging.error("Error in Get File Properties Function!!!", exc_info=True)
        return ""

def get_write_file(data_frame, file_name, folder_location):
    try:
        write_path = folder_location + "/" + file_name
        data_frame.to_excel(write_path, index=False)
        return True
    except Exception as e:
        print(e)
        logging.error("Error in Get Write File Function!!!", exc_info=True)
        return None

def create_new_column(data_frame, data_frame_series_tuple, new_column_name_tuple):
    try:
        for i in range(0, len(new_column_name_tuple)):
            data_frame[new_column_name_tuple[i]] = data_frame_series_tuple[i]
        return data_frame
    except Exception as e:
        print(e)
        logging.error("Error in Create New Column Function!!!", exc_info=True)
        return None

def add_column_with_date_val(data_frame, validate_date_column_name_list):
    try:
        data_column_converter = {}
        for column in  validate_date_column_name_list:
            data_column_converter[column] = str
            new_column_name = column.replace(" ", "_").lower() + '_validate_Yes_or_No'
            # print(data_frame[column])
            data_frame[new_column_name] = data_frame[column].apply(
                lambda x : 'Yes' if re.search(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', str(x)) else 'No'
            )

        return data_frame
    except Exception as e:
        print(e)
        logging.error("Error in Add Column with Date Val Function!!!", exc_info=True)
        return None

def get_date_difference(date_string_1, date_string_2):
    try:
        if re.search(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', str(date_string_1)) and re.search(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', str(date_string_2)):
            date_string_1_to_date = datetime.strptime(date_string_1, '%Y-%m-%d %H:%M:%S')
            date_string_2_to_date = datetime.strptime(date_string_2, '%Y-%m-%d %H:%M:%S')
            date_delta = date_string_1_to_date - date_string_2_to_date
            return date_delta.days
        return np.nan
    except Exception as e:
        print(e)
        logging.error("Error in Get Date Difference!!!", exc_info=True)
        return None