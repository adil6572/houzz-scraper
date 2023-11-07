

BOT_NAME = "houzz"

SPIDER_MODULES = ["houzz.spiders"]
NEWSPIDER_MODULE = "houzz.spiders"

# USER_AGENT='Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

FEED_FORMAT = 'json'  # Set the output format to JSON
FEED_URI = 'output.json'  # Set the output file name (you can change 'output.json' to your preferred filename)



REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
