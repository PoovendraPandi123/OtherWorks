import pandas as pd

associate_data = pd.read_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/Testing/associate_check.xlsx")
mis_data = pd.read_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/Testing/mis_check.xlsx")

# Outer
data_result_outer = pd.merge(associate_data, mis_data, left_on=['Client Id'], right_on=['Client Id'], how='outer', suffixes=('', '_y'))
data_result_outer.drop(data_result_outer.filter(regex='_y$').columns, axis=1, inplace=True)

data_result_outer.to_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/Testing/associate_mis_outer.xlsx", index=False)

# Inner
data_result_inner = pd.merge(associate_data, mis_data, left_on=['Client Id'], right_on=['Client Id'], how='inner', suffixes=('', '_y'))
data_result_inner.drop(data_result_inner.filter(regex='_y$').columns, axis=1, inplace=True)

data_result_inner.to_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/Testing/associate_mis_inner.xlsx", index=False)

# Left
data_result_left = pd.merge(associate_data, mis_data, left_on=['Client Id'], right_on=['Client Id'], how='left', suffixes=('', '_y'))
data_result_left.drop(data_result_left.filter(regex='_y$').columns, axis=1, inplace=True)

data_result_left.to_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/Testing/associate_mis_left.xlsx", index=False)

# Right
data_result_right = pd.merge(associate_data, mis_data, left_on=['Client Id'], right_on=['Client Id'], how='right', suffixes=('', '_y'))
data_result_right.drop(data_result_right.filter(regex='_y$').columns, axis=1, inplace=True)

data_result_right.to_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/Testing/associate_mis_right.xlsx", index=False)


"""

      "columns": ["ass_client_id", "ass_client_name", "ass_emp_no", "ass_associate_name", "ass_email_id", "ass_mobile_number", "ass_gender", "ass_dob", "ass_designation",
      "ass_ins_comp_name", "ass_doj", "ass_actual_dol", "ass_active_status", "ass_stop_pay_status", "ass_ol_basic", "ass_ol_da", "ass_ol_empf", "ass_ol_emp_comp", "ass_ol_esic",
      "ass_ol_ctc", "ass_ol_gross", "ass_sr_basic", "ass_sr_da", "ass_sr_empf", "ass_sr_emp_comp", "ass_sr_esic", "ass_sr_ctc", "ass_sr_gross", "ass_sr_effective_date", "ass_dol",
      "mis_sl_no", "mis_corp_id", "mis_client_id", "mis_status", "mis_policy_type", "mis_gmc", "mis_gpa", "mis_premium_cost", "mis_billing_type", "mis_ec_industry",
      "mis_ec_industry_sales_force", "mis_ec_rates_for_lombard", "mis_updated_date", "mis_updated_name", "mis_gtl_policy", "mis_remarks_2", "mis_ins_company", "mis_pol_start_date",
      "mis_pol_end_date", "mis_parental_id", "mis_tpa_name"],

"""