Python libraries required:

matplotlib==1.5.1
scipy==0.17.1

Programme Execution:

1. Open a terminal and go into the main folder with gui_filter.py.
2. Type in the terminal: python gui_filter.py


Installation of the Python libraries (for MacOSX / Linux):

1. If the programme does not run, you need to install missing libraries. You can do it by using command "virtualenv env" for creating a new virtual environment (if not installed "sudo pip install virtualenv", see also http://sourabhbajaj.com/mac-setup/Python/virtualenv.html )
2. Activate clean environment by using "source venv/bin/activate"
3. Try install scipy via "pip install scipy==0.17.1"
4. Try install matplotlib via "pip install matplotlib==1.5.1"
5. Search for the file "matplotlibrc" inside the virtual environment folder "venv" and change line "backend: MacOSX" (or maybe some other backend) to the line "backend: TkAgg"
6. Type in the terminal:python gui_filter.py. 