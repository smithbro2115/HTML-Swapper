from setuptools import setup

setup(name='HTML-Swapper',
      version='0.1',
      description='Swap HTML tags',
      url='https://github.com/smithbro2115/HTML-Swapper',
      author='smithbro',
      author_email='smithbro2115@gmail.com',
      license='Apache License 2.0',
      packages=['HTML-Swapper'],
      install_requires=[
          'BeautifulSoup4', 'PyQt5',
      ],
      zip_safe=False)
