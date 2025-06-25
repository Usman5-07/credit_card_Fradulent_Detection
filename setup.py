from setuptools import find_packages, setup
from typing import List


def get_requirements(packages_file_path) -> List[str]:
    requirements = []
    with open (packages_file_path) as file:
        requirements = file.readlines
        # Replace the new line escape sequence empth space. Use LIST COMPREHENSION
        requirements = [req.replace('/n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
        
        return requirements

setup(
    name='ETL Pipeline',
    version='0.0.1',
    description='Pipeline for credit card fraud detection data.',
    author='Muhammad Usman',
    packages=find_packages(),
    install_packages= get_requirements('requirements.txt')
)