# Python Examples


- Hello, a minimal python package example

## Python env

When starting python dev its recommended to define a python environment in the repo u are working in.
This will ensure dependcies your project dont get mixed up with other projets.

To do this run:
- python -m venv "venv"

this will create a new folder with name "venv". To use it run:
- source venv/bin/activate

of if on windows run bash command:
-  source venv/Scripts/activate

now any subsequent pip commands will install stuff localy to this project
and python invocation will only have acces to the localy installed packages

To install the requirements that fallowing sections need run:
> pip install -r dev_requirements.txt

## Documentation
Python documentation is much more convient when the source code being documented is installed as editable package with pip. This lets the tools find the source regardless of their relative locations to your cwd.

To install the hello example package run:
``` console
$ pip install -e hello
```
the -e flag means editable package mode. And it very convient to use this for packages under development. With this flag there is no need to re install every time change the source code. 

``` console
# to view genereted documenation
$ pdoc hello

pdoc server ready at http://localhost:8080
# stop hosting with ctrl-c
# save documentation in a folder with -o
pdoc hello -o doc/

```



## Testing

Python as with documenation, testing is easier to when the source is installed as editable package.
So if you have not already go a head and run:

``` console
$ pip install -e hello
```
the -e flag means editable package mode. And it very convient to use this for packages under development. With this flag there is no need to re install every time change the source code. 

### pytest

Run test functions/unit tests simply run:
``` console
$ pytest

======================== test session starts =========================
platform linux -- Python 3.10.6, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/gws/projects/gh-issue-templates/examples/py
collected 1 item                                                     

hello/tests/test_math.py .                                     [100%]

========================= 1 passed in 0.01s ==========================
```
it will look for tests in folders named "test/" or "tests/"
and look in every python file(.py) that has a name like one the two:
- "test_anything.py"
- "anything_test.py"

And in those it will run functions and classes the name prefix "test_".
Read more about [pytest here](https://docs.pytest.org/)


### Code style
flake8 is a tool that test adherence to the pep8
pep8 is coding style guide written by the python founder: Guido van Rossum.
pep8 by convetion many projects fallow this guide, including the python standard library.

to use flake8 simply run:
``` bash
$ flake8

./hello/main.py:6:11: E201 whitespace after '('
./hello/main.py:6:24: E202 whitespace before ')'

```
flake8 can aslo be configured with many ways. For example see the ".flake8" file in this folder.

It configures flake8 to ignore unconventionally long lines.

To automate adherence to pep8 the autopep8 tool can be used.

to preview changes it would make run:
``` python
$ autopep8 -d -r hello/

--- original/hello/main.py
+++ fixed/hello/main.py
@@ -6,7 +6,7 @@
-def hello(              ):
+def hello():
     print("Hello, world!")

$ autopep8 -i -r hello/
```
- -d: print diff
- -r: recursive
- -i: make changes to the files

## Static analysis
python is a dynamic langage but u can create type hints.

mypy is a tool that lets u test if the types are consistent
``` python
$ mypy hello

hello/math.py:21: error: Incompatible return value type (got "float", expected "str")
```

