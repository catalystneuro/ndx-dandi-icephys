# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from shutil import copy2
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup_args = {
    'name': 'ndx-labmetadata-abf',
    'version': '0.1.1',
    'description': 'LabMetaData extension.',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': 'Luiz Tauffer and Ben Dichter',
    'author_email': 'ben.dichter@gmail.com',
    'url': '',
    'license': '',
    'install_requires': ['pynwb>=1.0.2'],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx_labmetadata_giocomo': [
        'spec/ndx-labmetadata-abf.namespace.yaml',
        'spec/ndx-labmetadata-abf.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-labmetadata-abf.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-labmetadata-abf.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_labmetadata_abf', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
