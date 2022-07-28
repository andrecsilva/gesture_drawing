#!/bin/env python
from pathlib import Path
import sys, os, django

#sys.path.append("$HOME/programming/django/drawing") 
#print(sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gesture_drawing.settings")

django.setup()

from gesture.models import Reference,Tag

if __name__=='__main__':

    if len(sys.argv) < 3:
        print('Usage: ./auto_tagger folder tag1 tag2 tag3 ...')
        print('folder should be the full path relative to the media folder')
        sys.exit()

    folder = sys.argv[1]

    tags = sys.argv[2:]
    actual_tags = []
    for t in tags:
        qs = Tag.objects.filter(name=t)
        if qs.count()>0:
            actual_tags.append(qs[0])
        else:
            print(f'{t} : invalid tag')

    all_refs = Reference.objects.filter(image__startswith=folder)

    for r in all_refs:
        for t in actual_tags:
            r.tags.add(t)
            r.save()
