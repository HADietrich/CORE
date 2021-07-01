import pandas as pd
import xlrd
from LaborProfileCreator import LaborProfile, LaborProfiles
from TaskCreator import Task, Tasks
from CostLineCreator import CostLine, CostLines
from Core import Requirements, Requirement
from Constants import PE_PRR_Dict

location = ("POM24CSV.xls")
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)

i = 0
labor_profiles = LaborProfiles()
tasks = Tasks()
cost_lines = CostLines()
requirements = Requirements()
profile_id = 2
task_id = 1
for row in sheet:
    row_values = sheet.row_values(i)
    i += 1
    fe_name = row_values[15]
    if not tasks.check_for_existing(fe_name):
            task = Task(row_values, task_id)
            tasks.add_task(task)
            task_id += 1

    labor_profile_name = row_values[18]
    funded_activity = row_values[16]
    labor_rate = row_values[34]
    if labor_rate != 0:
        composite_key = str(funded_activity) + str(labor_profile_name)
        if not labor_profiles.check_for_existing(composite_key):
            labor_profile = LaborProfile(row_values, profile_id)
            labor_profiles.add_labor_profile(labor_profile)
            profile_id += 1
        else:
           labor_profile = labor_profiles.find_profile(composite_key)
    else:
        labor_profile = LaborProfile(row_values, profile_id)
        labor_profile.set_other_cost_profile()

    requirement = Requirement(row_values)
    requirements.add_requirement(requirement)


    cost_line = CostLine(row_values, task, labor_profile)
    cost_lines.add_cost_line(cost_line)



# data_frame = requirements.create_data_frame()
# datatoexcel = pd.ExcelWriter('Requirements.xlsx')
# data_frame.to_excel(datatoexcel)
# datatoexcel.save()


data_frame = cost_lines.create_dataframe()
datatoexcel = pd.ExcelWriter('Costlines.xlsx')
data_frame.to_excel(datatoexcel)
datatoexcel.save()

data_frame = tasks.create_data_frame()
datatoexcel = pd.ExcelWriter('Tasks.xlsx')
data_frame.to_excel(datatoexcel)
datatoexcel.save()

data_frame = labor_profiles.create_data_frame()
datatoexcel = pd.ExcelWriter('LaborProfiles.xlsx')
data_frame.to_excel(datatoexcel)
datatoexcel.save()





