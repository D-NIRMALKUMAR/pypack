from sklearn.dataset import load_iris
import pandas as pd 
import csv
iris=load_iris()
myvar=pd.Series(iris)
print(myvar)
# name of csv file
