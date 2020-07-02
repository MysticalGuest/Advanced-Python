import pandas as pd

iris = pd.read_csv("iris.data", header=None)
iris.columns=['a','b','c','d','e']
iris