from conans import ConanFile, tools, os

class BoostLexical_CastConan(ConanFile):
    name = "Boost.Lexical_Cast"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-lexical_cast"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["lexical_cast"]
    requires =  "Boost.Array/1.65.1@bincrafters/testing", \
                      "Boost.Assert/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Container/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Integer/1.65.1@bincrafters/testing", \
                      "Boost.Math/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Numeric_Conversion/1.65.1@bincrafters/testing", \
                      "Boost.Range/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing"

                      #array3 assert1 config0 container7 core2 integer3 math8 mpl5 numeric~conversion6 range7 static_assert1 throw_exception2 type_traits3

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()