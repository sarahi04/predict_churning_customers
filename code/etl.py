

import pandas as pd

#ETL

def read_local_path(file_path_ch_cust):
    #Extract 
    df = pd.read_csv(file_path_ch_cust)
    #Transform
    df = df.drop(columns=['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', 'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'])
    #Load
    df.to_csv(r"c:\Users\sarah\Desktop\ch_customers\data\bank_churners_drop_incorrect_columns.csv", index=False)
    return df


if __name__ == "__main__":

    file_path_ch_cust = r"c:\Users\sarah\Desktop\ch_customers\data\BankChurners.csv"
    etl_churners_df = read_local_path(file_path_ch_cust)
    print(etl_churners_df)



