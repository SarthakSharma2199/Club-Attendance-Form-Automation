import pandas as pd
from attendance_driver import *

participants=pd.read_excel("./participants.xlsx")

for index, row in participants.iterrows():
    participant_name=row['Name']
    participant_reg_no=row['Reg. No']
    mark_attendance(participant_name, participant_reg_no)
