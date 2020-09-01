#Checks if the set of subdirectories in two different directories is identical.
#Returns two lists - one of subdirs that are in directory A but not directory B, and one of subdirs in directory B but not A.
import os
import re


def get_subdirs(dir1, dir2):
    x1 = next(os.walk(dir1))[1]
    x2 = next(os.walk(dir2))[1]
    return [x1, x2] #Returns as a list of two lists.

def find_diffs(x1, x2):
    y1 = list(set(x1)-set(x2)) #Things in x1 that aren't in x2
    y2 = list(set(x2)-set(x1)) #Things in x2 that aren't in x1
    return [y1, y2]

def extractInts(x):
    #Extracts the integers from all strings in the passed list.
    i = 0
    for s in x:
        try:
            s = int(re.search(r'\d+', s).group())
            x[i] = s
            i += 1
        except:
            print("Exception")
    return x
