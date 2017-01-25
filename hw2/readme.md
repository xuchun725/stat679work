# homework 2

- all the codes / commands should be run in `stat679work/hw2/`
- python version: 3.5.2
- jump to explanations below on the [script](#script) and script [usage](#usage)

# Getting python

follow instructions to install Python with Anaconda
from [software carpentry](http://uw-madison-aci.github.io/2016-06-08-uwmadison/#python).
For Mac OS X, these instructions basically direct you to Anaconda
[downloads](https://www.continuum.io/downloads).
Make sure to choose python 3.5 and not Python 2.7.
Anaconda installs Python, a pre-defined (large) set of Python packages,
and the conda package management system
(such as to easily install new packages in the future).

If you need to use Python 2 for other purposes, (Ana)conda
lets you switch between Python 2 and 3 very easily.
From a basic installation of Anaconda with Python 3.5,
conda has a single "environment", named "root", which runs
python 3.5:

```
$ python --version
Python 3.5.2 :: Anaconda 4.2.0 (x86_64)

$ conda info -e
# conda environments:
#
root                  *  /Users/ane/anaconda
```

To install Python 2.7 and its packages, simply ask conda
to create a new environment that runs python 2.7. The command
below names this new environment "python2":

```
conda create -n python2 python=2.7 anaconda
```

When we ask conda for information on its environments,
we see that "python2" appeared, but the star is still on "root",
meaning that if we currently call Python, it will use python 3.5:

```
$ conda info -e
# conda environments:
#
python2                  /Users/ane/anaconda/envs/python2
root                  *  /Users/ane/anaconda

$ python --version
Python 3.5.2 :: Anaconda 4.2.0 (x86_64)
```

To activate our new environment and run python 2.7, use:

```
$ source activate python2
(python2) $
(python2) $ python --version
Python 2.7.12 :: Anaconda 4.2.0 (x86_64)
(python2) $
```

This change only affects the current terminal.
Now if we ask conda for information about its environments,
we see our 2 environments as before, one for python 2.7 (python2)
and one for python 3.5 (root).
The star is on python2 because it's the one being used now:

```
(python2) $ conda info -e
# conda environments:
#
python2               *  /Users/ane/anaconda/envs/python2
root                     /Users/ane/anaconda
```

To switch back to python 3.5 in the same shell session,
we can deactivate our "python2" environment:

```
(python2) $ source deactivate python2
$ python --version
Python 3.5.2 :: Anaconda 4.2.0 (x86_64)
```


## Data

two files in the `data` folder, both in csv format:

- [water temperature](data/201608waterTemperature.csv)
- [energy](data/201608energy.csv)

## Script

- [merge.py](https://github.com/xuchun725/stat679work/blob/master/hw2/merge.py)

The python module `merge` can be used to merge data from a temperature
file (hourly records) and an energy file (daily records). It aims to:

  - keep all information in the temperature file
  - match the energy value for a particular time with the temperature value logged just before that time
  - divide energy values by 1000 (to convert Wh into kWh) and write them in an additional column

### Features

- **check assumptions** (if violated, an error message will be displayed)
  - times in temperature file should be in ascending order
  - times in energy file should be at midnight (00:00:00), Wisconsin time (GMT-06:00 or GMT-05:00 for daylight saving)
- be safe for user: **not overwriting** existing files unintentionally
- have an option to **append** to an existing file

Other assumptions:

- the water temperature file has 2 header lines. In the example provided, these lines look like this:

        "Plot Title: 10679014 jackson July29"
        "#","Date Time, GMT-05:00","K-Type, °F (LGR S/N: 10679014, SEN S/N: 10679014, LBL: water pipe)"

- the energy file is assumed to have a one-line header
- the last line in the energy file is ignored:
  it looks like this in the example provided:

      Total,139935


## Usage

### run as a script in the shell

#### preparation

- the script `merge.py` starts with this shebang line `#!/usr/bin/env python`
  so that it can be executed with `./merge.py` at the shell prompt
- change the permission of the script file to be executable:
  `chmod u+x ./merge.py`

#### script usage

to get help, type this in the shell:

```shell
./merge.py --help
```

```
usage: merge.py [-h] [-t TEMPERATUREFILE] [-e ENERGYFILE] [-o OUTPUTFILE] [-a]

Merge data from temperature file and energy file (both in csv format). Assume
the temperature file has 3 columns representing "#", "Date Time",
"Temperature" and the energy file has 2 columns representing "Date Time",
"Energy Produced(Wh)". Times in temperature file should be in ascending order
and times in energy file should be at midnight (00:00:00, GMT-05:00 (daylight savings) or GMT-06:00), otherwise
an error message will be displayed. All information in temperature file will
be kept, the energy value for a particular time will be matched with the
temperature value logged just before that time, energy values will be dicided
by 1000 and written in an additional column. The output is also in csv format
including 5 columns: #, Date Time, Temperature, Energy Produced (Wh), Energy
Produced (kWh).

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPERATUREFILE, --temperatureFile TEMPERATUREFILE
                        required; temperature file in csv format
  -e ENERGYFILE, --energyFile ENERGYFILE
                        required; energy file in csv form
  -o OUTPUTFILE, --outputFile OUTPUTFILE
                        optional; if missing, STDOUT, otherwise, the output
                        will be directed to a new file named by it
  -a, --append          optional; if not missing, append the output to an
                        existing file
```

#### examples

- to send the output to the screen (or "standard output"), either will work:

```shell
python merge.py -t data/201608waterTemperature.csv -e data/201608energy.csv
./merge.py -t data/201608waterTemperature.csv -e data/201608energy.csv
```
<!--
python merge.py -t data/oct8antifreeze2.csv -e data/oct8energy.csv
-->

- to create a new file "output.csv" with the results:

```shell
./merge.py -t data/201608waterTemperature.csv -e data/201608energy.csv -o output.csv
```

- to append the results to an existing file "output.csv":

```shell
./merge.py -t data/201608waterTemperature.csv -e data/201608energy.csv -o output.csv --append
```

### inside a python session as a module

import the package:

```python
import merge
```

get info on the package:

```python
help(merge.merge)
```

```
Help on function merge in module merge:

merge(temperatureFile, energyFile, outputFile='', append=False)
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
(END)
```

usage examples:

```python
merge.merge('waterTemperature.csv', 'energy.csv') # result sent to standard output
# create a new file "output.csv" to store the results:
merge.merge('waterTemperature.csv', 'energy.csv', 'output.csv')
# append results to "output.csv":
merge.merge('waterTemperature.csv', 'energy.csv', 'output.csv', append=True)
```

## Results

- [output.csv](https://github.com/xuchun725/stat679work/blob/master/hw2/output.csv)
