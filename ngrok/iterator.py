class PagedIterator(object):
    def __init__(self, client, page, list_property):
        self.n = 0
        self.list_property = list_property
        self.client = client
        self.page = page

    def __next__(self):
        try:
            item = self.page._props[self.list_property][self.n]
            self.n += 1
            return item
        except IndexError:
            if self.page.next_page_uri is None:
                raise StopIteration
            else:
                props = self.client.api_client.request("get", self.page.next_page_uri)
                self.n = 0
                self.page = self.page.__class__(self.client, props)
                return self.__next__()
