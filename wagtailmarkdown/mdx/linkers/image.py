# vim:sw=4 ts=4 et:
# Copyright (c) 2015 Torchbox Ltd.
# felicity@torchbox.com 2015-09-14
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#

from django.core.exceptions import ObjectDoesNotExist
from markdown.util import etree
from wagtail import wagtailimages

# TODO: Default spec and class should be configurable, because they're
# dependent on how the project is set up.  Hard-coding of 'left',
# 'right' and 'full-width' should be removed.


class Linker:
    @staticmethod
    def run(fname, optstr):
        opts = {'spec': 'width-500', 'classname': 'left'}

        for opt in optstr:
            bits = opt.split('=', 1)
            opt = bits[0]
            value = ''

            if len(bits) > 1:
                value = bits[1]

            width = None
            height = None

            if opt == 'left':
                opts['classname'] = 'left'
            elif opt == 'right':
                opts['classname'] = 'right'
            elif opt == 'full':
                opts['classname'] = 'full-width'
            elif opt == 'width':
                if not value.isdigit():
                    raise ValueError("An integer was expected for key '{1}'. Found '{2}'".format(opt), value)
                opts['spec'] = "width-%d" % int(value)
            elif opt == 'height':
                if not value.isdigit():
                    raise ValueError("An integer was expected for key '{1}'. Found '{2}'".format(opt), value)
                opts['spec'] = "height-%d" % int(value)

        try:
            image = wagtailimages.get_image_model().objects.get(title=fname)
        except ObjectDoesNotExist:
            return '[image %s not found]' % (fname,)

        rendition = image.get_rendition(opts['spec'])

        a = etree.Element('a')
        a.set('data-toggle', 'lightbox')
        a.set('data-type', 'image')
        a.set('href', image.file.url)
        img = etree.SubElement(a, 'img')
        img.set('src', rendition.url)
        img.set('class', opts['classname'])
        img.set('width', str(rendition.width))
        img.set('height', str(rendition.height))
        return a
