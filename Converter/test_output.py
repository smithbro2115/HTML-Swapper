import unittest
from Converter.Output import Output
from Converter import Rules
import bs4


class OutputTest(unittest.TestCase):
    def setUp(self):
        html = '<a href="/users/413897/ladyfafa" title="1,661 reputation" class="comment-user owner">ladyfafa</a>'
        attributes_to_save, contents_to_save, tags, alls = Rules.get_separated_list_of_values_saved(
            [Rules.HasAttribute(does=True, condition='href')])
        self.soup = bs4.BeautifulSoup(html, 'html.parser')
        expression = '<div src="[href]">[Contents]</div>'
        self.output = Output(expression, attributes=attributes_to_save[0], alls=[Rules.AllContents()])

    def test_make_tag(self):
        self.assertEqual(str(self.output.make_tag(self.soup.find('a'))),
                         '<div src="/users/413897/ladyfafa">ladyfafa</div>')
