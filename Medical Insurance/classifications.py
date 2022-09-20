import pandas as pd
import re
import logging
from func import *

class Classification:

    def __init__(self):
        pass

    def no_insurance(self, data_frame):
        try:
            data_frame['classification'] = data_frame.apply(
                lambda x: 'No Insurance' if re.search(r'noinsurance', str(x['mis_ins_company']).replace(" ", "").lower()) else x['classification'], axis=1
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

            doj_validated_yes['classification'] = doj_validated_yes.apply(
                lambda x : 'Next Month Addition' if int(str(x['ass_doj'].split("-")[1])) >= int(upload_month) and int(str(x['ass_doj']).split("-")[0]) >= int(upload_year) else x['classification'], axis = 1
            )

            frames = [doj_validated_yes, doj_validated_no]
            result = pd.concat(frames).sort_index()

            return result
        except Exception as e:
            print(e)
            logging.error("Error in Get Next Month Addition Function!!!", exc_info=True)
            return ''