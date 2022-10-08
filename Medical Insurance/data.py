import re
from func import *
import pandas as pd
import logging


def get_associate_data(file_properties_data, excel_write_folder_location):
    try:

        associate_data_properties = file_properties_data["associate_data"][0]

        associate_data = get_data(
            file_path=associate_data_properties["file_path"],
            sheet_name=associate_data_properties["sheet_name"],
            source_extension=associate_data_properties["source_extension"],
            attribute_list=associate_data_properties["source_columns"],
            column_start_row=associate_data_properties["column_start_row"],
            attribute_data_types_list=associate_data_properties["attribute_data_types_list"],
            unique_list=associate_data_properties["unique_list"]
        )

        associate_data['ass_client_id_proper'] = associate_data.apply(
            lambda x : x['Client Id'].lower() if len(x['Client Id']) > 0 else x['Client Id'], axis = 1
        )

        if get_write_file(data_frame=associate_data, file_name="associate_data_aug_2022_proper.xlsx", folder_location=excel_write_folder_location):
            print("Associate Data Written Successfully!!!")
        else:
            print("Error in Writing Associate Data!!!")


    except Exception as e:
        print(e)
        logging.error("Error in Get Associate Data Function!!!", exc_info=True)

def get_salary_register(file_properties_data, excel_write_folder_location):
    try:

        salary_register_data_properties = file_properties_data["salary_register"][0]

        salary_register = get_data(
                file_path = salary_register_data_properties["file_path"],
                sheet_name = salary_register_data_properties["sheet_name"],
                source_extension = salary_register_data_properties["source_extension"],
                attribute_list = salary_register_data_properties["source_columns"],
                column_start_row = salary_register_data_properties["column_start_row"],
                attribute_data_types_list = salary_register_data_properties["attribute_data_types_list"],
                unique_list = salary_register_data_properties["unique_list"],
                attribute_list_var_one = salary_register_data_properties["source_columns_var_one"],
                attribute_data_types_list_var_one = salary_register_data_properties["attribute_data_types_list_var_one"],
                unique_list_var_one = salary_register_data_properties["unique_list_var_one"],
                missing_columns_list = salary_register_data_properties["missing_columns_list"]
        )

        salary_register_columns_dict = salary_register_data_properties["rename_columns"]
        salary_register.rename(columns = salary_register_columns_dict, inplace=True)

        # Adding new columns to the salary register to match with the Associate Data """
        salary_register_data = create_new_column(data_frame=salary_register, data_frame_series_tuple=(salary_register["OL CTC"], salary_register["OL_ESIC"]), new_column_name_tuple=('SR CTC', 'SR_ESIC'))

        salary_register_data['ass_client_id_proper'] = salary_register_data.apply(
            lambda x : x['Client Id'].lower() if len(x['Client Id']) > 0 else x['Client Id'], axis = 1
        )

        if get_write_file(data_frame=salary_register_data, file_name="salary_register_aug_2022_proper.xlsx", folder_location=excel_write_folder_location):
            print("Salary Register Written Successfully!!!")
        else:
            print("Error in Writing Salary Register!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Salary Register Function!!!", exc_info=True)

def get_mis_data(file_properties_data, excel_write_folder_location):
    try:
        mis_data_properties = file_properties_data["mis"][0]

        mis = get_data(
            file_path=mis_data_properties["file_path"],
            sheet_name=mis_data_properties["sheet_name"],
            source_extension=mis_data_properties["source_extension"],
            attribute_list=mis_data_properties["source_columns"],
            column_start_row=mis_data_properties["column_start_row"],
            attribute_data_types_list=mis_data_properties["attribute_data_types_list"],
            unique_list=mis_data_properties["unique_list"]
        )

        mis['client_id_proper'] = mis.apply(
            lambda x : x['ClientID'].lower() if len(x['ClientID']) > 0 else x['ClientID'], axis = 1
        )

        if get_write_file(data_frame=mis, file_name="mis_aug_2022_proper.xlsx", folder_location=excel_write_folder_location):
            print("MIS Written Successfully!!!")
        else:
            print("Error in Writing MIS Data!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get MIS Data Function!!!", exc_info=True)

def get_alcs_exit_report(file_properties_data, excel_write_folder_location):
    try:

        exit_report_data_properties = file_properties_data["exit_report"][0]

        exit_report = get_data(
            file_path = exit_report_data_properties["file_path"],
            sheet_name = exit_report_data_properties["sheet_name"],
            source_extension = exit_report_data_properties["source_extension"],
            attribute_list = exit_report_data_properties["source_columns"],
            column_start_row = exit_report_data_properties["column_start_row"],
            attribute_data_types_list = exit_report_data_properties["attribute_data_types_list"],
            unique_list = exit_report_data_properties["unique_list"]
        )

        if get_write_file(data_frame=exit_report, file_name="alcs_exit_report_aug_2022_proper.xlsx", folder_location=excel_write_folder_location):
            print("ALCS Exit Report Written Successfully!!!")
        else:
            print("Error in Writing ALCS Exit Report!!!")

    except Exception as e:
        print(e)
        logging.error("Error in GET ALCS Exit Report Function!!!", exc_info=True)

def get_death_report(file_properties_data, excel_write_folder_location):
    try:

        death_tracker_data_properties = file_properties_data["death_tracker"][0]

        death_tracker = get_data(
            file_path = death_tracker_data_properties["file_path"],
            sheet_name = death_tracker_data_properties["sheet_name"],
            source_extension = death_tracker_data_properties["source_extension"],
            attribute_list = death_tracker_data_properties["source_columns"],
            column_start_row = death_tracker_data_properties["column_start_row"],
            attribute_data_types_list = death_tracker_data_properties["attribute_data_types_list"],
            unique_list = death_tracker_data_properties["unique_list"]
        )

        if get_write_file(data_frame=death_tracker, file_name="death_report_aug_2022_proper.xlsx", folder_location=excel_write_folder_location):
            print("Death Report Written Successfully!!!")
        else:
            print("Error in Writing Death Report!!!")

    except Exception as e:
        print(e)
        logging.error("Error in GET Death Report Function!!!", exc_info=True)

def get_inception_data(file_properties_data, excel_write_folder_location):
    try:

        insurance_company_properties = file_properties_data["insurance_companies"][0]

        inception_data = get_data(
            file_path=insurance_company_properties["file_path"],
            sheet_name=insurance_company_properties["sheet_name"],
            source_extension=insurance_company_properties["source_extension"],
            attribute_list=insurance_company_properties["source_columns"],
            column_start_row=insurance_company_properties["column_start_row"],
            attribute_data_types_list=insurance_company_properties["attribute_data_types_list"],
            unique_list=insurance_company_properties["unique_list"]
        )

        inception_data["Status"] = inception_data.apply(
            lambda x : 'Inactive' if x['Classification'] in ["Deletion"] else 'Active', axis = 1
        )

        inception_data['policy_type_proper'] = inception_data.apply(
            lambda x : 'Non Floater' if re.search(r'non', x['Type'].lower()) else 'Floater', axis = 1
        )

        if get_write_file(data_frame=inception_data, file_name='inception_united_aug_2022_proper.xlsx', folder_location=excel_write_folder_location):
            print("Inception Data Written Successfully")
        else:
            print("Error in Writing Inception Data!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Writing Inception Data!!!", exc_info=True)
