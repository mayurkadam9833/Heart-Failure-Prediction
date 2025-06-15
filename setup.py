from setuptools import find_packages,setup
from typing import List


def get_requirements()->list[str]:
    requirement_lst:list[str]=[]
    try: 
        with open("requirements.txt","r")as file: 
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != "-e .": 
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt  is not found")

    return requirement_lst

setup(
    version="0.0.1",
    author="mayur",
    packages=find_packages(),
    install_requires=get_requirements()
    )
