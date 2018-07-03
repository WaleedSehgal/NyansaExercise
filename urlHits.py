# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 20:21:14 2018

@author: Waleed
"""

import time
import operator


'''
NOTE: Time complexity analysis:
    
The worst case time complexity will be O(n), where n are the total entries (lines) in
the 'input.txt' file and n is greater than the distinct dates and urls.
'''

#helper function to convert epoch to GMT
def toGMT(epoch):
    gmt = time.strftime('%m/%d/%Y', time.gmtime(epoch))
   
    return gmt

    
'''
function that takes as input text file and returns a hashmap of dates as keys  
urls&hits as nested key-value hashmap.
'''
def outGMT(file):
    
    out_map = dict()
    
    with open(file) as f:
       
        for entry in f:
            entry = entry.split('|')
            
            entry[0] = toGMT(int(entry[0]))
            entry[1] = entry[1].strip() 
           
            if entry[0] not in out_map.keys():
                out_map[entry[0]] = {entry[1]:1}
            
            else:
                if entry[1] not in out_map[entry[0]].keys():
                    out_map[entry[0]][entry[1]] = 1
                else:
                    out_map[entry[0]][entry[1]] += 1
                              
    return out_map


'''
Main function that takes as input unsorted hashmap from outGMT
then sorts and outputs data in the required format.
'''
def dailyRep(file):
    
    out_map = outGMT(file)
    dates = sorted(out_map,key=lambda date: time.strptime(date, "%m/%d/%Y"))
    for day in dates:
        print(day + ' GMT')
        
        url_hits = sorted(out_map[day].items(), key=operator.itemgetter(1), reverse = True)
        
        for url in url_hits:
            print(url[0],url[1])

        
#call to main function
dailyRep('input.txt')        
