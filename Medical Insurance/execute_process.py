from process import *
from func import *
from data import *
from merge_data import *


class Execution:

    def __init__(self):
        file_properties_data = get_file_properties_data()
        excel_write_folder_location = 'H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022'

        """ Reading Data """
        # get_associate_data(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)
        # get_salary_register(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)
        # get_mis_data(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)
        # get_alcs_exit_report(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)
        # get_death_report(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)
        # get_inception_data(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)


        """ Merging Data """

        # Adding Associate and Salary Register
        # salary_register_file_path = excel_write_folder_location + "/" + "salary_register_aug_2022_proper.xlsx"
        # associate_data_file_path = excel_write_folder_location + "/" + "associate_data_aug_2022_proper.xlsx"
        #
        # get_ass_merge_sales_register(salary_register_file_path=salary_register_file_path, associate_data_file_path=associate_data_file_path, excel_write_folder_location=excel_write_folder_location)

        # Joining Associate Added Sales Register and MIS Data

        # associate_merged_sales_file_path = excel_write_folder_location + "/" + "associate_added_sales_aug_2022.xlsx"
        # mis_file_path = excel_write_folder_location + "/" + "mis_aug_2022_proper.xlsx"
        #
        # get_ass_merged_sales_merge_mis_data(associate_merged_sales_file_path=associate_merged_sales_file_path, mis_file_path=mis_file_path, excel_write_folder_location=excel_write_folder_location)

        # Filter Only United Insurance Company
        # associate_merged_sales_merged_mis_data_path = excel_write_folder_location + "/" + "associate_merged_sales_merged_mis_data_aug_2022.xlsx"
        #
        # get_filter_insurance_company(associate_merged_sales_merged_mis_data_path=associate_merged_sales_merged_mis_data_path, insurance_company_name='United India Insurance Company Limited', excel_write_folder_location=excel_write_folder_location)

        # Merging Death Tracker
        # data_path = excel_write_folder_location + "/" + "associate_merged_sales_merged_mis_data_united_aug_2022.xlsx"
        # death_tracker_path = excel_write_folder_location + "/" + "death_report_aug_2022_proper.xlsx"
        #
        # get_ass_data_merge_death_tracker(data_path = data_path, death_tracker_path = death_tracker_path, excel_write_folder_location = excel_write_folder_location)

        # Rename Columns
        # data_path = excel_write_folder_location + "/" + "associate_data_united_proper_aug_2022.xlsx"
        #
        # get_rename_columns_for_proper_data(data_path=data_path, file_properties_data=file_properties_data, excel_write_folder_location = excel_write_folder_location)

        # Date Validation and Policy Type
        # data_path = excel_write_folder_location + "/" + "associate_data_for_process_aug_2022.xlsx"
        #
        # get_validate_columns(data_path=data_path, file_properties_data=file_properties_data, excel_write_folder_location=excel_write_folder_location)

        # Create Classification Columns
        # data_path = excel_write_folder_location + "/" + "data_date_validated_aug_2022.xlsx"
        #
        # get_create_classification_columns(data_path=data_path, excel_write_folder_location=excel_write_folder_location)


        """ Process """

        medical_insurance_no_insurance()
        medical_insurance_prior_to_policy()
        medical_insurance_live()
        medical_insurance_deletion()
        medical_insurance_addition_and_deletion()
        medical_insurance_already_deletion()
        medical_insurance_addition()
        medical_insurance_reactivation()
        medical_insurance_next_month_addition()
        medical_insurance_next_month_deletion()
        medical_insurance_migration_addition()
        medical_insurance_death()
        medical_insurance_policy_type()
