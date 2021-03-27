# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:31:57 2020

@author: karin
"""


''' Import libraries'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#sklearn
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

from sklearn.feature_selection import mutual_info_regression

#kfold
from sklearn.model_selection import KFold,RepeatedKFold
from sklearn.ensemble import IsolationForest


#tensorflor
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers,initializers,activations,regularizers
from keras.layers import LeakyReLU,Dense, Dropout, Flatten
from keras.layers import Layer
from keras.models import Sequential
from keras.constraints import maxnorm
from keras.optimizers import adam






class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')



class MyFunctions():
    
        
    def to_1D(self,lista):
        return pd.Series([x for _list in lista for x in _list])
    
    def boolean_df(self,item_lists, unique_items):
        # Create empty dict
        bool_dict = {}
    
        # Loop through all the tags
        for i, item in enumerate(unique_items):
            
            # Apply boolean mask
            bool_dict[item] = item_lists.apply(lambda x: item in x)
                
        # Return the results as a dataframe
        return pd.DataFrame(bool_dict)
    


'''
 * Class CreateModel ()
 
 Classe for create ANN model
 Build Model 
''' 

class CreateModel():
    
    def __init__(self, n_inputs,EPOCHS,early_stop):
        self.n_inputs = n_inputs
        self.EPOCHS=EPOCHS
        self.early_stop=early_stop
        self.rsme=0.0
        self.sucess=0
        self.model=0
       

    
    def build_model(self):
        model= Sequential()
        
        model.add(Dense(150,kernel_initializer='he_normal',\
        kernel_constraint=maxnorm(8),input_shape=(self.n_inputs,),activation='tanh',\
           kernel_regularizer=regularizers.l1_l2(l1=0, l2=1e-7),))
            
        model.add(Dropout(rate=0.4))
        

        
        model.add(Dense(1,activation='linear',kernel_initializer='normal'))
            
         
        optimizer=adam(lr=0.002,decay=1e-08)      
      
            
        model.compile(loss='mse',optimizer=optimizer,metrics=['mse'])
        
        return model



class Plots():
    
    
    def __init__(self, history,labels,predictions):
        self.history=history
        self.labels=labels
        self.predictions=predictions
    
    def plot_history(self):
        hist = pd.DataFrame(self.history.history)
        hist['epoch'] = self.history.epoch
        plt.figure()
        plt.xlabel('Época')
        plt.ylabel('REMQ')
        plt.plot(hist['epoch'], hist['mse'],
               label='Erro Treino')
        plt.plot(hist['epoch'], hist['val_mse'],
               label = 'Val Erro')
        plt.ylim([0,20])
        plt.legend()
        plt.show()
      


    def plot_compare(self):
        dt = 1
        t = np.arange(0, len(self.labels), dt)

        fig = plt.figure(figsize=(25,20),dpi=200)
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(t, self.labels, '--x',label='real')
        ax.plot(t, self.predictions, 'o',label='predição',color='red')
 
        plt.xlabel('amostras',fontsize=30)
        plt.ylabel('preço',fontsize=30)
        plt.legend(loc='lower right',fontsize=20)
        plt.show()



 