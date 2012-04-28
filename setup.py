#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(
    name = "yandex-dummy",
    version = "0.0.1-4",
    description = "Yandex Dummy",
    long_description = "Yandex Dummy Application",
    url = "https://hg.yandex-team.ru/dummy",
    author = "Andrey Sibiryov",
    author_email = "me@kobology.ru",
    license = "Proprietary",
    platforms = ["Linux", "BSD", "MacOS"],
    packages = ["yandex.dummy"],
    requires = ["cocaine"]
)
