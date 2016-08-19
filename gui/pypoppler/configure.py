# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import os
import sipconfig
import PyQt4.pyqtconfig as pyqtconfig

# The name of the SIP build file generated by SIP and used by the build
# system.
build_file = "QtPoppler.sbf"

# Get the PyQt configuration information.
config = pyqtconfig.Configuration()


print(dir(config))
# Get the extra SIP flags needed by the imported qt module.  Note that
# this normally only includes those flags (-x and -t) that relate to SIP's
# versioning system.
qt_sip_flags = config.pyqt_sip_flags

# Run SIP to generate the code.  Note that we tell SIP where to find the qt
# module's specification files using the -I flag.
os.system(" ".join([config.sip_bin, "-c", ".", "-b", build_file, "-I", config.pyqt_sip_dir, qt_sip_flags, "poppler-qt4.sip"]))

# We are going to install the SIP specification file for this module and
# its configuration module.
installs = []

installs.append(["poppler-qt4.sip", os.path.join(config.default_sip_dir, "QtPoppler")])

installs.append(["pypopplerqt4config.py", config.default_mod_dir])

# Create the Makefile.  The QtModuleMakefile class provided by the
# pyqtconfig module takes care of all the extra preprocessor, compiler and
# linker flags needed by the Qt library.
makefile = pyqtconfig.QtGuiModuleMakefile(
    configuration=config,
    build_file=build_file,
    installs=installs
)

# Add the library we are wrapping.  The name doesn't include any platform
# specific prefixes or extensions (e.g. the "lib" prefix on UNIX, or the
# ".dll" extension on Windows).
makefile.extra_lib_dirs = [config.qt_lib_dir]
makefile.extra_libs = ["poppler-qt4"]
makefile.extra_include_dirs = [config.qt_inc_dir+"/QtXml", "/usr/include/poppler"]

# Generate the Makefile itself.
makefile.generate()

# Now we create the configuration module.  This is done by merging a Python
# dictionary (whose values are normally determined dynamically) with a
# (static) template.
content = {
    # Publish where the SIP specifications for this module will be
    # installed.
    "pypopplerqt4_sip_dir":    config.default_sip_dir,

    # Publish the set of SIP flags needed by this module.  As these are the
    # same flags needed by the qt module we could leave it out, but this
    # allows us to change the flags at a later date without breaking
    # scripts that import the configuration module.
    "pypopplerqt4_sip_flags":  qt_sip_flags
}

# This creates the helloconfig.py module from the helloconfig.py.in
# template and the dictionary.
sipconfig.create_config_module("pypopplerqt4config.py", "pypopplerqt4config.py.in", content)