# Simple Log Counter

A small Python script for analyzing basic log files. It counts lines countaining 'INFO', 'WARNING' and 'ERROR' and saves a schort summary

## Featutes
-Reads a '.log' o '.txt' file
-Counts total lines as well as INFO, WARNING and ERROR entries
-Prints the summary to the terminal and saves it to 'report.txt'

# How to rung 
'''bash 
python log_counter.py 
''' 
A 'sample.log' file is included for testing( jsut press Enter when asked fpr a filename).

## Ideas for Later
- [ ] Export only 'ERROR' lines to a separate file
- [ ] Pass the filename as a command-line argument