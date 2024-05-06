import pandas as pd
from matplotlib import pyplot as plt
import os

all_views = os.listdir('./views')
for view in all_views:
    names = view.split('-')
    xlabel = names[0]
    agg = names[2][:-4]
    ylabel = names[1] + '('+ agg +')'
    data = pd.read_csv('./views/'+view)
    plt.bar(data[xlabel], data[agg])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('./figures/'+view[:-4])