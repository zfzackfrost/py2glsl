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
"""Define ShaderIOVar class."""

# pylint: disable=bad-continuation

from py2glsl.shader.statement.base import ShaderStatementBase
from py2glsl.enum.glsl_io_vartype import GlslIOVarType
from py2glsl.enum.glsl_type import GlslType


class ShaderIOVar(ShaderStatementBase):
    """ShaderIOVar"""
    def __init__(
        self, name: str, direction: GlslIOVarType, glsl_type: GlslType,
        location: int
    ):
        self.__name = name
        self.__glsl_type = glsl_type
        self.__location = location if location is not None else -1
        self.__direction = direction

    @property
    def direction(self):
        """direction"""
        return self.__direction

    @property
    def name(self):
        """name"""
        return self.__name

    @property
    def glsl_type(self):
        """GLSL type name"""
        return self.__glsl_type

    @property
    def location(self):
        """GLSL variable location"""
        return self.__location

    def generate(self):
        return f'layout (location = {self.location}) {self.direction} {self.glsl_type} {self.name};'
