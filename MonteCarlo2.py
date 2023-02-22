import numpy as np

f = open('MonteCarlo2.txt','w')

for i in np.arange(2,21,1):

    hits = np.array([np.random.uniform(0,1,i*1000000)]).reshape(1000000,i)
    circle = np.count_nonzero(1 > np.sqrt(np.power(hits,2).sum(axis=1)))
    newVo = np.power(2,i)*circle/1000000
    Vo = np.power(np.pi,i/2) / np.math.gamma(i/2+1)
    
    f.write(str(i)+' ) '+
            str(newVo)+' , '+
            str(newVo/Vo)+' , '+
            str(circle)+'\n')

f.close()
