from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="housing_price_prediction",
    version="0.0.1",
    author="Akshaj Alva",
    author_email="akshajalva0@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
