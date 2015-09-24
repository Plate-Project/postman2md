# -*- coding:utf-8 -*-
__author__ = 'sh84.ahn@gmail.com'

import os


def convert(postman_file, multi_file=True):
    # todo : try-catch exception
    with open(postman_file, 'r') as f:
        import json
        postman_json =json.loads(f.read())

    # make dir
    dir_path = "./" + postman_json['name']

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    from markdownwriter import MarkdownWriter
    from markdownwriter import MarkdownTable

    for req in postman_json['requests']:

        if multi_file:
            mode = 'w+'
            md_file_name = req['name'] + '.md'
        else:
            mode = 'a+'
            md_file_name = postman_json['name'] + '.md'


        with open(os.path.join(dir_path, md_file_name), mode) as f:
            md = MarkdownWriter()
            md.addHeader(req['name'], 1)
            md.addSimpleLineBreak()
            if len(req['description']) > 0:
                md.addText('-' + req['description'])
                md.addSimpleLineBreak()
            md.addHeader('Resource URL', 2)
            md.addSimpleLineBreak()

            md.addSpace()
            md.addText('-')
            md.addSpace()
            md.addText("[" + req['method'] + "] : ")

            method = req['method'].upper()
            if method == 'GET':
                from urlparse import urlparse
                o = urlparse(req['url'])
                base_url = o.scheme + "://" + o.netloc

                md.addLink(base_url, base_url)
            else:

                md.addLink(req['url'], req['url'])

            md.addDoubleLineBreak()

            if method == 'GET':
                if o.query:
                    md.addHeader('Request Parameters', 2)
                    md.addSimpleLineBreak()
                    mt = MarkdownTable(['name', 'type', 'example value'])

                    from urlparse import parse_qs
                    qs = parse_qs(o.query)
                    for k, v in qs.items():
                        mt.addRow([k, 'text', v[0]])
                    md.addTable(mt)
                    md.addDoubleLineBreak()
            else:
                if req['data']:
                    md.addHeader('Request Parameters', 2)
                    md.addSimpleLineBreak()
                    mt = MarkdownTable(['name', 'type', 'example value'])

                    for d in req['data']:
                        mt.addRow([d['key'], d['type'], d['value']])

                    md.addTable(mt)
                    md.addDoubleLineBreak()

            md.addHeader('Request example:', 3)
            if method == 'GET':
                md.addCodeBlock(req['url'])
            else:
                qs = {}
                for d in req['data']:
                    qs[d['key']] = d['value']
                from urllib import urlencode
                post_qs = urlencode(qs)
                md.addCodeBlock(req['url'] + "\n" + post_qs)

            md.addDoubleLineBreak()

            f.write(md.getStream())
