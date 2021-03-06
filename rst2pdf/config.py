# -*- coding: utf-8 -*-
# See LICENSE.txt for licensing terms
"""Singleton config object"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()


import configparser
import os
from rst2pdf.rson import loads

cfdir = os.path.join(os.path.expanduser('~'), '.rst2pdf')
cfname = os.path.join(cfdir, 'config')


def getValue(section, key, default=None):
    section = section.lower()
    key = key.lower()
    try:
        return loads(conf.get(section, key))
    except Exception:
        return default


class ConfigError(Exception):

    def __init__(self, modulename, msg):
        self.modulename = modulename
        self.msg = msg

conf = configparser.SafeConfigParser()

def parseConfig(extracf=None):
    global conf
    cflist = ["/etc/rst2pdf.conf", cfname]
    if extracf:
        cflist.append(extracf)
    conf = configparser.SafeConfigParser()
    conf.read(cflist)
    
parseConfig()
