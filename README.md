# Python-Record-Structure
## File Record Format for Python (3.4) using JSON and collections.namedtuple

**Caveat's:** This code was written on MS windows 7 pro. It should run without modification in Linux, but since my Linux box is currently down, hasn't been tested on that OS nor has it been tested on OS-X.

**```stkmktrec.dbtabledesc```**
**```stkmktrec.columns[0].db_column_name```**

Here's a sample of how used:

**To read data:**
```
class ShowData:
    def __init__(self):
        self.rr = RdRec.ReadRecord('StockData.json')
        self.stock_market_record = self.rr.read_data_file()
```

**To display parts of the record:**

```
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
```

Results in:
```
Record fields: ('url', 'dbtablename', 'delimiter', 'notes', 'stk_mkt_filename', 'local_file', 'columns', 'numfields', 'dbtabledesc')

Entire record: data(url='http://www.asx.com.au/asx/research/ASXListedCompanies.csv', dbtablename='ASXListed', delimiter=',', notes="Timestamp first format: 'ASX listed companies as at Sat Aug 13 21:00:02 EST 2016' followed by several empty lines, followed by header format: 'Company name,ASX code,GICS industry group'", stk_mkt_filename='ASXListedCompanies.csv', local_file='/stock_market/data/DailyFiles/USA/ASXListedCompanies.csv', columns=[data(db_column_desc='The company name', field_name='Company name', db_column_type='VARCHAR', db_column_name='CompanyName'), data(db_column_desc='The ASX Code (symbol)', field_name='ASX code', db_column_type='VARCHAR', db_column_name='AsxSymbol'), data(db_column_desc='Name of Industry Group', field_name='GICS industry group', db_column_type='VARCHAR', db_column_name='GicsIndustryGroup')], numfields=3, dbtabledesc='ASX - one of the world’s leading financial market exchanges')

dbtabledesc: ASX - one of the world’s leading financial market exchanges

database column 0: data(db_column_desc='The company name', field_name='Company name', db_column_type='VARCHAR', db_column_name='CompanyName')
database column 1: data(db_column_desc='The ASX Code (symbol)', field_name='ASX code', db_column_type='VARCHAR', db_column_name='AsxSymbol')
database column 2: data(db_column_desc='Name of Industry Group', field_name='GICS industry group', db_column_type='VARCHAR', db_column_name='GicsIndustryGroup')

Column 0 all: data(db_column_desc='The company name', field_name='Company name', db_column_type='VARCHAR', db_column_name='CompanyName')
Column data 0 field_name: Company name
Column data 0 db_column_name: CompanyName
Column data 0 db_column_desc: The company name
Column data 0 db_column_type: VARCHAR

Column 1 all: data(db_column_desc='The ASX Code (symbol)', field_name='ASX code', db_column_type='VARCHAR', db_column_name='AsxSymbol')
Column data 1 field_name: ASX code
Column data 1 db_column_name: AsxSymbol
Column data 1 db_column_desc: The ASX Code (symbol)
Column data 1 db_column_type: VARCHAR

Column 2 all: data(db_column_desc='Name of Industry Group', field_name='GICS industry group', db_column_type='VARCHAR', db_column_name='GicsIndustryGroup')
Column data 2 field_name: GICS industry group
Column data 2 db_column_name: GicsIndustryGroup
Column data 2 db_column_desc: Name of Industry Group
Column data 2 db_column_type: VARCHAR

Using get_field_item - Column 1, db_column_desc: None
With bad data you get: None
```

**Goal:** To build a file record format, for immutable data (once written), that would be transferable between python and other computer languages. Allow for python names like:

1 - Be Textual, allowing for human-readable collection of data that we can access in a really logical manner

2 - Be simple to design, read and write

3 - Be easily converted to an existing built-in python data type

4 - Be self-documenting so that reading the python script would immediately indicate what the data element was.

Solutions:
  1 Be Textual and use a format understood by other non-python programs. This was easy, JSON already exists and is ready as is.

  2 Be simple to design, read and write – Again easy using a python dictionary structure, in combination with python list for the repeated parts of a record design.

  3, 4  Be easily converted to an existing built-in python data type. Reading JSON into a python collections named tuple is clean, simple, and elegant. This also satisfies the self-documentation requirement, as will be seen below.


Before I finished the design, I had a dictionary which contained following components:
For the purpose of example, I will use the publicly available Australian Exchange Listed Companies file - ASXListedCompanies.csv, and some modules from my soon to be published Stock Market Data engine, which is a set of python scripts designed to be used by game programmers.

```
{
    "numfields": 3,
    "delimiter": ",",
    "dbtablename": "ASXListed",
    "stk_mkt_filename": "ASXListedCompanies.csv",
    "columns": [
        {
            "db_column_type": "VARCHAR",
            "db_column_desc": "The company name",
            "field_name": "Company name",
            "db_column_name": "CompanyName"
        },
        {
            "db_column_type": "VARCHAR",
            "db_column_desc": "The ASX Code (symbol)",
            "field_name": "ASX code",
            "db_column_name": "AsxSymbol"
        },
        {
            "db_column_type": "VARCHAR",
            "db_column_desc": "Name of Industry Group",
            "field_name": "GICS industry group",
            "db_column_name": "GicsIndustryGroup"
        }
    ],
    "notes": "Timestamp first format: 'ASX listed companies as at
                   Sat Aug 13 21:00:02 EST 2016' followed by several empty
                   lines, followed by header format: 'Company name, 
                   ASX code,GICS industry group'",
    "url": "http://www.asx.com.au/asx/research/
              ASXListedCompanies.csv",
    "dbtabledesc": "ASX - one of the world\u2019s leading financial
                            market exchanges",
    "local_file": "/stock_market/data/DailyFiles/USA/
                        ASXListedCompanies.csv"
}
```

This dictionary structure is perfect for conversion to JSON

The example will contain the following programs:

- WriteRecord.py - This program is a quick and dirty way to create a JSON file which will contain one record for the sample data. Normally this will be replaced by a GUI or otherwise data entry program that would populate and maintain the required fields. It can even come from a manually entered dictionary in a text file.

- ReadRecord.py - Reads the JSON data and converts to namedtuple. This script can be used without knowing the format of the data to be read. This is the 'Ready to use as is', reusable  part of the example code.

- ShowData.py - This is used to present some of the ways that the namedtuple data can be used. It imports the ReadRecord script.






