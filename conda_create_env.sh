read -p 'Decide the name of conda environment: ' envname
conda create -y -n $envname python=3.7
eval "$(conda shell.bash hook)"
conda activate $envname
conda install -y -c anaconda scikit-learn
conda install -y -c anaconda numpy
conda install -y -c anaconda scipy