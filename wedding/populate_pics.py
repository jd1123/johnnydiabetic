# from django.core.management import setup_environ
# import settings
# setup_environ(settings)

from os import listdir
from os.path import isfile, join
from wedding.models import WeddingPic

def add_files(rootdir):
    all_entries = listdir(rootdir)
    files = []
    galleries = []
    for f in all_entries:
        if isfile(join(rootdir,f)):
            files.append(('',f))
        else:
            galleries.append(f)
    for g in galleries:
        ent = listdir(join(rootdir, g))
        for e in ent:
            files.append((g, e))
    for f in files:
        if f[0] == '':
            try:
                pass
            except:
                pass
        else:
            try:
                pass
            except:
                pass


pic_dir = '/home/jw/protected'
files = [f for f in listdir(pic_dir) if isfile(join(pic_dir, f))]
for f in files:
    try:
        p = WeddingPic.objects.get(pic_name=f).pic_name
        print "Entry already exists for " + str(p)
    except:
        print "Adding entry for " + str(f)
        WeddingPic.objects.create(pic_name=f, caption='')
