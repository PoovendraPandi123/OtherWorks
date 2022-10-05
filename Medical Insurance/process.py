import re

from func import *
import pandas as pd
import logging
from classifications import *

# def get_salary_register_data_columns(file_path, sheet_name, source_extension, column_start_row):
#     try:
#         data = pd.DataFrame()
#         if source_extension in ['xlsb']:
#             data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=int(column_start_row) - 1, engine='pyxlsb', nrows=1)
#
#             print("data")
#             print(data)
#
#         return list(data.columns)
#     except Exception:
#         logging.error("Error in Get Salary Register Data!!!", exc_info=True)
#         return []
#
# def get_check_salary_register_columns(given_columns, required_columns):
#     try:
#         required_columns_length = len(required_columns)
#         column_found = 0
#
#         for i in range(0, len(required_columns)):
#             for j in range(0, len(given_columns)):
#                 if given_columns[j] == required_columns[i]:
#                     column_found = column_found + 1
#
#         if column_found == required_columns_length:
#             return True
#         else:
#             return False
#
#     except Exception:
#         logging.error("Error in Get Check Salary Register Columns!!!", exc_info=True)
#         return None

def get_required_added_data(file_properties_data, excel_write_folder_location):
    try:
        """ Reading Associate Data: """
        print("Reading Associate Data!!!")
        associate_data_properties = file_properties_data["associate_data"][0]

        associate_data = get_data(
            file_path = associate_data_properties["file_path"],
            sheet_name = associate_data_properties["sheet_name"],
            source_extension = associate_data_properties["source_extension"],
            attribute_list = associate_data_properties["source_columns"],
            column_start_row = associate_data_properties["column_start_row"],
            attribute_data_types_list = associate_data_properties["attribute_data_types_list"],
            unique_list = associate_data_properties["unique_list"]
        )

        print("associate_data")
        print(associate_data)

        """ Reading Salary Register """
        print("Reading Salary Register!!!")
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

        #
        # salary_register_columns_given_list = get_salary_register_data_columns(
        #     file_path=salary_register_data_properties["file_path"],
        #     sheet_name=salary_register_data_properties["sheet_name"],
        #     column_start_row=salary_register_data_properties["column_start_row"],
        #     source_extension=salary_register_data_properties["source_extension"]
        # )
        #
        # check_column_match = get_check_salary_register_columns(
        #     given_columns = salary_register_columns_given_list,
        #     required_columns = salary_register_data_properties["source_columns"]
        # )
        #
        # print("check_column_match", check_column_match)

        # if check_column_match is True:
        #     print("True Side")
        #     salary_register = get_data(
        #         file_path = salary_register_data_properties["file_path"],
        #         sheet_name = salary_register_data_properties["sheet_name"],
        #         source_extension = salary_register_data_properties["source_extension"],
        #         attribute_list = salary_register_data_properties["source_columns"],
        #         column_start_row = salary_register_data_properties["column_start_row"],
        #         attribute_data_types_list = salary_register_data_properties["attribute_data_types_list"],
        #         unique_list = salary_register_data_properties["unique_list"]
        #     )
        #
        #     get_write_file(data_frame=salary_register, file_name='salary_register_changed_august.xlsx', folder_location=excel_write_folder_location)
        # elif check_column_match is False:
        #     print("False Side")
        #     salary_register = get_data(
        #         file_path = salary_register_data_properties["file_path"],
        #         sheet_name = salary_register_data_properties["sheet_name"],
        #         source_extension = salary_register_data_properties["source_extension"],
        #         attribute_list = salary_register_data_properties["source_columns_var_one"],
        #         column_start_row = salary_register_data_properties["column_start_row"],
        #         attribute_data_types_list = salary_register_data_properties["attribute_data_types_list_var_one"],
        #         unique_list = salary_register_data_properties["unique_list_var_one"]
        #     )
        #
        #     # Adding Necessary four columns
        #     salary_register["Basic"] = 'NA'
        #     salary_register['DA'] = 'NA'
        #     salary_register['EMPF'] = 'NA'
        #     salary_register['EMPCOMP'] = 'NA'
        #
        #     get_write_file(data_frame=salary_register, file_name='salary_register_changed_august.xlsx', folder_location=excel_write_folder_location)
        #
        # elif check_column_match is None:
        #     print("Getting None in Get Check Salary Register Columns!!!")

        # get_write_file(data_frame=salary_register, file_name='salary_register_changed_one_august.xlsx', folder_location=excel_write_folder_location)

        # Rename the columns to compare with Associate Data """
        salary_register_columns_dict = salary_register_data_properties["rename_columns"]
        salary_register.rename(columns = salary_register_columns_dict, inplace=True)

        print("salary_register")
        print(salary_register)

        # Adding new columns to the salary register to match with the Associate Data """
        salary_register_data = create_new_column(data_frame=salary_register, data_frame_series_tuple=(salary_register["OL CTC"], salary_register["OL_ESIC"]), new_column_name_tuple=('SR CTC', 'SR_ESIC'))

        """ Reading MIS Data """
        print("Reading MIS Data!!!")
        mis_data_properties = file_properties_data["mis"][0]

        mis = get_data(
            file_path = mis_data_properties["file_path"],
            sheet_name = mis_data_properties["sheet_name"],
            source_extension = mis_data_properties["source_extension"],
            attribute_list = mis_data_properties["source_columns"],
            column_start_row = mis_data_properties["column_start_row"],
            attribute_data_types_list = mis_data_properties["attribute_data_types_list"],
            unique_list = mis_data_properties["unique_list"]
        )

        print("mis")
        print(mis)

        """ Reading Exit Report """
        print("Reading Exit Report!!!")
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

        print("exit_report")
        print(exit_report)

        """ Reading Death Tracker """
        print("Reading Death Case Tracker!!!")
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

        print("death_tracker")
        print(death_tracker)

        """ Reading Insurance Companies """
        print("Reading Insurance Company!!!")

        insurance_company_properties = file_properties_data["insurance_companies"][0]

        insurance_data = get_data(
            file_path = insurance_company_properties["file_path"],
            sheet_name = insurance_company_properties["sheet_name"],
            source_extension = insurance_company_properties["source_extension"],
            attribute_list = insurance_company_properties["source_columns"],
            column_start_row = insurance_company_properties["column_start_row"],
            attribute_data_types_list = insurance_company_properties["attribute_data_types_list"],
            unique_list = insurance_company_properties["unique_list"]
        )

        print("insurance_data")
        print(insurance_data)

        """ Adding Records in Associate Data by Comparing with Salary Data """

        if associate_data is not None:
            if salary_register_data is not None:
                if mis is not None:
                    if exit_report is not None:
                        if death_tracker is not None:
                            if insurance_data is not None:
                                salary_register_write = get_write_file(data_frame=salary_register_data, file_name="salary_register_added.xlsx", folder_location=excel_write_folder_location)
                                if salary_register_write:
                                    print("Salary Register File Written Successfully!!!")
                                else:
                                    print("Error in Writing Salary Register File!!!")

                                """ Adding Records from salary Register """
                                # associate_added_sr = pd.merge(associate_data, salary_register_data, left_on = ['Employee No'], right_on = ['Employee No'], how = 'left', suffixes=('', '_y'))

                                associate_added_sr = pd.merge(salary_register_data, associate_data, left_on = ['Employee No'], right_on = ['Employee No'], how = 'left', suffixes=('', '_y'))
                                associate_added_sr.drop(associate_added_sr.filter(regex='_y$').columns, axis=1, inplace=True)

                                print("associate_added_sr")
                                print(associate_added_sr)

                                if len(associate_added_sr) > 0:
                                    associate_added_sr_write = get_write_file(data_frame=associate_added_sr, file_name="associate_added_salary_register.xlsx", folder_location=excel_write_folder_location)
                                    if associate_added_sr_write:
                                        print("Associated added SR Written Successfully!!!")
                                    else:
                                        print("Error in Writing Associate added SR!!!")

                                    if len(mis) > 0:
                                        mis_write = get_write_file(data_frame=mis, file_name="mis_data.xlsx", folder_location=excel_write_folder_location)
                                        if mis_write:
                                           print("Mis Data Written Successfully!!!")
                                        else:
                                            print("Error in Writing Mis Data!!!")

                                        if len(exit_report) > 0:
                                            exit_report_write = get_write_file(data_frame = exit_report, file_name = "exit_report.xlsx", folder_location=excel_write_folder_location)
                                            if exit_report_write:
                                               print("Exit Report Written Successfully!!!")
                                            else:
                                               print("Error in Writing Exit Report!!!")

                                            if len(death_tracker) > 0:
                                                death_tracker_write = get_write_file(data_frame=death_tracker, file_name = "death_tracker.xlsx", folder_location=excel_write_folder_location)
                                                if death_tracker_write:
                                                    print("Death Tracker Written Successfully!!!")
                                                else:
                                                    print("Error in Writing Death Tracker!!!")

                                                if len(insurance_data) > 0:
                                                    insurance_data_write = get_write_file(data_frame=insurance_data, file_name="united_insurance.xlsx", folder_location=excel_write_folder_location)
                                                    if insurance_data_write:
                                                        print("Insurance Data Written Successfully!!!")
                                                    else:
                                                        print("Error in Writing Insurance Data!!!")

                                                else:
                                                    print("Length of Insurance Data is equals to Zero!!!")
                                            else:
                                                print("Length of Death Tracker is equals to Zero!!!")
                                        else:
                                            print("Length of Exit Report is equals to Zero!!!")
                                    else:
                                        print("Length of MIS is equals to Zero!!!")
                                else:
                                    print("Length of Associate Added SR is equals to Zero!!!")
                            else:
                                print("Insurance Data is None!!!")
                        else:
                            print("Death Tracker is None!!!")
                    else:
                        print("Exit Report is None!!!")
                else:
                    print("MIS Data is None!!!")
            else:
                print("Salary Register is None!!!")
        else:
           print("Associate Data is None!!!")


        """ Increasing Records in Associate Data by comparing with MIS Data """

        # Read from Written Files (associate_data and mis_data):
        associate_added_sr_data = get_read_proper_data('G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/associate_added_salary_register.xlsx')
        mis_data = get_read_proper_data("G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/mis_data.xlsx")

        print("associate_added_sr_data")
        print(associate_added_sr_data)

        print("mis_data")
        print(mis_data)

        if len(associate_added_sr_data) > 0 and len(mis_data) > 0:
             associated_sr_mis_data = pd.merge(associate_added_sr_data, mis_data, left_on=['Client Id'], right_on=['ClientID'], how='left', suffixes=('', '_y'))
             associated_sr_mis_data.drop(associated_sr_mis_data.filter(regex='_y$').columns, axis=1, inplace=True)

             # associate_sr_mis_properties = file_properties_data["associate_sr_mis"][0]
             # associated_sr_mis_data.columns = associate_sr_mis_properties["columns"]

             if len(associated_sr_mis_data) > 0:
                 # associated_sr_mis_data_write = get_write_file(data_frame=associated_sr_mis_data, file_name="associated_sr_mis_data.xlsx", folder_location=excel_write_folder_location)
                 # if associated_sr_mis_data_write:
                 #     print("Associated SR MIS Data Written Successfully!!!")
                 # else:
                 #     print("Error in Writing Associated SR MIS Data!!!")

                 """ Comparing associate_added_sr_data with Exit Report Records """

                 associated_sr_mis_exit_data = pd.merge(associated_sr_mis_data, exit_report, left_on=['Employee No'], right_on=['Employee No'], how='left', suffixes=('', '_y'))
                 # associated_sr_mis_exit_data.drop(associated_sr_mis_exit_data.filter(regex='_y$').columns, axis=1, inplace=True)

                 if len(associated_sr_mis_exit_data) > 0:
                     associated_sr_mis_exit_data_write = get_write_file(data_frame=associated_sr_mis_exit_data, file_name="associated_sr_mis_exit_data.xlsx", folder_location=excel_write_folder_location)
                     if associated_sr_mis_exit_data_write:
                         print("Associate SR MIS Exit Written Successfully!!!")
                     else:
                         print("Error in Writing Associate SR MIS Exit !!!")

                     associated_sr_mis_exit_death_data = pd.merge(associated_sr_mis_exit_data, death_tracker, left_on=['Employee No'], right_on=['Emp Code'], how='left', suffixes=('', '_y'))
                     # associated_sr_mis_exit_death_data.drop(associated_sr_mis_exit_death_data.filter(regex='_y$').columns, axis=1, inplace=True)

                     if len(associated_sr_mis_exit_death_data) > 0:
                         associated_sr_mis_exit_death_data_write = get_write_file(data_frame=associated_sr_mis_exit_death_data, file_name="associated_sr_mis_exit_death_data.xlsx", folder_location=excel_write_folder_location)
                         if associated_sr_mis_exit_death_data_write:
                             print("Associate SR MIS Exit Death Written Successfully!!!")
                         else:
                             print("Error in Writing Associate SR MIS Exit Death!!!")

             else:
                 print("Length of Associated SR Mis Data is equals to Zero!!!")


        """ Validating Dates for Further Classifications """

        associate_merged_sr_mis_exit_death_properties = file_properties_data["associate_merged_sr_mis_exit_death"][0]

        # Read from Written Files (associated_sr_mis_data)
        associate_merged_sr_mis_exit_death_data = get_read_proper_data('G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/associated_sr_mis_exit_death_data.xlsx')
        associate_merged_sr_mis_exit_death_data_proper = associate_merged_sr_mis_exit_death_data[associate_merged_sr_mis_exit_death_properties["columns"]]
        print("associate_merged_sr_mis_exit_death_data_proper")
        print(associate_merged_sr_mis_exit_death_data_proper)

        associate_merged_sr_mis_exit_death_data_proper.columns = associate_merged_sr_mis_exit_death_properties["rename_columns"]

        # Validating All Data Fields and Creating New Date Column with status Flag "Yes" or "No"
        associate_merged_sr_mis_exit_death_data_date_validated = add_column_with_date_val(data_frame=associate_merged_sr_mis_exit_death_data_proper, validate_date_column_name_list=associate_merged_sr_mis_exit_death_properties["date_validation_columns"])
        print("associate_merged_sr_mis_exit_death_data_date_validated")
        print(associate_merged_sr_mis_exit_death_data_date_validated)

        if associate_merged_sr_mis_exit_death_data_date_validated is not None:
            associate_merged_sr_mis_exit_death_data_date_validated_write = get_write_file(
                data_frame=associate_merged_sr_mis_exit_death_data_date_validated, file_name="associate_merged_sr_mis_exit_death_data_date_validated.xlsx", folder_location=excel_write_folder_location
            )
            if associate_merged_sr_mis_exit_death_data_date_validated_write:
                print('Associate Merged SR MIS Exit Death Data Date Validated Written Successfully!!!')
            else:
                print("Error in Writing Associate Merged SR MIS Exit Death Data Validated!!!")
        else:
            print("Associate Merged SR MIS Exit Death Date Validated is None!!!")

        return "Success"
    except Exception as e:
        logging.error("Error in Get Required Data Function!!!", exc_info=True)
        return None

