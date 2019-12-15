# Copyright 2019 Zachary Frost
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Define the shader_base() function"""

# pylint: disable=bad-continuation
# pylint: disable=too-few-public-methods

from py2glsl.util.sequence import flatten
from py2glsl.shader.statement.base import ShaderStatementBase
from py2glsl.shader.statement.lib_base import ShaderLibBase
from py2glsl.shader.statement.uniform import ShaderUniform
from py2glsl.shader.statement.io_var import ShaderIOVar
from py2glsl.shader.statement.action.base import ShaderActionBase


class ShaderMeta(type):
    """Docstring for ShaderMeta. """

    # pylint: disable=super-init-not-called
    # pylint: disable=unused-argument

    def __init__(cls, clsname, superclasses, attributedict):
        cls.shader_code = None
        cls.glsl_version = '330 core'
        cls.shaderlibs = []
        cls.io_vars = []
        cls.actions = []
        cls.uniforms = []

        for name, statement in attributedict.items():
            if isinstance(statement, ShaderStatementBase):
                tmp_statement = cls.__process_shader_statement(
                    cls, statement
                )
                setattr(cls, name, tmp_statement)

        cls.shader_code = cls.__generate_shader_code(cls, attributedict)

    @classmethod
    def __process_shader_uniform(cls, init_cls, uniform: ShaderUniform):
        init_cls.uniforms.append(uniform)
        return uniform

    @classmethod
    def __process_shader_lib(cls, init_cls, shaderlib: ShaderLibBase):
        init_cls.shaderlibs.append(shaderlib)
        return shaderlib

    @classmethod
    def __process_shader_io_var(cls, init_cls, io_var: ShaderIOVar):
        init_cls.io_vars.append(io_var)
        return io_var

    @classmethod
    def __process_shader_action(cls, init_cls, action: ShaderActionBase):
        init_cls.actions.append(action)
        return action

    @classmethod
    def __process_shader_statement(
        cls,
        init_cls,
        statement: ShaderStatementBase,
    ):
        """process_shader_statement

        Args:
            statement (ShaderStatementBase): Shader statement to process

        Returns:
            ShaderStatementBase: `statement` with auto-generated values
        """
        if isinstance(statement, ShaderUniform):
            statement = cls.__process_shader_uniform(init_cls, statement)
        if isinstance(statement, ShaderLibBase):
            statement = cls.__process_shader_lib(init_cls, statement)
        if isinstance(statement, ShaderIOVar):
            statement = cls.__process_shader_io_var(init_cls, statement)
        if isinstance(statement, ShaderActionBase):
            statement = cls.__process_shader_action(init_cls, statement)
        return statement

    @classmethod
    def __generate_shaderlibs(cls, init_cls, attributedict):
        all_shaderlibs = init_cls.shaderlibs
        shaderlib_code_list = [slib.generate() for slib in all_shaderlibs]
        shaderlib_list = flatten(shaderlib_code_list)
        shaderlib_unique = [
            x for i, x in enumerate(shaderlib_list)
            if i == shaderlib_list.index(x)
        ]
        return '\n'.join(shaderlib_unique)

    @classmethod
    def __generate_io_vars(cls, init_cls, attributedict):
        io_vars_list = init_cls.io_vars
        io_vars_code_list = [ov.generate() for ov in io_vars_list]
        return '\n'.join(io_vars_code_list)

    @classmethod
    def __generate_actions(cls, init_cls, attributedict):
        actions_list = init_cls.actions
        actions_code_list = [ac.generate() for ac in actions_list]
        return '\n'.join(actions_code_list)

    @classmethod
    def __generate_uniforms(cls, init_cls, attributedict):
        uniforms_list = init_cls.uniforms
        uniforms_code_list = [un.generate() for un in uniforms_list]
        return '\n'.join(uniforms_code_list)

    @classmethod
    def __generate_shader_code(cls, init_cls, attributedict):
        uniforms_code = cls.__generate_uniforms(init_cls, attributedict)
        io_vars_code = cls.__generate_io_vars(init_cls, attributedict)
        shaderlib_code = cls.__generate_shaderlibs(init_cls, attributedict)
        actions_code = cls.__generate_actions(init_cls, attributedict)

        return (
            f'#version {init_cls.glsl_version}\n'
            f'\n{io_vars_code}\n'
            f'\n{uniforms_code}\n'
            f'\n{shaderlib_code}\n'
            f'\nvoid main() {{\n'
            f'{actions_code}\n'
            f'}}'
        )

class ShaderBase(metaclass=ShaderMeta):
    """Wrapper for ShaderMeta."""
