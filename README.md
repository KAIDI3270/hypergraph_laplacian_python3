# hypergraph_laplacian_python

## Description
python version implementation of [(AAAI 18) Hypergraph p-Laplacian: A Differential Geometry View](https://arxiv.org/abs/1711.08171).\
The original implementation by author can be found at [here.](https://github.com/ShotaSAITO/Hypergraph-Laplacian)

## Use
```console
foo@bar:~/Desktop/hypergraph_laplacian_python$ python3 main.py
```


## Environment
- Used Anaconda3 environment.
- environment.yml contains necessary environments for the code
- You can create conda environment 'hlaplacian' by using the command below.
```console
foo@bar:~/Desktop/hypergraph_laplacian_python$ conda env create -f environment.yml
```
- The environment contains followings
    - python 3.7.11
    - numpy 1.20.3
    - scipy 1.6.2
    - scikit-learn 0.23.2

- conda_create_env.sh can create and install necessary environment. You will be asked to decide environment name.
    - The created conda environment installs the followings but the version may differ from my implementation.
        - python 3.7
        - numpy
        - scipy
        - scikit-learn
    - This is the last resort for creating conda environment when environment.yml does not work properly. (due to conflict with the computer environment of user.)
    - But this does not guarantee the proper operation of code.
```console
foo@bar:~/Desktop/hypergraph_laplacian_python$ ./conda_create_env.sh
```