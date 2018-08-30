#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#    whofer
#
#    Copyright (C) 2015,2016,2017,2018  Mike Harris
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

__version__ = '0.0.1'
__author__ = 'Mike Harris, MikeDawg@gmail.com'

__doc__ = """
whofer https://www.556forensics.com https://github.com/MikeDawg/whofer

by Mike Harris, MikeDawg

Requires python-whois https://pypi.python.org/pypi/python-whois https://bitbucket.org/richardpenman/pywhois
"""
import sys
import getopt
import os
import string
import tempfile
import whois
import argparse
import array
import re
import sqlite3
import random
import uuid
import errno
from datetime import datetime

#----

parser = argparse.ArgumentParser(description='whofer by MikeDawg')
parser.add_argument('-d','--domain', help='Domain Name',required=True)
args = parser.parse_args()

#---- Variables
datestr = "{0.year}-{00.month}-{0.day}".format(datetime.now())

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]
#----
random_string_name = my_random_string(6)
random_date_str = datestr + random_string_name
db_name = ("%s" % random_date_str)
domain_name_from_user = (args.domain)
current_working_directory = os.getcwd()
w = whois.whois(domain_name_from_user)
emails_from_whois = (w.emails)
#---- End Variables
#----
# -- Create db
print db_name

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
#----
filename = "./data"
if (mkdir_p(filename)):
        print "Created dir : %s" % (os.path.dirname(filename))

db = sqlite3.connect('data/whofer.sqlite3')
cursor = db.cursor()
cursor.execute('''
        Create TABLE IF NOT EXISTS whofer(id INTEGER PRIMARY KEY, URL TEXT, addy TEXT)
        ''')
db.commit()
    #----
for item in emails_from_whois:
    cursor.execute('''INSERT INTO whofer(URL, addy)
    VALUES(?,?)''', (domain_name_from_user,item))
    db.commit()
#----
db = sqlite3.connect('data/whofer.sqlite3')
cursor.execute('''SELECT URL, addy FROM whofer''')
for row in cursor:
    print('{0} : {1}'.format(row[0], row[1]))
    
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
