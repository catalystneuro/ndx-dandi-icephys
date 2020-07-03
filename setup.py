# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from shutil import copy2
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup_args = {
    'name': 'ndx-dandi-icephys',
    'version': '0.3.0',
    'description': 'DandiIcephysMetadata extension.',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': 'Luiz Tauffer and Ben Dichter',
    'author_email': 'ben.dichter@gmail.com',
    'url': '',
    'license': 'BSD3',
    'install_requires': ['pynwb>=1.0.2'],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx_dandi_icephys': [
        'spec/ndx-dandi-icephys.namespace.yaml',
        'spec/ndx-dandi-icephys.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-dandi-icephys.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-dandi-icephys.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_dandi_icephys', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
