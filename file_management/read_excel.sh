#!/bin/bash

# Check if the required command line tools are installed
if ! command -v xlsx2csv &> /dev/null
then
    echo "Please install the xlsx2csv command first. You can install it using the command 'apt install xlsx2csv' or 'yum install xlsx2csv'"
    exit 1
fi

if ! command -v column &> /dev/null
then
    echo "Please install the column command first. You can install it using the command 'apt install bsdmainutils' or 'yum install bsdmainutils'"
    exit 1
fi

if [ $# -ne 1 ]; then
    echo "Please specify the excel file as an argument"
    exit 1
fi

# Check if the specified file exists
if [ ! -f "$1" ]; then
    echo "The specified file does not exist"
    exit 1
fi

# Convert the Excel file to CSV format and display it in the console
xlsx2csv "$1" | column -s , -t | less -#2 -N -S
