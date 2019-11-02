from scrapy import cmdline

name = 'pythonPosition'

cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())


