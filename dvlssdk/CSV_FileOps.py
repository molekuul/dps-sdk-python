from csv import DictReader, DictWriter
from io import StringIO
from os import remove
from zipfile import ZipFile


class DVLS_CSV_File:
    """Use this class and its methods to interact with a DVLS Database file (.csv)
        This class can import the .csv from a password protected .zip
    """

    def __init__(self, zip_file, zip_pwd='', csv_file=None):
        if isinstance(zip_file, str) and isinstance(zip_pwd, str):
            self.zip_file = zip_file
            self.zip_pwd = bytes(zip_pwd, 'utf-8')
            if not csv_file:
                self.csv_file = zip_file.replace('.zip', '.csv').split('/')[-1]
            else:
                if isinstance(csv_file, str):
                    if csv_file.count() > 4 and csv_file.endswith('.csv'):
                        self.csv_file = csv_file
                    else:
                        print("Parameter error")
                else:
                    print("Parameter error")
            self.csv_field_names = None
            self.mode = None
            self.opened = False
        else:
            print("Parameter error")

    def get_csv_content(self):
        zip_file = ZipFile(self.zip_file, 'r')
        r_csv_obj = zip_file.open(self.csv_file, mode='r', pwd=self.zip_pwd)
        self.opened = True
        r_csv_obj = StringIO(r_csv_obj.read().decode('utf-8'))
        csv_reader = DictReader(r_csv_obj)
        self.csv_field_names = csv_reader.fieldnames
        csv_content = []
        for c in csv_reader:
            csv_content.append(c)
        r_csv_obj.close()
        return csv_content

    # This function deletes the existing zip and creates a new one
    # Maybe split this function in two : write_csv and write_zip ?
    def modify_zipped_csv(self, csv_content, del_zip=True):
        if del_zip:
            remove(self.zip_file)
        with ZipFile(self.zip_file, mode='w') as zip_file:
            string_buffer = StringIO()
            csv_writer = DictWriter(string_buffer, delimiter=',', fieldnames=self.csv_field_names)
            csv_writer.writeheader()
            csv_writer.writerows(csv_content)
            zip_file.writestr(self.csv_file, string_buffer.getvalue())

    # This function creates a new zipped (without password) csv using a list of entries gotten from the DVLS server's web API (using a list of entries - converted from a tree format)
    def create_zipped_csv(self, dvls_entries_list):
        self.csv_field_names = set()
        for e in dvls_entries_list:
            self.csv_field_names.update(e.keys())
        tmp_dict_lst = []
        for d in dvls_entries_list:
            tmp_dict = {}
            for f in self.csv_field_names:
                if f in d.keys():
                    tmp_dict[f] = d[f]
            tmp_dict_lst.append(tmp_dict)
        self.modify_zipped_csv(tmp_dict_lst, del_zip=False)
