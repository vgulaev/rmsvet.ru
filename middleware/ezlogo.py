def ls( one ):
    return str( one.real ) + "," + str( one.imag )

g = 4 + 5j

print( g.real,  )
k = 470 / 650
c = 650

x1 = 0 + c * 1j
ca = c * 0.5 * 0.5
h = c * 0.5 * 0.866
x2 = c + c * 1j
x3 = c - ca + ( c - h ) * 1j

print( ls( x1 ), ls( x2 ), ls( x3 ) )

import math

h = 36
ah = h / math.sin( math.radians( 15 ) ) * math.cos( math.radians( 15 ) )
c2 = c * k
x4 = x1 + ( ah - h * 1j )
x5 = x2 - ( h * 2 * math.cos( math.radians( 30 ) ) + h * 1j )
dx = h * ( math.cos( math.radians( -105 ) ) - math.sin( math.radians( -105 ) ) * 1j ) 
print( abs( dx ) )
x6 = x3 + dx

#dx = ( c - c2 ) / 2 - ( ( h - h2 ) / 2 ) * 1j
#dx = (c - c2) * 1j - ( ( h - h2 ) / 2 ) * 1j + ( c - c2 ) / 2
#print( dx )

print( ls( x4 ), ls( x5 ), ls( x6 ) )
print( ls( x4 ), ls( x1 ), ls( x3 ), ls( x2 ), ls( x1 ), ls( x4 ), ls( x5 ), ls( x6 ), ls( x4 ) )

print( "Hi" )