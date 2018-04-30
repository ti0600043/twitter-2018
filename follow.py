# -*- coding: utf-8 -*-
import tweepy
import time
import datetime
import sys
import codecs
import subprocess

# python2系で起動するときは必要
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

subprocess.call("python follow_002.py", shell=True)
subprocess.call("python follow_003.py", shell=True)
subprocess.call("python follow_502.py", shell=True)
    
