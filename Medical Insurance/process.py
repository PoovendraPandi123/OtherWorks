import re

from func import *
import pandas as pd
import logging
from classifications import *


def medical_insurance_no_insurance():
    try:

        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/data_aug_2022_proper.xlsx")

        classification = Classification()

        data_no_insurance = classification.no_insurance(data_frame=data)

        if get_write_file(data_frame=data_no_insurance, file_name="med_ins_aug_22_data_no_insurance.xlsx", folder_location=excel_write_folder_location):
            print("No Insurance Written Successfully!!!")
        else:
            print("Error in Writing No Insurance!!!")

    except Exception as e:
        print(e)
        logging.error("Error in No Insurance Function!!!", exc_info=True)

def medical_insurance_prior_to_policy():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_no_insurance.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_ptp = classification.prior_to_policy(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_ptp, file_name="med_ins_aug_22_data_ptp.xlsx", folder_location=excel_write_folder_location):
            print("Prior To Policy Written Successfully!!!")
        else:
            print("Error in Writing Prior to Policy!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Prior to Policy Function!!!", exc_info=True)

def medical_insurance_live():
    try:

        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_ptp.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

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

def medical_insurance_deletion():
    try:

        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_live.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_deletion = classification.deletion(data_frame=data, inception_data_frame=inception_data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_deletion, file_name="med_ins_aug_22_data_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Deletion Written Successfully!!!")
        else:
            print("Error in Writing Deletion!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Deletion Function!!!", exc_info=True)

def medical_insurance_addition_and_deletion():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_deletion.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_addition_and_deletion = classification.addition_and_deletion(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_addition_and_deletion, file_name="med_ins_aug_22_data_addition_and_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Addition and Deletion Written Successfully!!!")
        else:
            print("Error in Writing Addition and Deletion!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Addition and Deletion Function!!!", exc_info=True)

def medical_insurance_already_deletion():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_addition_and_deletion.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_already_deletion = classification.already_deletion(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_already_deletion, file_name="med_ins_aug_22_data_already_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Already Deletion Written Successfully!!!")
        else:
            print("Error in Writing Already Deletion!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Already Deletion Function!!!", exc_info=True)

def medical_insurance_addition():
    try:

        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_already_deletion.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_addition = classification.additions(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_addition, file_name="med_ins_aug_22_data_addition.xlsx", folder_location=excel_write_folder_location):
            print("Addition Written Successfully!!!")
        else:
            print("Error in Writing Addition!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Addition Function!!!", exc_info=True)

def medical_insurance_reactivation():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_addition.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_reactivation = classification.reactivation(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_reactivation, file_name="med_ins_aug_22_data_reactivation.xlsx", folder_location=excel_write_folder_location):
            print("Reactivation Written Successfully!!!")
        else:
            print("Error in Writing Reactivation!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Reactivation Function!!!", exc_info=True)

def medical_insurance_next_month_addition():
    try:

        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"
        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_reactivation.xlsx")

        classification = Classification()

        data_next_month_addition = classification.next_month_addition(data_frame=data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_next_month_addition, file_name="med_ins_aug_22_data_next_month_addition.xlsx", folder_location=excel_write_folder_location):
            print("Next Month Addition Written Successfully!!!")
        else:
            print("Error in Writing Next Month Addition!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Next Month Addition Function!!!", exc_info=True)

def medical_insurance_next_month_deletion():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"
        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_next_month_addition.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_next_month_deletion = classification.next_month_deletion(data_frame=data, inception_data_frame=inception_data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_next_month_deletion, file_name="med_ins_aug_22_data_next_month_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Next Month Deletion Written Successfully!!!")
        else:
            print("Error in Writing Next Month Deletion!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Next Month Deletion Function!!!", exc_info=True)

def medical_insurance_alcs_deletion():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_next_month_deletion.xlsx")

        classification = Classification()

        data_alcs_deletion = classification.alcs_deletion(data_frame=data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_alcs_deletion, file_name="med_ins_aug_22_data_alcs_deletion.xlsx", folder_location=excel_write_folder_location):
            print("ALCS Deletion Written Successfully!!!")
        else:
            print("Error in Writing ALCS Deletion!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance ALCS Deletion Function!!!", exc_info=True)

def medical_insurance_next_month_alcs_deletion():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_alcs_deletion.xlsx")

        classification = Classification()

        data_next_month_alcs_deletion = classification.next_month_alcs_deletion(data_frame=data, upload_month=8, upload_year=2022)

        if get_write_file(data_frame=data_next_month_alcs_deletion, file_name="med_ins_aug_22_data_next_month_alcs_deletion.xlsx", folder_location=excel_write_folder_location):
            print("Next Month ALCS Deletion Written Successfully!!!")
        else:
            print("Error in Writing Next Month ALCS Deletion!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Next Month ALCS Deletion Function!!!", exc_info=True)

def medical_insurance_migration_addition():
    try:

        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_next_month_deletion.xlsx")
        inception_data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/inception_july_2022_united.xlsx")

        classification = Classification()

        data_migration_addition = classification.migration_addition(data_frame=data, inception_data_frame=inception_data)

        if get_write_file(data_frame=data_migration_addition, file_name="med_ins_aug_22_data_migration_addition.xlsx", folder_location=excel_write_folder_location):
            print("Migration Addition Written Successfully!!!")
        else:
            print("Error in Writing Migration Addition!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Migration Addition Function!!!", exc_info=True)


def medical_insurance_death():
    try:

        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_migration_addition.xlsx")

        classification = Classification()

        data_death = classification.death(data_frame=data)

        if get_write_file(data_frame=data_death, file_name="med_ins_aug_22_data_death.xlsx", folder_location=excel_write_folder_location):
            print("Death Written Successfully!!!")
        else:
            print("Error in Writing Death!!!!")

    except Exception as e:
        print(e)
        print("Error in Medical Insurance Death Function")


def medical_insurance_policy_type():
    try:
        excel_write_folder_location = "H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022"

        data = get_read_proper_data(file_location="H:/Testing/Medical Insurance/A-Testing/Medical Insurance/august-2022/08102022/med_ins_aug_22_data_death.xlsx")

        classification = Classification()

        data_policy_type = classification.policy_type(data_frame=data)

        if get_write_file(data_frame=data_policy_type, file_name="med_ins_aug_22_data_policy_type.xlsx", folder_location=excel_write_folder_location):
            print("Policy Type Written Successfully!!!")
        else:
            print("Error in Writing Policy Type!!!")

    except Exception as e:
        print(e)
        logging.error("Error in Medical Insurance Policy Type!!!")


