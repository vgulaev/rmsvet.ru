from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup( directories = [ "" ] )

template_dir = "html/templates/"
html_dir = "html/"

def rerender( filename ):
    t = Template( filename = template_dir + filename, input_encoding = "utf-8", output_encoding = "utf-8", lookup = mylookup )
    res = t.render()
    f = open( html_dir + filename[ : -4 ] + "html", "wb" )
    f.write( res )

def rerenderall():
    filenames = [ "index.mako", "orders.mako" ]
    for e in filenames:
        rerender( e )