# Python-Record-Structure
## File Record Format for Python (3.4) using JSON and collections.namedtuple

**Caveat's:** This code was written on MS windows 7 pro. It should run without modification in Linux, but since my Linux box is currently down, hasn't been tested on that OS nor has it been tested on OS-X.

**Goal:** To build a file record format, for immutable data (once written), that would be transferable between python and other computer languages (JSON format). Allow for python names like:

**```stkmktrec.dbtabledesc```**
**```stkmktrec.columns[0].db_column_name```**

1 - Be Textual, allowing for human-readable collection of data that we can access in a really logical manner

2 - Be simple to design, read and write

3 - Be easily converted to an existing built-in python data type

4 - Be self-documenting so that reading the python script would immediately indicate what the data element was.

Solutions:
  1 Be Textual and use a format understood by other non-python programs. This was easy, JSON already exists and is ready as is.

  2 Be simple to design, read and write – Again easy using a python dictionary structure, in combination with python list for the repeated parts of a record design.

  3, 4  Be easily converted to an existing built-in python data type. Reading JSON into a python collections named tuple is clean, simple, and elegant. This also satisfies the self-documentation requirement, as will be seen below.

Here's a sample of how used:

**To read data:**
```
class ShowData:
    def __init__(self):
        self.rec = Record.Record(filename)
        stkrec = self.rec.record
```

**To display parts of the record:**

```
        keys = stkrec._asdict().keys()
        print('\nKeys:')
        for key in keys:
            print('\nkey: {}'.format(key))
            thisrec = getattr(stkrec, key)
            print('filename: {}'.format(thisrec.filename))
            print('number of columns: {}'.format(len(thisrec.columns)))
            print('column 0 column name: {}'.format(thisrec.columns[0].db_column_name))
```

Results in:
```
Keys:

key: nasdaqlisted
filename: nasdaqlisted.txt
number of columns: 8
column 0 column name: Symbol

key: ASXListedCompanies
filename: ASXListedCompanies.csv
number of columns: 3
column 0 column name: CompanyName

```

The sample file can be regenerated by running WriteRecord.py
It contains two records for stock market data as shown below:

```
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
```

The class contains iter types so that:
```
for rec in stkrec:
    ...
```

is valid

The only module needed to use is Record.py.

The other python scripts are for creating data and example only.

The JSON file can be created by web form or whatever.
