#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test module
"""

# pylint: disable=import-error
from py2glsl.enum.glsl_type import GlslType
from py2glsl.enum.glsl_varname import GlslVarName
from py2glsl.enum.glsl_location import GlslLocation
from py2glsl.enum.glsl_io_vartype import GlslIOVarType
from py2glsl.shader.base import ShaderBase
from py2glsl.shader.statement.lib_base import ShaderStdLib
from py2glsl.shader.statement.io_var import ShaderIOVar
from py2glsl.shader.statement.uniform import ShaderUniform
from py2glsl.shader.statement.action.solid_color import SolidColorAction

COLORTEMP = ShaderUniform('colorTemp', lambda: 300.0, GlslType.Float)
class TestShader(ShaderBase):
    """Test shader."""

    lib = ShaderStdLib(['temp2rgb'])
    fcolor = ShaderIOVar(
        GlslVarName.FragColor,
        GlslIOVarType.Out,
        GlslType.Vec4,
        GlslLocation.FragColor,
    )
    color_temp = COLORTEMP
    solidcolor = SolidColorAction(lambda: COLORTEMP.name, GlslVarName.FragColor)

def main():
    """Main function"""
    print(TestShader.shader_code)

if __name__ == "__main__":
    main()
