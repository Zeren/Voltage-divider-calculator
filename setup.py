from setuptools import setup

PROJECT_NAME = 'Voltage-divider-calculator'
PROJECT_PACKAGE_NAME = 'Voltage-divider-calculator'
PROJECT_LICENSE = 'Creative Commons Zero v1.0 Universal'
PROJECT_AUTHOR = 'Jan Spacil'
PROJECT_URL = 'https://github.com/Zeren/Voltage-divider-calculator'
PROJECT_EMAIL = 'zeren.yuufana@gmail.com'

setup(
    name='Voltage-divider-calculator',
    version='1.3',
    packages=['voltdiv'],
    url=PROJECT_URL,
    license=PROJECT_LICENSE,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    description='Find appropriate resistors for voltage divider',
    python_requires='>3.9.0',
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'divider_list = voltdiv.findlist:main',
            'divider = voltdiv.finddiv:main'
        ]
    },
)
