import numpy as np
with open('test.txt','r') as f:
    marks=f.readlines()
    mark=[]
    for i in marks:
        mark.append(float(i))

    mark=np.array(mark)
    
    print(np.sort(mark))
    print(np.percentile(mark,55))