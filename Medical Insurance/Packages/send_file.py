import pandas as pd
import numpy as np

def get_write_file(data_frame, file_name, folder_location):
    try:
        write_path = folder_location + "/" + file_name
        data_frame.to_excel(write_path, index=False)
        return True
    except Exception as e:
        print(e)
        return False


data = pd.read_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022/data_classification_3.xlsx")

data_proper = data.replace(np.nan, "")

data_proper["ass_mobile_number"] = data_proper["ass_mobile_number"].apply(
    lambda x : x.replace("/#/", "")
)

data_proper.drop(['ass_dob_validate_Yes_or_No', 'ass_doj_validate_Yes_or_No', 'ass_actual_dol_validate_Yes_or_No', 'ass_sr_effective_date_validate_Yes_or_No',
                  'ass_dol_validate_Yes_or_No', 'mis_pol_start_date_validate_Yes_or_No', 'mis_pol_end_date_validate_Yes_or_No', 'exit_actual_dol_validate_Yes_or_No'
                  ], axis = 1, inplace=True)


get_write_file(data_frame=data_proper, file_name="mis_recon_aug_out_29082022.xlsx", folder_location="G:/AdventsProduct/Others/A-Testing/Medical Insurance/august-2022")