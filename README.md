# Machine conditions monitoring

## Description

Creating a machine learning model that's able to monitor the operations and identify anomalies in sound patterns. The dataset is [Machine Condition Monitoring](https://zenodo.org/record/3384388#.YFIrNXnvJEY).

We were able to classify normal and abnormal sounds through one particular soundfeature called Mel-frequency cepstrum.

## Installation

Python 3 should be install in you system.
To install python you can follow the link [Install Python](https://realpython.com/installing-python/#how-to-install-python-on-macos)
You can find the libraries that are required in `requirements.txt`

## Usage
[machine_monitoring.ipynb](machine_monitoring.ipynb)


## Repo Architecture
```
machine-conditions-monitoring
│
│   README.md                   :explains the project
│   abnormal_audio_file.ipynb   :this notebook contains the observation on abnormal audio file
│   audio_dataset.csv           :it contains dataset for creating the model 
│   collect_data.py             :this file will create dataset with audio file for training and testing model 
│   file_list.csv               :this will contain the list of all the normal audio file path and machine type 
│   machine_monitoring.ipynb    :this file will create model and validate it with validation data
│   model.pkl                   :this is model which you can load for machine monitoring
│   normal_audio_file.ipynb     :this notebook contains the observation on normal audio file
│   validation_dataset.csv      :it contains dataset for validating the model
│   validation_file_list.csv    :this will contain the list of all the abnormal audio file path and machine type
│   requirements.txt            :contains list of python libraries required to run the project
```
## Contributors 

This project is a cooperation of the following team:

- [Reena](https://github.com/reenakoshta10)
- [Sebastian](https://github.com/sebastianchavezz)      

## Timeline 

December 2021.
We had about 1 week for this challenge. We began our journey by understanding the challenge, what a sound was made of and the important features of sound. Then we made a script that organized the data. After that we modeled the data. 
