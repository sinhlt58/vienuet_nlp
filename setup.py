import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open('requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

VIENUET_NLP  = __import__('vienuet_nlp')
VERSION      = VIENUET_NLP.__version__
AUTHOR       = VIENUET_NLP.__author__
AUTHOR_EMAIL = VIENUET_NLP.__email__
URL          = VIENUET_NLP.__url__
DESCRIPTION  = VIENUET_NLP.__doc__

setuptools.setup(
    name='vienuet_nlp',
    version=VERSION,
    url=URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=setuptools.find_packages(),
    package_dir={'vienuet_nlp': 'vienuet_nlp'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    python_requires='>=3.6.5, <4',
    platforms=['ubuntu'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: Ubuntu',
    ]
)