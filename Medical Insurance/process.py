from func import *
import pandas as pd
import logging
from classifications import *

def get_required_added_data(file_properties_data, excel_write_folder_location):
    try:
        """ Reading Associate Data: """
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
        #
        # """ Reading Salary Register """
        # salary_register_data_properties = file_properties_data["salary_register"][0]
        #
        # salary_register = get_data(
        #     file_path = salary_register_data_properties["file_path"],
        #     sheet_name = salary_register_data_properties["sheet_name"],
        #     source_extension = salary_register_data_properties["source_extension"],
        #     attribute_list = salary_register_data_properties["source_columns"],
        #     column_start_row = salary_register_data_properties["column_start_row"],
        #     attribute_data_types_list = salary_register_data_properties["attribute_data_types_list"],
        #     unique_list = salary_register_data_properties["unique_list"]
        # )
        #
        # # Rename the columns to compare with Associate Data """
        # salary_register_columns_dict = salary_register_data_properties["rename_columns"]
        # salary_register.rename(columns = salary_register_columns_dict, inplace=True)
        #
        # print("salary_register")
        # print(salary_register)
        #
        # # Adding new columns to the salary register to match with the Associate Data """
        # salary_register_data = create_new_column(data_frame=salary_register, data_frame_series_tuple=(salary_register["OL CTC"], salary_register["OL_ESIC"]), new_column_name_tuple=('SR CTC', 'SR_ESIC'))
        #
        # """ Reading MIS Data """
        # mis_data_properties = file_properties_data["mis"][0]
        #
        # mis = get_data(
        #     file_path = mis_data_properties["file_path"],
        #     sheet_name = mis_data_properties["sheet_name"],
        #     source_extension = mis_data_properties["source_extension"],
        #     attribute_list = mis_data_properties["source_columns"],
        #     column_start_row = mis_data_properties["column_start_row"],
        #     attribute_data_types_list = mis_data_properties["attribute_data_types_list"],
        #     unique_list = mis_data_properties["unique_list"]
        # )
        #
        # print("mis")
        # print(mis)

        """ Reading Exit Report """
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

        """ Adding Records in Associate Data by Comparing with Salary Data """

        # if associate_data is not None:
        #     if salary_register_data is not None:
        #         if mis is not None:
        #             if exit_report is not None:
        #                 if death_tracker is not None:
        #                     salary_register_write = get_write_file(data_frame=salary_register_data, file_name="salary_register_added.xlsx", folder_location=excel_write_folder_location)
        #                     if salary_register_write:
        #                         print("Salary Register File Written Successfully!!!")
        #                     else:
        #                         print("Error in Writing Salary Register File!!!")
        #
        #                     """ Adding Records from salary Register """
        #                     # associate_added_sr = pd.merge(associate_data, salary_register_data, left_on = ['Employee No'], right_on = ['Employee No'], how = 'left', suffixes=('', '_y'))
        #
        #                     associate_added_sr = pd.merge(salary_register_data, associate_data, left_on = ['Employee No'], right_on = ['Employee No'], how = 'left', suffixes=('', '_y'))
        #                     associate_added_sr.drop(associate_added_sr.filter(regex='_y$').columns, axis=1, inplace=True)
        #
        #                     print("associate_added_sr")
        #                     print(associate_added_sr)
        #
        #                     if len(associate_added_sr) > 0:
        #                         associate_added_sr_write = get_write_file(data_frame=associate_added_sr, file_name="associate_added_salary_register.xlsx", folder_location=excel_write_folder_location)
        #                         if associate_added_sr_write:
        #                             print("Associated added SR Written Successfully!!!")
        #                         else:
        #                             print("Error in Writing Associate added SR!!!")
        #
        #                         if len(mis) > 0:
        #                             mis_write = get_write_file(data_frame=mis, file_name="mis_data.xlsx", folder_location=excel_write_folder_location)
        #                             if mis_write:
        #                                print("Mis Data Written Successfully!!!")
        #                             else:
        #                                 print("Error in Writing Mis Data!!!")
        #
        #                             if len(exit_report) > 0:
        #                                 exit_report_write = get_write_file(data_frame = exit_report, file_name = "exit_report.xlsx", folder_location=excel_write_folder_location)
        #                                 if exit_report_write:
        #                                    print("Exit Report Written Successfully!!!")
        #                                 else:
        #                                    print("Error in Writing Exit Report!!!")
        #
        #                                 if len(death_tracker) > 0:
        #                                     death_tracker_write = get_write_file(data_frame=death_tracker, file_name = "death_tracker.xlsx", folder_location=excel_write_folder_location)
        #                                     if death_tracker_write:
        #                                         print("Death Tracker Written Successfully!!!")
        #                                     else:
        #                                         print("Error in Writing Death Tracker!!!")
        #
        #                                 else:
        #                                     print("Length of Death Tracker is equals to Zero!!!")
        #                             else:
        #                                 print("Length of Exit Report is equals to Zero!!!")
        #                         else:
        #                             print("Length of MIS is equals to Zero!!!")
        #                     else:
        #                         print("Length of Associate Added SR is equals to Zero!!!")
        #                 else:
        #                     print("Death Tracker is None!!!")
        #             else:
        #                 print("Exit Report is None!!!")
        #         else:
        #             print("MIS Data is None!!!")
        #     else:
        #         print("Salary Register is None!!!")
        # else:
        #    print("Associate Data is None!!!")


        """ Increasing Records in Associate Data by comparing with MIS Data """
        #
        # # Read from Written Files (associate_data and mis_data):
        # associate_added_sr_data = get_read_proper_data('G:/AdventsProduct/Others/A-Testing/Medical Insurance/associate_added_salary_register.xlsx')
        # mis_data = get_read_proper_data("G:/AdventsProduct/Others/A-Testing/Medical Insurance/mis_data.xlsx")
        #
        # print("associate_added_sr_data")
        # print(associate_added_sr_data)
        #
        # print("mis_data")
        # print(mis_data)
        #
        # if len(associate_added_sr_data) > 0 and len(mis_data) > 0:
        #      associated_sr_mis_data = pd.merge(associate_added_sr_data, mis_data, left_on=['Client Id'], right_on=['ClientID'], how='left', suffixes=('', '_y'))
        #      associated_sr_mis_data.drop(associated_sr_mis_data.filter(regex='_y$').columns, axis=1, inplace=True)
        #
        #      # associate_sr_mis_properties = file_properties_data["associate_sr_mis"][0]
        #      # associated_sr_mis_data.columns = associate_sr_mis_properties["columns"]
        #
        #      if len(associated_sr_mis_data) > 0:
        #          # associated_sr_mis_data_write = get_write_file(data_frame=associated_sr_mis_data, file_name="associated_sr_mis_data.xlsx", folder_location=excel_write_folder_location)
        #          # if associated_sr_mis_data_write:
        #          #     print("Associated SR MIS Data Written Successfully!!!")
        #          # else:
        #          #     print("Error in Writing Associated SR MIS Data!!!")
        #
        #          """ Comparing associate_added_sr_data with Exit Report Records """
        #
        #          associated_sr_mis_exit_data = pd.merge(associated_sr_mis_data, exit_report, left_on=['Employee No'], right_on=['Employee No'], how='left', suffixes=('', '_y'))
        #          # associated_sr_mis_exit_data.drop(associated_sr_mis_exit_data.filter(regex='_y$').columns, axis=1, inplace=True)
        #
        #          if len(associated_sr_mis_exit_data) > 0:
        #              associated_sr_mis_exit_data_write = get_write_file(data_frame=associated_sr_mis_exit_data, file_name="associated_sr_mis_exit_data.xlsx", folder_location=excel_write_folder_location)
        #              if associated_sr_mis_exit_data_write:
        #                  print("Associate SR MIS Exit Written Successfully!!!")
        #              else:
        #                  print("Error in Writing Associate SR MIS Exit !!!")
        #
        #              associated_sr_mis_exit_death_data = pd.merge(associated_sr_mis_exit_data, death_tracker, left_on=['Employee No'], right_on=['Emp Code'], how='left', suffixes=('', '_y'))
        #              # associated_sr_mis_exit_death_data.drop(associated_sr_mis_exit_death_data.filter(regex='_y$').columns, axis=1, inplace=True)
        #
        #              if len(associated_sr_mis_exit_death_data) > 0:
        #                  associated_sr_mis_exit_death_data_write = get_write_file(data_frame=associated_sr_mis_exit_death_data, file_name="associated_sr_mis_exit_death_data.xlsx", folder_location=excel_write_folder_location)
        #                  if associated_sr_mis_exit_death_data_write:
        #                      print("Associate SR MIS Exit Death Written Successfully!!!")
        #                  else:
        #                      print("Error in Writing Associate SR MIS Exit Death!!!")
        #
        #      else:
        #          print("Length of Associated SR Mis Data is equals to Zero!!!")


        """ Validating Dates for Further Classifications """

        # Read from Written Files (associated_sr_mis_data)
        associate_merged_sr_mis_exit_death_data = get_read_proper_data('G:/AdventsProduct/Others/A-Testing/Medical Insurance/associated_sr_mis_exit_death_data.xlsx')
        print("associate_merged_sr_mis_exit_death_data")
        print(associate_merged_sr_mis_exit_death_data)

        associate_merged_sr_mis_exit_death_properties = file_properties_data["associate_merged_sr_mis_exit_death"][0]
        associate_merged_sr_mis_exit_death_data.columns = associate_merged_sr_mis_exit_death_properties["columns"]

        # Validating All Data Fields and Creating New Date Column with status Flag "Yes" or "No"
        associate_merged_sr_mis_exit_death_data_date_validated = add_column_with_date_val(data_frame=associate_merged_sr_mis_exit_death_data, validate_date_column_name_list=associate_merged_sr_mis_exit_death_properties["date_validation_columns"])
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

