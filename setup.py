from setuptools import find_packages, setup
from typing import List

hypendot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    retrun sthe list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if hypendot in requirements:
            requirements.remove(hypendot)

setup(
name='mlproject',
version='0.0.1',
author='Dnyaneshwar Itankar',
packages=find_packages(), 
install_requires=get_requirements('requirements.txt')    
)