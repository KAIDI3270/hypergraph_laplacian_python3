import numpy as np
import utils
import scipy.io
X = np.asarray(scipy.io.loadmat('cancerinputs.mat')['cancerInputs'],dtype=np.double)
Y = np.asarray(scipy.io.loadmat('cancerTargets.mat')['cancerTargets'],dtype=np.intc)

k = 2 # number of clusters
H = utils.MakingHypMat(X) #Making a hypergraph representation node x edge matrix

LZhou = utils.HypLap(H,'Zhou')
ErrZhou,_ = utils.GraphClustering(LZhou,k,Y)
print(f'error for Zhou is {ErrZhou}')

LRod = utils.HypLap(H,'Rod')
ErrRod,_ = utils.GraphClustering(LRod,k,Y)
print(f'error for Rodriguez is {ErrRod}')

LSaito = utils.HypLap(H,'Saito')
ErrSaito,_ = utils.GraphClustering(LSaito,k,Y)
print(f'error for Saito is {ErrSaito}')
