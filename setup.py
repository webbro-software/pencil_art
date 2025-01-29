from setuptools import setup, find_packages

setup(
    name='pencil_art',
    version='0.1.8',  
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'opencv-python',  
    ],
    author='Usmonov Shoxruxmirzo',
    author_email='usmonovshohruxmirzo@gmail.com',
    description='Pencil Art Generator from Images',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/webbro-software/pencil-art',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
