####### Declaration
The project was forked from Nilabhra's RNTN project and I have modified it for myself.
#### TOPIC: Sentiment Classification from Movie Reviews
##### Package and Evironment
Setup a python3.7 virtual env and install the following packages: numpy, scipy, matplotlib, sklearn.

##### Preprocess and Get Data Used Later
Run command `python data_handler.py` and the results are generated in the **current** folder.

You can load all original data from directory `dataset`. 

##### EDA
Run command `python plot_dist.py`and the results are generated in the **current** folder.

##### Models
- RNTN: Run command `python ex.py` to train and `python evalute.py` to evalute, the trained model will saved in the **current** folder and the evalute results will be printed in the console.

> We saved one trained model with a certain parameters combination at `save.pkl`, you can directly run command `python evaluate.py` to get the test set accuracy.

- SVM: Run command `python svm.py` and the results will be printed in the console.
- Naive Bayes: Run command `python naive_bayes.py` and the results will be printed in the console.

