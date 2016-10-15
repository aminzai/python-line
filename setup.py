import os
from setuptools import setup
from setuptools import find_packages
from pip.req import parse_requirements

package_root = os.path.abspath(os.path.dirname(__file__))
requirements_txt = os.path.join(package_root, 'requirements.txt')
requires = [
    str(r.req) for r in parse_requirements(requirements_txt, session=False)]


setup(
    name='line',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requires,
    include_package_data=True,
    author='Kang-min Wang(Aminzai)',
    author_email='lagunawang@gmail.com',
    description=('A client library for LINE BOT'),
    )
