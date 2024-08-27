from setuptools import find_packages,setup
from typing import List


flag='-e .'
def reqs(file_path:str)->List[str]:

	'''
	list of requirments
	'''

	requirements=[]
	with open(file_path) as file_obj:
		requirements=file_obj.readlines()
		requirements=[r.replace("\n","") for r in requirements]
		if flag in requirements:
			requirements.remove(flag)

	return requirements
setup(
name='mlproject',
version='0.0.1',
author='Kishor',
author_email='kishormanohar.14@gmail.com',
packages=find_packages(),
install_requires=reqs('requirements.txt'))