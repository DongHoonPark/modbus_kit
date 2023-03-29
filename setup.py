from setuptools import setup

setup(
    name='modbus-kit',
    version='0.0.0',
    description='Modbus GUI to test, develop modbus hardware',
    author='donghoon-park',
    author_email='donghun94@gmail.com',
    url='https://github.com/donghoonpark/modbus_kit',
    packages=['modbus_kit'],
    install_requires=[
        # list of dependencies
        'PySide6',
        'pymodbus',
        'typing_extensions',
        'QtAwesome'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'modbus-kit = modbus_kit:main',
        ]
    }
)