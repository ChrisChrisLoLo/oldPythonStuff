import cx_Freeze
#cx freeze is a porgram that helps export our pygames into executables, by a process called freezing
#for other projects it is strongly recommended to read the documents for this program

#NOTE: you must have all files referenced below in the same folder as this file
executables = [cx_Freeze.Executable("15.Score and Pause.py")]

#In options, we make a dictionary stating that we need to include py game as well as to include
#our sprites
#The rest(aside from executables) is pretty self explanatory
#To use cx_Freeze go to https://www.youtube.com/watch?v=xz2q2GaTBYE

cx_Freeze.setup(
    name="Slither",
    options={"build_exe":{"packages":["pygame"],"include_files":["Apple.png","SnakeHead.png"]}},

    description = "Slither Game Tutorial",
    executables = executables
    )
#You esstially open up cmd and go into the folder that has this file
#Then type python 16.setup.py build to make an .exe build
#If that doesnt work, you'll want to go through the full directory to python
#Ex. C:/python34/python (thisfile'sname).py build
#If you want to make an installer, type in python 16.setup.py bdist_msi
#NOTE: it will make an installer that has the same kind as your 32/64 bit OS. In this case,
#it will make a 64 bit installer. With limited knowledge, the only way to remedy this is to run
#this file on a 32 bit OS.
