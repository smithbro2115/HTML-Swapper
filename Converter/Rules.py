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
        self.values_saved = []

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

    # def __eq__(self, other):
    #     if isinstance(other, self) and other.kwargs == self.kwargs:
    #         return True
    #     else:
    #         return False
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)


class AttributeRule(Rule):
    def __init__(self, **kwargs):
        super(AttributeRule, self).__init__(**kwargs)


class ContentRule(Rule):
    def __init__(self, **kwargs):
        super(ContentRule, self).__init__(**kwargs)


class TagRule(Rule):
    def __init__(self, **kwargs):
        super(TagRule, self).__init__(**kwargs)


class HasAttribute(AttributeRule):
    needs_condition = True
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(HasAttribute, self).__init__(**kwargs)
        self.values_saved.append(self.kwargs['condition'])
        self.readable_string = "Tag " + self.bool_to_words() + " have " + self.kwargs['condition'] + " as an attribute"

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.has_attr(self.kwargs['condition'])


class HasAttributeThatIs(AttributeRule):
    needs_condition = True
    needs_attribute = True
    needs_does = True

    def __init__(self, **kwargs):
        super(HasAttributeThatIs, self).__init__(**kwargs)
        self.values_saved.append(self.kwargs['condition'])
        self.attribute_value = self.kwargs['attribute_value']
        self.condition = self.kwargs['condition']
        self.readable_string = "Tag " + self.bool_to_words() + " have the attribute: " + self.condition + " that = " \
                               + self.attribute_value

    def meets_condition(self, tag: bs4.element.Tag):
        for k, v in tag.attrs.items():
            if isinstance(v, list):
                for a in v:
                    if k == self.condition and a == self.attribute_value:
                        return True
            else:
                if k == self.condition and v == self.attribute_value:
                    return True
        return False


class HasContents(ContentRule):
    needs_condition = False
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(HasContents, self).__init__(**kwargs)
        self.values_saved.append('Contents')
        self.readable_string = "Tag " + self.bool_to_words() + " have contents"

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.contents != []


class Contains(ContentRule):
    needs_condition = True
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(Contains, self).__init__(**kwargs)
        self.values_saved.append('Contents')
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
        self.values_saved.append(self.kwargs['condition'] + ' Tag')
        self.readable_string = "Tag " + self.bool_to_words() + " contain a(n) " + self.kwargs['condition'] + " tag"

    def meets_condition(self, tag: bs4.element.Tag):
        for content in tag.contents:
            if self.is_tag(content):
                return True

    def is_tag(self, tag):
        return tag.name == self.kwargs['condition']


class TagIs(TagRule):
    needs_condition = True
    needs_attribute = False
    needs_does = True

    def __init__(self, **kwargs):
        super(TagIs, self).__init__(**kwargs)
        self.readable_string = "Element is a(n) <" + self.kwargs['condition'] + "> tag"

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.name == self.kwargs['condition']


class All:
    pass


class AllAttributes(All):
    def __init__(self):
        self.values_saved = ['Attributes']


class AllContents(All):
    def __init__(self):
        self.values_saved = ['Contents']


class AllOfTag(All):
    def __init__(self):
        self.values_saved = ['Full Tag']


class TagType(All):
    def __init__(self):
        self.values_saved = ['Tag Type']


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


def separate_rules_into_sorted_lists(rules):
    attributes = []
    contents = []
    tags = []
    alls = []
    for rule in rules:
        if isinstance(rule, AttributeRule):
            attributes.append(rule)
        elif isinstance(rule, ContentRule):
            contents.append(rule)
        elif isinstance(rule, TagRule):
            tags.append(rule)
        elif isinstance(rule, All):
            alls.append(rule)
    return attributes, contents, tags, alls


def get_all_values_saved(rules):
    values_saved = []
    for rule in rules:
        for value_saved in rule.values_saved:
            values_saved.append(value_saved)
    return values_saved


def get_separated_list_of_values_saved(rules):
    attributes, contents, tags, alls = separate_rules_into_sorted_lists(rules)
    return get_all_values_saved(attributes), get_all_values_saved(contents), get_all_values_saved(tags), alls
