def check(menp, womenp):
    engaged = {}
    freemen = list(menp.keys())
    proposals = {m:0 for m in menp}
    
    while freemen:
        man = freemen.pop(0)
        woman = menp[man][proposals[man]]
        proposals[man] += 1
        
        if woman not in engaged:
            engaged[woman] = man
            
        else:
            current = engaged[woman]
            if womenp[woman].index(current) > womenp[woman].index(man):
                engaged[woman] = man
                freemen.append(current)
            else:
                freemen.append(man)
                
    return engaged

if __name__ == '__main__':
    
    men_preferences = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'X', 'Z'],
        'C': ['X', 'Z', 'Y']
    }
    
    women_preferences = {
        'X': ['B', 'A', 'C'],
        'Y': ['C', 'B', 'A'],
        'Z': ['A', 'B', 'C']
    }
    
    print(check(men_preferences, women_preferences))
