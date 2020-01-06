# Copyright 2020 Zachary Frost
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
"""Define ShaderProgram class."""

from typing import List, Type, Optional

from py2glsl.shader.base import ShaderBase
from py2glsl.enum.gl_shader_type import GlShaderType

# pylint: disable=import-error
import OpenGL.GL as GL
# pylint: enable=import-error


class ShaderProgram:
    """OpenGL shader program wrapper for use with shader classes."""

    # pylint: disable=no-self-use
    def __init__(self, *args: Type[ShaderBase]):
        self.__shaders: List[ShaderBase] = []
        for s in args:
            self.__shaders.append(s())

        self.id: Optional[int] = None

    def compile(self) -> bool:
        """Compile shader program."""
        success = True
        for s in self.__shaders:
            code = s.__class__.shader_code
            shader_type = s.shader_type
            if isinstance(code, str):
                success = success and s.compile(code)
            else:
                raise RuntimeError(
                    'Failed to compile `{0}` shader: No source code.'.format(
                        GlShaderType(shader_type).name
                    )
                )
            # Don't continue if compilation fails
            if not success:
                break
        if not success:
            return False

        shader_ids = [s.id for s in self.__shaders]
        program_id = GL.glCreateProgram()
        for s_id in shader_ids:
            if isinstance(s_id, int):
                GL.glAttachShader(program_id, s_id)
        GL.glLinkProgram(program_id)

        status = GL.glGetProgramiv(program_id, GL.GL_LINK_STATUS)
        if not status:
            info = GL.glGetProgramInfoLog(program_id)
            print('Failed to link program:'.format())
            # Indent info log
            info_lines = str(info.decode('utf-8')).split('\n')
            print('\n'.join(map(lambda s: '  ' + s, info_lines)))
            # Return False on failure
            return False

        self.id = program_id
        return True

    def bind(self):
        """Make this shader program the current one."""
        if self.id is not None:
            GL.glUseProgram(self.id)

    def unbind(self):
        """Unbind the current shader program."""
        GL.glUseProgram(0)
