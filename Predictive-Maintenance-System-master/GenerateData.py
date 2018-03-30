"""
-----------------------------------------------------------------------------

Rowan Computer Science Dept Spring 2018 Software Engineering Team Ostriches
Predictive Maintenance System for ASRC Federal Mission Solutions Engineering

Team Ostriches Members:
Product Owner:  Craig Wert
 Scrum Master:  John Stranahan
    Developer:  Tapan Soni
    Developer:  Michael Matthews
    Developer:  Joshua Jackson
    Developer:  Nicholas La Sala

-----------------------------------------------------------------------------

Description:



-----------------------------------------------------------------------------
"""

#Generates new data randomly based upon lower bound and maxium bound on actual data set
#note this algorithm can be imporved in the followin ways
    #have stages of data that its based upon for the example since the engine is deterioting the frist 10% will look different than the second 10% etc.
    #possibly do somthing with averages and standard deviation

#Todo: when generating new data feature that columns that were only ints in real data set will only be ints in generated data set
# program can run more efficently by
#    1.) parralizing reading of the dataset
#    2.) exporting and importing generated random dataset, columns avgs. etc so it doesn't have to be everytime the progarm is run

import numpy as np
import random
import math
from sklearn import preprocessing


#Generate takes three parameters
#   min - the minimum bound
#   max - the maximum bound
def generate(min, max,size):
    new_data_set = np.zeros((size, 30))

    for x in range(0,30):
        for y in range(0,size):
            new_data_set[y][x] = random.uniform(min[x]/2, max[x]*2)

    return new_data_set