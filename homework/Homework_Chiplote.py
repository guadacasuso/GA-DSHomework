# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:46:46 2016

@author: guadalupecasuso
"""


import csv

path= "./data/chipotle.tsv"

applicationsFile= open(path)

applicationsFileReader = csv.reader(applicationsFile)
applicationsData= list(applicationsFileReader)

#Understanding the Data 
print 'Raw Data:',  applicationsData [0]

#Total companies aplying to FAA Exemptions 
print 'Total Companies application' , len(applicationsData) 


