import numpy as np
def calculate(list1):
    if len(list1)==9:
        arr=np.array(list1).reshape((3,3))
    calculations ={}
    calculations['mean'] = [list1.mean(axis=0).tolist(),list1.mean(axis=1).tolist(),np.mean(list1).tolist()],
    calculations['variance'] = [list1.var(axis=0).tolist(),list1.var(axis=1).tolist(),np.var(list1).tolist()],
    calculations['standard deviation']= [list1.std(axis=0).tolist(),list1.std(axis=1).tolist(),np.std(list1).tolist()],
    calculations['max'] = [list1.max(axis=0).tolist(),list1.max(axis=1).tolist(),np.max(list1).tolist()],
    calculations['min'] = [list1.min(axis=0).tolist(),list1.min(axis=1).tolist(),np.min(list1).tolist()],
    calculations['sum'] = [list1.sum(axis=0).tolist(),list1.sum(axis=1).tolist(),np.sum(list1).tolist()]
    
    return calculations
list1=[0,1,2,3,4,5,6,7,8]
print(calculate(list1))
    