try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config={
	'description':'my first project',
	'author':'zhouchao',
	'url':'www.keddoo.com',
	'download_url':'www.keddoo.com',
	'author_email':'android.wdmz.zc@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['NAME'],
	'scripts':[]
	'name':'projectname'
}
setup(**config)