def medical_insurance_test():
    try:

        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022"

        # file_properties_data = get_file_properties_data()

        # Pre Required Files
        # get_required_added_data(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)

        """ Classifications """

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/associate_merged_sr_mis_exit_death_data_date_validated.xlsx")
        inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/united_insurance.xlsx")

        # Updating Status Column in Inception Data

        inception_data["Status"] = inception_data.apply(
            lambda x : 'Active' if x['Classification'] in ["Deletion", "Migration Deletion", "Deletion"] else 'Inactive', axis = 1
        )

        print("data")
        print(data)

        print("inception_data")
        print(inception_data)

        classification_1_data = ''
        classification_2_data = ''
        classification_3_data = ''

        if len(data) > 0:
            if len(inception_data) > 0:

                # Lookup Data with Insurance Data only on Employee Number

                # data_merged_inception = pd.merge(data, insurance_data, left_on=['ass_emp_no'], right_on=['Emp Code'], how='left', suffixes=('', '_y'))
                #
                # get_write_file(data_frame=data_merged_inception, file_name='data_merged_inception.xlsx', folder_location=excel_write_folder_location)

                # Creating one column for a Classification
                data["classification_1"] = ''
                data["classification_2"] = ''
                data["classification_3"] = ''

                """  1) No Insurance """

                classification = Classification()

                data_no_insurance = classification.no_insurance(data_frame=data)

                # data_no_insurance = pd.DataFrame()

                if len(data_no_insurance) > 0:
                    # data_no_insurance_write = get_write_file(data_frame=data_no_insurance, file_name="data.xlsx", folder_location=excel_write_folder_location)
                    # if data_no_insurance_write:
                    #     print("Data Classification No Insurance Written Successfully!!!")
                    # else:
                    #     print("Error in Writing Data Classification No Insurance!!!")

                    """ 2) Next Month Addition """

                    data_next_month_addition = classification.next_month_addition(data_frame=data_no_insurance, upload_month=8, upload_year=2022)

                    if len(data_next_month_addition) > 0:
                        # data_next_month_addition_write = get_write_file(data_frame=data_next_month_addition, file_name='data1.xlsx', folder_location=excel_write_folder_location)
                        # if data_next_month_addition_write:
                        #     print("Data Classification Next Month Addition Written Successfully!!!")
                        # else:
                        #     print("Error in Writing Data Classification Next Month Addition!!!")

                        """ 3) ALCS Deletion """

                        data_alcs_deletion = classification.alcs_deletion(data_frame=data_next_month_addition, upload_month=8, upload_year=2022)

                        if len(data_alcs_deletion) > 0:
                            # data_alcs_deletion_write = get_write_file(data_frame=data_alcs_deletion, file_name="data2.xlsx", folder_location=excel_write_folder_location)
                            # if data_alcs_deletion_write:
                            #     print("Classification ALCS Deletion Written Successfully!!!")
                            # else:
                            #     print("Error in Writing ALCS Deletion")

                            """ 4) Next Month ALCS Deletion """

                            data_next_month_alcs_deletion = classification.next_month_alcs_deletion(data_frame=data_alcs_deletion, upload_month=8, upload_year=2022)

                            if len(data_next_month_alcs_deletion) > 0:
                                # data_next_month_alcs_deletion_write = get_write_file(data_frame=data_next_month_alcs_deletion, file_name="data3.xlsx", folder_location=excel_write_folder_location)
                                # if data_next_month_alcs_deletion_write:
                                #     print("Classification Next Month ALCS Deletion Written Successfully!!!")
                                # else:
                                #     print("Error in Writing Next Month ALCS Deletion!!!")

                                """ 5) Prior To Policy """

                                data_prior_to_policy = classification.prior_to_policy(data_frame=data_next_month_alcs_deletion, inception_data_frame=inception_data)

                                if len(data_prior_to_policy) > 0:
                                    # data_prior_to_policy_write = get_write_file(data_frame=data_prior_to_policy, file_name="data_ptp.xlsx", folder_location=excel_write_folder_location)
                                    # if data_prior_to_policy_write:
                                    #     print("Classification Prior To Policy Written Successfully!!!")
                                    # else:
                                    #     print("Error in Writing Prior To Policy!!!")

                                    """ 6) Addition and Deletion """

                                    data_addition_and_deletion = classification.addition_and_deletion(data_frame = data_prior_to_policy)

                                    if len(data_addition_and_deletion) > 0:
                                        # data_addition_and_deletion_write = get_write_file(data_frame=data_addition_and_deletion, file_name="data_addition_and_deletion.xlsx", folder_location=excel_write_folder_location)
                                        # if data_addition_and_deletion_write:
                                        #     print("Classification Addition and Deletion Written Successfully!!!")
                                        # else:
                                        #     print("Error in Writing Addition and Deletion!!!")

                                        """ 7) Already Deletion """

                                        data_already_deletion = classification.already_deletion(data_frame=data_addition_and_deletion, inception_data_frame=inception_data)

                                        if len(data_already_deletion) > 0:
                                            # data_already_deletion_write = get_write_file(data_frame=data_already_deletion, file_name="data_already_deletion.xlsx", folder_location=excel_write_folder_location)
                                            # if data_already_deletion_write:
                                            #     print("Classification Already Deletion Written Successfully!!!")
                                            # else:
                                            #     print("Error in Writing Already Deletion!!!")

                                            """ 8) Addition """

                                            data_addition = classification.additions(data_frame=data_already_deletion, inception_data_frame=inception_data)

                                            if len(data_addition) > 0:
                                                # data_addition_write = get_write_file(data_frame=data_addition, file_name="data_addition.xlsx", folder_location=excel_write_folder_location)
                                                # if data_addition_write:
                                                #     print("Classification Addition Written Successfully!!!")
                                                # else:
                                                #     print("Error in Writing Addition!!!")

                                                """ 9) Live """

                                                data_live = classification.live(data_frame=data_addition, inception_data_frame=inception_data)

                                                if len(data_live) > 0:
                                                    # data_live_write = get_write_file(data_frame=data_live, file_name="data_live.xlsx", folder_location=excel_write_folder_location)
                                                    # if data_live_write:
                                                    #     print("Classification Live Written Successfully!!!")
                                                    # else:
                                                    #     print("Error in Writing Live!!!")

                                                    """ 10) Migrations """

                                                    data_migration_addition = classification.migration_addition(data_frame=data_live, inception_data_frame=inception_data)

                                                    if len(data_migration_addition) > 0:
                                                        # data_migration_addition_write = get_write_file(data_frame=data_migration_addition, file_name='data_migration_addition.xlsx', folder_location=excel_write_folder_location)
                                                        # if data_migration_addition_write:
                                                        #     print("Classification Migration Addition Written Successfully!!!")
                                                        # else:
                                                        #     print("Error in Writing Migration Addition!!!")
                                                        pass

                                                    else:
                                                        print("Length of Migration Addition is equals to Zero!!!")
                                                else:
                                                    print("Length of Live is equals to Zero!!!")
                                            else:
                                                print("Length of Addition is equals to Zero!!!")
                                        else:
                                            print("Length of Already Deletion is equals to Zero!!!")
                                    else:
                                        print("Length of Addition and Deletion is equals to Zero!!!")
                                else:
                                    print("Length of Prior To Policy is equals to Zero!!!")
                            else:
                                print("Length of Next Month ALCS Deletion is equals to Zero!!!")
                        else:
                            print("Length of Data ALCS Deletion is equals to Zero!!!")
                    else:
                        print("Length of Data Next Month Addition is equals to Zero!!!")
                else:
                    print("Length of Data No Insurance is equals to Zero!!!")


                """ Policy Type """

                # data_policy_type = classification.policy_type(data_frame=classification_1_data)
                # classification_3_data = data_policy_type
                # if len(data_policy_type) > 0:
                #     data_policy_type_write = get_write_file(data_frame=classification_3_data, file_name='data_final.xlsx', folder_location=excel_write_folder_location)
                #     if data_policy_type_write:
                #         print("Data Policy Type Written Successfully!!!")
                #     else:
                #         print("Error in Writing Policy Type!!!")
                # else:
                #     print("Length of Data Policy Type is equals to Zero!!!")
            else:
                print("Length of Inception Data is equals to Zero!!!")
        else:
            print("Length of Data is equals to Zero!!!")
    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Function!!!", exc_info = True)


