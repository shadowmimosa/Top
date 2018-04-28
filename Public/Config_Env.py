#coding=utf-8
import sys
import time,traceback
import os
import platform
import subprocess
import random
import re

a = 'Test'
def RunEnv(a):
	RunEnv=a
	if 'test' in RunEnv or 'Test' in RunEnv  or  RunEnv==0 :
		return str('Test')
	else:
		return str('Online')
JoyrunEvn =  RunEnv(a)