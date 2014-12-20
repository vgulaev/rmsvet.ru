from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup( directories = [ "" ] )

def rerender( filename ):
    t = Template( filename = "html/templates/index.mako", input_encoding = "utf-8", output_encoding = "utf-8", lookup = mylookup )
    res = t.render()
    f = open( "html/index.html", "wb" )
    f.write( res )