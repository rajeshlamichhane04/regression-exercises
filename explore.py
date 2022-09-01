import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_variable_pairs(df):
#function takes in df of random sample of 10000 and gives out pairplot
    sns.pairplot(data=df.sample(10000), kind='reg', diag_kind='kde', corner = True, plot_kws={'line_kws':{'color':'red'}})    

def plot_categorical_and_continous(cat_var,con_var,train):
    plt.figure(figsize= (20,10))
    plt.subplot(131)
    sns.boxplot(x = cat_var, y = con_var, data = train.sample(10000))
    plt.subplot(132)
    sns.swarmplot(x = cat_var, y = con_var, data = train.sample(10000))
    plt.subplot(133)
    sns.barplot(x = cat_var, y = con_var, data = train.sample(10000))
    plt.figure()