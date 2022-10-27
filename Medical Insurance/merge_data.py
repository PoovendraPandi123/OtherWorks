import re
from func import *
import pandas as pd
import logging

def get_ass_merge_sales_register(salary_register_file_path, associate_data_file_path, excel_write_folder_location):
    try:

        salary_register_data = get_read_proper_data(file_location=salary_register_file_path)
        associate_data = get_read_proper_data(file_location=associate_data_file_path)

        associate_added_sr = pd.merge(associate_data, salary_register_data, left_on=['Employee No'], right_on=['Employee No'], how='outer', suffixes=('', '_y'))
        associate_added_sr.drop(associate_added_sr.filter(regex='_y$').columns, axis=1, inplace=True)

        if get_write_file(data_frame=associate_added_sr, file_name="associate_added_sales_sept_2022.xlsx", folder_location=excel_write_folder_location):
            print("Associate Added Sales Register Written Successfully!!!")
        else:
            print("Error in Associate Added Sales Register!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Associate Merged Sales Register!!!", exc_info=True)

def get_ass_merged_sales_merge_mis_data(associate_merged_sales_file_path, mis_file_path, excel_write_folder_location):
    try:

        associate_merged_sales_data = get_read_proper_data(file_location=associate_merged_sales_file_path)
        mis_data = get_read_proper_data(file_location=mis_file_path)

        associate_merged_sales_merged_mis_data = pd.merge(associate_merged_sales_data, mis_data, left_on=['ass_client_id_proper'], right_on=['client_id_proper'], how='left', suffixes=('', '_y'))
        associate_merged_sales_merged_mis_data.drop(associate_merged_sales_merged_mis_data.filter(regex='_y$').columns, axis=1, inplace=True)

        if get_write_file(data_frame=associate_merged_sales_merged_mis_data, file_name="associate_merged_sales_merged_mis_data_sept_2022.xlsx", folder_location=excel_write_folder_location):
            print("Associate Merged Sales Merged MIS Data Written Successfully!!!")
        else:
            print("Error in Writing Associate Merged Sales Merged MIS Data!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Associate Merged Sales Merge MIS Data!!!", exc_info=True)

def get_filter_insurance_company(associate_merged_sales_merged_mis_data_path, insurance_company_name, excel_write_folder_location):
    try:

        associate_merged_sales_merged_mis_data = get_read_proper_data(associate_merged_sales_merged_mis_data_path)

        data_insurance_company = associate_merged_sales_merged_mis_data[associate_merged_sales_merged_mis_data['Insurance Company'] == insurance_company_name]

        if get_write_file(data_frame=data_insurance_company, file_name="associate_merged_sales_merged_mis_data_united_sept_2022.xlsx", folder_location=excel_write_folder_location):
            print("Insurance Company Written Successfully!!!")
        else:
            print("Error in Writing Insurance Company Data!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Filter Insurance Company Function!!!", exc_info=True)

def get_ass_data_merge_death_tracker(data_path, death_tracker_path, excel_write_folder_location):
    try:

        data = get_read_proper_data(file_location=data_path)
        death_tracker_data = get_read_proper_data(file_location=death_tracker_path)

        associate_merged_death_data = pd.merge(data, death_tracker_data, left_on=['Employee No'], right_on=['Emp Code'], how='left', suffixes=('', '_y'))

        if get_write_file(data_frame=associate_merged_death_data, file_name="associate_data_united_proper_sept_2022.xlsx", folder_location=excel_write_folder_location):
            print("Associate Added Death Tracker Written Successfully!!!")
        else:
            print("Error in Writing Associate Added Death Tracker!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Associate Data Merge Death Tracker!!!", exc_info=True)

def get_rename_columns_for_proper_data(data_path, file_properties_data, excel_write_folder_location):
    try:

        data = get_read_proper_data(file_location=data_path)

        data.columns = file_properties_data["associate_merged_sr_mis_exit_death"][0]["rename_columns_one"]

        if get_write_file(data_frame=data, file_name="associate_data_for_process_sept_2022.xlsx", folder_location=excel_write_folder_location):
            print("Data Required Written Successfully!!!")
        else:
            print("Error in Writing Data Required!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Rename Columns For Proper Data Function!!!", exc_info=True)

def get_validate_columns(data_path, file_properties_data, excel_write_folder_location):
    try:

        data = get_read_proper_data(file_location=data_path)

        data["policy_type_proper"] = data.apply(
            lambda x : 'Non Floater' if re.search(r'non', x['mis_policy_type'].lower()) else 'Floater', axis = 1
        )

        data_date_validated = add_column_with_date_val(data_frame=data, validate_date_column_name_list=file_properties_data["associate_merged_sr_mis_exit_death"][0]["date_validation_columns_one"])

        if get_write_file(data_frame=data_date_validated, file_name="data_date_validated_sept_2022.xlsx", folder_location=excel_write_folder_location):
            print("Data Date Validated Written Successfully")
        else:
            print("Error in Writing Data Date Validated!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Validate Data Columns!!!", exc_info=True)

def get_create_classification_columns(data_path, excel_write_folder_location):
    try:

        data = get_read_proper_data(file_location=data_path)

        data['classification_1'] = ''
        data['classification_2'] = ''
        data['classification_3'] = ''

        if get_write_file(data_frame=data, file_name="data_sept_2022_proper.xlsx", folder_location=excel_write_folder_location):
            print("Classification Columns Written Successfully!!!")
        else:
            print("Error in Writing Classification Columns!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Get Create Classification Columns!!!", exc_info=True)

def get_update_inception_data_column(data_dict, column_name):
    try:
        data_column_name = column_name + "_y"
        return data_dict[data_column_name]

    except Exception as e:
        print(e)
        logging.error("Error in Get Update Inception Data!!!", exc_info=True)

def get_inception_data_all(data_path_last_month, data_path_second_last_month, excel_write_folder_location):
    try:

        inception_data_last_month = get_read_proper_data(file_location=data_path_last_month)
        inception_data_second_last_month = get_read_proper_data(file_location=data_path_second_last_month)

        inception_data = pd.merge(inception_data_last_month, inception_data_second_last_month, left_on=['Emp Code'], right_on=['Emp Code'], how='outer', suffixes=('', '_y'))

        inception_data_proper = inception_data.replace(np.nan, '')

        inception_data_columns = list(inception_data_last_month.columns)
        inception_data_columns.remove('Emp Code')
        inception_data_columns.remove('Sl No')

        for column in inception_data_columns:

            inception_data_proper[column] = inception_data_proper.apply(
                lambda x : get_update_inception_data_column(x, column) if x["Sl No"] == '' else x[column], axis=1
            )

        inception_data_proper['Sl No'] = inception_data_proper.apply(
            lambda x: get_update_inception_data_column(x, "Sl No") if x["Sl No"] == '' else x["Sl No"], axis=1
        )

        inception_data_proper.drop(inception_data_proper.filter(regex='_y$').columns, axis=1, inplace=True)

        if get_write_file(data_frame=inception_data_proper, file_name="inception_data_united_all.xlsx", folder_location=excel_write_folder_location):
            print("Data Inception Written Successfully!!!")
        else:
            print("Error in Writing Inception Data!!!")


    except Exception as e:
        print(e)
        logging.error("Error in Get Inception Data!!!", exc_info=True)