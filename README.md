## Cython

### Installation
- Need to have a C compiler of some description on the system
	- On mac, need to have `gcc` installed somehow. You can download Apple's XCode program from the App Store to get this.
	- On Linux, just `sudo apt-get install build-essential`
	- On Windows, just stop using Windows
- now just `pip install Cython`

## Important Findings
- You don't need to use an `__init__.py` file in a Cython module. Cython takes care of import stuff automatically, and putting one there messes up the location that the compiled C file is created in. Just treat Cython modules as a separate thing from Python modules
- Pass the `annotate=True` argument to `cythonize` in the setup file to produce an HTML file that illuminates how the C code interacts with Python

### Start
Save python code to `.pyx` files. Then, create a `setup.py` file to instruct Cython on how to compile the Python code into C. Finally, you need to use Cython to build the C file and compiled C file. This can be done from the commandline
#### Example
Given a directory with two files in it, `helloworld.pyx` and `setup.py`

`helloworld.pyx`
```python
print("Hello World!")
```

`setup.py`
```python
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("helloworld.pyx")
```
Run the following from a terminal shell in the same directory as the above files
```terminal
$ python setup.py build_ext --inplace
```
This will create several files in the current directory. `helloworld.c` contains the result of transpiling the Python code in `helloworld.pyx` into C, as well as the code required to allow you to import the compiled C file into Python and use it as if it were a Python module. There will also be a compiled C file, whose exact extention will depend on the system; mine is `helloworld.cpython-35m-darwin.so`. This is the actual executable bytecode file that you can run. A `build` directory will also be created, containing temporary files created to help optimize the compilation process.

The compiled C file can be imported as if it were a native Python module. Start a Python interpreter in the same directory as the file
`$ python`
And import the C module
```python
>>> import helloworld
Hello World!
```
You can sometimes use `pyximport` to skip the compilation process
```python
>>> import pyximport
>>> pyximport.install()
>>> import helloworld
Hello World!
```
