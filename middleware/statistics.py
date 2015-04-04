# -*- coding: utf-8 -*-
import os
import git
import platform
from checon.PyLibCC import FilePath as FP

def getrootdir(): 
	if (platform.system() == "Windows"):
		dirsym = "\\"
	else:
		dirsym = "/"
	path = __file__.split( dirsym )
	rootdir = dirsym.join( path[0:-2] )
	return rootdir

def stat_info():
	#pr = r'C:\Users\MoViS\Desktop\rmsvetCLONE'
	pr = getrootdir()
	repo = git.Repo( pr )
	assert not repo.bare
	head = repo.head
	mater = head.reference
	allFile = FP( pr + "//middleware" )
	stat = {".css" : {}, ".js" : {}, ".py" : {}, ".html" : {}}
	for e in stat:
		stat[e]["ext"] = e
		stat[e]["lines1"] = 0
		stat[e]["dol1"] = 0
		stat[e]["items"] = 0
		stat[e]["avtor"] = []
		stat[e]["avtor"].append({})
		stat[e]["avtor"].append({})
		stat[e]["avtor"].append({})
		stat[e]["avtor"][0]["name"]="ROOT"
		stat[e]["avtor"][1]["name"]="Valentin"
		stat[e]["avtor"][2]["name"]="MoViS"
		for i in range(3):
			stat[e]["avtor"][i]["lines2"] = 0
			stat[e]["avtor"][i]["dol2"] = 0
	stat[".py"]["items3"] = 0
	for i in range(3):
		stat[".py"]["avtor"][i]["dol3"] = 0
		stat[".py"]["avtor"][i]["lines3"] = 0
	for file in allFile:
		fileName, fileExtension = os.path.splitext(file)
		if (( fileExtension in stat ) == True ):
			try:
				for ( commit, lines ) in repo.blame('HEAD', file):
					count = len(lines)
					autorStr = str( commit.author.name ).lower()
					if autorStr == "root":
						stat[fileExtension]["avtor"][0]["lines2"] += count
						stat[fileExtension]["avtor"][0]["dol2"] += 12 * count
						stat[".py"]["avtor"][0]["lines3"] += count
						stat[".py"]["avtor"][0]["dol3"] += 12 * count
					elif autorStr == "valentin":
						stat[fileExtension]["avtor"][1]["lines2"] += count
						stat[fileExtension]["avtor"][1]["dol2"] += 12 * count
						stat[".py"]["avtor"][1]["lines3"] += count
						stat[".py"]["avtor"][1]["dol3"] += 12 * count
					elif autorStr == "movis08":
						stat[fileExtension]["avtor"][2]["lines2"] += count
						stat[fileExtension]["avtor"][2]["dol2"] += 12 * count
						stat[".py"]["avtor"][2]["lines3"] += count
						stat[".py"]["avtor"][2]["dol3"] += 12 * count
					stat[fileExtension]["lines1"] += count
					stat[fileExtension]["dol1"] += 12 * count
				stat[fileExtension]["items"] += 1
				stat[".py"]["items3"] += 1
			except:
				pass
	return stat
