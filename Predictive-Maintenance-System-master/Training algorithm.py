#install numpy, scipy, scikit to workspace

import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#imports we will use

import sklearn;
import numpy;
from sklearn import svm;
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score
#imports we probably won't use

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis;
from sklearn import preprocessing



#need to use data split


#unable to find .csv path issue probably
#test1 = open('dataSpeed1.csv',"rb")
#reader1 = csv.reader(test1)



#test array 1 represent the training data, sample
X = np.array([[0], [1], [2], [3],[4],[5],[6],[8],[9]]);
#target values, sample
y = np.array([1,1,0,0,1,0,0,1,1]);

#test valdation set, not used yet, might not be needed
v= np.array([[2,1],[3,0],[5,1],[6,1],[9,0],[5,1],[4,0]]);
xtrain,xtest,ytrain,ytest= train_test_split(X,y,test_size=0.33, random_state=42)
#classifier initilized
clf = KNeighborsClassifier(n_neighbors=3);

#weighted score, tracks accuracy
dscore =[.7,[9]];

#fits sample data sets to classifier, trains classifier
neighbor = clf.fit(X, y);

def train(xtrain,ytrain):
    return

#sample prediction, results not always as predicated
prediction = clf.predict([[0.5],[2.5],[3.3]]);
print(prediction)
print(ytest)
prediction=prediction.reshape(-1,1)
print(prediction)
ytest=ytest.reshape(-1,1)
print(ytest)
#Shows probability of 0 and 1.  Not sure why it does not seem accurate
print(clf.predict_proba([[0.9]]))

#not working scoring
score= clf.score(ytest, prediction)
print(score)


#serialize object, not sure what needs to be added or how to use it
#clf.pickle



#####################
#Mike's section
#length 589223
whole_data_set = np.genfromtxt('/Users/MM/Downloads/data.txt', delimiter='\t') #File path for file you'd like to import
#max_abs_scaler = preprocessing.MaxAbsScaler() #normalizes data
#whole_data_set = max_abs_scaler.fit_transform(whole_data_set)

print(whole_data_set.size/30)

import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

#print(np.random.randn(500))
x = whole_data_set[:,0]
#values = [go.Histogram(x=x)]
#py.iplot(values, filename='test')

plt.hist(x)
plt.title("Column 1")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()

plot_url = py.plot_mpl(fig, filename='testing&432')

for column in range(0,30):
    #column = 1
    temp = whole_data_set[0][column]
    temp_min = whole_data_set[0][column]

    for x in range(1,589223):
        current = whole_data_set[x][column]
        if(current> temp):
            temp = current
        if(current< temp_min):
            temp_min = current
        #print(whole_data_set[x][1])

    print('Max:',temp)
    print('Min: ',temp_min)
    #print(avg/(whole_data_set.size/30))
    print('SD: ',np.std(whole_data_set[:,column]))
    print('Var: ',np.var(whole_data_set[:,column]))
    print('Avg: ',np.mean(whole_data_set[:,column]))

trainingData_first_half = whole_data_set[:117844] #getting the first 20% of the data set
trainingData_second_half = whole_data_set[589223-117844:589223] #getting the last 20% of the data set

tags = []
for i in range(0, 117844): #making the first half of the tagging array which will all be initilzed to '0'
    tags.append(0)
for i in range(0, 117844): #making the rest of the tagging array which will all be '1'
    tags.append(1)

data = numpy.concatenate((trainingData_first_half, trainingData_second_half), axis = 0) #concates the first 20% and last 20% of dataset

classy = KNeighborsClassifier(n_neighbors=1);
classy = classy.fit(data, tags)

#for x in range(200000,205000):
#    print(classy.predict([whole_data_set[x]]))