def medical_insurance_test_2():
    try:
        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022"

        # file_properties_data = get_file_properties_data()

        # Pre Required Files
        # get_required_added_data(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)

        """ Classifications """

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/associate_merged_sr_mis_exit_death_data_date_validated.xlsx")
        inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/united_insurance.xlsx")

        # Updating Status Column in Inception Data

        inception_data["Status"] = inception_data.apply(
            lambda x : 'Active' if x['Classification'] in ["Deletion", "Migration Deletion", "Deletion"] else 'Inactive', axis = 1
        )

        print("data")
        print(data)

        print("inception_data")
        print(inception_data)

        if len(data) > 0:
            if len(inception_data) > 0:

                upload_month = 8
                upload_year = 2022
                data_next_month_deletion = ''

                # Creating one column for a Classification
                data["classification_1"] = ''
                data["classification_2"] = ''
                data["classification_3"] = ''

                classification = Classification()

                # Updating Classifications

                data_no_insurance = classification.no_insurance(data_frame=data)
                if len(data_no_insurance) > 0:
                    data_prior_to_policy = classification.prior_to_policy(data_frame=data_no_insurance, inception_data_frame=inception_data)
                    if len(data_prior_to_policy) > 0:
                        data_live = classification.live(data_frame=data_prior_to_policy, inception_data_frame=inception_data)
                        if len(data_live) > 0:
                            data_deletion = classification.deletion(data_frame=data_live, inception_data_frame=inception_data)
                            if len(data_deletion) > 0:
                                data_addition_and_deletion = classification.addition_and_deletion(data_frame=data_deletion)
                                if len(data_addition_and_deletion) > 0:
                                    data_already_deletion = classification.already_deletion(data_frame=data_addition_and_deletion, inception_data_frame=inception_data)
                                    if len(data_already_deletion) > 0:
                                        data_addition = classification.additions(data_frame=data_already_deletion, inception_data_frame=inception_data)
                                        if len(data_addition) > 0:
                                            data_reactivation = classification.reactivation(data_frame=data_addition, inception_data_frame=inception_data)
                                            if len(data_reactivation) > 0:
                                                data_migrations = classification.migration_addition(data_frame=data_reactivation, inception_data_frame=inception_data)
                                                if len(data_migrations) > 0:
                                                    data_next_month_addition = classification.next_month_addition(data_frame=data_migrations, upload_month=upload_month, upload_year=upload_year)
                                                    if len(data_next_month_addition) > 0:
                                                        data_alcs_deletion = classification.alcs_deletion(data_frame=data_next_month_addition, upload_month=upload_month, upload_year=upload_year)
                                                        if len(data_alcs_deletion) > 0:
                                                            data_next_month_alcs_deletion = classification.next_month_alcs_deletion(data_frame=data_alcs_deletion, upload_month=upload_month, upload_year=upload_year)
                                                            if len(data_next_month_alcs_deletion) > 0:
                                                                data_next_month_deletion = classification.next_month_deletion(data_frame=data_next_month_alcs_deletion, upload_month=upload_month, upload_year=upload_year)
                                                            else:
                                                                print("Length of Data Next Month Deletion is equals to Zero!!!")
                                                        else:
                                                            print("Length of Data ALCS Deletion is equals to Zero!!!")
                                                    else:
                                                        print("Length of Data Next Month Addition is equals to Zero!!!")
                                                else:
                                                    print("Length of Data Migrations is equals to Zero!!!")
                                            else:
                                                print("Length of Data Reactivation is equals to Zero!!!")
                                        else:
                                            print("Length of Data Addition is equals to Zero!!!")
                                    else:
                                        print("Length of Data Already Deletion is equals to Zero!!!")
                                else:
                                    print("Length of Data Addition and Deletion is equals to Zero!!!")
                            else:
                                print("Length of Data Deletion is equals to Zero!!!")
                        else:
                            print("Length of Data Live is equals to Zero!!!")
                    else:
                        print("Length of Data Prior to Policy is equals to Zero!!!")
                else:
                    print("Length of Data No Insurance is equals to Zero!!!")

                classification_1_data = data_next_month_deletion

                if len(classification_1_data) > 0:
                    # Updating Classification_2 (Death Cases)
                    classification_2_data = classification.death(data_frame=classification_1_data)
                    if len(classification_2_data) > 0:
                        # Updating Classification_2 (Policy)
                        classification_3_data = classification.policy_type(data_frame=classification_2_data)

                        if len(classification_3_data) > 0:
                            classification_3_data_write = get_write_file(data_frame=classification_3_data, file_name="data_classification_3.xlsx", folder_location=excel_write_folder_location)
                            if classification_3_data_write:
                                print("Classification 3 Written Successfully!!!")
                            else:
                                print("Error in Writing Classification 3!!!")
                        else:
                            print("Length of Classification 3 Data is equals to Zero!!")
                    else:
                        print("Length of Classification 2 Data is equals to Zero!!!")
                else:
                    print("Length of Classification 1 Data is equals to Zero!!!")

            else:
                print("Length of Inception Data is equals to Zero!!!")
        else:
            print("Length of Data is equals to Zero!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Function!!!", exc_info=True)


