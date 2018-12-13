#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostLexical_CastConan(base.BoostBaseConan):
    name = "boost_lexical_cast"
    url = "https://github.com/bincrafters/conan-boost_lexical_cast"
    lib_short_names = ["lexical_cast"]
    header_only_libs = ["lexical_cast"]
    cycle_group = "boost_cycle_group_b"
    b2_requires = ["boost_cycle_group_b"]
