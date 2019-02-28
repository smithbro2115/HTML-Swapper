from setuptools import setup

setup(name='html_swapper',
      version='0.1',
      description='Swap HTML tags',
      url='https://github.com/smithbro2115/html_swapper',
      author='smithbro',
      author_email='smithbro2115@gmail.com',
      license='Apache License 2.0',
      packages=['html_swapper'],
      install_requires=[
          'BeautifulSoup4', 'PyQt5',
      ],
      zip_safe=False)