def medical_insurance_test_3():
    try:

        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/New"

        # file_properties_data = get_file_properties_data()

        # Pre Required Files
        # get_required_added_data(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)

        # Updating Policy Type in Data
        # data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/associate_merged_sr_mis_exit_death_data_date_validated.xlsx")
        #
        # data["policy_type_proper"] = data.apply(
        #     lambda x : 'Non Floater' if re.search(r'non', x['mis_policy_type'].lower()) else 'Floater', axis = 1
        # )
        #
        # get_write_file(data_frame=data, file_name="data_aug_2022.xlsx", folder_location=excel_write_folder_location)

        # inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/New/inception_united_aug_2022.xlsx")
        #
        # inception_data['policy_type_proper'] = inception_data.apply(
        #     lambda x : 'Non Floater' if re.search(r'non', x['Type'].lower()) else 'Floater', axis = 1
        # )
        #
        # get_write_file(data_frame=inception_data, file_name="inception_united_aug_2022_proper.xlsx", folder_location=excel_write_folder_location)

        """ Classifications """

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/New/data_aug_2022.xlsx")
        inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/New/inception_united_aug_2022_proper.xlsx")


        if len(data) > 0:
            if len(inception_data) > 0:

                upload_month = 8
                upload_year = 2022
                data_next_month_deletion = ''

                # Creating one column for a Classification
                data["classification_1"] = ''
                data["classification_2"] = ''
                data["classification_3"] = ''

                classification = Classification()

                # No Insurance
                data_no_insurance = classification.no_insurance(data_frame=data)
                if len(data_no_insurance) > 0:
                    # Prior to Policy
                    data_prior_to_policy = classification.prior_to_policy(data_frame=data_no_insurance, inception_data_frame=inception_data)
                    if len(data_prior_to_policy) > 0:
                        if get_write_file(data_frame=data_prior_to_policy, file_name="med_ins_aug_22_data_ptp.xlsx", folder_location=excel_write_folder_location):
                            print("Success")
                        else:
                            print("Length of Data Live is equals to Zero!!!")
                    else:
                        print("Length of Data Prior to Policy is equals to Zero!!!")
                else:
                    print("Length of Data No Insurance is equals to Zero!!!")
            else:
                print("Length of Inception Data is equals to Zero!!!")
        else:
            print("Length of Data is equals to Zero!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Function!!!", exc_info=True)

