import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from os import listdir, makedirs, system
from os.path import exists


def DataLoader(path):
    data = []
    title = []
    artist = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            list = []
            for i in range(len(row)-2):
                list.append(float(row[i]))
            data.append(list)
            title.append(row[15])
            artist.append(row[16])
    data = np.array(data)
    return header, data, title, artist

def Normalize(data):
    for i in range(data.shape[1]-1):
        x = data[:,i+1]
        min = x.min()
        max = x.max()
        data[:,i+1] = (x - min)/(max-min)

def Get_Heatmap(data, header, file_name):
    dir_name = './output/'
    if not exists(dir_name):
        makedirs(dir_name)
    h_map = np.corrcoef(data[:,1:-1].T)
    df = pd.DataFrame(data=h_map, index=header[1:-3], columns=header[1:-3])

    plt.figure(figsize=(15,15),dpi=200)
    sns.heatmap(df,square=True, cmap='hot',vmax=1, vmin=-1, center=0, annot=True)
    plt.savefig(dir_name + file_name)
    plt.close('all')

def Classify(data):
    like = []
    dislike = []
    for i in range(data.shape[0]):
        if data[i,14]==1:
            like.append(data[i,:])
        else:
            dislike.append(data[i,:])
    like = np.array(like)
    dislike = np.array(dislike)
    return like, dislike

def Get_Histogram(like, dislike,header, file_name):
    dir_name = './output/'
    if not exists(dir_name):
        makedirs(dir_name)
    value_l = like[:,1:-1].T
    value_d = dislike[:,1:-1].T
    plt.figure(figsize=(20,10),dpi=200)
    for i in range(value_l.shape[0]):
        plt.subplot(3,5,i+1)
        plt.hist([value_l[i,:],value_d[i,:]], rwidth=0.9,label=['like', 'dislike'])
        plt.title(header[i+1])
        plt.legend(loc='upper right')
    plt.savefig(dir_name + file_name)
    plt.close('all')

if __name__ == '__main__':
    path = "./data/Spotify.csv"
    header, data, title, artist = DataLoader(path)
    Normalize(data)
    like, dislike = Classify(data)
    Get_Histogram(like, dislike, header,file_name='histogram.png' )
    Get_Heatmap(data, header, file_name='heatmap.png')
    Get_Heatmap(like, header, file_name='like_heatmap.png')
    Get_Heatmap(dislike, header, file_name='dislike_heatmap.png')