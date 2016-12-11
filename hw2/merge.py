#!/usr/bin/env python
"""merge: module to merge data from temperature file
and energy file
"""
import time
import os
import sys

def merge(temperatureFile, energyFile, outputFile="", append=False):
    """
    Merge data from temperature file and energy file:
        keep all information in temperature file
        match the energy value for a particular time with the temperature value logged just before that time
        divide energy values by 1000 and write them in an additional column

    Arguments:
        temperatureFile: csv format; 3 columns (#, Date Time, Temperature)
        energyFile: csv format; 2 columns (Date/Time, Energy Produced in Wh)
        ourputFile: the output file name; default: STDOUT
        append: whether append output to an existing file; default: False

    Assumptions: (if violated, an error message will be displayed)
        Times in temperature file should be in ascending order;
        Times in energy file should be at midnight (00:00:00), GMT-05:00 (daylight savings) or GMT-06:00;
        If append = True, outputFile must be an existing file;
        If append = False, outputFile can't be an existing file so that won't overwrite it.

    Output:
        csv format (5 columns):
            #
            Date Time
            Temperature
            Energy Produced (Wh)
            Energy Produced (kWh)
        directed to:
            STDOUT: if outputFile="" and append = False (default)
            a new csv file named by outputFile: if outputFile is a new file and append = False
            append to an existing file outputFile: if outputFile is an existing file and append = True
    """

    # check arguments:
    if append:
        assert os.path.exists(outputFile), "If append=True, outputFile should be an existing file."
    else:
        assert not os.path.exists(outputFile), "The output shouldn't overwrite an existing file. Please change outputFile or set append = True or remove the existing file."

    # read temperature file into 3 vectors & read energy file into 2 vectors:
    with open(temperatureFile, 'r', encoding = 'utf-8') as temp:
        lines = [line.rstrip() for line in temp if line != '\n'][2:]
        # the line above assumes 2 lines for the header in the temperature file.
        # change [2:] to [1:] at the end of the previous line (49) if only 1-line header
        num = [line.split(',')[0] for line in lines]
        time_temp = [line.split(',')[1] for line in lines]
        value_t = [line.split(',')[2] for line in lines]
    with open(energyFile, 'r') as energy:
        lines = [line.rstrip() for line in energy if line != '\n'][1:-1]
        # above: skips 1-line header and skips last line too, for "Total"
        time_e = [i.split(',')[0] for i in lines]
        value_e = [i.split(',')[1] for i in lines]

    # check assumptions about time in temperature and energy files:
    t_temp = [time.strptime(time_temp[i], '%m/%d/%y %I:%M:%S %p') for i in range(len(time_temp))]
    t_e = [time.strptime(time_e[i], '%Y-%m-%d %H:%M:%S %z') for i in range(len(time_e))]
    assert sorted([time.mktime(i) for i in t_temp]) == [time.mktime(i) for i in t_temp], "Dates and times in temperature file should be in ascending order."
    assert all([i.tm_hour==0 and i.tm_min==0 and i.tm_sec==0 for i in t_e]), "Times in energy file should be at midnight(00:00:00)."
    assert all([i.tm_gmtoff==-18000 or i.tm_gmtoff==-21600 for i in t_e]), "Time zone in energy file should be GMT-05:00 (daylight savings) or GMT-06:00."
    # 18000 seconds = 5h, 21600 seconds = 6h

    # match the energy value for a particular time with the temperature value logged just before that time
    new = ['' for i in range(len(t_temp))]
    for i in range(len(t_e)):
        if time.mktime(t_temp[0])-time.mktime(t_e[i]) > 0:
            continue
        else:
            for j in range(len(t_temp)):
                if time.mktime(t_temp[j])-time.mktime(t_e[i]) > 0:
                    break
            new[j-1] = value_e[i]

    # devide energy value by 1000:
    new2 = [str(float(i)/1000) if i else '' for i in new]

    # re-construct the time format:
    time_new = [time.strftime('%Y-%m-%d %H:%M:%S', i) for i in t_temp]

    # output:
    header = '#,Date Time,Temperature,Energy Produced(Wh),Energy Produced(kWh)\n'
    data = [','.join([num[i], time_new[i], value_t[i], new[i], new2[i]]) for i in range(len(num))]
    out = header+'\n'.join(data)+'\n'
    if outputFile:
        if append:
            with open(outputFile,  'a') as f:
                f.write(out)
        else:
            with open(outputFile,  'x') as f:
                f.write(out)
    else:
        sys.stdout.write(out)

# execute only if run as a script:
if __name__ == "__main__":
    # import argparse to handle script arguments:
    import argparse
    parser = argparse.ArgumentParser(description = """Merge data from temperature file and energy file (both in csv format).
    Assume the temperature file has 3 columns representing "#", "Date Time", "Temperature"
    and the energy file has 2 columns representing "Date Time", "Energy Produced(Wh)".
    Times in temperature file should be in ascending order and times in energy file should be at midnight (00:00:00, GMT-05:00 (daylight savings) or GMT-06:00),
    otherwise an error message will be displayed.
    All information in temperature file will be kept, the energy value for a particular time will be matched with the temperature value logged just before that time,
    energy values will be dicided by 1000 and written in an additional column.
    The output is also in csv format including 5 columns: #, Date Time, Temperature, Energy Produced (Wh), Energy Produced (kWh).""")
    parser.add_argument("-t", "--temperatureFile", help="required; temperature file in csv format")
    parser.add_argument("-e", "--energyFile", help="required; energy file in csv form")
    parser.add_argument("-o", "--outputFile", default = "", help="optional; if missing, STDOUT, otherwise, the output will be directed to a new file named by it")
    parser.add_argument("-a", "--append", action = "store_true", help="optional; if not missing, append the output to an existing file")
    args = parser.parse_args()
    # test argument problems:
    if not os.path.exists(args.temperatureFile):
        raise Exception("-t(--temperatureFile) should be an existing file")
    if not os.path.exists(args.energyFile):
        raise Exception("-e(--energyFile) should be an existing file")
    if not (args.temperatureFile and args.energyFile):
        raise Exception("needs at least 2 arguments: -t (temperature csv file) and -e (energy csv file)")
    if args.append and (not os.path.exists(args.outputFile)):
        raise Exception("if -a (--append), needs argument -o (--outputFile) to specify an existing file to append")
    if (not args.append) and (os.path.exists(args.outputFile)):
        raise Exception("the output can't overwrites existing file")

    # call merge() function:
    merge(args.temperatureFile, args.energyFile, args.outputFile, args.append)
