class Bin(object):
    def __init__(self, capacity):
        self.items = []
        self.sum = 0
        self.cap = capacity
        self.waste = capacity;

    def append(self, item):
        self.items.append(item)
        self.sum += item
        self.waste = self.cap - self.sum
        

def firstFit(weights,capacity):
     bins = []
     for weight in weights:
        #see if the item fits
        for bin in bins:
            if bin.sum + weight <= capacity:
                #Add weight to bin
                bin.append(weight)
                break
        else:
            #Weight does not fit into any bin - new bin
            bin = Bin(capacity)
            bin.append(weight)
            bins.append(bin)
     return bins

def firstFitDecr(weights, capacity):
     sortedWgt = sorted(weights, reverse = True)
     result = firstFit(sortedWgt, capacity)
     return result

def bestFit(weight, capacity): 
    #Count bins)
    n = len(weight)  
    result = 0; 
    bins = []
    #Remaining space in bins 
    spaceRem = [0] * n; 
    #Iterate weights
    for i in range(len(weight)):   
        j = 0; 
        #Minimum space left and index  of best bin 
        min = capacity + 1; 
        binIdx = 0; 

        for j in range(result): 
            if (spaceRem[j] >= weight[i] and spaceRem[j] - weight[i] < min): 
                binIdx = j; 
                min = spaceRem[j] - weight[i]; 
              
        #If no bin could hold weight,create new bin
        if (min == capacity + 1): 
            spaceRem[result] = capacity - weight[i]; 
            result += 1; 
            
            #Weight does not fit into any bin - new bin
            bin = Bin(capacity)
            bin.append(weight[i])
            bins.append(bin)
        
        #Else, Put weight in best bin 
        else: 
            spaceRem[binIdx] =  spaceRem[binIdx] - weight[i];
            bins[binIdx].append(weight[i])
    return bins;