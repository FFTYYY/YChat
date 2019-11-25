from setuptools import setup, find_packages

with open('README.md', encoding = 'utf-8') as f:
	readme = f.read()

with open('LICENSE', encoding = 'utf-8') as f:
	license = f.read()

setup(
	name					= 'LetsTalk',
	version					= '0.1.0',
	description				= '',
	long_description		= readme,
	long_description_content_type	= 'text/markdown',
	license					= license,
	author					= 'YYY',
	python_requires			= '>=3.0',
	packages				= ['LetsTalk'],
	entry_points			= {'console_scripts': ['YGLOB=YGlobalFunctions.entry:main']}
)
