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
"""
Define GlslType enumeration
"""

from py2glsl.enum.base import StrEnum

class GlslType(StrEnum):
    """GLSL data types for use with shader classes.

    Each value is the GLSL name of the data type that
    the key maps to.
    """

    Bool = 'bool'
    Int = 'int'
    Float = 'float'
    Vec2 = 'vec2'
    Vec3 = 'vec3'
    Vec4 = 'vec4'
    Mat2 = 'mat2'
    Mat3 = 'mat3'
    Mat4 = 'mat4'
    Sampler2D = 'sampler2D'
