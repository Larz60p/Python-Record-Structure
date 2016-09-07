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
import json


class WriteRecord:
    def create_data_file(self):
        self.jsonrec = {
            "ASXListedCompanies": {
                "filename": "ASXListedCompanies.csv",
                "source": "ASX",
                "url": "http://www.asx.com.au/asx/research/ASXListedCompanies.csv",
                "local_file": "/stock_market/data/DailyFiles/USA/ASXListedCompanies.csv",
                "notes":
                    "Timestamp first format: 'ASX listed companies as at Sat Aug 13"
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
            },
            "nasdaqlisted": {
                "filename": "nasdaqlisted.txt",
                "source": "NASDAQ",
                "url": "ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt",
                "local_file": "\stock_market\data\DailyFiles\\USA\\nasdaqlisted.txt",
                "notes":
                    "Order Must be maintained in header - Use Number key to access"
                    "The last row of each Symbol Directory text file contains a"
                    " timestamp that reports the File Creation Time. The file"
                    " creation time is based on when NASDAQ Trader generates the"
                    " file and can be used to determine the timeliness of the"
                    " associated data. The row contains the words File Creation Time"
                    " followed by mmddyyyyhhmm as the first field, followed by all"
                    " delimiters to round out the row. An example: File Creation"
                    " Time: 1217200717:03|||||"
                    "CreatedDate - 'File Creation Time: MMDDYYYYHR:MN']",
                "delimiter": "|",
                "numfields": 8,
                "dbtablename": "NasdaqListed",
                "dbtabledesc":
                    "ASX is one of the world’s leading financial market"
                    " exchanges, offering a full suite of services,"
                    " including listings, trading, clearing and settlement,"
                    " across a comprehensive range of asset classes. As the"
                    " first major financial market open every day, ASX is a"
                    " world leader in raising capital, consistently ranking"
                    " among the top five exchanges globally. With a total"
                    " market capitalisation of around $1.5 trillion, ASX is"
                    " home to some of the world’s leading resource, finance"
                    " and technology companies. Our $47 trillion interest rate"
                    " derivatives market is the largest in Asia and among the"
                    " biggest in the world.",
                "columns": [
                    {
                        "field_name": "Symbol",
                        "db_column_name": "Symbol",
                        "db_column_desc":
                            "The one to four or five character identifier for each"
                            " NASDAQ-listed security.",
                        "db_column_type": "VARCHAR"
                    },
                    {
                        "field_name": "Security Name",
                        "db_column_name": "SecurityName",
                        "db_column_desc": "Company issuing the security.",
                        "db_column_type": "VARCHAR"
                    },
                    {
                        "field_name": "Market Category",
                        "db_column_name": "MarketCategory",
                        "db_column_desc": "The category assigned to the issue by NASDAQ based on Listing Requirements. Values",
                        "db_column_type": "VARCHAR"
                    },
                    {
                        "field_name": "Test Issue",
                        "db_column_name": "TestIssue",
                        "db_column_desc": "Indicates whether or not the security is a test security.",
                        "db_column_type": "VARCHAR"
                    },
                    {
                        "field_name": "Financial Status",
                        "db_column_name": "FinancialStatus",
                        "db_column_desc": "Indicates when an issuer has failed to submit its regulatory filings on a timely basis, has failed to meet NASDAQ's continuing listing standards, and/or has filed for bankruptcy.",
                        "db_column_type": "VARCHAR"
                    },
                    {
                        "field_name": "Round Lot Size",
                        "db_column_name": "RoundLotSize",
                        "db_column_desc": "Indicates the number of shares that make"
                                          " up a round lot for the given security.",
                        "db_column_type": "NUMERIC"
                    },
                    {
                        "field_name": "ETF",
                        "db_column_name": "ETF",
                        "db_column_desc": "Identifies whether the security is an"
                                          " exchange traded fund",
                        "db_column_type": "VARCHAR"
                    },
                    {
                        "field_name": "Next Shares",
                        "db_column_name": "NextSghares",
                        "db_column_desc": "",
                        "db_column_type": "VARCHAR"
                    }
                ]
            }
        }

        with open('StockData.json', 'w') as f:
            j = json.dumps(self.jsonrec)
            f.write(j)

if __name__ == '__main__':
    wd = WriteRecord()
    wd.create_data_file()
    print(wd.jsonrec)
