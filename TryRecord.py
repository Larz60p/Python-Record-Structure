"""
Example usage of Record class

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
import Record

class TryRecord:
    def __init__(self, filename=None):
        if filename:
            self.rec = Record.Record(filename)

    def try_record(self):
        stkrec = self.rec.record

        print('\nrecords:')
        for record in stkrec:
            print(record)

        keys = stkrec._asdict().keys()
        print('\nKeys:')
        for key in keys:
            print('\nkey: {}'.format(key))
            thisrec = getattr(stkrec, key)
            print('filename: {}'.format(thisrec.filename))
            print('number of columns: {}'.format(len(thisrec.columns)))
            print('column 0 column name: {}'.format(thisrec.columns[0].db_column_name))


if __name__ == '__main__':
    tr = TryRecord('StockData.json')
    tr.try_record()
