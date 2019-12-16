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
"""Define PyQt5 OpenGL provider."""

import time

from py2glsl.gl_provider.base import OpenGLProviderBase
# pylint: disable=import-error
from PyQt5.QtWidgets import QOpenGLWidget, QApplication
from OpenGL import GL
# pylint: enable=import-error


class GLWidget(QOpenGLWidget):
    """GLWidget"""

    # pylint: disable=invalid-name
    # pylint: disable=missing-function-docstring
    # pylint: disable=no-self-use
    def __init__(self, on_update_getter, version_profile=None, parent=None):
        super().__init__(parent)
        self.version_profile = version_profile
        self.on_update_getter = on_update_getter
        self.__last_time = time.monotonic()

    def initializeGL(self):
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        delta = time.monotonic() - self.__last_time
        on_update = self.on_update_getter()
        on_update(delta)

        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        self.update()
        self.__last_time = time.monotonic()


class PyQt5OpenGLProvider(OpenGLProviderBase):
    """OpenGL provider using PyQt5.

    See Also:
        py2glsl.gl_provider.base.OpenGLProviderBase
    """
    def __init__(self, title=None):
        super().__init__()
        self.__title = title

    def main(self, argv):
        app = QApplication(argv)
        w = GLWidget(lambda: self.on_update)
        if self.__title is not None:
            w.setWindowTitle(self.__title)
        w.show()
        return app.exec_()