def medical_insurance_live():
    try:

        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022"

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/med_ins_aug_22_data_ptp.xlsx")
        inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/inception_united_aug_2022_proper.xlsx")

        classification = Classification()

        data_live = classification.live(data_frame=data, inception_data_frame=inception_data)

        if len(data_live) > 0:

            if get_write_file(data_frame=data_live, file_name="med_ins_aug_22_data_live.xlsx", folder_location=excel_write_folder_location):
                print("Live Written Successfully!!!")
            else:
                print("Error in Writing Live!!!")

        else:
            print("Length of Data Live is equals to Zero!!!")


    except Exception as e:
        print(e)
        logging.error("Error in Check Live Function!!!", exc_info=True)

def filter_ins_company():
    try:

        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022"
        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/med_ins_aug_22_data_live.xlsx")

        data_required = data[data['mis_ins_company'] == 'United India Insurance Company Limited']

        if get_write_file(data_frame=data_required, file_name="med_ins_aug_22_data_required.xlsx", folder_location=excel_write_folder_location):
            print("Success")
        else:
            print("Error")

    except Exception as e:
        print(e)
        logging.error("Error in Fileter Insurance Company Function!!!", exc_info=True)

def medical_insurance_deletion():
    try:

        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022"

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/med_ins_aug_22_data_required.xlsx")
        inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/inception_united_aug_2022_proper.xlsx")

        classification = Classification()

        data_deletion = classification.deletion(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_deletion, file_name="med_ins_aug_22_data_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Success")
        else:
            print("Error")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Deletion Function!!!", exc_info=True)

