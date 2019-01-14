from scrapy import cmdline

# autohome
cmdline.execute("scrapy crawl douban ".split())

# douban
# cmdline.execute("scrapy crawl douban -o top250movie.json -s FEED_EXPORT_ENCODING=utf-8".split())