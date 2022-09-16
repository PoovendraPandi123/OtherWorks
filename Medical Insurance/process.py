from Packages import read_file as rf
from Packages import file_properties as fp
import logging

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

        if read_data["Status"] == "Success":
            return read_data["data"]
        else:
            return None
    except Exception as e:
        print(e)
        logging.error("Error in Get Data Function!!!", exc_info=True)
        return None

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

def medical_insurance():
    try:
        file_properties_data = get_file_properties_data()

        # Reading Associate Data:
        # associate_data_properties = file_properties_data["associate_data"][0]
        #
        # associate_data = get_data(
        #     file_path = associate_data_properties["file_path"],
        #     sheet_name = associate_data_properties["sheet_name"],
        #     source_extension = associate_data_properties["source_extension"],
        #     attribute_list = associate_data_properties["source_columns"],
        #     column_start_row = associate_data_properties["column_start_row"],
        #     attribute_data_types_list = associate_data_properties["attribute_data_types_list"],
        #     unique_list = associate_data_properties["unique_list"]
        # )
        #
        # print("associate_data")
        # print(associate_data)

        # Reading Salary Register
        salary_register_data_properties = file_properties_data["salary_register"][0]

        salary_register = get_data(
            file_path = salary_register_data_properties["file_path"],
            sheet_name = salary_register_data_properties["sheet_name"],
            source_extension = salary_register_data_properties["source_extension"],
            attribute_list = salary_register_data_properties["source_columns"],
            column_start_row = salary_register_data_properties["column_start_row"],
            attribute_data_types_list = salary_register_data_properties["attribute_data_types_list"],
            unique_list = salary_register_data_properties["unique_list"]
        )
        # Rename the columns to compare with Associate Data
        salary_register_columns_dict = salary_register_data_properties["rename_columns"]
        salary_register.rename(columns = salary_register_columns_dict, inplace=True)

        # Adding new column to the salary register
        salary_register_data = create_new_column(data_frame=salary_register, data_frame_series_tuple=(salary_register["OL CTC"]), new_column_name_tuple=('SR CTC'))


    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Function!!!", exc_info = True)



# # Reading the required Data
#
# # 1) Associate Data for Insurance Team
#
# associate_data = get_data(
#     file_path = "H:/Clients/TeamLease/Medical Insurance Recon/2022/01. Advent All file/Associate_data_for_Insurance_team- June.xlsb",
#     sheet_name = "Associate_data_for_Insurance_te",
#     source_extension="xlsb",
#     attribute_list = []
# )