import sublime
import sublime_plugin
import os
import subprocess
import json
from . import pyperclip

class SelectionsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		textToPaste = ""
		title = "Null"

		curr_dirr = os.path.dirname(__file__)
		os.chdir(curr_dirr)
		print (curr_dirr)

		with open('config.json') as data_file:
			config = json.load(data_file)
			username = config["User"]["username"]
			password = config["User"]["password"]
			login = username+":"+password

		if(view.file_name() is None):
			point = self.view.text_point(0,0)
			region = self.view.full_line(point)
			title = self.view.substr(region)
			title = title.replace("\\","\\\\")
			title = title.replace("\n","")
			title = title.replace("\t","\\t")
			title = title.replace("\'","\'\\\'\'")
			title = title.replace("\"","\\\"")
			# Titles can't contain /
			title = title.replace("/","")
		else:
			title = view.file_name().split('/')[-1]

		for i,region in enumerate(view.sel()):
			textToPaste += view.substr(region)

		print( title )
		# The order is important for parsing purposes
		textToPaste = textToPaste.replace("\\","\\\\")
		textToPaste = textToPaste.replace("\"","\\\"")
		textToPaste = textToPaste.replace("\n","\\n")
		textToPaste = textToPaste.replace("\t","\\t")
		textToPaste = textToPaste.replace("\'","\'\\\'\'")
		# ---------------------------------------------
		#textToPaste = textToPaste.replace("\"","\"\\\"\"")
		#textToPaste = textToPaste.replace("\'","\u0027")
		print( textToPaste )

		# Send the paste to the configured user and obtains url from JSON 
		# object obtained from the result of the CURL
		command = "curl -X POST -d '{\"public\":true,\"files\":{\""+ title+"\":{\"content\":\""+textToPaste+"\"}}}' -u " + login + " https://api.github.com/gists"
		#command = command.replace("\\","")
		print ("COMANDO: " + command)
		result = os.popen(command).read()
		print (str(result))
		result = json.loads(str(result))

		result = str(result["html_url"])
		print ("RESULTING URL = " + result)

		# Save URL to Clipboard
		pyperclip.copy(result)


class FileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		textToPaste = ""
		title = "Null"

		curr_dirr = os.path.dirname(__file__)
		os.chdir(curr_dirr)
		print (curr_dirr)

		with open('config.json') as data_file:
			config = json.load(data_file)
			username = config["User"]["username"]
			password = config["User"]["password"]
			login = username+":"+password

		if(view.file_name() is None):
			point = self.view.text_point(0,0)
			region = self.view.full_line(point)
			title = self.view.substr(region)
			title = title.replace("\\","\\\\")
			title = title.replace("\n","")
			title = title.replace("\t","\\t")
			title = title.replace("\'","\'\\\'\'")
			title = title.replace("\"","\\\"")
			# Titles can't contain /
			title = title.replace("/","")
		else:
			title = view.file_name().split('/')[-1]

		#for i,region in enumerate(view.sublime.Selection.add(0,view.size())):
		#	textToPaste += view.substr(region)

		#for i,region in enumerate(view.sel()):
		#	textToPaste += view.substr(region)	

		regionAllText = sublime.Region(0,view.size())
		regionAllTextSplit = view.split_by_newlines(regionAllText)
		for lineRegion in regionAllTextSplit:
			textToPaste += view.substr(lineRegion)
			textToPaste += "\n"
		#for i,region in enumerate(view.full_line(sublime.Region(0,view.size))):
		#	textToPaste += view.susbtr(region)

		print( title )
		# The order is important for parsing purposes
		textToPaste = textToPaste.replace("\\","\\\\")
		textToPaste = textToPaste.replace("\"","\\\"")
		textToPaste = textToPaste.replace("\n","\\n")
		textToPaste = textToPaste.replace("\t","\\t")
		textToPaste = textToPaste.replace("\'","\'\\\'\'")
		# ---------------------------------------------
		#textToPaste = textToPaste.replace("\"","\"\\\"\"")
		#textToPaste = textToPaste.replace("\'","\u0027")
		print( textToPaste )

		# Send the paste to the configured user and obtains url from JSON 
		# object obtained from the result of the CURL
		command = "curl -X POST -d '{\"public\":true,\"files\":{\""+ title+"\":{\"content\":\""+textToPaste+"\"}}}' -u " + login + " https://api.github.com/gists"
		#command = command.replace("\\","")
		print ("COMANDO: " + command)
		result = os.popen(command).read()
		print (str(result))
		result = json.loads(str(result))

		result = str(result["html_url"])
		print ("RESULTING URL = " + result)

		# Save URL to Clipboard
		pyperclip.copy(result)