# Orca Controller Client Experiment

This repository is an experiment for controlling the Orca screen reader from external clients. It has been tested with Orca version 46.1 on Ubuntu 24.04 

This repository's eventual goal is to provide a simple way for clients to send commands to Orca like speaking text, or changing settings. The design of this is inspired by the interface provided by the [NVDA controller client](https://github.com/nvaccess/nvda/blob/master/extras/controllerClient/readme.md). In an ideal world there would be a full fledged Orca plugin system, however, this is not the case yet and it would be a significant amount of work to implement while doing so in a way that prevents unintended user code from breaking the screen reader. A simple controller client like this still allows for a lot of customization while preventing users from messing with Orca internals.

Note this repo is mainly for documentation and serving as a template for others who are interested, not production usage.

## Installation

Run `./install.sh` to install. Fundamentally all this does is copy `orca-customizations.py` to `~/.local/share/orca/orca-customizations.py`. However, we also check to make sure that file doesn't already exist, since we don't want to overwrite user changes. 

## Running

Run `make test` to run a test which sends a healthcheck message to the screen reader and waits for an ipc response. More generalized functionality and clients for other languages could be added in the future. All that a client needs to do to communicate with this server is send a message to the named pipe `/tmp/orca_controller_request.pipe` and receive a response on the named pipe `/tmp/orca_controller_response.pipe`. Since the extension can run any Python code inside Orca, using this ipc interface you can essentially run whatever you want provided you are willing to dig inside the code a bit. 

## Orca Limitations

- To my understanding at the moment Orca only imports directly from `~/.local/share/orca/orca-customizations.py`. As a result, you have to bundle all your Python code in this file, else it will not work. I have tried putting helper code in a `lib/` package with a corresponding `__init__.py` file, but it did not work. All user code being in one file makes installing scripts a bit harder and we need to check more edge cases to make sure that we don't break user customizations.
- `~/.local/share/orca/orca-scripts/` appears to be another location that Orca imports from, but in my testing it does not seem to auto import nor run the Python scripts inside. 
- Orca runs all custom Python on the same thread as the main screenreader, thus in order to prevent custom code blocking Orca, you should run it in a separate new thread.
- The internals of Orca are not necessarily inteded to be scripted in a general purpose way and thus you should limit using anything too deep in the codebase since it could easily be broken between Orca version updates.

