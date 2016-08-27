"""
The MIT License (MIT)

Copyright (c) <2016> <Larry McCaig (aka: Larz60+ aka: Larz60p)>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
from collections import namedtuple
import pprint
import json


class ReadRecord:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.j = None

    def read_data_file(self):
        with open(self.filename, 'r') as f:
            self.j = f.read()
            return json.loads(
                self.j, object_hook=lambda data: namedtuple('data', data.keys())(*data.values()))

    def json_pp(self):
        pprint.pprint(self.j)

    def get_field(self, fieldno, key):
        return self.data.recfields[fieldno][key]

    def get_field_item(self, fieldno, itemname=None):
        try:
            return self.data.columns[fieldno][itemname]
        except Exception:
            return None


if __name__ == '__main__':
    wd = ReadRecord('StockData.json')
    wd.read_data_file()
    wd.json_pp()
