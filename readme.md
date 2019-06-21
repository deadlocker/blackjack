
try to import pygame as simple gui if you want to use simplegui by codeskulptor in your pc that
has python pygame features installed.
if you dont have the features , then try to copy this code and run at www.codeskulptor.org
"""




How to install pygame in linux

# Installing with pip

System-wide installation WARNING: This is not advised! Don't do this if you don't know what you're doing!
sudo pip install hg+http://bitbucket.org/pygame/pygame
 
 
# Using a virtual environment. This is the recommended approach.
mkvirtualenv NAME_OF_PROJECT
cd /path/to/project/root
echo hg+http://bitbucket.org/pygame/pygame >> requirements.txt
pip install -r requirements.txt

"""

# Installing with normal dependencies

"""
sudo apt-get update
sudo apt-get install python-pygame

#install dependencies
sudo apt-get install mercurial python3-dev python3-setuptools python3-numpy python3-opengl \ libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \ libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \ libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont \ xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf


#setup and install
cd pygamepython3 
setup.py build
sudo python3 setup.py install

"""


