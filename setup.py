from setuptools import setup


setup(
  name = 'TOPSIS-Jay-101803206',         # How you named your package folder (MyLib)
  packages = ['Topsis_Jay'],   # Chose the same as "name"
  version = '0.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Multiple Criteria Decision Making System using TOPSIS',   # Give a short description about your library
  long_description='''
# TOPSIS - JAY - 101803206

Simple Python module for Multiple Criteria Decision Making System using TOPSIS.

Input/Output Files:
 - Input File
        o Input file contain three or more columns
        o First column is the object/variable name (e.g. M1, M2, M3, M4…...)
        o From 2nd to last columns contain numeric values only
 - Output Files
        o Result file contains all the columns of input file and two additional columns having TOPSIS SCORE and RANK

There is also Check For :
 - Check for:
• Correct number of parameters (inputFileName, Weights, Impacts, resultFileName).
• Show the appropriate message for wrong inputs.
• Handling of “File not Found” exception*]!vmN;Gv97GR8b
• Input file must contain three or more columns.
• From 2nd to last columns must contain numeric values only (Handling of non-numeric values)
• Number of weights, number of impacts and number of columns (from 2nd to last columns) must be same.
• Impacts must be either +ve or -ve.
• Impacts and weights must be separated by ‘,’ (comma).

### Installation
TOPSIS requires python v3+ to run.

```sh
 $ pip install TOPSIS-JAY-101803206
```

### Usage Example

```sh
 import Topsis_Jay as Tj
 
 # DEFINE FEW ATTRIBUTES
 Fn = "inputfile.csv" # PROVIDE THE INPUT FILE NAME 
 W = "1,1,1,2" # PROVIDE WEIGHTS 
 I = "+,+,-,+" # PROVIDE IMPACT VALUES
 Yu = "Result.csv" # PROVIDE OUTPUT FILE NAME

 Tj.TOPSIS(Fn,W,I,Yu) # Function Call

```

#### Result
```
# Result File Saved as : Result.csv
```

[PYPI](https://pypi.org/project/TOPSIS-Jay-101803206/0.4/)
[LINKDIN](https://www.linkedin.com/in/jay-sood/)


  ''',
  long_description_content_type="text/markdown",
  author = 'Jay Sood',                   # Type in your name
  author_email = 'jaisood08@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Jaisood08/TOPSIS-JAY-101803206',   # Provide either the link to your github or to your website
  keywords = ['TOPSIS', '101803206', 'JAY Sood','DS-ASSIGNMENT 6 '],   # Keywords that define your package best
  install_requires=[ 'pandas'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)