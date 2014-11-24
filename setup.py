from setuptools import setup, find_packages

setup(
    name='lazymanssh',
    description="Lazyman's SSH config manager",
    url='https://github.com/barraponto/lazymanssh',
    version='0.0.0',
    author='Capi Etheriel',
    author_email='barraponto@gmail.com',
    maintainer='Capi Etheriel',
    maintainer_email='barraponto@gmail.com',
    packages=find_packages(),
    install_requires=['stormssh', 'click'],
    entry_points={
        'console_scripts': [
            'lazymanssh = lazymanssh.lazymanssh:lazyness'
        ]
    }
)
