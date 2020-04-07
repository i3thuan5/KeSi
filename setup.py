from distutils.core import setup
from panpun import PANPUN


setup(
    name='KeSi',
    description='台語文NLP家私',
    long_description='Kā台文轉做電腦通利用ê格式。臺灣言語工具翻新。',
    packages=['kesi', 'kesi.butkian', 'kesi.susia', ],
    version=PANPUN,
    author='Tshuà Bûn-lī',
    author_email='ithuan@ithuan.tw',
    url='https://ithuan.tw/',
    download_url='https://github.com/i3thuan5/KeSi',
    keywords=[
        'Parser', 'Alignment', 'Taigi', 'Hanji', 'Lomaji',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
)
