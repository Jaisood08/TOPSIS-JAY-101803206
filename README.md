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