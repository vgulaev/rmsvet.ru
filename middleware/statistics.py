# -*- coding: utf-8 -*-
import os
import platform

def stat_info():
	if (platform.system() == "Windows"):
		dirsym = "\\"
	else:
		dirsym = "/"
	path = __file__.split(dirsym)
	rootdir = dirsym.join(path[0:-2])
	stat = {".css" : {}, ".js" : {}, ".py" : {}, ".html" : {}}
	for e in stat:
		stat[e] = {"items" : 0, "lines" : 0}
	totallines = 0
	for root, subFolders, files in os.walk(rootdir):
		#print subFolders
		#break
		for fl in files:
			fileName, fileExtension = os.path.splitext(fl)
			if root.find(dirsym + "libs" + dirsym) != -1:
				continue
			f = open(root + dirsym + fl)
			if ((fileExtension in stat) == True):
				stat[fileExtension]["items"] = stat[fileExtension]["items"] + 1
				lines = len(f.readlines())
				stat[fileExtension]["lines"] = stat[fileExtension]["lines"] + lines
				totallines = totallines + lines
			f.close()			
	return stat

#print index()