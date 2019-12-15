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
"""Sequence utility functions."""

from collections.abc import Sequence

def is_sequence(s):
    """Check for sequence

    Args:
        s: object to check

    Returns:
        bool: True if `s` is a sequence (but not a `str`), False otherwise.
    """
    return isinstance(s, Sequence) and not isinstance(s, str)

def flatten(l):
    """Flatten a sequence

    Args:
        l: The sequence to flatten
    """
    contains_seq = lambda l: len(list(filter(is_sequence, l))) > 0

    def flatten_base(x):
        flat_list = []
        for sublist in x:
            if not is_sequence(sublist):
                flat_list.append(sublist)
                continue
            for item in sublist:
                flat_list.append(item)
        return flat_list

    tmp_l = list(l)
    while contains_seq(tmp_l):
        tmp_l = flatten_base(tmp_l)

    return tmp_l
