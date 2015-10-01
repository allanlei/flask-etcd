# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='flask_etcd',
    author='Allan Lei',
    author_email='allanlei@helveticode.com',
    version='0.1',
    url='http://github.com/allanlei/flask-etcd',
    py_modules=['flask_etcd'],
    description='etcd client access in flask',
    zip_safe=False,
    install_requires=[
        'flask',
        'python-etcd>=0.3',
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
