# -*- coding: utf-8 -*-

import sys			# to manage inline arguments
import argparse			# to convert python script into program with options
import pandas as pd		# to easily parse json object and filter out data; require installation with conda or pip
from datetime import datetime	# to create unique tag into the default output filename


def convert_jsonp_to_json(label_file, data_file, label_col, output_format, outfile):

###-- read inputs and create data structure
    labs = pd.read_excel(label_file, index_col=None, header=0)	# read xlsx file with pairs of matched labales (labels.xlsx, e.g., F-set_complete.xlsx)
    data = pd.read_excel(data_file, index_col=None, header=0)	# read xlsx file with data annotated by single label (data.xlsx, e.g., Sample_check_by_F-number.xlsx)
    dlab = data.columns.tolist()[label_col]			# header of the label column in data_file
    lab1 = ''							# header of the column of the known label in label_file
    lab2 = ''							# header of the column of the other (matching) label in label_file

    for i in labs.columns.tolist():				# identify column with known label
        if len(labs[labs[i] == data.iloc[0, label_col]]) > 0:
            lab1 = i						# if test_label is found in column, it is known label
        else:
    	    lab2 = i						# if test_label is not found in column, it is matching label
#    print(dlab, lab1, lab2)

###-- assign matching labels
    data.insert(label_col+1, lab2, '')				# insert new label column into data (next to known label)				
    for idx, i in data[dlab].iteritems():
        val = labs[labs[lab1] == i]				# find matching row in labels dataframe
        if len(val) > 0:
            data.at[idx, lab2] = val[lab2].values[0]		# assign matching label if exists
        else:
            data.at[idx, lab2] = -9999.99			# assign error val if no matching label    
#    print(data)
            
###-- export output file
    if outfile == 'output':
        outfile += datetime.now().strftime("-%d-%m-%Y-%H%M%S")
    if output_format == 1:
        data.to_csv(outfile+'.csv', sep=',', encoding='utf-8')     # output in CSV format
    else:					
        data.to_excel(outfile+'.xlsx', index=False, header=True)   # output in xlsx format (Excel)


###-- add options to the argument parser to make it easier to customize and run the script from the command line
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='data_matcher.py',
        description="""Add matching labels from the reference 2-column file of label pairs.\n 
                       Requirements: python3, pandas, openpyxl""",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=''
    )
    parser.add_argument(
        '-l', '--labels-filename',
        help='[string] input 2-col file in the xlsx format',
        metavar='labels',
        dest='labels',
        required=True
    )
    parser.add_argument(
        '-f', '--data-file',
        help='[string] input multi-col file in the xlsx format',
        metavar='data',
        dest='data',
        required=True
    )
    parser.add_argument(
        '-c', '--label-column',
        help='[string] index of the label column in the data_file',
        metavar='col',
        type=int,
        default=0,
        dest='col'
    )
    parser.add_argument(
        '-o', '--output-format',
        help='select format for output file: 0 - xlsx, 1 - csv',
        metavar='format',
        type=int,
        default=0,
        dest='out'
    )
    parser.add_argument(
        '-n', '--output-filename',
        help='provide custom name for the output file',
        metavar='outfile',
        type=str,
        default='output',
        dest='outfile'
    )

###-- print example of usage and help message when script is run without required arguments
    if len(sys.argv) < 3:
        parser.print_help()
        print("\nUSAGE:\n	e.g., python3 data_matcher.py -l labels.xlsx -f data.xlsx\n")
        sys.exit(1)

    args = parser.parse_args()
    convert_jsonp_to_json(args.labels, args.data, args.col, args.out, args.outfile)
