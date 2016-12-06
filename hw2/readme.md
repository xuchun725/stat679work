# howmework 2
- all the codes / commands should be run in `stat679work/hw2/`
- python version: 3.5.2

## Data
- [waterTemperature.csv](https://github.com/xuchun725/stat679work/blob/master/hw2/waterTemperature.csv)
- [energy.csv](https://github.com/xuchun725/stat679work/blob/master/hw2/energy.csv)

## Script
- [merge.py](https://github.com/xuchun725/stat679work/blob/master/hw2/merge.py)

### Purpose
create a python module `merge` that can be used to merge data from temperature file and energy file
  - keep all information in temperature file
  - match the energy value for a particular time with the temperature value logged just before that time
  - divide energy values by 1000 and write them in an additional column

### Features

- **check assumptions** (if violated, an error message will be displayed)
  - times in temperature file should be in ascending order
  - times in energy file should be at midnight(00:00:00), Wisconsin time(GMT-05:00)
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
### run as a script in bash
#### preparation
- the script `merge.py` starts with this shebang line `#!/usr/bin/env python`
  so that it can be executed with `./merge.py` at the shell prompt
- change the permission of the script file to be executable:
  `chmod u+x ./merge.py`

#### help message
```shell
./merge.py --help
```

```
usage: merge.py [-h] [-t TEMPERATUREFILE] [-e ENERGYFILE] [-o OUTPUTFILE] [-a]

Merge data from temperature file and energy file (both in csv format). Assume
the temperature file has 3 columns representing "#", "Date Time",
"Temperature" and the energy file has 2 columns representing "Date Time",
"Energy Produced(Wh)". Times in temperature file should be in ascending order
and times in energy file should be at midnight(00:00:00, GMT-05:00), otherwise
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
python merge.py -t waterTemperature.csv -e energy.csv
./merge.py -t waterTemperature.csv -e energy.csv
```
- create a new file to store the results
```shell
./merge.py -t waterTemperature.csv -e energy.csv -o output.csv
```
- append results to an existing file
```shell
./merge.py -t waterTemperature.csv -e energy.csv -o output.csv --append
```


### inside a python session as a module
```python
import merge
```
#### help message
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
        temperatureFile: csv format; 3 columns(#, Date Time, Temperature)
        energyFile: csv format; 2 columns(Date/Time, Energy Produced (Wh))
        ourputFile: the output file name; default: STDOUT
        append: whether append output to an existing file; default: False

    Assumptions: (if violated, an error message will be displayed)
        Times in temperature file should be in ascending order;
        Times in energy file should be at midnight(00:00:00), GMT-05:00;
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

#### example
- standard output
```python
merge.merge('waterTemperature.csv', 'energy.csv')
```
- create a new file to store the results
```python
merge.merge('waterTemperature.csv', 'energy.csv', 'output.csv')
```
- append results to an existing file
```python
merge.merge('waterTemperature.csv', 'energy.csv', 'output.csv', append=True)
```

## Results
- [output.csv](https://github.com/xuchun725/stat679work/blob/master/hw2/output.csv)
