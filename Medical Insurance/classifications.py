import pandas as pd
import re
import logging
from func import *

class Classification:

    def __init__(self):
        pass

    def no_insurance(self, data_frame):
        try:
            data_frame['classification_1'] = data_frame.apply(
                lambda x: 'No Insurance' if re.search(r'noinsurance', str(x['mis_ins_company']).replace(" ", "").lower()) and x['classification_1'] == '' else x['classification_1'], axis=1
            )
            return data_frame

        except Exception as e:
            print(e)
            logging.error("Error in Get No Insurance Function!!!", exc_info=True)
            return ''

    def prior_to_policy(self, data_frame, inception_data_frame):
        try:

            def get_check_prior_to_policy(data_dict):
                try:
                    # print("data_dict", data_dict)
                    if data_dict["ass_actual_dol_validate_Yes_or_No"].lower() == "yes":
                        if (data_dict["ass_active_status"].lower() == 'inactive') and \
                                (get_date_difference(data_dict["ass_actual_dol"],
                                                     data_dict["mis_pol_start_date"]) < 0) and \
                                (data_dict["ass_emp_no"] not in inception_data_employee_list):
                            return 'Prior To Policy'
                        return data_dict['classification_1']
                    return data_dict['classification_1']

                except Exception as e:
                    print(e)
                    logging.error("Error in Get Check Prior To Policy Function in Prior to Policy Function!!!", exc_info=True)

            inception_data_employee_list = inception_data_frame["Emp Code"].tolist()

            # data_frame_united_ins_company = data_frame[(data_frame['mis_ins_company'] == 'United India Insurance Company Limited') & (data_frame['ass_actual_dol_validate_Yes_or_No'] == 'Yes')]
            # data_frame_not_united_ins_company = data_frame[(data_frame['mis_ins_company'] != 'United India Insurance Company Limited') & (data_frame['ass_actual_dol_validate_Yes_or_No'] != 'Yes')]
            #
            # data_frame_united_ins_company['classification_1'] = data_frame_united_ins_company.apply(
            #     lambda x : 'Prior To Policy' if ( x['ass_active_status'].lower() == 'inactive' ) and
            #                                     ( get_date_difference(x['ass_actual_dol'], x['mis_pol_start_date']) <= 0 ) and
            #                                     ( x['ass_emp_no'] not in inception_data_employee_list )
            #     else x['classification_1'], axis = 1
            # )
            #
            # frames = [data_frame_united_ins_company, data_frame_not_united_ins_company]
            #
            # result = pd.concat(frames).sort_index()
            #
            # return result

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_check_prior_to_policy(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame

        except Exception as e:
            print(e)
            logging.error("Error in Prior to Policy Function!!!", exc_info=True)
            return ''

    def live(self, data_frame, inception_data_frame):
        try:
            def get_live(data_dict):
                try:
                    if data_dict["ass_active_status"].lower() in ["active"]:
                        if data_dict['ass_emp_no'] in inception_data_emp_list:
                            if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["gmc"] == data_dict["mis_gmc"]:
                                if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["gpa"] == data_dict["mis_gpa"]:
                                    if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["policy_type"].lower() == data_dict["policy_type_proper"].lower():
                                        return 'Live'
                                    else:
                                        return data_dict['classification_1']
                                else:
                                    return data_dict['classification_1']
                            else:
                                return data_dict['classification_1']
                        else:
                            return data_dict['classification_1']
                    else:
                        return data_dict['classification_1']

                except Exception as e:
                    print(e)
                    logging.error("Error in Get Live Function in Live Function!!!", exc_info=True)
                    return ''

            inception_data_emp_list = []
            inception_data_emp_status_list = []

            for index, rows in inception_data_frame.iterrows():
                if rows['Classification'] not in ['Migration Deletion'] and rows["Status"].lower() == 'active':
                    data_dict = {
                        "emp_no": rows['Emp Code'].lower().replace("m", ""),
                        'classification': rows['Classification'],
                        'client_id': rows["Client ID"],
                        "policy_type": rows["policy_type_proper"],
                        "gmc": rows["GMC"],
                        "gpa": rows["GPA"],
                        "status": rows["Status"]
                    }
                    inception_data_emp_status_list.append(data_dict)
                    inception_data_emp_list.append(rows['Emp Code'].lower().replace("m", ""))

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_live(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Live Function!!!", exc_info=True)
            return ''

    def deletion(self, data_frame, inception_data_frame, upload_month, upload_year):
        try:

            def get_check_deletion(data_dict):
                try:
                    if (data_dict["ass_active_status"].lower() in ['inactive', 'no insurance']) and (data_dict["ass_actual_dol_validate_Yes_or_No"].lower() == "yes"):
                        if data_dict['ass_emp_no'] in inception_data_emp_list:
                            if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["status"].lower() in ["active"]:
                                if int(data_dict['ass_actual_dol'].split("-")[1]) <= int(upload_month) and int(data_dict['ass_actual_dol'].split("-")[0]) <= int(upload_year):
                                    return 'Deletion'
                                else:
                                    return data_dict['classification_1']
                            else:
                                return data_dict['classification_1']
                        else:
                            return data_dict['classification_1']
                    else:
                        return data_dict['classification_1']
                except Exception as e:
                    print(e)
                    logging.error("Error in Get Check Deletion Function in Deletion Function!!!", exc_info=True)
                    return ''

            inception_data_emp_list = []
            inception_data_emp_status_list = []

            for index, rows in inception_data_frame.iterrows():
                data_dict = {"emp_no": rows['Emp Code'], 'status': rows['Status']}
                inception_data_emp_status_list.append(data_dict)
                inception_data_emp_list.append(rows['Emp Code'])

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_check_deletion(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Deletion Function!!!", exc_info=True)
            return ''

    def addition_and_deletion(self, data_frame, inception_data_frame):
        try:
            def get_addition_and_deletion(data_dict):
                try:
                    if data_dict["ass_emp_no"] not in inception_data_emp_list:
                        if data_dict["ass_actual_dol_validate_Yes_or_No"].lower() == "yes":
                            if data_dict["ass_active_status"].lower() in ["inactive"]:

                                actual_dol_month = int(data_dict["ass_actual_dol"].split("-")[1])
                                actual_dol_year = int(data_dict["ass_actual_dol"].split("-")[0])

                                policy_start_date_month = int(data_dict["mis_pol_start_date"].split("-")[1])
                                policy_start_date_year = int(data_dict["mis_pol_start_date"].split("-")[0])

                                if ( actual_dol_month >= policy_start_date_month and  actual_dol_year >= policy_start_date_year):
                                    if ( data_dict['ass_actual_dol'] >= data_dict["mis_pol_start_date"] ) and \
                                            not ( data_dict["ass_actual_dol"] > data_dict["mis_pol_end_date"] ) :
                                        return 'Addition and Deletion'
                                    else:
                                        return data_dict['classification_1']
                                else:
                                    return data_dict['classification_1']
                            else:
                                return data_dict['classification_1']
                        else:
                            return data_dict['classification_1']
                    else:
                        return data_dict['classification_1']

                except Exception as e:
                    print(e)
                    logging.error("Error in Get Addition and Deletion Function of Addition and Deletion Function!!!", exc_info=True)
                    return ''

            inception_data_emp_list = []

            for index, rows in inception_data_frame.iterrows():
                inception_data_emp_list.append(rows['Emp Code'])

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_addition_and_deletion(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Addition and Deletion Function!!!", exc_info=True)
            return ''

    def already_deletion(self, data_frame, inception_data_frame):
        try:

            def get_already_deletion(data_dict):
                try:
                    if data_dict['classification_1'] in ['Deletion', 'Addition and Deletion', '']:
                        if data_dict['ass_emp_no'] in inception_data_emp_list:
                            if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["classification"] in ["Deletion", "Addition and Deletion", "Already Deletion"]:
                                if data_dict['ass_actual_dol_validate_Yes_or_No'].lower() == 'yes':
                                    return 'Already Deletion'
                                else:
                                    return data_dict['classification_1']
                            else:
                                return data_dict['classification_1']
                        else:
                            return data_dict['classification_1']
                    else:
                        return data_dict['classification_1']

                except Exception as e:
                    print(e)
                    logging.error("Error in Get Already Deletion Function of Already Deletion!!!", exc_info=True)
                    return ''

            inception_data_emp_list = []
            inception_data_emp_status_list = []

            for index, rows in inception_data_frame.iterrows():
                data_dict = {"emp_no": rows['Emp Code'], 'classification': rows['Classification']}
                inception_data_emp_status_list.append(data_dict)
                inception_data_emp_list.append(rows['Emp Code'])

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_already_deletion(x) if x['mis_ins_company'].lower() == "united india insurance company limited" else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Already Deletion Function!!!", exc_info=True)
            return ''

    def additions(self, data_frame, inception_data_frame):
        try:

            def get_addition(data_dict):
                try:
                    if data_dict["ass_active_status"].lower() in ["active"] and data_dict["ass_actual_dol_validate_Yes_or_No"] == 'No':
                        if data_dict["ass_emp_no"] not in inception_data_employee_list:
                            return 'Addition'
                        else:
                            return data_dict["classification_1"]
                    return data_dict["classification_1"]
                except Exception as e:
                    print(e)
                    logging.error("Error in Get Addition Function of Addition Function!!!", exc_info=True)
                    return ''

            inception_data_employee_list = inception_data_frame["Emp Code"].tolist()

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_addition(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Addition Function!!!", exc_info=True)
            return ''

    def reactivation(self, data_frame, inception_data_frame):
        try:

            def get_check_reactivation(data_dict):
                try:
                    if data_dict["ass_active_status"].lower() in ["active"] and data_dict["ass_actual_dol_validate_Yes_or_No"] == "No":
                        if data_dict["ass_emp_no"] in inception_data_emp_list:
                            if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["status"].lower() in ["inactive"]:
                                return 'Reactivation'
                            else:
                                return data_dict["classification_1"]
                        else:
                            return data_dict["classification_1"]
                    else:
                        return data_dict["classification_1"]

                except Exception as e:
                    print(e)
                    logging.error("Error in Reactivation Function!!!", exc_info=True)
                    return ''

            inception_data_emp_list = []
            inception_data_emp_status_list = []

            for index, rows in inception_data_frame.iterrows():
                data_dict = {"emp_no": rows['Emp Code'], 'status': rows['Status']}
                inception_data_emp_status_list.append(data_dict)
                inception_data_emp_list.append(rows['Emp Code'])

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_check_reactivation(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Reactivation Function!!!", exc_info=True)
            return ''

    def next_month_addition(self, data_frame, upload_month, upload_year):
        try:

            def get_check_next_month_addition(data_dict):
                try:
                    if data_dict['ass_doj_validate_Yes_or_No'].lower() == "yes":
                        if int(data_dict['ass_doj'].split("-")[1]) > int(upload_month) and int(data_dict['ass_doj'].split("-")[0]) >= int(upload_year):
                            return 'Next Month Addition'
                        else:
                            return data_dict["classification_1"]
                    else:
                        return data_dict["classification_1"]

                except Exception as e:
                    print(e)
                    logging.error("Error in Get Check Next Month Addition Function in Next Month Addition Function!!!", exc_info=True)
                    return ''


            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_check_next_month_addition(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Next Month Addition Function!!!", exc_info=True)
            return ''

    def next_month_deletion(self, data_frame, inception_data_frame, upload_month, upload_year):
        try:

            def get_check_next_month_deletion(data_dict):
                try:
                    if data_dict["ass_active_status"].lower() in ["inactive", "no insurance"] and data_dict["ass_actual_dol_validate_Yes_or_No"].lower() == "yes":
                        if data_dict['ass_emp_no'] in inception_data_emp_list:
                            if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["status"].lower() in ["active"]:
                                if int(data_dict['ass_actual_dol'].split("-")[1]) > int(upload_month) and int(data_dict['ass_actual_dol'].split("-")[0]) >= upload_year:
                                    return 'Next Month Deletion'
                                else:
                                    return data_dict['classification_1']
                            else:
                                return data_dict['classification_1']
                        else:
                            return data_dict['classification_1']
                    else:
                        return data_dict['classification_1']
                except Exception as e:
                    print(e)
                    logging.error("Error in Get Check Next Month Deletion Function in Next Month Deletion Function!!!", exc_info=True)
                    return ''

            inception_data_emp_list = []
            inception_data_emp_status_list = []

            for index, rows in inception_data_frame.iterrows():
                data_dict = {"emp_no": rows['Emp Code'], 'status': rows['Status']}
                inception_data_emp_status_list.append(data_dict)
                inception_data_emp_list.append(rows['Emp Code'])

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_check_next_month_deletion(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Next Month Deletion Function!!!", exc_info=True)
            return ''

    def alcs_deletion(self, data_frame, upload_month, upload_year):
        try:

            def get_check_alcs_deletion(data_dict):
                try:
                    if data_dict['ass_active_status'].lower() in ['inactive']:
                        if data_dict['exit_actual_dol_validate_Yes_or_No'].lower() == "yes":
                            if int(data_dict['exit_actual_dol'].split("-")[1]) <= int(upload_month):
                                if int(data_dict['exit_actual_dol'].split("-")[0]) <= int(upload_year):
                                    return 'ALCS Deletion'
                                else:
                                    return data_dict['classification_1']
                            else:
                                return data_dict['classification_1']
                        else:
                            return data_dict['classification_1']
                    else:
                        return data_dict['classification_1']

                except Exception as e:
                    print(e)
                    logging.error("Error in Get Check ALCS Deletion Function in ALCS Deletion Function!!!", exc_info=True)
                    return ''

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_check_alcs_deletion(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in ALCS Deletion Function!!!", exc_info=True)
            return ''

    def next_month_alcs_deletion(self, data_frame, upload_month, upload_year):
        try:

            def get_check_next_month_alcs_deletion(data_dict):
                try:
                    if data_dict['ass_active_status'].lower() in ['inactive']:
                        if data_dict['exit_actual_dol_validate_Yes_or_No'].lower() == "yes":
                            if int(data_dict['exit_actual_dol'].split("-")[1]) > int(upload_month):
                                if int(data_dict['exit_actual_dol'].split("-")[0]) <= int(upload_year):
                                    return 'Next Month ALCS Deletion'
                                else:
                                    return data_dict['classification_1']
                            else:
                                return data_dict['classification_1']
                        else:
                            return data_dict['classification_1']
                    else:
                        return data_dict['classification_1']
                except Exception as e:
                    print(e)
                    logging.error("Error in Get Check Next Month ALCS Deletion Function in Next Month ALCS Deletion Function!!!", exc_info=True)

            data_frame['classification_1'] = data_frame.apply(
                lambda x: get_check_next_month_alcs_deletion(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis=1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Next Month ALCS Deletion!!!", exc_info=True)
            return ''

    def migration_addition(self, data_frame, inception_data_frame):
        try:

            def get_migration_addition(data_dict):
                try:
                    if data_dict["ass_active_status"].lower() in ["active"]:
                        if data_dict['ass_emp_no'] in inception_data_emp_list:
                            if inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["gmc"] != data_dict["mis_gmc"] or \
                                    inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["gpa"] != data_dict["mis_gpa"] or \
                                    inception_data_emp_status_list[inception_data_emp_list.index(data_dict['ass_emp_no'])]["policy_type"].lower() != data_dict["policy_type_proper"].lower():
                                return 'Migration Addition'
                            return data_dict['classification_1']
                        return data_dict['classification_1']
                    return data_dict['classification_1']
                except Exception as e:
                    print(e)
                    logging.error("Error in Get Migration Addition in Migration Addition Function!!!")
                    return ''

            inception_data_emp_list = []
            inception_data_emp_status_list = []

            for index, rows in inception_data_frame.iterrows():
                data_dict = {
                    "emp_no": rows['Emp Code'],
                    'classification': rows['Classification'],
                    'client_id': rows["Client ID"],
                    "policy_type": rows["policy_type_proper"],
                    "gmc": rows["GMC"],
                    "gpa": rows["GPA"]
                }
                inception_data_emp_status_list.append(data_dict)
                inception_data_emp_list.append(rows['Emp Code'])

            data_frame['classification_1'] = data_frame.apply(
                lambda x : get_migration_addition(x) if x['mis_ins_company'].lower() == "united india insurance company limited" and x['classification_1'] == '' else x['classification_1'], axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Migrations Function!!!", exc_info=True)
            return ''

    def death(self, data_frame):
        try:
            data_frame['classification_2'] = data_frame.apply(
                lambda x : 'Death' if len(x['death_emp_code']) > 2 else '', axis = 1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Death Function!!!", exc_info=True)
            return ''

    def policy_type(self, data_frame):
        try:

            data_frame['classification_3'] = data_frame.apply(
                lambda x : 'EC/WC' if ( str(x['ass_ol_emp_comp']).replace(" ", "").replace("NA", "").replace("0", "") != '' or str(x['ass_sr_emp_comp']).replace(" ", "").replace("NA", "").replace("0", "") != '') and x['classification_3'] == '' else x['classification_3'], axis = 1
            )

            data_frame['classification_3'] = data_frame.apply(
                lambda x : 'ESIC' if ( str(x['ass_ol_esic']).replace(" ", "").replace("NA", "").replace("0", "") != '' or str(x['ass_sr_esic']).replace(" ", "").replace("NA", "").replace("0", "") != '' ) and x['classification_3'] == '' else x['classification_3'], axis = 1
            )

            data_frame['classification_3'] = data_frame.apply(
                lambda x : x['classification_3'] if x['classification_3'] in ['EC/WC', 'ESIC'] else 'NO EC AND ESIC', axis=1
            )

            return data_frame
        except Exception as e:
            print(e)
            logging.error("Error in Policy Type Function!!!", exc_info=True)
            return ''

    # def policy_type_1(self, data_frame):
    #     try:
    #
    #         data_frame['classification_3'] = data_frame.apply(
    #             lambda x : 'EC/WC' if ( str(x['ass_ol_emp_comp']).replace(" ", "").replace("NA", "").replace("0", "") != '' or str(x['ass_sr_emp_comp']).replace(" ", "").replace("NA", "").replace("0", "") != '') and x['classification_3'] == '' else x['classification_3'], axis = 1
    #         )
    #
    #         # Filter Updated Data and Non Updated Data EC/WC
    #         data_frame_ec_updated = data_frame[data_frame['classification_3'] == 'EC/WC']
    #         data_frame_ec_not_updated = data_frame[data_frame['classification_3'] != 'EC/WC']
    #
    #         # Update ESIC on not updated data only EC/WC
    #         data_frame_ec_not_updated['classification_3'] = data_frame_ec_not_updated.apply(
    #             lambda x : 'ESIC' if ( str(x['ass_ol_esic']).replace(" ", "").replace("NA", "").replace("0", "") != '' or str(x['ass_sr_esic']).replace(" ", "").replace("NA", "").replace("0", "") != '' ) and x['classification_3'] == '' else x['classification_3'], axis = 1
    #         )
    #
    #         # Filter Updated Data and Non Updated Data ESIC
    #         data_frame_esic_updated = data_frame_ec_not_updated[data_frame_ec_not_updated['classification_3'] == 'ESIC']
    #         data_frame_esic_not_updated = data_frame_ec_not_updated[data_frame_ec_not_updated['classification_3'] != 'ESIC']
    #
    #         # Update No ESIC on not updated data only ESIC
    #         data_frame_esic_not_updated['classification_3'] = data_frame_esic_not_updated['classification_3'].apply(
    #             lambda x : x if x in ['ESIC', 'EC/WC'] else 'NO EC AND ESIC'
    #         )
    #
    #         overall_data_frames = [data_frame_ec_updated, data_frame_esic_updated, data_frame_esic_not_updated]
    #
    #         merged_data_frame = pd.concat(overall_data_frames).sort_index()
    #
    #         return merged_data_frame
    #     except Exception as e:
    #         print(e)
    #         logging.error("Error in Get Policy Type EC/WC Function!!!", exc_info=True)
    #         return ''

    # def next_month_alcs_deletion_1(self, data_frame, upload_month, upload_year):
    #     try:
    #         exit_actual_dol_validated_yes = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'Yes']
    #         exit_actual_dol_validated_no = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'No']
    #
    #         exit_actual_dol_validated_yes['classification_1'] = exit_actual_dol_validated_yes.apply(
    #             lambda x: 'Next Month ALCS Deletion' if int(str(x['exit_actual_dol'].split("-")[1])) > int(upload_month) and int(str(x['exit_actual_dol']).split("-")[0]) >= int(upload_year) else x['classification_1'], axis=1
    #         )
    #
    #         frames = [exit_actual_dol_validated_yes, exit_actual_dol_validated_no]
    #         result = pd.concat(frames).sort_index()
    #
    #         return result
    #     except Exception as e:
    #         print(e)
    #         logging.error("Error in Get ALCS Deletion Function!!!", exc_info=True)
    #         return ''

    # def alcs_deletion_1(self, data_frame, upload_month, upload_year):
    #     try:
    #         exit_actual_dol_validated_yes = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'Yes']
    #         exit_actual_dol_validated_no = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'No']
    #
    #         exit_actual_dol_validated_yes['classification_1'] = exit_actual_dol_validated_yes.apply(
    #             lambda x : 'ALCS Deletion' if int(str(x['exit_actual_dol'].split("-")[1])) <= int(upload_month) and int(str(x['exit_actual_dol']).split("-")[0]) <= int(upload_year) else x['classification_1'], axis = 1
    #         )
    #
    #         frames = [exit_actual_dol_validated_yes, exit_actual_dol_validated_no]
    #         result = pd.concat(frames).sort_index()
    #
    #         return result
    #     except Exception as e:
    #         print(e)
    #         logging.error("Error in Get ALCS Deletion Function!!!", exc_info=True)
    #         return ''

    # def next_month_deletion_1(self, data_frame, upload_month, upload_year):
    #     try:
    #
    #         actual_dol_validated_yes = data_frame[data_frame['ass_actual_dol_validate_Yes_or_No'] == 'Yes']
    #         actual_dol_validated_no = data_frame[data_frame['ass_actual_dol_validate_Yes_or_No'] == 'No']
    #
    #         actual_dol_validated_yes['classification_1'] = actual_dol_validated_yes.apply(
    #             lambda x : 'Next Month Deletion' if int(str(x['ass_dol']).split("-")[1]) >= int(upload_month) and int(str(x['ass_dol']).split("-")[0]) >= int(upload_year) else x['classification_1'], axis = 1
    #         )
    #
    #         frames = [actual_dol_validated_yes, actual_dol_validated_no]
    #         result = pd.concat(frames).sort_index()
    #
    #         return result
    #     except Exception as e:
    #         print(e)
    #         logging.error("Error in Next Month Deletion Function!!!", exc_info=True)

    # def next_month_addition_1(self, data_frame, upload_month, upload_year):
    #     try:
    #         doj_validated_yes = data_frame[data_frame['ass_doj_validate_Yes_or_No'] == 'Yes']
    #         doj_validated_no = data_frame[data_frame['ass_doj_validate_Yes_or_No'] == 'No']
    #
    #         doj_validated_yes['classification_1'] = doj_validated_yes.apply(
    #             lambda x : 'Next Month Addition' if int(str(x['ass_doj'].split("-")[1])) >= int(upload_month) and int(str(x['ass_doj']).split("-")[0]) >= int(upload_year) else x['classification_1'], axis = 1
    #         )
    #
    #         frames = [doj_validated_yes, doj_validated_no]
    #         result = pd.concat(frames).sort_index()
    #
    #         return result
    #     except Exception as e:
    #         print(e)
    #         logging.error("Error in Get Next Month Addition Function!!!", exc_info=True)
    #         return ''