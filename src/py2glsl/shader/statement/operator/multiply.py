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
"""Define MultiplyOperator class."""

from typing import List
from py2glsl.shader.statement.operator.base import ShaderOperatorBase
from py2glsl.shader.statement.operator.types import OperatorArg, OperatorArgData

class MultiplyOperator(ShaderOperatorBase):
    """Shader operator for multiplication."""
    def __init__(self, *args: List[OperatorArg]):
        self.__args: List[OperatorArgData] = []
        for a in args:
            if isinstance(a, OperatorArgData):
                self.__args.append(a)
            else:
                tmp_a = OperatorArgData(a, None, None)
                self.__args.append(tmp_a)

    def generate(self):
        arg_strs = [ShaderOperatorBase._eval_operator_var_name(a.var) for a in self.__args]
        return ' * '.join(arg_strs)
