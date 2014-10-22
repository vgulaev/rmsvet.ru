# -*- coding: utf-8 -*-
from objsql import objsql
from propdict import propdict

schema = { "objects" : [
	objsql( pname = "order",
		pprop = [ 
			propdict( pname = "number", ptype = "CHAR(36)" )
		],
		ptables = [
		] ),
	objsql( pname = "goods", 
		pprop = [ 
			propdict( pname = "caption", ptype = "CHAR(250)" )
		] ),
	objsql( pname = "organization",
		pprop = [ 
			propdict( pname = "caption", ptype = "CHAR(250)" )
		] ),
	objsql( pname = "prices",
		pprop = [ 
			propdict( pname = "good", ptype = "own:goods" ),
			propdict( pname = "price", ptype = "DECIMAL(10, 2)" )
		] )
	] }