#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:02:58 2020

@author: ajay
"""

import sys
import os
import re

Autosys_File = 'D:\\Autosys\\Python_Autosys\\Autosys_Jil\\JIL.txt'
MAIN_LIST = []
JobCount = 0

def main():
    read_jil(Autosys_File)


if __name__=="__main__":
    lst = ['insert_job','owner','permission','date_conditions','days_of_week','start_time','box_success','box_failure','description','max_run_alarm','alarm_if_fail','timezone']
    main()

def read_jil(filename):
    print(filename)
    read_file=open(filename,'r')
    for line in read_file.readlines():
        header = line.split(':')[0]
        trailer = line.split(':')[1]
        if header=='insert_job':
            call_insert_job()
        if header=='owner':
            call_owner()
        if header=='owner':
            call_owner()
        if header=='permission':
            call_owner()
        if header=='date_conditions':
            call_owner()
        if header=='days_of_week':
            call_owner()
        if header=='start_time':
            call_owner()
        if header=='owner':
            call_owner()
        if header=='owner':
            call_owner()
        if header=='owner':
            call_owner()
        if header=='owner':
            call_owner()
        if header=='owner':
            call_owner()
        if header=='owner':
            call_owner()

            newlist.append(trailer)
