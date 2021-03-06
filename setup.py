"""
    @TODO write docs
"""


from setuptools import setup

setup(
    name="server",
    entry_points={
        "console_scripts": [
            "server = server.app:main",
        ]
    },
    version="0.0.1",
    python_requires=">=3.8",
    packages=["server", "server.network"],
    setup_requires=["pytest-runner"],
    tests_requires=["pytest"],
    url="",
    license="",
    author="Konstantin Morozov",
    author_email="morozov-kst@yandex.ru",
    description="Server for GoodOK",
)
