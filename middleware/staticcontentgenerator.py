# -*- coding: utf-8 -*-
import common as cm

def _h(s):
	return str(s).replace("<", "").replace(">", "")

def html_view_for_addfld( id ):
	sql = "select * from additionalfields where price_id = %s"
	cm.ldb.execute(sql, [ id ])
	row = cm.ldb.cursor.fetchone()
	#while (row is not None):
	#	pass
	#return str(row)
	return ""

def  goods_main_view(url):
	_templ_res = cm.read_file_to_str("html/goods_main_view.html")
	obj = cm.prices_sql()
	id = url[-36:] 
	obj.find(id = cm._Q(id))
	res = _templ_res.format(gd = obj, addfld = html_view_for_addfld(id))
	return res