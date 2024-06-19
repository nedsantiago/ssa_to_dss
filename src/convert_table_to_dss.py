import file_dialog
import pandas as pd
import numpy as np
from datetime import datetime
from pydsstools.heclib.dss import HecDss
from pydsstools.core import TimeSeriesContainer
from os.path import basename, splitext


def main():
    # request the text file
    text_table_dir = file_dialog.request_open_file("Text Table File")
    dss_filename = splitext(basename(text_table_dir))[0] + ".dss"

    # read the text table file
    df = read_format_ssa_floodrates(text_table_dir)

    # iterate through the columns and write to dss
    df_to_dss(df, dss_filename)

def df_to_dss(df, dss_filename):
    # get column count
    col_count = len(df.columns)
    # get row count
    row_count = len(df.index)

    # set the steps to average over
    steps_to_average = 1

    # create a constant time series list
    # datetime year, month, day, hour, minute
    timeseries_list = [datetime(2000,1, mintues // 1440 + 1, mintues // 60 % 24, mintues % 60) for mintues in range(0, row_count // steps_to_average + 1)]

    # iterate over all columns
    for i in range(0, col_count):
        # print(f"iter: \t{i}\t{df.columns[i]}")
        
        # create numpy array from dataframe
        value_list = df.iloc[:,i].to_numpy()
        # get an average of the number of steps
        valueseries_list = value_list.reshape(-1, steps_to_average).mean(axis=1)
        valueseries_list = np.append(valueseries_list, 0)
        
        # get name of column
        name = df.columns[i]

        # write this column to dss
        write_dss(name, timeseries_list, valueseries_list, dss_filename)

def write_dss(name, timeseries_list, valueseries_list, dss_filename):
    dss_file = dss_filename
    pathname = f"/IRREGULAR/TIMESERIES/FLOW/01JAN2000/IR-DECADE/{name}/"

    tsc = TimeSeriesContainer()
    tsc.numberValues = len(valueseries_list)
    tsc.pathname = pathname
    tsc.units ="m^3/s"
    tsc.type = "INST"
    tsc.interval = -1
    tsc.values = valueseries_list

    tsc.times = timeseries_list

    with HecDss.Open(dss_file) as fid:
        status = fid.put_ts(tsc)


def read_format_ssa_floodrates(text_table_file):
    """
    This function takes a string representing the directory of a table text file.
    This function was made to open the table output of Autodesk Storm and Sanitary Analysis
    """
    
    # read the file as csv while ignoring first two rows
    df = pd.read_csv(text_table_file, sep=r"\s+", skiprows=[0, 1], engine='python')
    
    # arrange and correct the headers
    df.loc[0,:] = df.loc[0,:].shift(periods=2, axis=0)
    df.iloc[0,0] = "Days"
    df.iloc[0,1] = "Hours"
    df.columns = df.iloc[0,:]

    # remove the row used to create the header
    df = df.drop([0])

    df = df.iloc[:,2:]

    return df.apply(pd.to_numeric)


if __name__ == "__main__":
    print(f"Beginning {__file__}")
    main()
    print(f"Completed {__file__}")