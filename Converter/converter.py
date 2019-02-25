import bs4
import re


class Converter:
    def __init__(self):
        self.soup = None
        self.replaced = []

    def convert(self, s, rules, outputs):
        print(s, rules, outputs)
        self.replaced = []
        self.soup = bs4.BeautifulSoup(s, 'html.parser')
        all_iframes = self.soup.find_all('iframe')
        all_p = self.soup.find_all('p')
        all_youtube_embeds = self.find_all_from_contents('https://youtu.be/', all_p)
        self.replace_embed_link_with_link(all_youtube_embeds)
        self.replace_embed_frame_with_link(all_iframes)
        text_html = str(self.soup)
        return text_html, self.find_indexes_of_new_tags(text_html)

    def find_all_from_contents(self, content, sources):
        results = {}
        for s in sources:
            if content in s.contents[0]:
                results[s] = s.contents[0]
        return results

    def replace_embed_link_with_link(self, tags):
        for k, v in tags.items():
            new_tag = self.soup.new_tag('a')
            new_tag.string = str(v)
            new_tag['href'] = (str(v))
            self.soup.find(text=str(v)).parent.replaceWith(new_tag)
            self.replaced.append(v)
            print('replaced: ' + str(new_tag))

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
