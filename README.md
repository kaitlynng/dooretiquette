# push-pulling on a pull-push door
Download ngrok from https://ngrok.com/download

On command prompt, install python packages for flask, flask_ngrok, playsound, pathlib

  $ pip3 install <pkg name>

Preferably, use a virtual environment so that python versions don't clash. Also, make sure that the python version is 3
  
  $ python3 -m venv <virtual env name> 
  
  This is a good tutorial for setting this up: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Place the directory voicelinesforPP wherever you wish, but update the path on pushpull.py 

Then, navigate to your directory containing pushpull.py on command prompt

  $ py pushpull.py
  
  This should run a ngrok server. Website should load on localhost:5000
