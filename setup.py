#!/usr/bin/env python3


from robotpy_build.setup import Setup

s = Setup()
s.prepare()

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
except ImportError:
    pass
else:

    class bdist_wheel(_bdist_wheel):
        def get_tag(self):
            self.root_is_pure = False
            _impl, _abi_tag, plat_name = _bdist_wheel.get_tag(self)
            self.root_is_pure = True
            return ("py36", "none", plat_name)

    s.setup_kwargs["cmdclass"]["bdist_wheel"] = bdist_wheel

s.run()
