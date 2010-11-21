#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <tornado bdd sample>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
import sys
import daemon
import lockfile
from optparse import OptionParser
from os.path import dirname, abspath, join
pwd = abspath(dirname(__file__))
main_path = abspath(join(pwd, '..'))
sys.path.append(main_path)

import tornado.httpserver
import tornado.ioloop
from sample.app import application

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-p", "--port", dest="port",
                  help="the port to run server on", default='8000')

    parser.add_option("-d", "--daemon", dest="daemon", action='store_true',
                  help="run as daemon", default=False)

    parser.add_option("-w", "--working-directory", dest="working_directory",
                  help="the working directory to run in (works only with --daemon option)", default=main_path)

    parser.add_option("-P", "--pidfile-directory", dest="pidfile_path",
                  help="the pidfile directory to use (works only with --daemon option)", default=main_path)

    (options, args) = parser.parse_args()
    port = int(options.port)

    http_server = tornado.httpserver.HTTPServer(application)
    if options.daemon is True:
        pidfile_name = 'tornado-%d' % port
        pidfile = join(options.pidfile_path, pidfile_name)
        print "the pid file for this it at %s" % (pidfile)

        log_file = '%s.log' % join(options.working_directory, pidfile_name)
        print "logs at %s" % log_file

        log = open(log_file, 'a+')
        ctx = daemon.DaemonContext(
            stdout=log,
            stderr=log,
            working_directory=options.working_directory,
            pidfile=lockfile.FileLock(pidfile, threaded=False)
        )
        ctx.open()

    print "Tornado listening at localhost:%d" % port
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
