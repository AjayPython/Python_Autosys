#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:02:58 2020

@author: ajay
"""

import os


home_dir='/home/ajay/python_examples/'
p=os.chdir('/home/ajay/python_examples/')
box_string=""

def file_to_write(string_to_write):
    f.writelines("%s\n" % string_to_write)
    

def read_jil(read_file):
    call_box=""
    call_job=""
    global box_string
    for line in read_file.readlines():
        if line.find('job_type') >= 1:
            job_type=(line.split(':')[2]).rstrip('\n').strip()
            if job_type == 'b':
                call_box=1
                call_job=0
                box_str='box_name,owner,permission,date_conditions,days_of_week,exclude_calendar,start_times,description,term_run_time,job_name,job_box_name,command,machine,owner,permission,condition,description,std_out_file,std_err_file,alarm_if_fail'
                file_to_write(box_str)
            if job_type == 'c':
                call_job=1
                call_box=0
        if call_box==1:
            fun_call_box(line)
        if call_job==1:
            fun_call_job(line)
        
        if (line.find('application') >= 0) & (call_box==1):
            file_to_write(box_string.lstrip(',')+',,,,,,,,,,,')
            box_string=""

        if (line.find('application') >= 0) & (call_job==1):
            file_to_write(',,,,,,,,'+box_string)            
            
def fun_call_box(linecp):
    global box_string, f
    print(str(linecp.find('insert_job')) + linecp)
    print(str(linecp.find('owner')) + linecp)
    print(str(linecp.find('permission')) + linecp)
    if linecp.find('insert_job') == 0:
        box_name=linecp.split(':')[1].split(' ')[1]
        add_string(box_name)
    if linecp.find('owner') == 0:
        owner=linecp.split(':')[1].strip()
        add_string(str(owner))
    if linecp.find('permission') == 0:
        permission1=linecp.split(':')[1].strip()
        permission=permission1.replace(',','|')
        add_string(str(permission))
    if linecp.find('date_conditions') == 0:
        date_conditions=linecp.split(':')[1].strip()
        add_string(str(date_conditions))
    if linecp.find('days_of_week') == 0:
        days_of_week=linecp.split(':')[1].strip()
        final_days_of_week=days_of_week.replace(',','|')
        add_string(str(final_days_of_week))
    if linecp.find('exclude_calendar') == 0:
        exclude_calendar=linecp.split(':')[1].strip()
        add_string(str(exclude_calendar))
    if linecp.find('start_times') == 0:
        start_times=linecp.split('"')[1]
        add_string(str(start_times))
    if linecp.find('description') == 0:
        description=linecp.split(':')[1].strip()
        add_string(str(description))
    if linecp.find('term_run_time') == 0:
        term_run_time=linecp.split(':')[1].strip()
        add_string(str(term_run_time)) 
    

def fun_call_job(linecp):
    global box_string, f
    if linecp.find('insert_job') >= 0:
        job_name=linecp.split(':')[1].split(' ')[1]
        add_string(job_name)
    if linecp.find('box_name') >= 0:
        job_box_name=linecp.split(':')[1].strip()
        add_string(str(job_box_name))
    if linecp.find('command') >= 0:
        command=linecp.split(':')[1].strip()
        add_string(str(command))
    if linecp.find('machine') >= 0:
        machine=linecp.split(':')[1].strip()
        add_string(str(machine))
    if linecp.find('owner') >= 0:
        owner=linecp.split(':')[1].strip()
        add_string(str(owner))
    if linecp.find('permission') >= 0:
        permission1=linecp.split(':')[1].strip()
        permission=permission1.replace(',','|')
        add_string(str(permission))
    if linecp.find('condition') >= 0:
        condition1=linecp.split(':')[1]
        condition=condition1.rstrip('\n')
        add_string(str(condition))
    if linecp.find('description') >= 0:
        description=linecp.split(':')[1].strip()
        add_string(str(description))
    if linecp.find('std_out_file') >= 0:
        std_out_file=linecp.split(':')[1].strip()
        add_string(str(std_out_file))        
    if linecp.find('std_err_file') >= 0:
        std_err_file=linecp.split(':')[1].strip()
        add_string(str(std_err_file))
    if linecp.find('alarm_if_fail') >= 0:
        alarm_if_fail=linecp.split(':')[1].strip()
        add_string(str(alarm_if_fail))
    
def add_string(string1):
    global box_string
    box_string=box_string+','+str(string1)
    
def main():
    file="jil.txt"
    read_file=open(home_dir+file,'r')
    read_jil(read_file)
    read_file.close()
    
if __name__=="__main__":
    line=""
    call_box=0
    call_job=0
    read_file=""
    global f 
    filen=os.getcwd()+os.sep+'file1.csv'    
    f=open(filen,'w')

    main()
    f.close()