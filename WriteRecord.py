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
import json


class WriteRecord:
    def __init__(self):
        self.jsonrec = None

    def create_data_file(self):
        self.jsonrec = {
            "stk_mkt_filename": "ASXListedCompanies.csv",
            "url": "http://www.asx.com.au/asx/research/ASXListedCompanies.csv",
            "local_file": "/stock_market/data/DailyFiles/USA/ASXListedCompanies.csv",
            "notes": "Timestamp first format: 'ASX listed companies as at Sat Aug 13"
                     " 21:00:02 EST 2016' followed by several empty lines, followed"
                     " by header format: 'Company name,ASX code,GICS industry group'",
            "delimiter": ",",
            "numfields": 3,
            "dbtablename": "ASXListed",
            "dbtabledesc": "ASX - one of the world\u2019s leading financial market exchanges",
            "columns": [
                {
                    "field_name": "Company name",
                    "db_column_name": "CompanyName",
                    "db_column_desc": "The company name",
                    "db_column_type": "VARCHAR"
                },
                {
                    "field_name": "ASX code",
                    "db_column_name": "AsxSymbol",
                    "db_column_desc": "The ASX Code (symbol)",
                    "db_column_type": "VARCHAR"
                },
                {
                    "field_name": "GICS industry group",
                    "db_column_name": "GicsIndustryGroup",
                    "db_column_desc": "Name of Industry Group",
                    "db_column_type": "VARCHAR"
                }
            ]
        }

        with open('StockData.json', 'w') as f:
            j = json.dumps(self.jsonrec)
            f.write(j)

if __name__ == '__main__':
    wd = WriteRecord()
    wd.create_data_file()
    print(wd.jsonrec)
