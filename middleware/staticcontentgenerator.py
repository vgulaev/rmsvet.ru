# -*- coding: utf-8 -*-
import common as cm

def _h(s):
	return str(s).replace("<", "").replace(">", "")

def  goods_main_view(url):
	_templ_res = cm.read_file_to_str("html/goods_main_view.html")
	obj = cm.googs_sql()
	obj.find(id = cm._Q(url[-36:]))
	res = _templ_res.format(gd = obj)
	return res