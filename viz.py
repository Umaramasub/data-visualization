import os
import pandas as pd
import matplotlib.pyplot as plt

def readCSV(filepath):
    """filepath is provided as a string representing the path to the CSV
    file. The function will open this file, read in the contents, close the
    file, and then return the contents as a dataframe
    :param filepath:string as the absolute path to the file
    :return dataframe
    """

    # Normalize the file path to work on any system
    norm_filepath = os.path.normpath(filepath)

    # Open the file for reading
    file = open(norm_filepath, 'r')

    # Generate a data frame from the text and skip the first row as it is header
    data = pd.read_csv(norm_filepath, delimiter=',', header=0)
    file.close()
    return data


def plot(data):
    """data is a data frame containing the the data
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
    x2 = df4['ctm1']
    y2 = df4['ctm2']

    # Age and Length of stay for patients with CHF
    df5 = df2[df2['class'] == 1]
    x3 = df5['age']
    y3 = df5['length-of-stay']

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

    # Plot CTM1 and CTM2 for all patients

    # Add this sub plot to the third position
    ax3 = fig.add_subplot(233)

    # Add markers and legends to the plot
    ax3.scatter(x1, y1, color='r', marker='^', label='w/CHF')
    ax3.scatter(x2, y2, color='b', marker='x', label='w/o CHF')
    ax3.set_xlim([-2, 2])
    ax3.set_ylim([-2, 2])
    plt.title('All patients/CTM')
    plt.xlabel('CTM1')
    plt.ylabel('CTM2')

    # Add position to the legend
    plt.legend(loc='lower left')

    # Plot CTM1 Versus CTM2 for patients without CHF
    # Add this sub plot to the fourth position
    ax4 = fig.add_subplot(234)
    ax4.scatter(x2, y2)
    plt.title('Patients w/o CHF')
    plt.xlabel('CTM1')
    plt.ylabel('CTM2')

    # Plot age and length of stay for patients without CHF
    # Add this sub plot to the fifth position
    ax5 = fig.add_subplot(235)
    ax5.scatter(x4, y4)
    plt.title('Patients w/o CHF')
    plt.xlabel('Age')
    plt.ylabel('LOS')

    # Plot age and length of stay for all patients
    # Add this sub plot to the sixth position
    ax6 = fig.add_subplot(236)
    ax6.scatter(x3, y3, color='r', marker='x', label='w/CHF')
    ax6.scatter(x4, y4, color='b', marker='^', label='w/o CHF')
    ax6.set_xlim([-10, 80])
    ax6.set_ylim([-50, 400])
    plt.title('All patients / Age/LOS')
    plt.xlabel('Age')
    plt.ylabel('LOS')
    plt.legend(loc='lower left')


def readCSV_ecg(filepath):
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

    # Generate a data frame from the text and add column names
    data = pd.read_csv(norm_filepath, delimiter=',', header=None, na_values='?', names=[
        'survival', 'still-alive', 'age-at-heart-attack', 'pericardial effusion',
        'fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'mult', 'name', 'group',
        'alive-at-1'])
    file.close()
    return data


def ecg_plot(data):
    fig = plt.figure()

    # Box plot giving the age of heart attack with survival
    ax1 = fig.add_subplot(231)

    # Create subset of the data selecting the required columns
    df1 = data.loc[:, ['age-at-heart-attack', 'still-alive']]

    #  Get box plot for patients alive at end of one year
    alive_df1 = df1[df1['still-alive'] == 1]

    # Remove nas from the data set as box plot does not work with missing variables
    x1 = alive_df1['age-at-heart-attack'].dropna()

    #  Get box plot for patients who are dead at end of one year
    dead_df1 = df1[df1['still-alive'] == 0]
    x2 = dead_df1['age-at-heart-attack'].dropna()

    # Form a list of the points to be plotted
    data_AHA = [x1, x2]

    ax1.boxplot(data_AHA, labels=["Alive", 'Dead'])
    ax1.set_title("Comparison of age of heart attack with survival")
    ax1.set_xlabel('Status')
    ax1.set_ylabel('Age of heart attack')

    # Bar plots comparing the contractile features of heart with survival
    ax2 = fig.add_subplot(232)
    df2 = data.loc[:, ['fractional-shortening', 'epss', 'wall-motion-index', 'lvdd', 'still-alive']]
    # Form a subdata set with features for patients who are alive at end of one year
    alive_df2 = df2[df2['still-alive'] == 1]

    # Get the mean of all the features for patients who are alive to compare

    # Normalize the data to enable comparison

    a_mean1 = (alive_df2['fractional-shortening'] / max(data['fractional-shortening'])).mean()
    a_mean2 = (alive_df2['epss'] / max(data['epss'])).mean()
    a_mean3 = (alive_df2['wall-motion-index'] / max(data['wall-motion-index'])).mean()
    a_mean4 = (alive_df2['lvdd'] / max(data['lvdd'])).mean()

    data_alive = [a_mean1, a_mean2, a_mean3, a_mean4]

    # Get the mean  of all the features for patients who are dead to compare
    dead_df2 = df2[df2['still-alive'] == 0]

    d_mean1 = (dead_df2['fractional-shortening'] / max(data['fractional-shortening'])).mean()
    d_mean2 = (dead_df2['epss'] / max(data['epss'])).mean()
    d_mean3 = (dead_df2['wall-motion-index'] / max(data['wall-motion-index'])).mean()
    d_mean4 = (dead_df2['lvdd'] / max(data['lvdd'])).mean()

    data_dead = [d_mean1, d_mean2, d_mean3, d_mean4]

    # Add the position of the left side of bar along with colors

    p1 = ax2.bar([2, 5, 8, 11], data_alive, color='b')
    p2 = ax2.bar([1, 4, 7, 10], data_dead, color='r')

    plt.ylabel('Value')
    plt.title('Contractile factors affecting mortality')
    plt.xticks([2, 5, 8, 11], ('Fract_short', 'EPSS', 'WMI', 'LVDD'))
    plt.legend((p1[0], p2[0]), ('Dead', 'Alive'),loc ='upper left')

    # Comparison of Scatter plot of age of heart attack with EPSS with patients

    ax3 = fig.add_subplot(233)
    df3 = data.loc[:, ['age-at-heart-attack', 'epss', 'still-alive']]
    alive_df3 = df3[df3['still-alive'] == 1]
    alive_x1 = alive_df3['age-at-heart-attack']
    alive_y1 = alive_df3['epss']

    dead_df3 = df3[df1['still-alive'] == 0]
    dead_x1 = dead_df3['age-at-heart-attack']
    dead_y1 = dead_df3['epss']

    ax3.scatter(alive_x1, alive_y1, color='b', marker='^', label='Alive')
    ax3.scatter(dead_x1, dead_y1, color='r', marker='x', label='Dead')

    plt.title('All patients with heart attack')
    plt.xlabel('Age-at-heart-attack')
    plt.ylabel('EPSS')
    plt.legend(loc='upper right')

    # Comparison of scatter plot of wall motion index and age of heart attack
    ax4 = fig.add_subplot(234)

    df4 = data.loc[:, ['age-at-heart-attack', 'wall-motion-index', 'still-alive']]
    alive_df4 = df4[df4['still-alive'] == 1]
    alive_x1 = alive_df4['age-at-heart-attack']
    alive_y1 = alive_df4['wall-motion-index']

    dead_df4 = df4[df4['still-alive'] == 0]
    dead_x1 = dead_df4['age-at-heart-attack']
    dead_y1 = dead_df4['wall-motion-index']

    ax4.scatter(alive_x1, alive_y1, color='b', marker='^', label='Alive')
    ax4.scatter(dead_x1, dead_y1, color='r', marker='x', label='Dead')

    plt.title('All patients with heart attack')
    plt.xlabel('age-at-heart-attack')
    plt.ylabel('wall-motion-index')
    plt.legend(loc='upper right')

    # Presence of cardiac effusion affecting age of heart attack

    ax5 = fig.add_subplot(235)

    # Create subset of the data selecting the required columns
    df5 = data.loc[:, ['age-at-heart-attack', 'pericardial effusion']]

    #  Get box plot for patients with pericardial effusion
    peri_eff = df5[df5['pericardial effusion'] == 1]

    # Remove nas from the data set as box plot does not work with missing varaibles
    x1 = peri_eff['age-at-heart-attack'].dropna()

    #  Get box plot for patients dead at end of one year
    no_peri_eff = df5[df5['pericardial effusion'] == 0]
    x2 = no_peri_eff['age-at-heart-attack'].dropna()

    # Form a list of the points to be plotted
    data_plot = [x1, x2]

    ax5.boxplot(data_plot, labels=["w/effusion", 'w/o effusion'])
    ax5.set_title("Comparison of age of heart attack with pericardial effusion")
    ax5.set_xlabel('Status of effusion')
    ax5.set_ylabel('Age of heart attack')

    # Presence of pericardial effusion affecting contractility of heart

    ax6 = fig.add_subplot(236)

    df6 = data.loc[:, ['lvdd', 'epss', 'pericardial effusion']]
    peri_eff = df6[df6['pericardial effusion'] == 1]
    pe_x1 = peri_eff['lvdd']
    pe_y1 = peri_eff['epss']

    no_pe_eff = df6[df6['pericardial effusion'] == 0]
    no_pe_x1 = no_pe_eff['lvdd']
    no_pe_y1 = no_pe_eff['epss']

    ax6.scatter(no_pe_x1, no_pe_y1, color='b', marker='^', label='w/pericardial effusion')
    ax6.scatter(pe_x1, pe_y1, color='r', marker='x', label='w/o pericardial effusion')

    plt.title('All patients with pericardial effusion')
    plt.xlabel('LVDD')
    plt.ylabel('EPSS')
    plt.legend(loc='upper left')
    ax6.set_xlim([2, 8])
    ax6.set_ylim([0, 40])


if __name__ == '__main__':
    data = readCSV("data.csv")
    plot(data)
    plt.show()

    data_ecg = readCSV_ecg("data2.csv")
    ecg_plot(data_ecg)
    plt.show()


