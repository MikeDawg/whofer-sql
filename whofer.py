#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#    whofer
#
#    Copyright (C) 2015  Mike Harris
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

#----

parser = argparse.ArgumentParser(description='whofer by MikeDawg')
parser.add_argument('-d','--domain', help='Domain Name',required=True)
args = parser.parse_args()

#---- Variables
domain_name_from_user = (args.domain)
current_working_directory = os.getcwd()
w = whois.whois(domain_name_from_user)
emails_from_whois = (w.emails)
#---- End Variables
#----
fileno, tempfile_output = tempfile.mkstemp(suffix='.tmp',prefix='.whofer_email_',text=True,dir=current_working_directory)
print(tempfile_output)
try:
    fd = open(tempfile_output, mode='w')
    for item in emails_from_whois:
        fd.write("%s" % domain_name_from_user)
        fd.write("\t")
        fd.write("%s\n" % item)
finally:
    fd.close()
    #if os.path.isfile(tempfile_output):
        #os.remove(tempfile_output)
    #else:
        #print("Error: %s file not found" % tempfile_output)
#----
#for item2 in emails_from_whois:
    
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
