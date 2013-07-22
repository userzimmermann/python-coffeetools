# python-coffeetools
#
# Various Tools for processing CoffeeScript from Python.
#
# Copyright (C) 2011-2013 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# python-coffeetools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-coffeetools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with python-coffeetools.  If not, see <http://www.gnu.org/licenses/>.

"""coffeetools

.. moduleauthor:: Stefan Zimmermann <zimmermann.code@gmail.com>
"""
__all__ = ['CoffeeError', 'Coffee', 'coffee']

from subprocess import Popen, PIPE

class CoffeeError(Exception):
    pass

class Coffee(object):
    def __call__(self, script, require=None, options=[]):
        cmd = ['coffee', '-s']
        if require:
            cmd += ['-r', str(require)]
        cmd.extend(options)
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output = p.communicate(script)
        if output[1]:
            raise CoffeeError(output[1])
        return output[0]

    def compile(self, script, bare=False):
        options = ['-c']
        if bare:
            options.append('-b')
        return self(script, options=options)

coffee = Coffee()
