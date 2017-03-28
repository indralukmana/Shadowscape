from setuptools import setup

setup(
    name='shadowscape',
    packages=['shadowscape'],
    include_package_data=True,
    install_requires=[
        'flask', 'pyserial', 'flask_socketio'
    ],
)
