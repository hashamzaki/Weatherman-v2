from os import listdir
from os.path import join


class Reader:
    @staticmethod
    def read_one_file(file_path):
        with open(file_path, mode='r') as reader:
            file_data_line = reader.readlines()

        return file_data_line

    @classmethod
    def read_all_file(cls, file_path):
        files_name_list = listdir(file_path)
        files_data = []
        for file_name in files_name_list:
            files_data.append(cls.read_one_file(join(file_path, file_name)))

        return {'all_files_data': files_data, 'all_files_names': files_name_list}
