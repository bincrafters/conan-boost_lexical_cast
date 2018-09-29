#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostLexical_CastConan(base.BoostBaseConan):
    name = "boost_lexical_cast"
    url = "https://github.com/bincrafters/conan-boost_lexical_cast"
    lib_short_names = ["lexical_cast"]
    header_only_libs = ["lexical_cast"]
    cycle_group = "boost_level8group"
    b2_requires = [
        "boost_level8group",
    ]


