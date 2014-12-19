# -*- coding: utf-8 -*-
from .objsql import objsql
from .propdict import propdict

schema = { "objects" : [
	objsql( pname = "order",
		pprop = [ 
			propdict( pname = "number", ptype = "CHAR(36)" ),
			propdict( pname = "date", ptype = "DATETIME" ),
			propdict( pname = "partner", ptype = "own:partners" )
		],
		ptables = [
			objsql( pname = "goods", powner = "order", pprop = [
				#propdict( pname = "good", ptype = "own:prices" ),
				propdict( pname = "good", ptype = "CHAR(200) COLLATE utf8_general_ci" ),
				propdict( pname = "quantity", ptype = "DECIMAL(10, 4)" ),
				propdict( pname = "price", ptype = "DECIMAL(10, 2)" ),
				propdict( pname = "sum", ptype = "DECIMAL(10, 2)" )
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
	objsql( pname = "domains",
		pprop = [ 
			propdict( pname = "caption", ptype = "CHAR(250)" ),
			propdict( pname = "organization", ptype = "own:organization" )
		] ),
	objsql( pname = "partners",
		pprop = [ 
			propdict( pname = "caption", ptype = "CHAR(250) COLLATE utf8_general_ci" )
		] ),
	objsql( pname = "prices",
		pprop = [ 
			propdict( pname = "caption", ptype = "CHAR(250) COLLATE utf8_general_ci" ),
			propdict( pname = "fantastic_url", ptype = "TEXT" ),
			propdict( pname = "good", ptype = "own:goods" ),
			propdict( pname = "price", ptype = "DECIMAL(10, 2)" ),
			propdict( pname = "vat", ptype = "INT" ),
			propdict( pname = "price_in", ptype = "DECIMAL(10, 2)" ),
			propdict( pname = "currency_in", ptype = "CHAR(50)" ),
			propdict( pname = "organization", ptype = "own:organization" ),
			propdict( pname = "synctag", ptype = "CHAR(50)" ),
			propdict( pname = "item_partner_id", ptype = "CHAR(50)" ),
			propdict( pname = "insearch", ptype = "BOOL" )
		] ),
	objsql( pname = "currency",
		pprop = [ 
			propdict( pname = "caption", ptype = "CHAR(50)" ),
			propdict( pname = "partner", ptype = "own:partners" ),
			propdict( pname = "ratedate", ptype = "DATE" ),
			propdict( pname = "rate", ptype = "DECIMAL(10, 4)" )
		] ),
	objsql( pname = "properties",
		pprop = [ 
			propdict( pname = "priceref", ptype = "own:prices" ),
			propdict( pname = "caption", ptype = "CHAR(250)" ),
			propdict( pname = "value", ptype = "CHAR(250)" )
		] ),
	objsql( pname = "images",
		pprop = [ 
			propdict( pname = "caption", ptype = "CHAR(250)" ),
			propdict( pname = "priceref", ptype = "own:prices" ),
			propdict( pname = "url", ptype = "CHAR(250)" )
		] )
	] }