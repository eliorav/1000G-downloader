from distutils.core import setup

setup(
    name='1000gDownloader',
    packages=['one_thousand_genomes_downloader'],
    version='0.1',
    license='MIT',
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
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6'
    ],
)
