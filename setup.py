import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'm5expr',
    version = '1.0',
    author = 'Eric Smith',
    author_email = 'spacewar@gmail.com',
    description = 'A simple arithmetic expression parser and evaluator',
    long_description_content = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/brouhaha/m5expr',
    packages = setuptools.find_packages(),
    install_requires = [
        'pyparsing',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Interpreters',
    ],
    python_requires='>=3.6',
)