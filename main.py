import pandas as pd
from attendance_driver import *

participants=pd.read_excel("./participants.xlsx")

for index, row in participants.iterrows():
    attendance_status=row['Attendance Status']
    if(attendance_status=='marked'):
        continue
    participant_name=row['Name']
    participant_reg_no=row['Reg. No']
    #Checking for NaN values
    if(participant_reg_no!=participant_reg_no):
        participant_reg_no=""
    mark_attendance(participant_name, participant_reg_no)
    participants.at[index,'Attendance Status']="marked"
    #print(participant_name, participant_reg_no, participants.at[index,'Attendance Status'])
    participants.to_excel("./participants.xlsx", index=False)

