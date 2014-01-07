# coding: utf8

from distutils.core import setup

setup(
    name='Flask-WebGlEarth',
    version='0.1.3',
    author='Nikolay Nikulesko',
    author_email='nikulesko@gmail.com',
    install_requires=['Flask'],
    packages=['flask_webglearth',],
    platforms='any',
    zip_safe=False,
    url='https://github.com/nikulesko/Flask-WebGLEarth',
    description='Simple extension for Flask to use WebGl Earth',
    long_description=open('README.md').read(),
    include_package_data=True,
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
