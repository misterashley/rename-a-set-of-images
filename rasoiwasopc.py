#products codes must be one per line
products = """34324P50
34324D30
34323P50
34323D31
34323C92
34236T21
34235T21
34235D30
34234T21
34234P50
34234D30
34232P50
34232D30
34231P50
34231D30
34230T21
34230D30
"""
#Your list of source images must be comma separated file names. Order is from item code to @1 and up. (@12 is max allowed.)
#this assumes your images are .jpgs.
images = "joelene.jpg,sally.jpg,smith.jpg,@3.jpg,@4.jpg,@5.jpg,bob.jpg"
# Supports up to 13 file name. The first will be product_code.jpg and then the rest will be
# product_code@1.jpg ... product_code@12.jpg

for item in products.split("\n"):
    for index,image in enumerate(images.split(",")):
        if index == 0 : print ("copy " + image + " " + item + ".jpg")
        else: print ("copy " + image + " " + item + "@" + str(index) + ".jpg")
        #print ("copy " + image + " " + item + image)
