# Simple Log Counter

A small Python script for analyzing basic log files. It counts lines containing `INFO`, `WARNING`, and `ERROR` and saves a short summary.

## Features
- Reads a `.log` or `.txt` file
- Counts total lines as well as INFO, WARNING, and ERROR entries
- Prints the summary to the terminal and saves it to `report.txt`

## How to run
```bash
python log_counter.py
```
A `sample.log` file is included for testing (just press Enter when asked for a filename).

## Ideas for later
- [ ] Export only `ERROR` lines to a separate file
- [ ] Pass the filename as a command-line argument
