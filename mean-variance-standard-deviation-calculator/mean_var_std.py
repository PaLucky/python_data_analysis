import numpy as np

def calculate(lista):
    try:
      a = np.array(lista).reshape(3,3)
    except ValueError:
      raise ValueError("List must contain nine numbers.")
      return "List must contain nine numbers."  
    calculations={}    
    mean_a1=list(np.mean(a,axis=0))
    mean_a2=list(np.mean(a,axis=1))   
    mean_flattened=a.mean()
    calculations['mean']=[mean_a1,mean_a2,mean_flattened]
    variance_a1=list(np.var(a,axis=0))
    variance_a2=list(np.var(a,axis=1))
    variance_flattened=a.var()
    calculations['variance']=[variance_a1,variance_a2,variance_flattened]
    deviation_a1=list(np.std(a,axis=0))
    deviation_a2=list(np.std(a,axis=1))
    deviation_flattened=a.std()
    calculations['standard deviation']=[deviation_a1,deviation_a2,deviation_flattened]
    max_a1=list(np.max(a,axis=0))
    max_a2=list(np.max(a,axis=1))
    max_flattened=a.max()
    calculations['max']=[max_a1,max_a2,max_flattened]
    min_a1=list(np.min(a,axis=0))
    min_a2=list(np.min(a,axis=1))
    min_flattened=a.min()
    calculations['min']=[min_a1,min_a2,min_flattened]
    sum_a1=list(np.sum(a,axis=0))
    sum_a2=list(np.sum(a,axis=1))
    sum_flattened=a.sum()
    calculations['sum']=[sum_a1,sum_a2,sum_flattened]
    #calculation +=
    #print(np.mean([a],axis=1))




    return calculations

#{'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889], 'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654], 'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266], 'max': [[8, 6, 7], [6, 8, 7], 8], 'min': [[1, 4, 0], [2, 0, 1], 0], 'sum': [[11, 15, 9], [10, 12, 13], 35]}