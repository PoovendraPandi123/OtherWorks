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
                lambda x: 'No Insurance' if re.search(r'noinsurance', str(x['mis_ins_company']).replace(" ", "").lower()) else x['classification_1'], axis=1
            )
            return data_frame

        except Exception as e:
            print(e)
            logging.error("Error in Get No Insurance Function!!!", exc_info=True)
            return ''

    def next_month_addition(self, data_frame, upload_month, upload_year):
        try:
            doj_validated_yes = data_frame[data_frame['ass_doj_validate_Yes_or_No'] == 'Yes']
            doj_validated_no = data_frame[data_frame['ass_doj_validate_Yes_or_No'] == 'No']

            doj_validated_yes['classification_1'] = doj_validated_yes.apply(
                lambda x : 'Next Month Addition' if int(str(x['ass_doj'].split("-")[1])) >= int(upload_month) and int(str(x['ass_doj']).split("-")[0]) >= int(upload_year) else x['classification_1'], axis = 1
            )

            frames = [doj_validated_yes, doj_validated_no]
            result = pd.concat(frames).sort_index()

            return result
        except Exception as e:
            print(e)
            logging.error("Error in Get Next Month Addition Function!!!", exc_info=True)
            return ''

    def alcs_deletion(self, data_frame, upload_month, upload_year):
        try:
            exit_actual_dol_validated_yes = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'Yes']
            exit_actual_dol_validated_no = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'No']

            exit_actual_dol_validated_yes['classification_1'] = exit_actual_dol_validated_yes.apply(
                lambda x : 'ALCS Deletion' if int(str(x['exit_actual_dol'].split("-")[1])) <= int(upload_month) and int(str(x['exit_actual_dol']).split("-")[0]) <= int(upload_year) else x['classification_1'], axis = 1
            )

            frames = [exit_actual_dol_validated_yes, exit_actual_dol_validated_no]
            result = pd.concat(frames).sort_index()

            return result
        except Exception as e:
            print(e)
            logging.error("Error in Get ALCS Deletion Function!!!", exc_info=True)
            return ''

    def next_month_alcs_deletion(self, data_frame, upload_month, upload_year):
        try:
            exit_actual_dol_validated_yes = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'Yes']
            exit_actual_dol_validated_no = data_frame[data_frame['exit_actual_dol_validate_Yes_or_No'] == 'No']

            exit_actual_dol_validated_yes['classification_1'] = exit_actual_dol_validated_yes.apply(
                lambda x: 'Next Month ALCS Deletion' if int(str(x['exit_actual_dol'].split("-")[1])) > int(upload_month) and int(str(x['exit_actual_dol']).split("-")[0]) >= int(upload_year) else x['classification_1'], axis=1
            )

            frames = [exit_actual_dol_validated_yes, exit_actual_dol_validated_no]
            result = pd.concat(frames).sort_index()

            return result
        except Exception as e:
            print(e)
            logging.error("Error in Get ALCS Deletion Function!!!", exc_info=True)
            return ''

    def policy_type(self, data_frame):
        try:

            data_frame['classification_3'] = data_frame.apply(
                lambda x : 'EC/WC' if ( str(x['ass_ol_emp_comp']).replace(" ", "") != '' or str(x['ass_sr_emp_comp']).replace(" ", "") != '' ) and x['classification_3'] == '' else x['classification_3'], axis = 1
            )

            # Filter Updated Data and Non Updated Data EC/WC
            data_frame_ec_updated = data_frame[data_frame['classification_3'] == 'EC/WC']
            data_frame_ec_not_updated = data_frame[data_frame['classification_3'] != 'EC/WC']

            # Update ESIC on not updated data only EC/WC
            data_frame_ec_not_updated['classification_3'] = data_frame_ec_not_updated.apply(
                lambda x : 'ESIC' if ( str(x['ass_ol_esic']).replace(" ", "") != '' or str(x['ass_sr_esic']).replace(" ", "") ) and x['classification_3'] == '' else x['classification_3'], axis = 1
            )

            # Filter Updated Data and Non Updated Data ESIC
            data_frame_esic_updated = data_frame_ec_not_updated[data_frame_ec_not_updated['classification_3'] == 'ESIC']
            data_frame_esic_not_updated = data_frame_ec_not_updated[data_frame_ec_not_updated['classification_3'] != 'ESIC']

            # Update No ESIC on not updated data only ESIC
            data_frame_esic_not_updated['classification_3'] = data_frame_esic_not_updated['classification_3'].apply(
                lambda x : x if x in ['ESIC', 'EC/WC'] else 'NO EC AND ESIC'
            )

            overall_data_frames = [data_frame_ec_updated, data_frame_esic_updated, data_frame_esic_not_updated]

            merged_data_frame = pd.concat(overall_data_frames).sort_index()

            # data_frame.loc[data_frame['ass_ol_emp_comp'] != '', 'classification_3'] = 'EC/WC'
            # data_frame.loc[data_frame['ass_sr_emp_comp'] != '', 'classification_3'] = 'EC/WC'
            # data_frame.loc[data_frame['ass_ol_esic'] != '', 'classification_3'] = 'ESIC'
            # data_frame.loc[data_frame['ass_sr_esic'] != '', 'classification_3'] = 'ESIC'

            # data_frame['classification_3'] = data_frame['classification_3'].apply(
            #     lambda x : 'NO EC AND ESIC' if x == '' else x
            # )

            return merged_data_frame
        except Exception as e:
            logging.error("Error in Get Policy Type EC/WC Function!!!", exc_info=True)
            return ''