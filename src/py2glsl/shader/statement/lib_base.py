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
"""Define ShaderLibBase class."""

# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods

from typing import Optional, List, Union, Any

from py2glsl.shader.statement.base import ShaderStatementBase
from py2glsl.util.sequence import flatten

def shaderlib_item(depends_on: Optional[List[Union[str, List[Any]]]] = None):
    """shaderlib_item

    Args:
        depends_on:
    """
    def sfunc_decorator(sfunc):
        def wrapper(lib):
            deps = [] if depends_on is None else depends_on
            l = [sfunc(lib)]
            d = [getattr(lib, f'generate_{x}', None) for x in deps]
            l = l + [x() for x in d if callable(x)]
            return l

        return wrapper

    return sfunc_decorator


class ShaderLibBase(ShaderStatementBase):
    # pylint: disable=no-self-use
    """ShaderStdLib"""
    def __init__(self, include_funcs):
        self.__include_funcs = include_funcs


    def generate(self):
        code_generator_names = self.__include_funcs
        code_generator_funcs = [
            getattr(self, f'generate_{x}', None) for x in code_generator_names
        ]
        code = [f() for f in code_generator_funcs if callable(f)]
        return flatten(code)


class ShaderStdLib(ShaderLibBase):
    """
    Standard shader library.
    """
    @shaderlib_item()
    def generate_saturate(self):
        """generate_saturate"""
        return (
            # yapf: disable
            'float saturate(float x) {\n'
            '  return clamp(x, 0.0f, 1.0f);\n'
            '}'
            # yapf: enable
        )

    @shaderlib_item(['saturate'])
    def generate_temp2rgb(self):
        """Color temperature to RGB
        TODO: implement
        """
        return (
            # yapf: disable
            'float temp2rgb(float K) {\n'
            '  return vec3(0.0f);\n'
            '}'
            # yapf: enable
        )
