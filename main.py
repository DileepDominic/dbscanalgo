# Start from importing necessary packages.
import warnings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd


from IPython.display import display
from sklearn import metrics # for evaluations
from sklearn.datasets import make_blobs, make_circles # for generating experimental data
from sklearn.preprocessing import StandardScaler # for feature scaling
from sklearn.cluster import KMeans 
from sklearn.cluster import DBSCAN

from pylab import rcParams
import seaborn as sb

from collections import Counter

# make matplotlib plot inline (Only in Ipython).
warnings.filterwarnings('ignore')
%matplotlib inline

df = pd.read_excel(r"C:\Users\dominic\code\inputhouse\galaxy.xlsx")
df.columns=['x-axis','y-axis']

model = DBSCAN(eps=0.8,min_samples=10)
model.fit(df)

data=df.iloc[:,0:2].values
outlier_df = pd.DataFrame(data)

print(Counter(model.labels_))

print(outlier_df[model.labels_ == -1])

