#!/usr/bin/python
"""
Test python cgi page, will return png images from webpages in a browser
It creates a lot of garbage in TMP at the moment

usage: http:/path/to.script/pycgitest.py?url=www.googole.com&width=500

Created on Jan 02, 2013

@author: Guy Sheffer <guysoft at gmail dot com>
"""
import cgitb
import cgi
import picturfy
import tempfile
cgitb.enable()
print "Content-type: image/png\n"

form=cgi.FieldStorage()
TMP_FILE=tempfile.mktemp(suffix=".png")
picturfy.html2png(form.getvalue("url"),form.getvalue("width"),TMP_FILE)

with open(TMP_FILE,"rb") as f:
    print f.read()
