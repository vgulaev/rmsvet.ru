# -*- coding: utf-8 -*-
import codecs

eng_sym = [ "a", "c", "e", "o", "x", "m", "k", "y", "p", "t" ]
rus_sym = [ "а", "с", "е", "o", "х", "м", "к", "у", "р", "т" ]

f = codecs.open( "collation.xml", "w", "utf-8" )
f.write( """<collation name="utf8_general_ci_eng_cy" id="1033">
<rules>\n""")

for ( e, r ) in zip( eng_sym, rus_sym ):
    f.write( "<reset>{l}</reset>\n".format( l = e ) )
    f.write( "<i>{l}</i>\n".format( l = r ) )
    f.write( "<reset>{l}</reset>\n".format( l = e.upper() ) )
    f.write( "<i>{l}</i>\n".format( l = r.upper() ) )
    print( e )

f.write( """</rules>    
  </collation>""")

print( ord( "х" ) )
import sys
print( sys.version )