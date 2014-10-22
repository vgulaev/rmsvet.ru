# -*- coding: utf-8 -*-
from objsql import objsql
from propdict import propdict
from sqlalchemy.sql.expression import column

schema = { "objects" : [
	objsql( pname = "order",
		pprop = [ 
			propdict( pname = "number", ptype = "CHAR(36)" )
		],
		ptables = [
			objsql( pname = "goods", powner = "order", pprop = [
				propdict( pname = "good", ptype = "own:prices" ),
				propdict( pname = "quantity", ptype = "DECIMAL(10, 4)" )
			] )
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