# import
from reddscrapper.scrap import scrapper


# context manager, with statement will call __init__ and __exit__,
with scrapper(teardown=False) as BOT:
    BOT.open_url()
    # BOT.get_links()
