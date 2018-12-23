# from transaction_3 import Transaction
# for ide
from session_5.transaction_3 import Transaction

class TransactionDataProcessor:

    def process_data(self, fileName, separator):
        file = open(fileName,mode="r")
        content = file.read()
        line_data = content.splitlines()
        transaction_list = []
        for row in line_data:
            row_line_data = row.split(separator)
            transaction = Transaction(row_line_data)
            # print(transaction.bagic_key + transaction.transaction_id)
            print(transaction.__dict__)
            transaction_list.append(transaction)
        return transaction_list


if __name__ == "__main__":

    processor = TransactionDataProcessor()
    separator = ","
    processor.process_data("a.csv", separator)
    #TODO: Exercise:: write same data into another file.....
