from bs4 import BeautifulSoup, Tag
import re


class Output:
    def __init__(self, expression, **kwargs):
        self.expression = expression
        self.kwargs = kwargs
        self.saved_attributes = {}
        self.saved_contents = {}
        self.saved_tag = ''

    def make_tag(self, tag: Tag):
        if self.kwargs['use tag']:
            tag_type = tag.name
            self.saved_tag = tag_type
        else:
            tag_type = self.kwargs['tag type']
        self.saved_attributes = self.get_all_attributes(tag)
        self.saved_contents = self.get_all_contents(tag)
        soup = BeautifulSoup()
        new_tag = soup.new_tag(tag_type, attrs=self.get_all_attributes(tag))
        new_tag.append(self.get_all_contents(tag))
        return tag

    def get_all_attributes(self, tag: Tag):
        unsorted_attributes = tag.attrs
        if self.kwargs['all attributes']:
            return unsorted_attributes
        attributes = {}
        for k, v in unsorted_attributes.items():
            if k in self.kwargs['attributes']:
                attributes[k] = v
        return attributes

    def get_all_contents(self, tag: Tag):
        unsorted_contents = tag.contents
        if self.kwargs['all contents']:
            return unsorted_contents
        contents = []
        for content in contents:
            if content in self.kwargs['contents']:
                contents.append(content)
        return contents

    def find_and_replace_values(self):
        values = re.findall('\[.*?\]', self.expression)
        for value in values:
            try:
                new_value = self.saved_attributes[value]
            except KeyError:
                try:
                    new_value = self.saved_contents[value]
                except KeyError:
                    new_value = self.saved_tag
            edited_text = re.sub("[\[].*?[\]]", "test", new_value)
