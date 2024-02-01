from intro_func import get_pdf_files, extract_data_from_pdf
from support_regex import dividing_by_banks_pattern, bank_pattern, operation_pattern
from output import write_to_xlsx


def main():
    pdf_file = get_pdf_files()
    text_file = extract_data_from_pdf(pdf_file)
    banks_operations = dividing_by_banks_pattern.findall(text_file)
    rows = []  # It'll contain the data to be written in the xlsx file
    for bank_operations in banks_operations:
        """bank_operation = stores a string with the data of the bank and his operations.
        Ex. 0049 BANCO SANTANDER, S.A.
            004929321530601243 V51 T11 EUR L10 G19 G10 24.108 0 0 0
            E14
            004929321530601256 V51 T11 EUR L10 G19 G10 24.356 0 0 0
            E14"""
        bank = bank_pattern.search(bank_operations).group(1)
        # bank = stores a string with the name of the bank Ex. "BBVA, S.A."
        operations = operation_pattern.findall(bank_operations)
        """operations = stores a list of tuples with the data of the operations
        Ex. [('004929321530601243 ', 'V51', 'T11', 'EUR', 'L10', 'G19', ' G10', '24.108', '0', '0', '0'),(...),(...),...]"""
        for operation in operations:
            # operation = ('004929321530601243 ', 'V51', 'T11', 'EUR', 'L10', 'G19', ' G10', '24.108', '0', '0', '0')
            operation = list(operation[:-4]) + [
                float(x.replace(".", "")) for x in operation[-4:]
            ]
            row = [bank] + operation
            rows.append(row)
            row = None
    write_to_xlsx(rows)


if __name__ == "__main__":
    main()
