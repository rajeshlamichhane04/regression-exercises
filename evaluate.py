#imports 
#data manioulation
import pandas as pd
import numpy as np

#sklearn metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#def function to do all the maths for me
def regression_errors(y,yhat):
    MSE = mean_squared_error(y,yhat)
    #print("MSE:", MSE) 
    RMSE = mean_squared_error(y,yhat,squared = False)
    #print("RMSE:", RMSE)
    SSE = MSE * len(y)
    #print("SSE:", SSE)
    ESS = sum((yhat - y.mean())**2)
    #print("ESS:",ESS)
    TSS = ESS + SSE
    #print("TSS:",TSS)
    
    return MSE,RMSE,SSE,ESS,TSS


def baseline_mean_errors(y):
    #repeat the mean of baseline upto the lenght of dataframe
    baseline = np.repeat(y.mean(),len(y))
    MSE_baseline = mean_squared_error(y, baseline)
    SSE_baseline= MSE_baseline * len(y)
    RMSE_baseline = MSE_baseline**.5
    
    return SSE_baseline, MSE_baseline, RMSE_baseline


def better_than_baseline(y, yhat):
    #get values of our metrics from function above
    MSE,RMSE,SSE,ESS,TSS = regression_errors(y, yhat)
    #get values of our metrics from function above
    SSE_baseline, MSE_baseline, RMSE_baseline = baseline_mean_errors(y)
    if SSE < SSE_baseline:
        print('model performs better than baseline')
    else:
        print('model performs worse than baseline')