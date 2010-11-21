# lettuce + sure + selenium + tornado

# What

a simple web application written with outside-in BDD technique through Lettuce + Sure + Selenium 2 + firefox

# requirements

* [selenium 2](http://pypi.python.org/pypi/selenium/) which provides firefox "native" support
* [sure](http://github.com/gabrielfalcao/sure)
* [lettuce](http://github.com/gabrielfalcao/lettuce)
* [tornado](http://tornadoweb.org/)
* [fabric](http://fabfile.org/)

## install them all in a single shot!

    sudo pip install -r requirements.txt

# running the tests

just go to the directory and run the command:

    fab test

# running the server

just go to the directory and run the command:

    python sample/__init__.py

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
