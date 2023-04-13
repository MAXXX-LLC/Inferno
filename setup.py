from setuptools import setup, find_packages

setup(
    name='maxxx-inferno',
    version='0.0.1',
    description='A command-line tool designed to easily set up a flexible and scalable backend using FastAPI and Firebase.',
    author='Mihir Desai',
    author_email='madesai98@outlook.com',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'inferno=inferno:main',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
