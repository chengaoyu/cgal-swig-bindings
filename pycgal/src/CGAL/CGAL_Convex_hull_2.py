# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_CGAL_Convex_hull_2')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_CGAL_Convex_hull_2')
    _CGAL_Convex_hull_2 = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_CGAL_Convex_hull_2', [dirname(__file__)])
        except ImportError:
            import _CGAL_Convex_hull_2
            return _CGAL_Convex_hull_2
        try:
            _mod = imp.load_module('_CGAL_Convex_hull_2', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _CGAL_Convex_hull_2 = swig_import_helper()
    del swig_import_helper
else:
    import _CGAL_Convex_hull_2
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

import CGAL.CGAL_Kernel

def convex_hull_2(range, result):
    return _CGAL_Convex_hull_2.convex_hull_2(range, result)
convex_hull_2 = _CGAL_Convex_hull_2.convex_hull_2

def ch_bykat(range, result):
    return _CGAL_Convex_hull_2.ch_bykat(range, result)
ch_bykat = _CGAL_Convex_hull_2.ch_bykat

def ch_eddy(range, result):
    return _CGAL_Convex_hull_2.ch_eddy(range, result)
ch_eddy = _CGAL_Convex_hull_2.ch_eddy

def ch_graham_andrew(range, result):
    return _CGAL_Convex_hull_2.ch_graham_andrew(range, result)
ch_graham_andrew = _CGAL_Convex_hull_2.ch_graham_andrew

def ch_melkman(range, result):
    return _CGAL_Convex_hull_2.ch_melkman(range, result)
ch_melkman = _CGAL_Convex_hull_2.ch_melkman

def ch_jarvis(range, result):
    return _CGAL_Convex_hull_2.ch_jarvis(range, result)
ch_jarvis = _CGAL_Convex_hull_2.ch_jarvis

def lower_hull_points_2(range, result):
    return _CGAL_Convex_hull_2.lower_hull_points_2(range, result)
lower_hull_points_2 = _CGAL_Convex_hull_2.lower_hull_points_2

def upper_hull_points_2(range, result):
    return _CGAL_Convex_hull_2.upper_hull_points_2(range, result)
upper_hull_points_2 = _CGAL_Convex_hull_2.upper_hull_points_2

def ch_akl_toussaint(range, result):
    return _CGAL_Convex_hull_2.ch_akl_toussaint(range, result)
ch_akl_toussaint = _CGAL_Convex_hull_2.ch_akl_toussaint

def ch_graham_andrew_scan(range, result):
    return _CGAL_Convex_hull_2.ch_graham_andrew_scan(range, result)
ch_graham_andrew_scan = _CGAL_Convex_hull_2.ch_graham_andrew_scan

def ch_jarvis_march(range, start_p, stop_p, result):
    return _CGAL_Convex_hull_2.ch_jarvis_march(range, start_p, stop_p, result)
ch_jarvis_march = _CGAL_Convex_hull_2.ch_jarvis_march

def is_ccw_strongly_convex_2(range):
    return _CGAL_Convex_hull_2.is_ccw_strongly_convex_2(range)
is_ccw_strongly_convex_2 = _CGAL_Convex_hull_2.is_ccw_strongly_convex_2

def is_cw_strongly_convex_2(range):
    return _CGAL_Convex_hull_2.is_cw_strongly_convex_2(range)
is_cw_strongly_convex_2 = _CGAL_Convex_hull_2.is_cw_strongly_convex_2

def ch_n_point(range, n):
    return _CGAL_Convex_hull_2.ch_n_point(range, n)
ch_n_point = _CGAL_Convex_hull_2.ch_n_point

def ch_s_point(range, s):
    return _CGAL_Convex_hull_2.ch_s_point(range, s)
ch_s_point = _CGAL_Convex_hull_2.ch_s_point

def ch_e_point(range, e):
    return _CGAL_Convex_hull_2.ch_e_point(range, e)
ch_e_point = _CGAL_Convex_hull_2.ch_e_point

def ch_w_point(range, w):
    return _CGAL_Convex_hull_2.ch_w_point(range, w)
ch_w_point = _CGAL_Convex_hull_2.ch_w_point

def ch_we_point(range, w, e):
    return _CGAL_Convex_hull_2.ch_we_point(range, w, e)
ch_we_point = _CGAL_Convex_hull_2.ch_we_point

def ch_ns_point(range, n, s):
    return _CGAL_Convex_hull_2.ch_ns_point(range, n, s)
ch_ns_point = _CGAL_Convex_hull_2.ch_ns_point

def ch_nswe_point(range, n, s, w, e):
    return _CGAL_Convex_hull_2.ch_nswe_point(range, n, s, w, e)
ch_nswe_point = _CGAL_Convex_hull_2.ch_nswe_point
# This file is compatible with both classic and new-style classes.

