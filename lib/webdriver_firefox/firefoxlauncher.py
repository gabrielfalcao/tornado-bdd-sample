# Copyright 2008-2009 WebDriver committers
# Copyright 2008-2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import time
from subprocess import Popen
from subprocess import PIPE

from webdriver_firefox import utils
from webdriver_firefox.extensionconnection import ExtensionConnection

MAX_START_ATTEMPTS = 50

class MyPopen(Popen):
    def __del__(self):
        try:
            super(MyPopen, self).__del__(self)
        except Exception:
            pass

class FirefoxLauncher(object):
    """Launches the firefox browser."""

    def __init__(self):
        self.extension_connection = ExtensionConnection()
        self._start_cmd = utils.get_firefox_start_cmd()
        self.process = None

    def launch_browser(self, profile):
        """Launches the browser for the given profile name.
        It is assumed the profile already exists.
        """
        self.profile = profile
        while self.extension_connection.is_connectable():
            self.extension_connection.connect_and_quit()
        self._start_from_profile_path(profile.path)

        attempts = 0
        while not self.extension_connection.is_connectable():
            attempts += 1
            if attempts > (MAX_START_ATTEMPTS * 10):
                sys.stderr.write("Unable to start firefox, exitting...")
                raise SystemExit(1)

            self._start_from_profile_path(profile.path)
            time.sleep(0.1)

    def _lock_file_exists(self):
        return os.path.exists(os.path.join(self.profile.path, ".parentlock"))

    def kill(self):
        """Kill the browser.

        This is useful when the browser is stuck.
        """
        try:
            if self.process:
                os.kill(self.process.pid, 9)
        except AttributeError:
            # kill may not be available under windows environment
            pass

    def _start_from_profile_path(self, path):
        os.environ["XRE_PROFILE_PATH"] = path
        self.process = MyPopen([self._start_cmd, "-no-remote"], stderr=PIPE, stdout=PIPE)#, shell=True)

    def _wait_until_connectable(self):
        """Blocks until the extension is connectable in the firefox."""
        while not self.extension_connection.is_connectable():
            if self.process.returncode:
                # Browser has exited
                return False
        return True
