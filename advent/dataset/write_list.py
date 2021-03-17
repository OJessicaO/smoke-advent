import os 

# all_images = []
for (root,dirs,files) in os.walk('/home/jjessica/Smoky/ADVENT/data/real_smoke/images', topdown=True):

    f = open("real_smoke_list/all.txt", "w")
    for file in files:
        f.write(file + "\n")
    f.close()