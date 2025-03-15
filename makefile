
all:
	bash install.sh	

test:
	pytest extension/

devDeps:
	git clone https://gitlab.gnome.org/GNOME/orca

devRun:
	cp extension/*.py ~/.local/share/orca/; orca --replace

clean:
	rm -rf ~/.local/share/orca/*.py