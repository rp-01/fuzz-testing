import random
import os
import subprocess
count =0
#open jpg file and import as byte array and close stream
with open("cross.jpg", "rb") as image:
    f = image.read()
    b = bytearray(f)
    f = image.close()
b1 = bytearray()

count = 0
for i in range(0,len(b)-1):
    # assign original image bytearray to another bytearray
    b1  = bytearray(b)
    # modify elements with random values at every loop run
    b1[i] = random.randint(1,254)        
    #check if the value is modified by comparing with original image byte array
    if b1[i]==b[i]:
        b1[i]=b1[i]+1
        
    # create new jpg with modified byte array and close stream
    with open("testing-{}.jpg".format(i), "wb") as image:
        f = image.write(b1)
        f = image.close()
    
    # call jpg2bmp executable
    import subprocess
    p = subprocess.Popen(["./jpg2bmp","testing-{}.jpg".format(i),"tmp.bmp"])
    p.wait()

    # capture exit code of executable file
    rc = p.returncode
    # check if error occured and remove jpg fiels that don't cause bug
    if rc == -11:
        # keep counter of how many times bugs occured.
        count=count+1
        print("FuzzInputNum = {}, fileName: testing-{}.jpg".format(i,i))
    else:
        #Remove modified jpg file if bugs not encountered.
        os.remove("testing-{}.jpg".format(i))
        
#print simple message indicating, number of times bugs encountered.
print("total number of time bugs occured = {}.".format(count))
