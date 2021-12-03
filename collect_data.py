import librosa as lb
import librosa.display
from glob import glob
import os 
import numpy as np
import pandas as pd
import csv

def create_csv(path, file_name):
    '''
    This function with create the csv file with all the audio file path and machine type
    Parameters:
        path : path for location where the all audio file present
        file_name : name of the csv file in which you want to save data
    '''
    header = ['filename', 'class']

    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for name in glob(path, recursive=True):
            data = []
            arr = name.split('/')
            print(arr)
            data.append(name)
            data.append(arr[-4]+"_"+arr[-2])
            writer.writerow(data)

            
def mfcc_array(i:int,data:object)->object:
    '''
    This function will help to get audio file feature and return it
    Parameters:
        i : file index
        data : audio data to calculate feature
    '''
    filename = files['filename'][i]
    librosa_load = lb.load(str(filename),sr=None)
    audio, sample_rate = librosa_load
    mfcc = lb.feature.mfcc(audio,sr=sample_rate,n_mfcc=1)
    mfcc = mfcc.flatten()
    if len(data) ==0:
        data = mfcc
    else:
        data = np.vstack((data,mfcc))
    
    return data


def get_target():
    '''This function will return the target'''
    lst = []
    for i in files.index:
        lst.append(files['class'][i])
    y =np.array(lst)
    y = np.reshape(y,(files.index.stop,-1))
    return y

#hstacking the features and the targets
def fuse_target_mfcc(data:object,y:object)->object:
    '''This function will combine the feature and target'''
    data = np.hstack((data, y))
    return data

#looping through csv file to calculate the mfcc from every file
def manageMfcc()->object:
    '''This function will get the feature for all the file list in csv'''
    lst=[]
    data =np.array(lst)
    for i in files.index:
        data = mfcc_array(i,data)
          
    return data


# Create Dataset to create model
create_csv('data/**/id_00/*/*.wav', 'file_list.csv')
files = pd.read_csv('file_list.csv')
data = fuse_target_mfcc(manageMfcc(),get_target())
df = pd.DataFrame(data)

df.to_csv("audio_dataset.csv", header=None, index=False)

# Create Dataset for model validation
create_csv('data/validation/*/*.wav', 'validation_file_list.csv')
files = pd.read_csv('validation_file_list.csv')
data = fuse_target_mfcc(manageMfcc(),get_target())
df = pd.DataFrame(data)

df.to_csv("validation_dataset.csv", header=None, index=False)

