# 2022_Bean_mergeData
Add matching labels from the reference 2-column file of label pairs.

## App description
The application enables: <br>
1) adding matching labels from the reference file of label pairs into the data file, <br>
2) transfering annotated data into the original (master) file of samples with assigned error_value=-9999.99 for missing data. <br>
* the user has to provide a 2-column file with pairs of corresponding labels (e.g., ARS label and Sample num) **[labels]**
* the user has to provide a multi-column file annotated with one of the reference labels (e.g., ARS label) **[data]**
* optionally, the user can provide a 1-column file with the list of all samples (e.g., Sample num) **[samples]**; when the file is provided the additional output will be generated automatically and it will contain the data assigned to the original samples while missing data fields will be filled with error_value
* the user should provide the index of label column in the **data** file; *by default, the algorithm assumes it is the first column in the data file (indexing starts from 0)*
* the user can customize the output filename and format of exported data; by default the filename is data_output-$date and it is exported as an Excel file

## Environmental requirememnts

**Requirements: python3, pandas, openpyxl**

1. If you use `conda` already, create a new **merge_data** environment and activate it:

```
conda create -n merge_data python=3.9
conda activate merge_data
```

2. Next, install the remaining requirements using `pip3`:

```
pip3 install pandas
pip3 install openpyxl
```

*^ If you do not use conda, but have python3 already installed, follow the instructions from section 2 directly.*

## Available options

optional arguments:<br>
```
  -h,          --help                         # show this help message and exit
  -l labels,   --labels-filename labels       # [string] input 2-col file in the xlsx format; required
  -f data,     --data-file data               # [string] input multi-col file in the xlsx format; required
  -t samples,  --master-file samples          # [string] input Master Excel (samples) file in the xlsx format; optional
  -c col,      --label-column col             # [string] index of the label column in the data_file; default=0
  -o format,   --output-format format         # [int] select format for output file: 0 - xlsx, 1 - csv; default=0
  -n outfile,  --output-filename outfile      # [string] provide custom name for the output file; default="data_output"
  -m master,   --output-masterfile master     # [string] provide custom name for the output master_file; default: "master_output"
```

## Example usage:<br>

```
data_matcher.py [-h] -l labels -f data [-t samples] [-c col] [-o format] [-n outfile] [-m master]
```

* minimal arguments to generate data_output:<br>

```
python3 data_matcher.py -l labels.xlsx -f data.xlsx
```

* minimal arguments to generate data_output and master_output:<br>

```
python3 data_matcher.py -l labels.xlsx -f data.xlsx -t samples.xlsx
```

## Input data and outputs

**data_output**<br>
The exact copy of the input datafile [*data.xlsx*] with one additional column (next to the ARS label) is created [*output.xlsx* by default]. The new column contains the corresponding sample label. If there is no matching sample label, the error value -f -9999.99 is assigned.

**master_output**<br>
The exact copy of the input sample file [*sample.xlsx*] (containing the sample labels) is extended of the corresponding ARS label and all remaining data columns (taken from data_file). If there is no matching hit for a sample label, the values in the new columns will contain the default (-9999.99) for the missing data.

Files description:<br>

|file | description|
|-----|------------|
|Original_Sample_Master_List.xlsx **[samples.xlsx]** | original **sample labels** of experimental data |
|F-set_complete.xlsx **[labels.xlsx]**| list of matching labels pairs; 2-column file |
|Sample_Data_by_ARS_F-number.xlsx| data annotated with **ARS label** |
|Sample_check_by_F-number.xlsx **[data.xlsx]**| data annotated with **ARS label** |
|data_matcher.py| python script |
