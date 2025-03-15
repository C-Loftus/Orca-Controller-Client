# Orca Controller Client

This repository is an experiment for controller the Orca scren reader from external clients. It has been tested with Orca version 46.1 on Ubuntu 24.04 

This repository's goal is to provide a simple way for clients to send commands to Orca like speaking text, or changing settings. The design of this is inspired by the interface provided by the [NVDA controller client](https://github.com/nvaccess/nvda/blob/master/extras/controllerClient/readme.md). In an ideal world there would be a full fledged Orca plugin system, however, this is not the case yet and it would be a significant amount of work to implement while doing so in a way that prevents unintended user code from breaking the screen reader. A simple controller client like this still allows for a lot of customization while preventing users from messing with Orca internals. 

## Installation

Run `./install.sh` to install. Fundamentally all this does is copy `orca-customizations.py` to `~/.local/share/orca/orca-customizations.py`. However, we also check to make sure that file doesn't already exist, since we don't want to overwrite user changes. 

## Limitations

To my understanding at the moment Orca only imports directly from `~/.local/share/orca/orca-customizations.py`. As a result, you have to bundle all your Python code in this file, else it will not work. I have tried putting helper code in a `lib/` package with a corresponding `__init__.py` file, but it did not work. All user code being in one file makes installing scripts a bit harder and we need to check more edge cases to make sure that we don't break user customizations.

`~/.local/share/orca/orca-scripts/` appears to be another location that Orca imports from, but in my testing it does not seem to auto import nor run the Python scripts inside. 