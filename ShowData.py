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
import ReadRecord as RdRec


class ShowData:
    def __init__(self):
        self.rr = RdRec.ReadRecord('StockData.json')
        self.stock_market_record = self.rr.read_data_file()

def show_data(self):
    stkmktrec = self.stock_market_record
    #  get a list of field names:
    print('Record fields: {}'.format(stkmktrec._fields))

    # List entire record
    print('\nEntire record: {}'.format(stkmktrec))

    # Get individual field
    print('\ndbtabledesc: {}'.format(stkmktrec.dbtabledesc))

    # Show database column entries
    print('\ndatabase column 0: {}'.format(stkmktrec.columns[0]))
    print('database column 1: {}'.format(stkmktrec.columns[1]))
    print('database column 2: {}'.format(stkmktrec.columns[2]))

    # Column data by key:
    for n in range(len(stkmktrec.columns)):
        column = stkmktrec.columns[n]
        print('\nColumn {} all: {}'.format(n, column))
        print('Column data {} field_name: {}'.format(n, column.field_name))
        print('Column data {} db_column_name: {}'.format(n, column.db_column_name))
        print('Column data {} db_column_desc: {}'.format(n, column.db_column_desc))
        print('Column data {} db_column_type: {}'.format(n, column.db_column_type))

    # Using get_field_item
    print('\nUsing get_field_item - Column 1, db_column_desc: {}'
          .format(self.rr.get_field_item(1, itemname='db_column_desc')))
    # same with bad data
    print('With bad data you get: {}'
          .format(self.rr.get_field_item(1, itemname='donkykong')))


if __name__ == '__main__':
    sd = ShowData()
    sd.show_data()
