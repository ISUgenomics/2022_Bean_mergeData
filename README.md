# 2022_Bean_mergeData
Add matching labels from the reference 2-column file of label pairs.

**Requirements: python3, pandas, openpyxl**

optional arguments:<br>
```
  -h,          --help                         # show this help message and exit
  -l labels,   --labels-filename labels       # [string] input 2-col file in the xlsx format; required
  -f data,     --data-file data               # [string] input multi-col file in the xlsx format; required
  -t samples,  --master-file samples          # [string] input Master Excel (samples) file in the xlsx format; optional
  -c col,      --label-column col             # [string] index of the label column in the data_file; default=0
  -o format,   --output-format format         # select format for output file: 0 - xlsx, 1 - csv; default=0
  -n outfile,  --output-filename outfile      # provide custom name for the output file; default="data_output"
  -m master,   --output-masterfile master     # provide custom name for the output master_file; default: "master_output"
```

USAGE:<br>

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

**data_output**<br>
The exact copy of the input datafile [*data.xlsx*] with one additional column (next to the ARS label) is created [*output.xlsx* by default]. The new column contains the corresponding sample label. If there is no matching sample label, the error value -f -9999.99 is assigned.

**master_output**<br>




Files description:<br>

|file | description|
|-----|------------|
|Original_Sample_Master_List.xlsx **[samples.xlsx]** | original **sample labels** of experimental data |
|F-set_complete.xlsx **[labels.xlsx]**| list of matching labels pairs; 2-column file |
|Sample_Data_by_ARS_F-number.xlsx| data annotated with **ARS label** |
|Sample_check_by_F-number.xlsx **[data.xlsx]**| data annotated with **ARS label** |
|data_matcher.py| python script |
