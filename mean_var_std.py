import numpy as np
def calculate(list1):
    if len(list1)==9:
        arr=np.array(list1).reshape((3,3))
    calculations ={}
    calculations['mean'] = [arr.mean(axis=0).tolist(),arr.mean(axis=1).tolist(),np.mean(arr).tolist()]
    calculations['variance'] = [arr.var(axis=0).tolist(),arr.var(axis=1).tolist(),np.var(arr).tolist()]
    calculations['standard deviation']= [arr.std(axis=0).tolist(),arr.std(axis=1).tolist(),np.std(arr).tolist()]
    calculations['max'] = [arr.max(axis=0).tolist(),arr.max(axis=1).tolist(),np.max(arr).tolist()]
    calculations['min'] = [arr.min(axis=0).tolist(),arr.min(axis=1).tolist(),np.min(arr).tolist()]
    calculations['sum'] = [arr.sum(axis=0).tolist(),arr.sum(axis=1).tolist(),np.sum(arr).tolist()]
    
    return calculations
list1=[0,1,2,3,4,5,6,7,8]
print(calculate(list1))
    
