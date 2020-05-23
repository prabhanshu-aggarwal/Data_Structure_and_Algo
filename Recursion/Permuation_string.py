# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:00:00 2020

@author: Prabhanshu Aggarwal
"""

# =============================================================================
# Fill Out Your Solution Below
# Let's think about what the steps we need to take here are:
# 
# Iterate through the initial string – e.g., ‘abc’.
# For each character in the initial string, set aside that character and get a list of all permutations of the string that’s left. So, for example, if the current iteration is on 'b', we’d want to find all the permutations of the string 'ac'.
# 
# Once you have the list from step 2, add each element from that list to the character from the initial string, and append the result to our list of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca', each of which we’d add to our final results.
# 
# Return the list of final results.
# 
# Let's go ahead and see this implement
# 
# =============================================================================


def permute(s):
    
    out = []
    
    if len(s)==1:
        out = [s]
        
    else:
        
        #for each letter in the string 
        for i, let in enumerate(s):
                
                for perm in permute(s[:i]+s[i+1:]):
                    
                    out+=[let+perm]
                    
    return out
            