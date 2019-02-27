from bs4 import BeautifulSoup, Tag
from Converter.Rules import AllOfTag, AllContents, AllAttributes, TagType
import re


class Output:
    def __init__(self, expression, **kwargs):
        self.expression = expression
        self.kwargs = kwargs
        self.saved_attributes = {}
        self.saved_contents = {}
        self.saved_tag = {}
        self.all_attributes = False
        self.all_contents = False
        self.all_of_tag = False
        self.tag_type = False
        self.empty = False
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
                elif isinstance(rule, TagType):
                    self.tag_type = True
        except IndexError:
            pass
        except TypeError:
            self.empty = True

    def make_tag(self, tag: Tag):
        if not self.empty:
            self.saved_attributes = self.get_all_attributes(tag)
            self.saved_contents = self.get_all_contents(tag)
            self.get_all_tag(tag)
            soup = BeautifulSoup(self.find_and_replace_values(), 'html.parser')
            return soup
        return tag

    def get_all_attributes(self, tag: Tag):
        unsorted_attributes = tag.attrs
        if self.all_attributes:
            print(unsorted_attributes)
            return unsorted_attributes
        attributes = {}
        for k, v in unsorted_attributes.items():
            if k in self.kwargs['attributes']:
                attributes[k] = v
        return attributes

    def add_all_attributes(self):
        s = ''
        for k, v in self.saved_attributes.items():
            if isinstance(v, list):
                values = ''
                for value in v:
                    values = f'{value} '
                s = f'{s} {k}="{values}"'
            else:
                s = f'{s} {k}="{v}"'
        return s

    def add_attribute(self, value):
        if isinstance(self.saved_attributes[value], list):
            s = ''
            for a in self.saved_attributes[value]:
                s = f'{s} {a}'
        else:
            return self.saved_attributes[value]

    def get_all_contents(self, tag: Tag):
        unsorted_contents = tag.contents
        if self.all_contents:
            return {'Contents': unsorted_contents}
        contents = {}
        for content in contents:
            if content in self.kwargs['contents']:
                content_title = self.kwargs['condition'][self.kwargs['condition'].index(str(content))]
                contents[content_title] = content
        return contents

    def get_all_tag(self, tag: Tag):
        if self.all_of_tag:
            self.saved_tag['Full Tag'] = tag
        if self.tag_type:
            self.saved_tag['Tag Type'] = tag.name

    def content(self, value):
        try:
            return str(self.saved_contents[value][0])
        except IndexError:
            return ''

    def find_and_replace_values(self):
        new_expression = self.expression
        values = [value.replace('[', '').replace(']', '') for value in re.findall('\[.*?\]', new_expression)]
        for value in values:
            try:
                if value == 'Attributes':
                    new_value = self.add_all_attributes()
                else:
                    new_value = self.add_attribute(value)
            except KeyError:
                try:
                    new_value = self.content(value)
                except KeyError:
                    new_value = self.saved_tag[value]
            print(new_value, new_expression)
            new_expression = re.sub(r"\[.*?\]", new_value, new_expression, 1)
        return new_expression
