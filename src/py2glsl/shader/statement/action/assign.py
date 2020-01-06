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
"""Define AssignAction class."""

from py2glsl.shader.statement.action.base import ShaderActionBase
from py2glsl.shader.statement.action.types import ActionVar

class AssignAction(ShaderActionBase):
    """AssignAction"""
    def __init__(self, source: ActionVar, target: ActionVar):
        self.__source = source
        self.__target = target

    @property
    def source(self):
        """source"""
        return ShaderActionBase._eval_action_var(self.__source)

    @property
    def target(self):
        """target"""
        return ShaderActionBase._eval_action_var(self.__target)

    def generate(self):
        return f'  {self.target} = {self.source};'
