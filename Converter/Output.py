from bs4 import BeautifulSoup, Tag
from Converter.Rules import AllOfTag, AllContents, AllAttributes
import re


class Output:
    def __init__(self, expression, **kwargs):
        self.expression = expression
        self.kwargs = kwargs
        self.saved_attributes = {}
        self.saved_contents = []
        self.saved_tag = ''
        self.all_attributes = False
        self.all_contents = False
        self.all_of_tag = False
        self.determine_all_rules()

    def determine_all_rules(self):
        try:
            for rule in self.kwargs['alls']:
                if isinstance(rule, AllOfTag):
                    self.all_of_tag = True
                elif isinstance(rule, AllAttributes):
                    self.all_attributes = True
                elif isinstance(rule, AllContents):
                    self.all_contents = True
        except IndexError:
            pass

    def make_tag(self, tag: Tag):
        self.saved_attributes = self.get_all_attributes(tag)
        self.saved_contents = self.get_all_contents(tag)
        soup = BeautifulSoup(self.find_and_replace_values(), 'html.parser')
        return soup

    def get_all_attributes(self, tag: Tag):
        unsorted_attributes = tag.attrs
        if self.all_attributes:
            return unsorted_attributes
        attributes = {}
        for k, v in unsorted_attributes.items():
            if k in self.kwargs['attributes']:
                attributes[k] = v
        return attributes

    def get_all_contents(self, tag: Tag):
        unsorted_contents = tag.contents
        if self.all_contents:
            return unsorted_contents
        contents = []
        for content in contents:
            if content in self.kwargs['contents']:
                contents.append(content)
        return contents

    def find_and_replace_values(self):
        values = [value.replace('[', '').replace(']', '') for value in re.findall('\[.*?\]', self.expression)]
        for value in values:
            try:
                new_value = self.saved_attributes[value]
            except KeyError:
                try:
                    new_value = ''.join(self.saved_contents)
                except KeyError:
                    new_value = self.saved_tag
            self.expression = re.sub("[\[].*?[\]]", new_value, self.expression, 1)
        return self.expression
