def rbs(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        
        if list[midpoint] == target:
            return True
        else: 
            if list [midpoint] < target:
                return rbs(list[midpoint+1:], target)
            else:
                return rbs(list[midpoint], target)