from setuptools import setup

setup(
    name="server",
    entry_points={
      'console_scripts': [
        'server = server.app:main',
        'my_network = server.my_network'
      ]
    },
    version="0.0.1",
    packages=["server",],
    # install_requires=['server.my_network'],
    url="",
    license="",
    author="Konstantin Morozov",
    author_email="morozov-kst@yandex.ru",
    description="Server for GoodOK",
)
