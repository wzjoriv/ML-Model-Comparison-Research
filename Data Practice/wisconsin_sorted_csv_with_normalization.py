#!/usr/bin/env python
# coding: utf-8

# In[14]:


#import os
import numpy as np
import pandas as pd
#base_path = r"C:\Users\jacob\Downloads\wisconsin"
#filename = "data.data"
#path_to_file = os.path.join(base_path, filename)


# In[15]:


df = pd.read_csv('data.csv', delimiter = ',')
#delete whitespace surrounding column names
df.columns = df.columns.str.replace(' ', '')
#delete rows with missing bland chromatin
df = df[df.Bare_Nuclei != '?']


# In[16]:


df
x = df.values
y = []
#create y using labels
x = list(x)
for row in x:
    row = list(row)
    y.append(row.pop())
x = np.array(x)

#delete label from x
x=x[:,:-1]
#delete id from x
x = x[:,1:]
print(x)
y = np.array(y)
print(y)
#notice we are not including id nor classification
feature_names = ['Clump_Thickness', 'Uniformity_of_Cell_Size', 'Uniformity_of_Cell_Shape', 'Marginal_Adhesion', 
'Single_Epithelial_Cell_Size', 'Bare_Nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses']


# In[17]:


print(x.shape)
print(y.shape)


# In[18]:


from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)


# In[19]:


print(xTrain.shape)
print(xTest.shape)
print(yTrain.shape)
print(yTest.shape)


# In[20]:


dfnew = df.drop(columns=['id'])


# In[21]:


#normalize the classes to be 0 for benign and 1 for malignant
dfnew['Class'] = (dfnew['Class'] > 3).astype(int)


# In[22]:


#normalize all the data from 0 - 1
#'Clump_Thickness', 'Uniformity_of_Cell_Size', 'Uniformity_of_Cell_Shape', 'Marginal_Adhesion', 
#'Single_Epithelial_Cell_Size', 'Bare_Nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses'
dfnew.Clump_Thickness = dfnew.Clump_Thickness.astype(float)
dfnew['Clump_Thickness'] = dfnew['Clump_Thickness'] / dfnew['Clump_Thickness'].max()

dfnew.Uniformity_of_Cell_Size = dfnew.Uniformity_of_Cell_Size.astype(float)
dfnew['Uniformity_of_Cell_Size'] = dfnew['Uniformity_of_Cell_Size'] / dfnew['Uniformity_of_Cell_Size'].max()

dfnew.Marginal_Adhesion = dfnew.Marginal_Adhesion.astype(float)
dfnew['Marginal_Adhesion'] = dfnew['Marginal_Adhesion'] / dfnew['Marginal_Adhesion'].max()

dfnew.Single_Epithelial_Cell_Size = dfnew.Single_Epithelial_Cell_Size.astype(float)
dfnew['Single_Epithelial_Cell_Size'] = dfnew['Single_Epithelial_Cell_Size'] / dfnew['Single_Epithelial_Cell_Size'].max()

dfnew.Bare_Nuclei = dfnew.Bare_Nuclei.astype(float)
dfnew['Bare_Nuclei'] = dfnew['Bare_Nuclei'] / dfnew['Bare_Nuclei'].max()

dfnew.Bland_Chromatin = dfnew.Bland_Chromatin.astype(float)
dfnew['Bland_Chromatin'] = dfnew['Bland_Chromatin'] / dfnew['Bland_Chromatin'].max()

dfnew.Normal_Nucleoli = dfnew.Normal_Nucleoli.astype(float)
dfnew['Normal_Nucleoli'] = dfnew['Normal_Nucleoli'] / dfnew['Normal_Nucleoli'].max()

dfnew.Mitoses = dfnew.Mitoses.astype(float)
dfnew['Mitoses'] = dfnew['Mitoses'] / dfnew['Mitoses'].max()
dfnew


# In[23]:


dfnew.to_csv(r'C:\Users\jacob\OneDrive\Documents\deeplearning\ML-Model-Comparison-Research\Data Practice\data_edited.csv')


# In[24]:


import seaborn as sns 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dfnew = dfnew.drop(columns=['Class'])
# generating correlation heatmap 
sns.heatmap(dfnew.corr(), annot = True) 
  
# posting correlation heatmap to output console  
plt.show() 


# In[ ]:





# In[ ]:




