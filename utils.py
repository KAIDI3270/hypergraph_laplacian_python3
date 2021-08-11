import numpy as np
import scipy
import scipy.linalg
import itertools
import numpy.linalg as nl
from sklearn.cluster import KMeans

def MakingHypMat(X):
    tmp = 0
    for i in range(np.shape(X)[0]):
        tmp = tmp + max(X[i])
    tmp = 0
    for i in range(np.shape(X)[0]):
        jj = sorted(list(set(X[i])))
        for j in range(np.shape(jj)[0]):
            tmp = tmp + 1
    H = np.zeros((np.shape(X)[1],tmp),dtype=np.intc)
    tmp = 0
    for i in range(np.shape(X)[0]):
        jj = list(map(np.double, sorted(list(set(X[i])))))
        for j in range(np.shape(jj)[0]):
            for a in [aa[0] for aa in np.argwhere(X[i] == jj[j])]:
                H[a][tmp] = 1
            tmp = tmp + 1
    return H

def HypLap(H,mode):
    De = np.diag(np.sum(H,0))
    Dn = np.diag(np.sum(H,1))
    w = np.diag(np.ones(np.shape(De)[1]))
    if mode=='Zhou':
        DeZhou = De
        AA = H @ nl.inv(DeZhou) @ w @ (H.T)
    elif mode=='Rod':
        AA = H @ w @ (H.T) - Dn
        Dn = np.diag(sum(AA))
    elif mode=='Saito':
        De = De - np.diag(np.ones(np.shape(De)[1]))
        A = H @ nl.inv(De) @ w @ (H.T)
        AA = A-np.diag(np.diag(A))
    else:
        print('You have to choose mode from either Zhou, Rod, or Saito')
        exit()
    L = scipy.linalg.fractional_matrix_power(Dn, -0.5) @ (Dn - AA) @ scipy.linalg.fractional_matrix_power(Dn, -0.5)
    return L

def GraphClustering(L,k,Y):
    _,U = nl.eig(L)
    U=U.real
    temp=[a[:k] for a in U]
    kmean_result = KMeans(n_clusters=k, random_state=0).fit(temp)  
    acc=AccMeasure(kmean_result.labels_,Y[0])
    err = (100 - acc)/100  
    return err, np.asarray(kmean_result.labels_,dtype=np.intc)


def AccMeasure(T,idx):
    k=max(T)+1
    n=max(np.shape(T))
    a=[]
    for i in range(k):
        temp = [aa[0] for aa in np.argwhere(T == i)]
        if temp==None:
            a.append([])
        else:
            a.append(temp)
    b1=np.asarray([])
    t1=np.zeros(k)
    for i in range(k):
        tt1= [aa[0] for aa in np.argwhere(idx == i)]
        for j in range(k):
            temp=[aa in a[j] for aa in tt1]
            t1[j]=sum(temp)
        if b1.size==0:
            b1=t1.copy()
        else:
            b1=np.vstack((b1,t1))
    Members=np.zeros(k) 
        
    P = list(itertools.permutations([a for a in range(k)]))
    Acc1=0
    for pi in range(np.shape(P)[0]):
        for ki in range(k):
            Members[ki]=b1[P[pi][ki]][ki] 

        if sum(Members)>Acc1:
            Acc1=sum(Members)
    rand_ss1=0
    rand_dd1=0
    for xi in range(n-1):
        for xj in range(xi+1,n):
            rand_ss1=rand_ss1+((idx[xi]==idx[xj]) and (T[xi]==T[xj]))
            rand_dd1=rand_dd1+((idx[xi]!=idx[xj]) and (T[xi]!=T[xj]))
    Acc=Acc1/n*100
    return Acc
