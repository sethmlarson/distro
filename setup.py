# Copyright 2015,2016 Nir Cohen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import codecs
from setuptools import setup

# The following version is parsed by other parts of this package.
# Don't change the format of the line, or the variable name.
package_version = "2.0.0"

here = os.path.abspath(os.path.dirname(__file__))

try:
    import argparse  # NOQA
    install_requires = []
except ImportError:
    install_requires = ['argparse']


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


setup(
    name='distro',
    version=package_version,
    url='https://github.com/nir0s/distro',
    author='Nir Cohen',
    author_email='nir36g@gmail.com',
    license='Apache License, Version 2.0',
    platforms='All',
    description='Distro - an OS platform information API',
    long_description=read('README.rst'),
    packages=['distro'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'distro = distro:main',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Operating System',
    ]
)
