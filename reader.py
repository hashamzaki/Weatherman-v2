from os import listdir
from os.path import join


class Reader:
    @staticmethod
    def read_one_file(file_path):
        with open(file_path, mode='r') as reader:
            file_data_line = reader.readlines()
        file_data_line.insert(1, file_path)

        return file_data_line

    def read_all_file(self, file_path):
        files_name_list = listdir(file_path)
        files_data = []
        for file_name in files_name_list:
            files_data.append(self.read_one_file(join(file_path, file_name)))

        return files_data
