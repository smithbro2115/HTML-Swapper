import bs4


class Output:
    def __init__(self, **kwargs):
        self.attributes = kwargs['attributes']
        self.contents = kwargs['contents']
        self.tag_type = kwargs['tag_type']
        self.all_contents = kwargs['all contents']
        self.all_attributes = kwargs['all attributes']

    def make_tag(self, attributes: dict, contents: list):
        soup = bs4.BeautifulSoup()
        tag = soup.new_tag(self.tag_type, attrs=self.get_all_attributes(attributes))
        tag.append(self.get_all_contents(contents))
        return tag

    def get_all_attributes(self, unsorted_attributes):
        if self.all_attributes:
            return unsorted_attributes
        attributes = {}
        for k, v in unsorted_attributes.items():
            if k in self.attributes.keys():
                attributes[k] = v
        return attributes

    def get_all_contents(self, unsorted_contents):
        if self.all_contents:
            return unsorted_contents
        contents = []
        for content in contents:
            if content in self.contents:
                contents.append(content)
        return contents
