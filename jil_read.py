#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:02:58 2020

@author: ajay
"""

import sys
import os
import re

home_dir='/home/ajay/python_examples/'
p=os.chdir('/home/ajay/python_examples/')
box_string=""

def read_jil(filename):
    print(filename)
    call_box=""
    call_job=""
    read_file=open(filename,'r')
    for line in read_file.readlines():
        if line.find('job_type') >= 1:
            job_type=(line.split(':')[2]).rstrip('\n').strip()
            if job_type == 'b':
                call_box=1
                call_job=0
            if job_type == 'c':
                call_job=1
                call_box=0
        
        if call_box==1:
            fun_call_box(line)
        if call_job==1:
            fun_call_job()
            
            
def fun_call_box(linecp):
    box_name=""
    owner=""
    permission=""
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
        permission=linecp.split(':')[1].strip()
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
        start_times=linecp.split(':')[1].strip()
        add_string(str(start_times))
    if linecp.find('description') == 0:
        description=linecp.split(':')[1].strip()
        add_string(str(description))
    if linecp.find('term_run_time') == 0:
        term_run_time=linecp.split(':')[1].strip()
        add_string(str(term_run_time))        
    
    filen=os.getcwd()+os.sep+'file1.csv'    
    f=open(filen,'w')
    f.write(box_string)
    f.close()
    

def fun_call_job():
    if line.find('insert_job') >= 1:
        box_name=line.split(':')[1].split(' ')[1]
    if line.find('owner') >= 1:
        owner=line.split(':')
    if line.find('permission') >= 1:
        permission=line.split(':')

def add_string(string1):
    global box_string
    box_string=box_string+','+str(string1)
    
def main():
    file="jil.txt"
    read_jil(home_dir+file)

if __name__=="__main__":
    line=""
    call_box=0
    call_job=0
    #For Box
    box_string=""
    box_name=""
    owner=""
    permission=""
    main()