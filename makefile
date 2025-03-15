
# Run the installer script
all:
	bash install.sh	

# Run the pytest tests against the extension
test:
	pytest extension/

# Clone orca so we can use the source code for python intellisense
devDeps:
	git clone https://gitlab.gnome.org/GNOME/orca

# Copy the extension to ~/.local/share/orca
# and run orca so we can test the extension
devRun:
	cp -r extension/* ~/.local/share/orca/ 
	chmod +x ~/.local/share/orca/**.py
	orca --replace

# Move all python files in the orca config location
# Orca will regenerate the necessary ones so we can
# clean all of them at once
clean:
	rm -rf ~/.local/share/orca/*.py
