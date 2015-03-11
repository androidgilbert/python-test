try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config={
	'description':'my second project',
	'author':'zhouchao',
	'url':'www.keddoo.com',
	'download_url':'www.keddoo.com',
	'author_email':'android.wdmz.zc@gmail.com',
	'version':'2',
	'install_requires':['nose'],
	'packages':['ex47'],
	'scripts':[]
	'name':'projectname'
}
setup(**config)