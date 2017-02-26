import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


def readCSV(filepath):
    """filepath is provided as a string representing an absolute path to the CSV
    file. The function will open this file, read in the contents, close the
    file, and then return the contents as a dataframe
    :param filepath:string as the absolute path to the file
    :return dataframe
    """
    # Normalize the file path to work on any system
    norm_filepath = os.path.normpath(filepath)

    # Open the file for reading
    file = open(norm_filepath, 'r')

    # Generate a rec array from the text and skip the first column
    data = pd.read_csv(norm_filepath, delimiter=',', header=0)
    file.close()
    return data


def plot(data):
    """data is a data frame containing the all the data
    :param data frame
    :return a figure with 6 subplots of 3 columns and 2 rows
    """
    fig = plt.figure()
    df1 = data.loc[:, ['ctm1', 'ctm2', 'class']]
    df2 = data.loc[:, ['age', 'length-of-stay', 'class']]

    ## ctm1 and ctm2 for chf patients
    df3 = df1[df1['class'] == 1]
    x1 = df1['ctm1']
    y1 = df1['ctm2']
    ax1 = fig.add_subplot(231)
    ax1.scatter(x1, y1)
    plt.title("Patients w/ CHF")
    plt.xlabel("CTM1")
    plt.ylabel('CTM2')


    ## age and los for chf patients
    df4 = df2[df2['class'] == 1]

    x2 = df4['age']
    y2 = df4['length-of-stay']
    ax2 = fig.add_subplot(232)
    ax2.scatter(x2, y2)
    plt.title("Patients w/ CHF")
    plt.xlabel("Age")
    plt.ylabel('LOS')


    # ctm 1 and ctm2 for all patients

    x3 = df1['ctm1']
    y3 = df1['ctm2']

    ax3 = fig.add_subplot(233)
    ax3.scatter(x3, y3)
    plt.title("All patients / CTM")
    plt.xlabel("CTM1")
    plt.ylabel('CTM2')

    ## Ctm1 and ctm2 for non chf patients
    df5 = df1[df1['class'] == 0]
    x4 = df5['ctm1']
    y4 = df5['ctm2']
    ax4 = fig.add_subplot(234)
    ax4.scatter(x4, y4)
    plt.title("Patients w/o CHF")
    plt.xlabel("CTM1")
    plt.ylabel('CTM2')


    ## age and los for non chf patients
    df6 = df2[df2['class'] == 0]
    x5 = df6['age']
    y5 = df6['length-of-stay']
    ax5 = fig.add_subplot(235)
    ax5.scatter(x5, y5)
    plt.title("Patients w/o CHF")
    plt.xlabel("age")
    plt.ylabel('LOS')

    ## age and los for all patients

    x6 = df2['age']
    y6 = df2['length-of-stay']
    ax6 = fig.add_subplot(236)
    ax6.scatter(x6, y6)
    plt.title("All patients / Age/LOS")
    plt.xlabel("Age")
    plt.ylabel('LOS')




if __name__ == '__main__':
    data = readCSV("data.csv")
    plot(data)
    plt.show()
