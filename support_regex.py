import re

""" dividing_by_banks_pattern: It allows to divide the text file by banks and his operations.
 Ex. 2100 CAIXABANK, S.A.
     001CNF620201006273926064 V27 T11 EUR L07 G19 G01 290.145 0 0 0
     3058 CAJAMAR CAJA RURAL, S.C.C.
     0005404068600001480000000000000020221231 V27 T11 EUR L07 G19 G10 231.494 0 0 0
     It'll return: ['2100 CAIXABANK, S.A.\n001CNF620201006273926064 V27 T11 EUR L07 G19 G01 290.145 0 0 0',
                    '3058 CAJAMAR CAJA RURAL, S.C.C.\n0005404068600001480000000000000020221231 V27 T11 EUR L07 G19 G10 231.494 0 0 0']"""

dividing_by_banks_pattern = re.compile(
    r"^\d{4}\s[A-Z].*?S\..*?(?=^(?:\d{4}\s[A-Z].*?S\..|TOTAL\sEN\sEL\sSISTEMA))",
    flags=re.DOTALL | re.MULTILINE,
)
# bank_pattern: It allows to get the name of the bank
bank_pattern = re.compile(r"^\d{4}\s([A-Z].*?S\..*?)\n", flags=re.MULTILINE)
# operation_pattern: It allows to get all the data of the operation except Solidario / Colectivo
operation_pattern = re.compile(
    r"^(.*)(V\d{2})\s(T\d{2})(?:\sT\d{2})?\s([A-Z]{3})(\sL\d{2})?(\sG\d{2})?(\sG\d{2})?\s([\d\.]+)\s([\d\.]+)\s([\d\.]+)\s([\d\.]+)",
    flags=re.MULTILINE,
)
