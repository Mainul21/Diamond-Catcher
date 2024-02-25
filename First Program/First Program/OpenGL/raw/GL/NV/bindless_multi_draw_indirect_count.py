'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_bindless_multi_draw_indirect_count'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_bindless_multi_draw_indirect_count',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint)
def glMultiDrawArraysIndirectBindlessCountNV(mode,indirect,drawCount,maxDrawCount,stride,vertexBufferCount):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint)
def glMultiDrawElementsIndirectBindlessCountNV(mode,type,indirect,drawCount,maxDrawCount,stride,vertexBufferCount):pass
