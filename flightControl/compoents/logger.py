import os
import pickle
import shutil
import time

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from others.helpers import Helpers


class DataEntry:
    def __init__(self, unit_name, data_type, content):
        self.unit_name = unit_name
        self.data_type = data_type
        self.content = content
        self.time = time.time()


class DataColumn:
    def __init__(self, title, time_codes, data):
        self.title = title
        self.time_codes = time_codes
        self.data = data


class Logger:
    MAX_ENTRY_PER_SAVE = 50000

    def __init__(self):
        self.logs = []
        self.data_entry_count = 0
        self.chunk_number = 0
        self.starting_time = time.time()

    @property
    def saving_path(self):
        time_stamp = Helpers.date_string(self.starting_time)
        package_name = time_stamp
        data_folder_name = "data"
        if not os.path.exists(data_folder_name):
            os.mkdir(data_folder_name)
        path = data_folder_name + "/" + package_name
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def update(self, unit_name, data_type, content):
        self.data_entry_count += 1
        self.logs.append(DataEntry(unit_name, data_type, content))
        if self.data_entry_count >= self.MAX_ENTRY_PER_SAVE:
            self.free_ram()

    def free_ram(self):
        path = self.saving_path + "/chunks"
        if not os.path.exists(path):
            os.mkdir(path)
        self.serialize(path + "/" + str(self.chunk_number))
        self.chunk_number += 1
        self.logs = []
        self.data_entry_count = 0
        return

    def save_to_pdf(self, file_name):
        data_to_plot = self.get_sorted_data()
        total_plot_count = len(data_to_plot)
        pdf_file_name = file_name + ".pdf"
        with PdfPages(pdf_file_name) as pdf:
            plot_per_page = 2
            plotted = 0
            fig = plt.figure()
            for i in range(total_plot_count):
                plotted += 1
                data_column = data_to_plot[i]
                time_code = data_column.time_codes
                data = data_column.data
                subplot_num = plotted % plot_per_page
                if subplot_num == 0:
                    subplot_num = plot_per_page
                plt.subplot(plot_per_page, 1, subplot_num)
                plt.plot(time_code, data)
                plt.title(data_column.title)

                if plotted % plot_per_page == 0 or plotted == total_plot_count:
                    pdf.savefig(fig)
                    fig = plt.figure()

    def get_sorted_data(self):
        result = []

        def get_unit_names_list(log):
            names_list = []
            for e in log:
                if e.unit_name not in names_list:
                    names_list.append(e.unit_name)

            return names_list

        unit_names_list = get_unit_names_list(self.logs)

        def get_unit_data_types_list(entries):
            types_list = []
            for e in entries:
                if e.data_type not in types_list:
                    types_list.append(e.data_type)
            return types_list

        def get_all_entries_of_unit(log, name):
            all_entries = []
            for e in log:
                if e.unit_name == name:
                    all_entries.append(e)
            return all_entries

        for unit_name in unit_names_list:
            all_entries_of_unit = get_all_entries_of_unit(self.logs, unit_name)
            unit_data_types_list = get_unit_data_types_list(all_entries_of_unit)
            for data_type in unit_data_types_list:
                title = unit_name + "_" + data_type
                time_codes = []
                data = []
                for entry in all_entries_of_unit:
                    if entry.data_type == data_type:
                        time_codes.append(entry.time - self.starting_time)
                        data.append(entry.content)
                data_column = DataColumn(title, time_codes, data)
                result.append(data_column)
        return result

    def serialize(self, file_name):
        file_name = file_name + ".pickle"
        file = open(file_name, "wb")
        pickle.dump(self, file)

    def save(self):
        path = self.saving_path
        if os.path.exists(path + "/chunks"):
            _, _, files = next(os.walk(path + "/chunks"))
            chunks_count = len(files)
            logs_in_chunks = []
            for i in range(chunks_count):
                file = open(path + "/chunks/" + str(i) + ".pickle", 'rb')
                chunk = pickle.load(file)
                logs_in_chunks.extend(chunk.logs)
            current_logs = self.logs
            self.logs = logs_in_chunks
            self.logs.extend(current_logs)
            shutil.rmtree(path + "/chunks")

        self.serialize(path + "/" + "serialized")
        self.save_to_pdf(path + "/" + "plots")
        print("saved as " + path)
