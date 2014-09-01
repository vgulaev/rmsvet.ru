import sitedb

def upp():
    dbw = sitedb.dbworker()
    goods_class = dbw.class_from_table("goods")
    gd = goods_class()
    gd.id = "Tanya"
    gd.caption = "Book Tolstoy"
    gd.price = 1.33
    gd.write()
    
    res = "I wrote to base: for {ow}, position {pos}, for price {pr}".format(ow = gd.id, pos = gd.caption, pr = gd.price)
    
    #fddffdf()
    return res

print "Hello"