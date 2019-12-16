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
"""Math utils."""

# pylint: disable=import-error

import numpy as np
from py2glsl.util.sequence import is_sequence

def lerp(a, b, t):
    max_len = 1
    if is_sequence(a) and len(a) > max_len:
        max_len = len(a)
    if is_sequence(b) and len(b) > max_len:
        max_len = len(b)
    if is_sequence(t) and len(t) > max_len:
        max_len = len(t)

    a = a if is_sequence(a) else np.full(max_len, a)
    b = b if is_sequence(b) else np.full(max_len, b)
    t = t if is_sequence(t) else np.full(max_len, t)
    result = np.add(a, np.multiply(t, np.subtract(b, a)))
    if len(result) == 1:
        return result[0]
    return result
