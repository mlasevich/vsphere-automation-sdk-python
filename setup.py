#!/usr/bin/env python

import os

from setuptools import setup, find_packages

setup(name='vsphere-automation-sdk-unofficial',
      version='1.31.0',
      description='VMware vSphere Automation SDK for Python',
      url='https://github.com/vmware/vsphere-automation-sdk-python',
      author='VMware, Inc.',
      license='MIT',
      package_dir={'': 'src'},
      package_data={'': ['*.properties']},
      packages=find_packages(where='./src'),
      install_requires=[
        'lxml >= 4.3.0',
        'suds ; python_version < "3"',
        'suds-jurko ; python_version >= "3.0"',
        'pyVmomi >= 6.7',
        'urllib3 (>=1.25.1)',
        'werkzeug (>=0.14.1)'
      ]
      )
