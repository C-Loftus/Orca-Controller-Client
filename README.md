# Orca Controller Client

This repository is an experiment for controller the Orca scren reader from external clients. 

It has been tested with Orca version 46.1 

## Limitations

To my understanding at the moment Orca only imports directly from `~/.local/share/orca/orca-customizations.py`. As a result, you have to bundle all your Python code in this file, else it will not work. I have tried putting helper code in a `lib/` package with a corresponding `__init__.py` file, but it did not work.

`~/.local/share/orca/orca-scripts/` appears to be another location that Orca imports from, but it does not seem to auto import and run the code. 