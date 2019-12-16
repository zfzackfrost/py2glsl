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
"""Define OpenGL provider base class."""

from abc import ABC, abstractmethod
from typing import List, Callable

UpdateCallback = Callable[[float], None]
"""An update callback for the OpenGL provider."""


class OpenGLProviderBase(ABC):
    """Abstract class for interfacing with OpenGL window/context library.

    Allows the window library to be swapped.
    """
    def __init__(self):
        self.__update_callbacks: List[UpdateCallback] = []

    @abstractmethod
    def main(self, argv):
        """Main function.

        Open a window and run the main loop.

        Args:
            argv (list): List of command line arguments
        Returns:
            int: Program return code
        """

    @property
    def on_update(self):
        """All registered update callbacks chained together."""
        def inner_on_update(delta):
            for cb in self.__update_callbacks:
                cb(delta)

        return inner_on_update

    def add_update_callback(self, cb: UpdateCallback):
        """Register an update callback.

        Args:
            cb (UpdateCallback): The callback to register.
        """
        self.__update_callbacks.append(cb)
        self.__update_callbacks = [
            x for i, x in enumerate(self.__update_callbacks)
            if i == self.__update_callbacks.index(x)
        ]
