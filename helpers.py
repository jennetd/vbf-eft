import warnings
import numpy as np
import numba
import matplotlib.pyplot as plt
import pandas as pd
import json

def weight_names(reweight_card):

    with open('dictionary.json') as f:
        d = json.load(f)
    
    array = []
    weight_index = 0
    
    with open(reweight_card, "r+") as file1:
        for line in file1.readlines():
            
            if 'launch' in line:
                weight_index += 1
                continue
                
            if 'rwgt' in line:
                continue
                
            array += [[weight_index]+line.split()[1:]]
            
    df = pd.DataFrame(array,columns=['weight_index','model','param_index','value'])
    df['value'] = df['value'].astype('float')
    df = df[df['value']>0]
    
    param_name = []
    for index, row in df.iterrows():
        param_name += [d[row['model']][row['param_index']]]
    
    df['param_name'] = param_name

    
    df['weight_name'] = df['param_name']+"="+df['value'].astype('string')
    
    names = []
    for i in np.unique(df['weight_index']):
        name = ""
        for n in df[df['weight_index']==i]["weight_name"]:
            if len(name)>0:
                name += ","
            name += n
        names += [name]

    return names

def param_names(reweight_card):
    df = pd.read_csv(reweight_card,sep=' ',skiprows=2,header=None)
    print(df)

def plot_variations(var, var_allw, w, w_rw, w_sm, wc, bins, name, plot_all=False):
    
    fig, (ax1, ax2) = plt.subplots(2,1)
    fig.subplots_adjust(hspace=0)
    fig.suptitle(wc+'=1.0')
    
    h_var    = ax1.hist(var,weights=w,histtype='step', 
                        bins=bins,density=True,label='Direct sim')
    h_var_rw = ax1.hist(var_allw,weights=w_rw,histtype='step', 
                        bins=bins,density=True,label='Reweighted')
    h_var_sm = ax1.hist(var_allw,weights=w_sm,histtype='step', 
                        bins=bins,color='black',density=True,label='SM')
    
    ax1.set_yscale('log')
    ax1.set_ylabel('AU')
    #ax1.set_xlabel(name)

    ax1.legend(frameon=False,bbox_to_anchor=(1.05,0.9))
    
    ax2.hist(bins[:-1],weights=h_var_sm[0]/h_var_sm[0],histtype='step',color='black')
    ax2.hist(bins[:-1],weights=h_var[0]/h_var_sm[0],histtype='step')
    ax2.hist(bins[:-1],weights=h_var_rw[0]/h_var_sm[0],histtype='step')
    ax2.set_ylabel('Ratio to SM')
    ax2.set_xlabel(name)
