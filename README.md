rpg-x
=====

Action-RPG Questionaire game with political candidates face-off.
Basically, it's a arcade-style two-player game fighting one another
by answer questions brought up by the moderator (system).

Each question has 4 choices; Each affect the player's HP and XP in 
different ways. Players fight off until one's HP hits 0.

Each player can choose any political character she wants. 

Requirements
------------

+ Python 2.7.x
+ Flask
+ Tornado
+ Bootstrap
+ Docker (optional)

Install & Run
-------------

To run on a local server, make sure you have 
+ [bower](http://bower.io/)
+ [virtualenv](https://pypi.python.org/pypi/virtualenv)
+ [pip](https://pip.pypa.io/en/stable/installing/)


run `run.sh` to install dependencies and run

```bash

$ source run.sh

```

Then browse to `http://127.0.0.1:8000`

To run with Docker, install [Docker Toolbox](https://www.docker.com/products/docker-toolbox) on Mac OS X
which include a docker cli and download and install [Virtualbox](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-OSX.dmg).

```bash

$ docker-compose up

```

Note that the VM generates its own ip address, which can be checked with:

```bash

$ docker-machine ip


```

Need IP change
--------------

Then browse to `http://<ip-address>:5000`.








