#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script for PyQt5 support.
"""
import sys
# pylint: disable=import-error
from py2glsl.gl_provider.pyqt5 import PyQt5OpenGLProvider

from py2glsl.enum.glsl_type import GlslType
from py2glsl.enum.glsl_varname import GlslVarName
from py2glsl.enum.glsl_location import GlslLocation
from py2glsl.enum.glsl_io_vartype import GlslIOVarType
from py2glsl.shader.base import FragmentShader, VertexShader
from py2glsl.shader.statement.lib_base import ShaderStdLib
from py2glsl.shader.statement.io_var import ShaderIOVar
from py2glsl.shader.statement.uniform import ShaderUniform
from py2glsl.shader.statement.action.assign import AssignAction
from py2glsl.shader.statement.operator.multiply import MultiplyOperator

VPOS = ShaderIOVar(
    GlslVarName.VertPos,
    GlslIOVarType.In,
    GlslType.Vec4,
    GlslLocation.VertPos,
)
MVP = ShaderUniform('mvp', lambda: 1.0, GlslType.Mat4)


class TestVertex(VertexShader):
    """Test vertex shader."""
    vpos = VPOS
    mvp = MVP
    assign_vpos = AssignAction(
        MultiplyOperator(MVP.name, VPOS.name), GlslVarName.GlPosition
    )


COLORTEMP = ShaderUniform('colorTemp', lambda: 300.0, GlslType.Vec4)


class TestFragment(FragmentShader):
    """Test fragment shader."""

    lib = ShaderStdLib(['temp2rgb'])
    fcolor = ShaderIOVar(
        GlslVarName.FragColor,
        GlslIOVarType.Out,
        GlslType.Vec4,
        GlslLocation.FragColor,
    )
    color_temp = COLORTEMP
    solidcolor = AssignAction(lambda: COLORTEMP.name, GlslVarName.FragColor)


def _render(gl):
    gl.glClearColor(1.0, 1.0, 0.0, 1.0)


def _init(_):
    test_vert = TestVertex()
    test_vert.compile(TestVertex.shader_code)
    print(TestVertex.shader_code)
    print(test_vert.id)


def _main():
    prov = PyQt5OpenGLProvider()
    prov.add_render_callback(_render)
    prov.add_init_callback(_init)
    prov.main(sys.argv)


if __name__ == "__main__":
    _main()
