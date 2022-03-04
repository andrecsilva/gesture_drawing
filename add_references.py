#!/bin/env python
from pathlib import Path
import sys, os, django

#sys.path.append("$HOME/programming/django/drawing") 
#print(sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gesture_drawing.settings")

django.setup()

from gesture.models import Reference,Tag

common_extensions = ['.jpg',
        '.gif',
        '.jpeg',
        '.png',
        '.bmp',
        '.webp'
        ]

def is_image(p):
    for ext in common_extensions:
        if p.suffix.lower() == ext:
            return True
    return False

def create_reference(pr):
    r = Reference.objects.create()
    r.image = str(pr)
    r.image.name = str(pr)
    return r

def already_exists(pr,path):
    qs = Reference.objects.filter(image__exact=pr)
    return qs.count()>0

if __name__=='__main__':
    path = Path(sys.argv[1])

    if not django.conf.settings.MEDIA_ROOT.exists():
        print(f'{django.conf.settings.MEDIA_ROOT} not found.');
        sys.exit()

    if (django.conf.settings.MEDIA_ROOT / path.name).exists():
        print(f'{path} already exists in {django.conf.settings.MEDIA_ROOT}');
        sys.exit()

    os.symlink(path, django.conf.settings.MEDIA_ROOT / path.name)

    all_pics = [p for p in path.rglob('*') if p.is_file() and is_image(p)] 

    for p in all_pics:
        pr = path.name / p.relative_to(path)
        #if not already_exists(pr,path):
        r = create_reference(pr)
        print(r)
        r.save()
