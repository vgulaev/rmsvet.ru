# -*- coding: utf-8 -*-
import common as cm
import pystache
import urllib

def _h(s):
	return str(s).replace("<", "").replace(">", "")

def html_view_for_addfld( id ):
	sql = "select * from additionalfields where price_id = %s"
	cursor = cm.ldb.execute(sql, [ id ])
	row = cursor.fetchone()
	res = []
	while (row is not None):
		if not (row[1][0 : 2] == "__"):
			el = {"name" : row[1], "value" : row[3]}
			res += [el]
		row = cursor.fetchone()
	cursor.close()
	#el = {"name" : "organization", "value" : cm.env["organization"]}
	#res += [el]
	return res

def  goods_main_view(url):
	_templ_res = cm.read_file_to_str("html/goods_main_view.html")
	obj = cm.prices_sql()
	img = cm.images_sql()
	id = url[-36:] 
	obj.find(id = id)
	#res = _templ_res.format(gd = obj, addfld = html_view_for_addfld(id))
	img_url = "/png/nophoto.png"
	if img.find(price_id = obj.id.val):
		img_url = img.url.val
	res = pystache.render(_templ_res, {"gd" : obj, "addfld" : html_view_for_addfld( id ), "img_url" : img_url})
	return res

import statistics
def stat():
	_templ_res = cm.read_file_to_str("html/stat.html")
	s = statistics.stat_info()
	ls = []
	total = 0
	for e in s:
		s[e]["name"] = e
		ls += [s[e]]
		total += s[e]["lines"]
	res = pystache.render(_templ_res, {"stats": ls, "total": total, "dol": total * 12})
	return res