def medical_insurance():
    try:

        excel_write_folder_location = "G:/AdventsProduct/Others/A-Testing/Medical Insurance"

        # file_properties_data = get_file_properties_data()

        # Pre Required Files
        # get_required_added_data(file_properties_data = file_properties_data, excel_write_folder_location = excel_write_folder_location)

        """ Classifications """

        data = get_read_proper_data(file_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/associate_merged_sr_mis_exit_death_data_date_validated.xlsx")

        print("data")
        print(data)

        classification_1_data = ''
        classification_2_data = ''
        classification_3_data = ''

        if len(data) > 0:
            # Creating one column for a Classification
            data["classification_1"] = ''
            data["classification_2"] = ''
            data["classification_3"] = ''

            """  1) No Insurance """

            classification = Classification()

            data_no_insurance = classification.no_insurance(data_frame=data)

            if len(data_no_insurance) > 0:
                # data_no_insurance_write = get_write_file(data_frame=data_no_insurance, file_name="data.xlsx", folder_location=excel_write_folder_location)
                # if data_no_insurance_write:
                #     print("Data Classification No Insurance Written Successfully!!!")
                # else:
                #     print("Error in Writing Data Classification No Insurance!!!")

                """ 2) Next Month Addition """

                data_next_month_addition = classification.next_month_addition(data_frame=data_no_insurance, upload_month=7, upload_year=2022)

                if len(data_next_month_addition) > 0:
                    # data_next_month_addition_write = get_write_file(data_frame=data_next_month_addition, file_name='data1.xlsx', folder_location=excel_write_folder_location)
                    # if data_next_month_addition_write:
                    #     print("Data Classification Next Month Addition Written Successfully!!!")
                    # else:
                    #     print("Error in Writing Data Classification Next Month Addition!!!")

                    """ 3) ALCS Deletion """

                    data_alcs_deletion = classification.alcs_deletion(data_frame=data_next_month_addition, upload_month=7, upload_year=2022)

                    if len(data_alcs_deletion) > 0:
                        # data_alcs_deletion_write = get_write_file(data_frame=data_alcs_deletion, file_name="data2.xlsx", folder_location=excel_write_folder_location)
                        # if data_alcs_deletion_write:
                        #     print("Classification ALCS Deletion Written Successfully!!!")
                        # else:
                        #     print("Error in Writing ALCS Deletion")

                        """ 4) Next Month ALCS Deletion """

                        data_next_month_alcs_deletion = classification.next_month_alcs_deletion(data_frame=data_alcs_deletion, upload_month=7, upload_year=2022)

                        if len(data_next_month_alcs_deletion) > 0:
                            # data_next_month_alcs_deletion_write = get_write_file(data_frame=data_next_month_alcs_deletion, file_name="data3.xlsx", folder_location=excel_write_folder_location)
                            # if data_next_month_alcs_deletion_write:
                            #     print("Classification Next Month ALCS Deletion Written Successfully!!!")
                            # else:
                            #     print("Error in Writing Next Month ALCS Deletion!!!")
                            classification_1_data = data_next_month_alcs_deletion

                        else:
                            print("Length of Next Month ALCS Deletion is equals to Zero!!!")
                    else:
                        print("Length of Data ALCS Deletion is equals to Zero!!!")
                else:
                    print("Length of Data Next Month Addition is equals to Zero!!!")
            else:
                print("Length of Data No Insurance is equals to Zero!!!")


            """ Policy Type """

            data_policy_type = classification.policy_type(data_frame=classification_1_data)
            classification_3_data = data_policy_type
            if len(data_policy_type) > 0:
                data_policy_type_write = get_write_file(data_frame=classification_3_data, file_name='data_final.xlsx', folder_location=excel_write_folder_location)
                if data_policy_type_write:
                    print("Data Policy Type Written Successfully!!!")
                else:
                    print("Error in Writing Policy Type!!!")
            else:
                print("Length of Data Policy Type is equals to Zero!!!")

        else:
            print("Length of Data is equals to Zero!!!")
    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Function!!!", exc_info = True)