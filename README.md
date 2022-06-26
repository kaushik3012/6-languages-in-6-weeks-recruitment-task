
# Performance Tester Script

This project is based on python programming language. 
The program runs loops on different threads and increments 
the value of a global variable 'n' synchronously. The loops end when 1 second is elapsed
and stops automatically. Final value of 'n' is displayed on the console/terminal.
The in-built 'threading' python library is used to execute the program parallelly 
over multiple threads.



## Installation

No formal installation is required as I have provided only the
python script and executable file.
Also, no dependencies are required as no external library is used.

Download the repository and start the executable directly. This runs the program with default
number of threads used as 2.


## Usage/Examples

To run the program, simply use the following command in the terminal:
```bash
  #Running through python script:
  python multithreading.py

  #Running through executable:
  start multithreading.exe
```
In the above case, number of threads used will be 2.

To run the program with different number of threads, run the python
script or executable in the terminal using following command:

```bash
  #Running through python script:
  python multithreading.py --th=TH

  #Running through executable:
  start multithreading.exe --th=TH
```
Here, TH denotes the desired number of threads to be used.

Example:

```bash
  #Running through python script:
  python multithreading.py --th=1

  #Running through executable:
  start multithreading.exe --th=4
```

The program exits when user presses Enter key after 
complete execution of the program.
