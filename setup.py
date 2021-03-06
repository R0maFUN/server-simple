from setuptools import find_packages, setup

setup(
    name="server",
    entry_points={
      'console_scripts': [
        'server = server.app:main',
        'my_network = server.network'
      ]
    },
    version="0.0.1",
    python_requires='>=3.8',
    packages=["server", ],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    url="",
    license="",
    author="Konstantin Morozov",
    author_email="morozov-kst@yandex.ru",
    description="Server for GoodOK",
)
