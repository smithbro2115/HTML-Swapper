# noinspection PyUnusedLocal,PyMethodMayBeStatic
import bs4
import re


class Rule:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.does = self.kwargs['does']
        self.readable_string = ''
        self.needs_condition = False
        self.needs_attribute = False
        self.needs_does = False

    def meets_condition(self, tag: bs4.element.Tag):
        """

        :param tag: bs4.element
        :return: bool
        :rtype: bool
        """
        return False

    def passes(self, element):
        return self.does == self.meets_condition(element)

    def bool_to_words(self):
        if self.does:
            return 'does'
        else:
            return "doesn't"


class AttributeRule(Rule):
    def __init__(self, **kwargs):
        super(AttributeRule, self).__init__(**kwargs)


class ContentRule(Rule):
    def __init__(self, **kwargs):
        super(ContentRule, self).__init__(**kwargs)


class HasAttribute(AttributeRule):
    needs_condition = True
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(HasAttribute, self).__init__(**kwargs)
        self.readable_string = "Tag " + self.bool_to_words() + " have " + self.kwargs['condition'] + " as an attribute"

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.has_attr(self.kwargs['condition'])


class HasAttributeThatIs(AttributeRule):
    needs_condition = True
    needs_attribute = True
    needs_does = True

    def __init__(self, **kwargs):
        super(HasAttributeThatIs, self).__init__(**kwargs)
        self.attribute_value = self.kwargs['attribute_value']
        self.condition = self.kwargs['condition']
        self.readable_string = "Tag " + self.bool_to_words() + " have the attribute: " + self.condition + " that = " \
                               + self.attribute_value

    def meets_condition(self, tag: bs4.element.Tag):
        for k, v in tag.attrs.items():
            for a in v:
                return k == self.condition and a == self.attribute_value
        return False


class HasContents(ContentRule):
    needs_condition = False
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(HasContents, self).__init__(**kwargs)
        self.readable_string = "Tag " + self.bool_to_words() + " have contents"

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.contents != []


class Contains(ContentRule):
    needs_condition = True
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(Contains, self).__init__(**kwargs)
        self.readable_string = "Tag " + self.bool_to_words() + " contain " + self.kwargs['condition']

    def meets_condition(self, tag: bs4.element.Tag):
        for content in tag.contents:
            if content == self.kwargs['condition']:
                return True
        return False


class ContainsTag(ContentRule):
    needs_condition = True
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(ContainsTag, self).__init__(**kwargs)
        self.readable_string = "Tag " + self.bool_to_words() + " contain a(n) " + self.kwargs['condition'] + " tag"

    def meets_condition(self, tag: bs4.element.Tag):
        for content in tag.contents:
            if self.is_tag(content):
                return True

    def is_tag(self, tag):
        return tag.name == self.kwargs['condition']


class Or:
    needs_condition = False
    needs_attribute = False
    needs_does = False

    def __init__(self, **kwargs):
        self.readable_string = 'OR'
        self.kwargs = kwargs


def get_rule_from_string(rule_string):
    rule_name = rule_string.replace(' ', '')
    for rule_class in Rule.__subclasses__():
        if rule_class.__name__ == rule_name:
            return rule_class
    else:
        return Or