def medical_insurance():
    try:
        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022"

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/med_ins_aug_22_data_deletion.xlsx")
        inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/inception_united_aug_2022_proper.xlsx")

        classification = Classification()

        data_addition_and_deletion = classification.addition_and_deletion(data_frame=data, inception_data_frame=inception_data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_addition_and_deletion, file_name="med_ins_aug_22_data_addition_and_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Success")
        else:
            print("Error")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Addition and Deletion Function!!!", exc_info=True)

def medical_insurance_reactivation():
    try:
        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022"

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/med_ins_aug_22_data_addition_and_deletion.xlsx")
        inception_data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/inception_united_aug_2022_proper.xlsx")

        classification = Classification()

        data_reactivation = classification.reactivation(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_reactivation, file_name="med_ins_aug_22_data_reactivation.xlsx", folder_location=excel_write_folder_location):
            print("Success")
        else:
            print("Error")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Reactivation Function!!!", exc_info=True)

def medical_insurance_next_month_addition():
    try:

        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022"
        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/med_ins_aug_22_data_reactivation.xlsx")

        classification = Classification()

        data_next_month_addition = classification.next_month_addition(data_frame=data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_next_month_addition, file_name="med_ins_aug_22_data_next_month_addition.xlsx", folder_location=excel_write_folder_location):
            print("Success")
        else:
            print("Error")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Next Month Addition Function!!!", exc_info=True)

def medical_insurance_next_month_deletion():
    try:
        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022"
        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/03102022/med_ins_aug_22_data_next_month_addition.xlsx")

        classification = Classification()

        data_next_month_deletion = classification.next_month_deletion(data_frame=data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_next_month_deletion, file_name="med_ins_aug_22_data_next_month_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Success")
        else:
            print("Error")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Next Month Deletion Function!!!", exc_info=True)