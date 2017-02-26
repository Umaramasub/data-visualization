import os
import pandas as pd
import matplotlib.pyplot as plt


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

    # Create sub data frames using relevant columns
    df1 = data.loc[:, ['ctm1', 'ctm2', 'class']]
    df2 = data.loc[:, ['age', 'length-of-stay', 'class']]

    # Get CTM 1 and CTM2 for patients with CHF
    df3 = df1[df1['class'] == 1]
    x1 = df3['ctm1']
    y1 = df3['ctm2']

    # Get CTM 1 and CTM2 for patients without CHF
    df4 = df1[df1['class'] == 0]
    x2= df4['ctm1']
    y2= df4['ctm2']

    # Age and Length of stay for CHF patients
    df5 = df2[df2['class'] == 1]
    x3= df5['age']
    y3=df5['length-of-stay']

    # Age and Length of stay for patients without CHF
    df6 = df2[df2['class'] == 0]
    x4 = df6['age']
    y4 = df6['length-of-stay']


    # Create a 2 by 3 plot and add the plot of the first position
    ax1 = fig.add_subplot(231)

    # Plot CTM1 by CTM2 for patients with CHF
    ax1.scatter(x1, y1)

    # Give title and label to the plot
    plt.title('Patients w/ CHF')
    plt.xlabel('CTM1')
    plt.ylabel('CTM2')

    # Plot age and LOS for CHF patients

    # Add this sub plot to the second position
    ax2 = fig.add_subplot(232)
    ax2.scatter(x3, y3)

    # Set limits for X and Y axis to help with comparison
    ax2.set_xlim([-10, 80])
    ax2.set_ylim([-50, 400])

    # Add titles and labels to the graph
    plt.title('Patients w/ CHF')
    plt.xlabel('Age')
    plt.ylabel('LOS')

    # CTM1 and CTM2 for all patients

    ax3 = fig.add_subplot(233)

    # Add markers and legends to the plot
    ax3.scatter(x1, y1, color='r', marker='^', label='w/CHF')
    ax3.scatter(x2, y2, color='b', marker='x', label='w/o CHF')
    ax3.set_xlim([-2, 2])
    ax3.set_ylim([-2, 2])
    plt.title('All patients/CTM')
    plt.xlabel('CTM1')
    plt.ylabel('CTM2')

    # Add the position of the legend
    plt.legend(loc='lower left')


    # Plot CTM1 Versus CTM2 for patients without CHF
    ax4 = fig.add_subplot(234)
    ax4.scatter(x2, y2)
    plt.title('Patients w/o CHF')
    plt.xlabel('CTM1')
    plt.ylabel('CTM2')

    # Plot age and length of stay for patients without CHF

    ax5 = fig.add_subplot(235)
    ax5.scatter(x4, y4)
    plt.title('Patients w/o CHF')
    plt.xlabel('Age')
    plt.ylabel('LOS')

    # age and los for all patients
    ax6 = fig.add_subplot(236)
    ax6.scatter(x3, y3, color='b', marker='x', label='w/CHF')
    ax6.scatter(x4, y4, color='r', marker='^', label='w/o CHF')
    ax6.set_xlim([-10, 80])
    ax6.set_ylim([-50, 400])
    plt.title('All patients / Age/LOS')
    plt.xlabel('Age')
    plt.ylabel('LOS')
    plt.legend(loc='lower left')


if __name__ == '__main__':
    data = readCSV("data.csv")
    plot(data)
    plt.show()
