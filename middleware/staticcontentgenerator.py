# -*- coding: utf-8 -*-
import common as cm
import pystache
import urllib

def _h(s):
	return str(s).replace("<", "").replace(">", "")

def html_view_for_addfld( id ):
	sql = "select * from properties where priceref = %s"
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

def  goods_main_view(url, url_type = None):
	_templ_res = cm.read_file_to_str("html/goods_main_view.html")
	obj = cm.prices_sql()
	img = cm.images_sql()
	id = url[-36:] 
	if (url_type == "id"):
		obj.find(id = id)
	else:
		u = urllib.quote(url[1:-6])
		#print url[1:-6], type(url[1:-6]), u
		obj.find(fantastic_url = u)
	#res = _templ_res.format(gd = obj, addfld = html_view_for_addfld(id))
	img_url = "/png/nophoto.png"
	if img.find( priceref = obj.id.val ):
		img_url = img.url.val
	res = pystache.render(_templ_res, {"gd" : obj, "addfld" : html_view_for_addfld( obj.id.val ), "img_url" : img_url})
	return res

def make_map( count ):
	_templ_res = cm.read_file_to_str("html/site-map.html")
	if count == "":
		count = "0"
	sql = """
	SELECT caption, fantastic_url FROM vg_site_db.prices 
	where organization = '{org_id}'
	order by insearch desc
	limit {count}, 50;
	""".format( org_id = cm.env["organization"].id.val, count = count )
	cursor = cm.ldb.execute( sql )
	row = cursor.fetchone()
	if row is None:
		nexthref = False
	else:
		nexthref = int( count ) + 50
	hrefs = []
	while (row is not None):
		hrefs += [{ "caption": row[0], "url": row[1] }]
		row = cursor.fetchone()
	cursor.close()
	res = pystache.render( _templ_res, { "hrefs" : hrefs, "nexthref" : nexthref } )
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