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
"""Define ShaderUniform class."""

from typing import Callable

from py2glsl.enum.glsl_type import GlslType
from py2glsl.shader.statement.base import ShaderStatementBase

class ShaderUniform(ShaderStatementBase):
    """ShaderUniform"""

    # pylint: disable=too-few-public-methods

    def __init__(self, name, get_value: Callable, glsl_type: GlslType):
        self.__name = name
        self.__get_value = get_value
        self.__location = 0
        self.__glsl_type = glsl_type

    @property
    def value(self):
        """value"""
        return self.__get_value()

    @property
    def name(self):
        """name"""
        return self.__name

    @property
    def glsl_type(self):
        """GLSL type string"""
        return self.__glsl_type

    def __repr__(self):
        return self.generate()

    def generate(self):
        return f'uniform {self.glsl_type} {self.name};'
