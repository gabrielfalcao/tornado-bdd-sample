# lettuce + sure + selenium + tornado

# What

a simple web application written with outside-in BDD technique through Lettuce + Sure + Selenium 2 + firefox

# requirements

* [selenium 2](http://pypi.python.org/pypi/selenium/) which provides firefox "native" support
* [sure](http://github.com/gabrielfalcao/sure)
* [lettuce](http://github.com/gabrielfalcao/lettuce)
* [tornado](http://tornadoweb.org/)
* [fabric](http://fabfile.org/)
* [daemon](http://pypi.python.org/pypi/python-daemon/)

## install them all in a single shot!

    sudo pip install -r requirements.txt

# running the tests

just go to the directory and run the command:

    fab test

# running the server

just go to the directory and run the command:

    python sample/start.py

## run as daemon

    python sample/start.py --daemon

## run in different ports (specially for [deployment in production](http://www.tornadoweb.org/documentation#running-tornado-in-production))

    python sample/start.py --port=8000

### more on daemon mode

all the parameters below are optional, if you don't set someone it
will default to the application path

#### setting the working directory

    python sample/start.py --daemon --working-directory=/path/to/working/dir/



#### setting the pidfile directory

    python sample/start.py --daemon --pidfile-directory=/var/run/ --port=8899

this will make the server run on `/var/run/tornado-8899.lock`

## putting all together

this will run your application as daemon in ports 8000 to 8003 working on `/srv/apps/tornado-app`:

    python sample/start.py --port=8000 --daemon --pidfile-directory=/var/run/ --working-directory=/srv/apps/tornado-app
    python sample/start.py --port=8001 --daemon --pidfile-directory=/var/run/ --working-directory=/srv/apps/tornado-app
    python sample/start.py --port=8002 --daemon --pidfile-directory=/var/run/ --working-directory=/srv/apps/tornado-app
    python sample/start.py --port=8003 --daemon --pidfile-directory=/var/run/ --working-directory=/srv/apps/tornado-app

and the pidfiles will be located at:

`/var/run/tornado-8000.lock`
`/var/run/tornado-8001.lock`
`/var/run/tornado-8002.lock`
`/var/run/tornado-8003.lock`

# in production

this app was made to run on [Amazon EC2](http://aws.amazon.com/ec2/) with [monit](http://mmonit.com/monit/) on it

you can set your monit to run the following script located at this project's root folder:

    ./deploy/server start 8000
    ./deploy/server start 8001
    ./deploy/server start 8002
    ./deploy/server start 8003

and stop them with

    ./deploy/server stop 8000
    ./deploy/server stop 8001
    ./deploy/server stop 8002
    ./deploy/server stop 8003

# license

this project is under MIT license, so that it can be embedded into
your project, and ran within your sandbox.

    Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
