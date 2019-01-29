# noinspection PyUnusedLocal,PyMethodMayBeStatic
import bs4
import re


class Rule:
    def __init__(self, does, condition):
        self.condition = condition
        self.does = does
        self.readable_string = ''

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


class HasAttribute(Rule):
    def __init__(self, does, condition):
        super(HasAttribute, self).__init__(does, condition)
        self.readable_string = "Tag " + self.bool_to_words() + " have " + self.condition + " as an attribute"

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.has_attr(self.condition)


class HasAttributeThatIs(Rule):
    def __init__(self, does, attribute, attribute_value):
        super(HasAttributeThatIs, self).__init__(does, None)
        self.attribute = attribute
        self.attribute_value = attribute_value
        self.readable_string = "Tag " + self.bool_to_words() + " have a(n) " + self.attribute + " that is " \
                               + self.attribute_value

    def meets_condition(self, tag: bs4.element.Tag):
        for k, v in tag.attrs.items():
            for a in v:
                return k == self.attribute and a == self.attribute_value
        return False


class HasContents(Rule):
    def __init__(self, does):
        super(HasContents, self).__init__(does, None)
        self.readable_string = "Tag " + self.bool_to_words() + " have contents"

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.contents != []


class Contains(Rule):
    def __init__(self, does, condition):
        super(Contains, self).__init__(does, condition)
        self.readable_string = "Tag " + self.bool_to_words() + " contain " + self.condition

    def meets_condition(self, tag: bs4.element.Tag):
        for content in tag.contents:
            if content == self.condition:
                return True
        return False


class ContainsTag(Rule):
    def __init__(self, does, condition):
        super(ContainsTag, self).__init__(does, condition)
        self.readable_string = "Tag " + self.bool_to_words() + " contain a(n) " + self.condition + " tag"

    def meets_condition(self, tag: bs4.element.Tag):
        for content in tag.contents:
            if self.is_tag(content):
                return True

    def is_tag(self, tag):
        return tag.name == self.condition


def get_rule_from_string(rule_string):
    rule_name = rule_string.replace(' ', '')
    for rule_class in Rule.__subclasses__():
        if rule_class.__name__ == rule_name:
            return rule_class
