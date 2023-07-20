from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Turkish lemmatizer'

with open('README.md', encoding='utf-8') as f:
    long = f.read()
setup(
        name="trlemma", 
        version=VERSION,
        author="Created by Abdullatif Köksal, packed by Mehmet Utku ÖZTÜRK",
        author_email="<contact@ælphard.tk>",
        description=DESCRIPTION,
        long_description=long,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[],
        python_requires='>3.9',
        keywords=['machine learning', 'nlp'],
        classifiers= [
            "Intended Audience :: Developers",
            "Natural Language :: Turkish",
            "Programming Language :: Python :: 3"
        ]
)
