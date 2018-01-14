#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  Copyright 2018 michaellanguage <michaellanguage@icloud.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
import datetime
from datetime import timedelta
from math import floor
import re
from dateutil.parser import parse as parse_time_from_string
def convert_date_to_format(datestring=None,date_format='%Y-%m-%d %H:%M:%S',diff=False):
	if datestring:
		datestring = str(datestring)
		today = datetime.date.today()
		try:
			date_object = parse_time_from_string(datestring,fuzzy_with_tokens=True)
			today = date_object[0]
		except:pass#will always fallback to today date
		if diff:
			return datetime.datetime.strptime("%s" % (today.strftime(date_format)),"%s" % (date_format))
		return str(today.strftime(date_format))
def str_number(s):
	try:
		return float(s)
	except ValueError:
		try:
			return int(s)
		except ValueError:
			raise ValueError('I need microseconds or datetime')
def date_time_match(timestr):
	if re.match(r"(sun|mon|tue|Weds|thu|Fri|sat|monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|tues|wed|thur|thurs|fri|sat|sun|pm|am|today|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|tues|wed|thur|thurs|fri|sat|sun|january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec|am|pm|\|:|-|/|(\d{2,4}[\:\-/ [\\\] ]{1,}\d{2}[\:\-/ [\\\] ]{0,}(\d{2,4})?)(\d{2}[\:\-/ [\\\] ]{0,}(\d{2,4})))", str(timestr), re.I | re.S | re.M):
		return True
	else:
		return False
class time_difference(object):
	date_format='%Y-%m-%d %H:%M:%S'
	def __init__(self,time1,time2):
		if date_time_match(time1) and date_time_match(time2):
			time1 = convert_date_to_format(time1, time_difference.date_format,diff=True)
			time2 = convert_date_to_format(time2, time_difference.date_format,diff=True)
		else:
			time1 = datetime.datetime.fromtimestamp(str_number(time1))
			time2 = datetime.datetime.fromtimestamp(str_number(time2))
		self.difference =   time1 -time2
		timedifference = abs(self.difference.total_seconds())
		self.years   = floor(timedifference / (365*60*60*24))
		self.months  = floor((timedifference -self.years * 365*60*60*24) / (30*60*60*24))
		self.days    = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24)/ (60*60*24))
		self.hours   = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24 -self.days*60*60*24)/ (60*60))
		self.minutes  = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24 -self.days*60*60*24 -self.hours*60*60)/ 60)
		self._seconds = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24 -self.days*60*60*24 -self.hours*60*60 -self.minutes*60))
	def __getattr__(self, ticktok):
		if ticktok in dir(self.difference):
			return getattr(self.difference, ticktok)
		raise AttributeError("AttributeError '%s'" % ticktok)
	@property              
	def seconds(self):
		return self._seconds
	@property              
	def min(self):
		return self.minutes
	@property              
	def any(self):
		"any time difference bool true/false"
		return any(ticktok>0 for ticktok in [self.years,self.months,self.days,self.minutes,self._seconds,self.hours])
	@property              
	def totaltime(self):
		return sum([self.years,self.months,self.days,self.minutes,self._seconds,self.hours])
	def totaltime_difference(self,time1, time2):
		"return total sum of time e.g second/min etc"
		if date_time_match(time1) and date_time_match(time2):
			time1 = convert_date_to_format(time1, time_difference.date_format,diff=True)
			time2 = convert_date_to_format(time2, time_difference.date_format,diff=True)
		else:
			time1 = datetime.datetime.fromtimestamp(str_number(time1))
			time2 = datetime.datetime.fromtimestamp(str_number(time2))
		self.difference =   time1 -time2
		timedifference = abs(self.difference.total_seconds())
		self.years   = floor(timedifference / (365*60*60*24))
		self.months  = floor((timedifference -self.years * 365*60*60*24) / (30*60*60*24))
		self.days    = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24)/ (60*60*24))
		self.hours   = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24 -self.days*60*60*24)/ (60*60))
		self.minutes  = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24 -self.days*60*60*24 -self.hours*60*60)/ 60)
		self._seconds = floor((timedifference -self.years * 365*60*60*24 -self.months*30*60*60*24 -self.days*60*60*24 -self.hours*60*60 -self.minutes*60))
		return self.totaltime
			
if __name__ == "__main__":
	time1 = 'Sat, 13 Jan 2018 08:00:01 -0800'
	time2 ='Sat, 13 Jan 2018 07:35:10 -0800'
	difference= time_difference(time1,time2)
	print(difference.hours)
	print(difference.min)
	print(difference.seconds)
	print(difference.totaltime)
	print(difference.any)
	time1 = '1515887914.51328'
	time2 ='1515891791.798922'
	totaltime = difference.totaltime_difference(time1,time2)
	print(difference.totaltime)
	print(totaltime)
	import time
	time.sleep(1)
	date2 = datetime.datetime.now()
	difference= time_difference(date1,date2)
	print(difference.seconds)
	print(difference.any)
	print(difference.totaltime)
