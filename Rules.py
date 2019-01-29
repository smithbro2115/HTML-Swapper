# noinspection PyUnusedLocal,PyMethodMayBeStatic
import bs4


class Rule:
    def __init__(self, does, condition):
        self.condition = condition
        self.does = does

    def meets_condition(self, tag: bs4.element.Tag):
        """

        :param tag: bs4.element
        :return: bool
        :rtype: bool
        """
        return False

    def passes(self, element):
        return self.does == self.meets_condition(element)


class HasAttribute(Rule):
    def meets_condition(self, tag: bs4.element.Tag):
        return tag.has_attr(self.condition)


class HasAttributeThatIs(Rule):
    def __init__(self, does, attribute, attribute_value):
        super(HasAttributeThatIs, self).__init__(does, None)
        self.attribute = attribute
        self.attribute_value = attribute_value

    def meets_condition(self, tag: bs4.element.Tag):
        for k, v in tag.attrs.items():
            for a in v:
                return k == self.attribute and a == self.attribute_value
        return False


class HasContents(Rule):
    def __init__(self, does):
        super(HasContents, self).__init__(does, None)

    def meets_condition(self, tag: bs4.element.Tag):
        return tag.contents != []


class Contains(Rule):
    def meets_condition(self, tag: bs4.element.Tag):
        for content in tag.contents:
            if content == self.condition:
                return True
        return False


class ContainsTag(Rule):
    def meets_condition(self, tag: bs4.element.Tag):
        for content in tag.contents:
            if self.is_tag(content):
                return True

    def is_tag(self, tag):
        return tag.name == self.condition
