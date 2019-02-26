import bs4


class Converter:
    def __init__(self):
        self.soup = None
        self.replaced = []
        self.rules = []

    def convert(self, s, rules, outputs):
        self.rules = rules
        self.replaced = []
        self.soup = bs4.BeautifulSoup(s, 'html.parser')
        self.replace_matching_tags(self.rules, self.get_list_of_tags(), outputs)
        return str(self.soup)

    def get_dict_of_old_and_new_tags(self, tags, outputs):
        tag_dict = {}
        for k, v in tags.items():
            for tag in v:
                print(k)
                tag_dict[tag] = outputs[k].output.make_tag(tag)
        return tag_dict

    def get_dict_of_old_and_new_tag(self, tag_with_group, outputs):
        tag_dict = {}
        for group_id, tag in tag_with_group.items():
                tag_dict[tag] = outputs[group_id].output.make_tag(tag)
        return tag_dict

    def get_list_of_tags(self):
        return self.soup.find_all()

    def replace_matching_tags(self, rules, tags, outputs):
        for tag in tags:
            old_new = self.get_dict_of_old_and_new_tag(self.test_if_tag_matches_any_rules(rules, tag), outputs)
            self.replace(old_new)

    @staticmethod
    def merge_dicts(dict_1, dict_2):
        new_dict = dict_1
        for k, v in dict_2.items():
            for tag in v:
                try:
                    new_dict[k].append(tag)
                except KeyError:
                    new_dict[k] = [tag]
        return new_dict

    def test_if_tag_matches_any_rules(self, rules, tag):
        tag_list_with_group_ids = {}
        for group, g_int in zip(rules, range(len(rules))):
            if self.test_if_tag_matches_group(group, tag):
                tag_list_with_group_ids[g_int + 1] = tag
        return tag_list_with_group_ids

    def test_if_tag_matches_group(self, group, tag):
        for or_group in group:
            if self.test_if_tag_matches_or_group(or_group, tag):
                return True
        return False

    def test_if_tag_matches_or_group(self, or_group, tag):
        for rule in or_group:
            if not rule.passes(tag):
                return False
        return True

    def replace(self, old_new_dict):
        for k, v in old_new_dict.items():
            new_tag = v
            string_soup = str(self.soup).replace(str(k), str(new_tag))
            self.soup = bs4.BeautifulSoup(string_soup, 'html.parser')


def make_html_file(text):
    with open('temp_html.html', 'w+') as f:
        f.write(text)
