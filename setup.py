from setuptools import setup, find_packages

install_requires = ['torch>=0.4.0', 'Pillow']

setup(
    name='CVdevKit',
    version='1.0.0',
    description='A development kit for GAN',
    url='https://github.com/JiaminRen/CVdevKit.git',
    author='Hong Jia',
    author_email='h.jia@unsw.edu.au',
    license='Apache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='GAN Dev',
    packages=find_packages(),
    install_requires=install_requires,
)
