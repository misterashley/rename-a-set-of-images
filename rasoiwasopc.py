#products codes must be comma-seperated
products = "ASADP1SD30L,ASADP1SD30R,ASADP1SD30S,ASADP1SD32L,ASADP1SD32R,itemcode,item code,etcerta"
#list of images must be comma-seperated. Order is from item code to @1 and up. (@12 is max allowed.)
#this assumes your images are .jpgs.
images = "joelene.jpg,sally.jpg,smith.jpg,@3.jpg,@4.jpg,@5.jpg,bob.jpg"

for item in products.split(","):
    for index,image in enumerate(images.split(",")):
        if index == 0 : print ("copy " + image + " " + item + ".jpg")
        else: print ("copy " + image + " " + item + "@" + str(index) + ".jpg")
        #print ("copy " + image + " " + item + image)
        
