__author__ = 'Christopher Arndt'
__version__ = '1.1'

import argparse
import logging
import os
import sys
import tempfile

from os.path import basename, join, splitext

import console
import editor

from markdown2pdf import markdown2pdf


def make_pdf_filename(fn):
    return splitext(basename(fn))[0] + '.pdf'


def main(args=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--current-file', action='store_true',
                    help='Use file currently opened in editor as input')
    ap.add_argument('-e', '--edit-buffer', action='store_true',
                    help='Use content of current editor buffer as input')
    ap.add_argument('infile', nargs='?', help='Input file name')

    args = ap.parse_args(args if args is not None else sys.argv[1:])

    if args.edit_buffer or args.current_file:
        pdf_bn = make_pdf_filename(editor.get_path())

    if args.current_file:
        with open(editor.get_path()) as f:
            md = f.read()
    elif args.edit_buffer:
        md = editor.get_text()
    elif args.infile:
        pfd_bn = make_pdf_filename(args.infile)
        with open(args.infile) as f:
            md = f.read()
    else:
        pdf_bn = 'markdown2pdf.pdf'

        try:
            choice = console.alert('Markdown to PDF', '',
                                   'Show README', 'Convert Clipboard', 'Convert URL')
        except KeyboardInterrupt:
            return

        if choice == 1:
            md = __doc__
        elif choice == 2:
            import clipboard
            md = clipboard.get()
        elif choice == 3:
            import re
            import clipboard
            try:
                cb = clipboard.get().strip()
                if not re.search('^(ht|f)tps?://', cb):
                    cb = ''
                url = console.input_alert('Enter URL', 'Download Markdown from URL:',
                                          cb, 'Download')
            except KeyboardInterrupt:
                return
            else:
                import urllib2
                import urlparse
                try:
                    r = urllib2.urlopen(url)
                except urllib2.URLError as exc:
                    print(exc)
                    console.hud_alert("Download error (see console)", 'error')
                    return
                else:
                    md = r.read()

                url = urlparse.urlparse(r.geturl())
                fn = make_pdf_filename(url.path)
                if fn:
                    pdf_bn = fn

    if not md:
        return

    tempdir = tempfile.mkdtemp()
    pdf_path = join(tempdir, pdf_bn)
    console.show_activity()
    status = markdown2pdf(md, pdf_path)
    console.hide_activity()

    try:
        choice = console.alert('Select Ouput', '',
                               'Save to file...', 'Open in...', 'View')
    except KeyboardInterrupt:
        return

    if choice == 1:
        try:
            filename = console.input_alert("Filename",
                                           "Enter PDF output filename\n(will overwrite existing files!):",
                                           pdf_bn, 'Save')
            os.rename(pdf_path, filename)
        except KeyboardInterrupt:
            return
        except (IOError, OSError) as exc:
            console.alert("Error", "Error writing PDF file:\n\n%s" % exc)
            return 1
    elif choice == 2:
        console.open_in(pdf_path)
    elif choice == 3:
        console.quicklook(pdf_path)

    try:
        os.unlink(pdf_path)
        os.rmdir(tempdir)
    except:
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main(sys.argv[1:])