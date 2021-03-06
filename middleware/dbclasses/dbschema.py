# -*- coding: utf-8 -*-
from .objsql import objsql
from .propdict import propdict

schema = { "objects" : [
    objsql( pname = "catalog_ocs",
		pprop = [
            propdict( pname = "cat_name", ptype = "VARCHAR(250)" ),
			propdict( pname = "c_id", ptype = "VARCHAR(50)" ),
			propdict( pname = "nesting_level", ptype = "INT" ),
			propdict( pname = "parent_c_id", ptype = "VARCHAR(50)" )
        ] ),
	objsql( pname = "order",
		pprop = [
			propdict( pname = "number", ptype = "VARCHAR(36)" ),
			propdict( pname = "date", ptype = "DATETIME" ),
			propdict( pname = "organization", ptype = "own:organization" ),
			propdict( pname = "partner", ptype = "own:partners" )
		],
		ptables = [
			objsql( pname = "goods", powner = "order", pprop = [
				propdict( pname = "good", ptype = "VARCHAR(500) COLLATE utf8_general_ci" ),
				propdict( pname = "quantity", ptype = "DECIMAL(10, 4)" ),
				propdict( pname = "vat", ptype = "TINYINT" ),
				propdict( pname = "price", ptype = "DECIMAL(10, 2)" ),
				propdict( pname = "vatsum", ptype = "DECIMAL(10, 2)" ),
				propdict( pname = "sum", ptype = "DECIMAL(10, 2)" )
			] )
		] ),
	objsql( pname = "goods", 
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(250)" )
		] ),
	objsql( pname = "organization",
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(250)" )
		] ),
	objsql( pname = "domains",
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(250)" ),
			propdict( pname = "organization", ptype = "own:organization" )
		] ),
	objsql( pname = "partners",
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(250) COLLATE utf8_general_ci" ),
            propdict( pname = "catalog_name", ptype = "VARCHAR(100)" )
		] ),
	objsql( pname = "prices",
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(500) COLLATE utf8_general_ci_eng_cy" ),
			propdict( pname = "fantastic_url", ptype = "TEXT" ),
			propdict( pname = "pricedate", ptype = "DATETIME" ),
			propdict( pname = "good", ptype = "own:goods" ),
			propdict( pname = "price", ptype = "DECIMAL(10, 2)" ),
            propdict( pname = "price_in", ptype = "DECIMAL(10, 2)" ),
            propdict( pname = "category", ptype = "own:catalog" ),
			propdict( pname = "vat", ptype = "INT" ),
			propdict( pname = "currency_in", ptype = "VARCHAR(50)" ),
			propdict( pname = "organization", ptype = "own:organization" ),
			propdict( pname = "synctag", ptype = "VARCHAR(50)" ),
			propdict( pname = "partner", ptype = "VARCHAR(50)" ),
			propdict( pname = "insearch", ptype = "BOOL" )
		] ),
	objsql( pname = "categoryprices",
		pprop = [
			propdict( pname = "price", ptype = "own:prices" ),
			propdict( pname = "category", ptype = "own:category" ),
		] ),
	objsql( pname = "category",
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(200) COLLATE utf8_general_ci_eng_cy" ),
			propdict( pname = "partner", ptype = "own:partners" ),
			propdict( pname = "level", ptype = "INT" ),
			propdict( pname = "parent", ptype = "own:category" )
		] ),
	objsql( pname = "currency",
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(50)" ),
			propdict( pname = "partner", ptype = "own:partners" ),
			propdict( pname = "ratedate", ptype = "DATE" ),
			propdict( pname = "rate", ptype = "DECIMAL(10, 4)" )
		] ),
	objsql( pname = "properties",
		pprop = [
			propdict( pname = "priceref", ptype = "own:prices" ),
			propdict( pname = "caption", ptype = "VARCHAR(250)" ),
			propdict( pname = "value", ptype = "VARCHAR(250)" )
		] ),
	objsql( pname = "users",
		pprop = [
			propdict( pname = "username", ptype = "VARCHAR(150)" ),
			propdict( pname = "userpassword", ptype = "VARCHAR(20)" )
		] ),
	objsql( pname = "sessions",
		pprop = [
			propdict( pname = "session", ptype = "VARCHAR(150)" ),
			propdict( pname = "username", ptype = "VARCHAR(150)" )
		] ),
	objsql( pname = "images",
		pprop = [
			propdict( pname = "caption", ptype = "VARCHAR(250)" ),
			propdict( pname = "priceref", ptype = "own:prices" ),
			propdict( pname = "url", ptype = "VARCHAR(250)" )
		] )
	] }
