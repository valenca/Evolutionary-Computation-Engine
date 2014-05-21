
# Sistemas Imunes Artificiais
""" 
Negative Selection
Ernesto Costa, May 2014.
"""

from random import randint

# Negative Selection

# Training phase

def ns_training(self,threshold,size,number):
    """ 
    self = list of self paterns. 
    threshold = for affinity measurement.
    size = dimensions of receptors. 
    number = number of T-cells.
    """
    tcr = []
    numb_t = 1
    while numb_t <= number:
        r_0 = create_detector(size)
        # avoid repetitions
        if r_0 in tcr:
            continue
        for elem in self:
            aff = affinity(r_0,elem)
            if aff >= threshold:
                break
        else:
            tcr.append(r_0)
            numb_t += 1
    return tcr

# ns_classification phase
def ns_classification(s_ns,tcr,threshold):
    """ 
    s_ns: self / non-self to monitor. 
    tcr= the t-cells receptors.
    threshold = the threshold for affinity.
    """
    danger = []
    for n,elem in enumerate(s_ns):
        temp = 0
        for detector in tcr:
            aff = affinity(elem, detector)
            if aff >= threshold:
                danger.append(1)
                temp = 1
                break
        if temp == 0:
            danger.append(0)
    return danger
        
def create_detector(size):
    return [[randint(0,1) for i in range(size[1])] for j in range(size[0])]

# Auxiliary

# Affinity

def affinity(s,t):
    """Hamming affinity based on identity"""
    count = 0
    for i in range(len(s)):
        count_line_i = 0
        for j in range(len(s[0])):
            if s[i][j] == t[i][j]:
                count_line_i += 1
        count += count_line_i
    return count
    

if __name__ == '__main__':
    one = [[0,0,1,0],[0,1,1,0,],[0,0,1,0],[0,0,1,0],[0,0,1,0]]
    two = [[0,1,1,1],[0,0,0,1],[0,0,1,0],[0,1,0,0],[0,1,1,1]]
    three = [[0,1,1,1],[0,0,0,1],[0,0,1,1],[0,0,0,1],[0,1,1,1]]
    four = [[1,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,1,1],[0,0,1,0]]
    five = [[1,1,1,0],[1,0,0,0],[0,1,1,0],[0,0,1,0],[1,1,1,0]]
    six = [[0,1,1,0],[1,0,0,0],[1,1,1,0],[1,0,0,1],[0,1,1,1]]
    seven = [[0,1,1,1],[0,0,0,1],[0,0,1,0],[0,0,1,0],[0,0,1,0]]
    eight = [[0,1,1,0],[1,0,0,1],[0,1,1,0],[1,0,0,1],[0,1,1,0]]
    #print(affinity(one,four))
    #print(create_detector([5,4]))
    # Data
    self = [one,two,three,four]
    threshold = 10
    size = [5,4]
    number = 10
    detectors = ns_training(self,threshold,size,number)
    #print(detectors)
    patterns = [one, two, three, four, five, six, seven, eight]
    print(ns_classification(patterns,detectors,threshold))

    
    
    

            
