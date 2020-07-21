from __future__ import print_function
import json
from template_cg import template
from datetime import date, timedelta

def reset_readme():
    with open('setting_cg.json', 'r') as f:
        setting_dict = json.load(f)

    for setting in setting_dict:
        print(setting)

    context = {
        "term": setting_dict['this_term'],
        "prof_name": setting_dict['instructor']['name'],
        "prof_website": setting_dict['instructor']['website'],
        "prof_email": setting_dict['instructor']['email'],
        "prof_phone": setting_dict['instructor']['phone'],
        "office_hour_day": setting_dict['office_hours']['day'],
        "office_hour_timeslot": setting_dict['office_hours']['timeslot'],
        "office_hour_location": setting_dict['office_hours']['location'],
        "midterm": setting_dict['schedule']['midterm'],
        "drop_date": setting_dict['schedule']['drop_date'],
        "reading_week": setting_dict['schedule']['reading_week'],
        "markus_link": setting_dict['markus_link']
    }

    a1_due_year = setting_dict['schedule']['A1_due']['year']
    a1_due_month = setting_dict['schedule']['A1_due']['month']
    a1_due_day = setting_dict['schedule']['A1_due']['day']
    a1_due = date(a1_due_year,a1_due_month,a1_due_day)

    for i in range(1, 7):
        key = "A" + str(i) + "_due"
        due_day = a1_due + timedelta((i-1) * 7)
        context[key] = str(due_day.day) + "/" + str(due_day.month)

    for i in range(7, 9):
        key = "A" + str(i) + "_due"
        due_day = a1_due + timedelta((i-1) * 7 + 14)
        context[key] = str(due_day.day) + "/" + str(due_day.month)

    print(context)

    with open('course_readme/csc418_readme.md','w') as myfile:
        myfile.write(template.format(**context))


if __name__ == '__reset_readme__':
    reset_readme()

