from os import listdir
from os.path import isfile, join
from wedding.models import WeddingPic

pic_dir = '/home/jw/protected'
files = [f for f in listdir(pic_dir) if isfile(join(pic_dir, f))]
for f in files:
    print "Adding entry for " + str(f)
    WeddingPic.objects.create(pic_name=f, caption='')
