from distutils.core import setup

setup(
    name='1000gDownloader',
    packages=['1000gDownloader'],
    version='0.1',
    license='Apache License 2.0',
    description='DNA sample downloader from 1000G project',
    author='Elior Avraham',
    author_email='elior.av@gmail.com',
    url='https://github.com/eliorav/1000G-downloader',
    download_url='https://github.com/eliorav/1000G-downloader/archive/0.1.tar.gz',
    keywords=['1000G'],
    install_requires=[
        'tqdm'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6'
    ],
)
