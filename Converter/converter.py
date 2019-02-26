import bs4
import re


class Converter:
    def __init__(self):
        self.soup = None
        self.replaced = []
        self.rules = []

    def convert(self, s, rules, outputs):
        self.rules = rules
        self.replaced = []
        self.soup = bs4.BeautifulSoup(s, 'html.parser')
        matching_tags = self.get_matching_tags(self.rules, self.get_list_of_tags())
        self.replace(self.get_dict_of_old_and_new_tags(matching_tags, outputs))
        return str(self.soup)

    def get_dict_of_old_and_new_tags(self, tags, outputs):
        tag_dict = {}
        for k, v in tags.items():
            print(k, v, '\n')
            for tag in v:
                tag_dict[tag] = outputs[1].output.make_tag(tag)
        return tag_dict

    def get_list_of_tags(self):
        return self.soup.find_all()

    def get_matching_tags(self, rules, tags):
        groups = {}
        for tag in tags:
            groups = self.merge_dicts(groups, self.test_if_tag_matches_any_rules(rules, tag))
        return groups

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
                try:
                    tag_list_with_group_ids[g_int + 1].append(tag)
                except KeyError:
                    tag_list_with_group_ids[g_int + 1] = [tag]
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

    def find_all_from_contents(self, content, sources):
        results = {}
        for s in sources:
            if content in s.contents[0]:
                results[s] = s.contents[0]
        return results

    def replace(self, old_new_dict):
        for k, v in old_new_dict.items():
            new_tag = v
            k.replaceWith(new_tag)

    def replace_embed_frame_with_link(self, frames):
        for frame in frames:
            original_href = frame['src']
            href = 'https://www.youtube.com/watch?v=' + original_href[original_href.rfind('/') + 1:]
            print(href)
            new_tag = self.soup.new_tag('a')
            new_tag.string = href
            new_tag['href'] = href
            frame.replaceWith(new_tag)
            self.replaced.append(href)
            print('replaced: ' + str(new_tag))

    def find_indexes_of_new_tags(self, html):
        indexes = []
        for t in self.replaced:
            re_search = re.finditer(str(t), html)
            temp = []
            for m in re_search:
                temp.append((m.start(), m.end()))
            indexes.append(temp[1])
        return indexes


def make_html_file(text):
    with open('temp_html.html', 'w+') as f:
        f.write(text)
