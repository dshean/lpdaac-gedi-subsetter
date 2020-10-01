import os
import sys
import logging
import subprocess
from setuptools import setup, find_packages

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
log = logging.getLogger()

# get install requirements
with open('requirements.txt') as fh:
    install_requires = fh.read().splitlines()

# run cmd from the command line
def check_output(cmd):
    return subprocess.check_output(cmd).decode('utf')

# check if GDAL is installed
gdal_output = [None] * 4
try:
    for i, flag in enumerate(("--cflags", "--libs", "--datadir", "--version")):
        gdal_output[i] = check_output(['gdal-config', flag]).strip()
except:
    log.warning('Failed to get options via gdal-config')
else:
    log.info("GDAL version from via gdal-config: {0}".format(gdal_output[3]))
# if setting GDAL version from via gdal-config
if gdal_output[3]:
    # add version information to gdal in install_requires
    gdal_index = install_requires.index('gdal')
    install_requires[gdal_index] = 'gdal=={0}'.format(gdal_output[3])

setup(
    name='lpdaac-gedi-subsetter',
    version='0.0.0.2',
    description='Program for using the LP.DAAC GEDI subsetter api for retrieving NASA GEDI data',
    url='https://github.com/tsutterley/lpdaac-gedi-subsetter',
    author='Tyler Sutterley',
    author_email='tsutterl@uw.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='LP.DAAC GEDI laser altimetry subsetting',
    packages=find_packages(),
    scripts=['lpdaac_subset_gedi.py'],
    install_requires=install_requires,
)
