import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.

base = 'Win32GUI' if sys.platform == 'win32' else None
include_files = [('icons/brightness-controller.svg',
                  'icons/brightness-controller.svg')]

buildOptions = dict(packages=[], excludes=[], include_files=include_files)

executables = [
    Executable('init.py', base=base, targetName='brightness')
]

setup(name='Brightness',
      version='2.3.4',
      description='Brightness Controller',
      options=dict(build_exe=buildOptions),
      executables=executables)
