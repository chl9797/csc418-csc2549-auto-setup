from __future__ import print_function
import json
from template_physics import template
from datetime import date, timedelta

def reset_readme(setting_dict):
    for setting in setting_dict:
        print(setting)

    context = {
        "term": setting_dict['this_term'],
        "prof_name": setting_dict['instructor']['name'],
        "prof_website": setting_dict['instructor']['website'],
        "prof_email": setting_dict['instructor']['email'],
        "prof_phone": setting_dict['instructor']['phone'],
        "drop_date": setting_dict['schedule']['drop_date'],
        "markus_link": setting_dict['markus_link']
    }

    a1_due_year = setting_dict['schedule']['A1_due']['year']
    a1_due_month = setting_dict['schedule']['A1_due']['month']
    a1_due_day = setting_dict['schedule']['A1_due']['day']
    a1_due = date(a1_due_year,a1_due_month,a1_due_day)

    for i in range(1, 9):
        key = "A" + str(i) + "_due"
        due_day = a1_due + timedelta((i-1) * 7)
        context[key] = str(due_day.day) + "/" + str(due_day.month)

    print(context)

    with open('course_readme/csc2549_readme.md','w') as myfile:
        myfile.write(template.format(**context))


