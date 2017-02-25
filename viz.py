import os
import pandas as pd

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
