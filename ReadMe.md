
# Upload Filter

Python Script that will go through a folder of csv files,
combine them, and filter them for Zip Code and PWC.
This is mostly useful for scrapes where you have the name and phone number but not much other information.

## Important info

This script requires that you put any sheets you wish to filter into a directory. It will attempt to filter all csv files found in the directory.

The script only looks at 4 columns per sheet, and you must format them in this order: Business Name, Phone, City, Source Link.

MAKE SURE SHEETS ARE FORMATTED THIS WAY! Order is very important
![image](https://user-images.githubusercontent.com/67815957/150601356-cf9afd92-eb19-441f-be6e-2f237de28334.png)

The City and Source Links can have blanks but the program will skip any rows with blanks in title or phone number.

## Installation

1. Clone into This repository and cd into the directory
```bash
git clone https://github.com/antide-xx/filters.git
cd filters/
```
2. Install Requirements
```bash
pip3 install -r requirements.txt
```

## Usage

This script takes 2 arguments, which can be seen by running the script and passing the -h flag
```bash
$ python3 filter.py -h 

usage: filter.py [-h] -i INPUT_PATH [-o OUTPUT_PATH]

options:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input INPUT_PATH
                        specify directory of csv files you
                        wish to filter
  -o OUTPUT_PATH, --output OUTPUT_PATH
                        specify where you want output to
                        be saved. default is in current
                        working directory

```
The -i or --input argument is required to specify the directory where the files you wish to filter are. the -o or --output argument will allow you to specify where you wish to save your file.

```bash
python3 filter.py -i (directory of csv files you wish to filter) -o (path to where output should save)
```
Ex: filter all files in the 'filterme' folder in Downloads and output the results in the directory you are in 
```bash
python3 filter.py ~/Downloads/filterme/ 
```

For best use I reccomend adding an alias in your terminal so you can run this command from any folder.

Edit your rc based on what shell you use

Bash
```bash
sudo nano ~/.bashrc
 ```
 ZSH
```bash
sudo nano ~/.zshrc
```

and add this line into the file:
```
alias filter='python3 /path/to/filters/filter.py'
```
For example mine looks like this:

```
alias filter='python3 ~/angi/bots/filters/filter.py'
```

once your line is correctly added, save and exit with ctrl+x and then Y
restart your terminal and you should now be able to type 'filter' and pass the necessary flagsad arguments

```bash
filter -i directory/to/filter/ -o directory/to/output
```

