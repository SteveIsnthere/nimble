import os
import pickle
import time

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from flightControl.compoents.helpers import Helpers


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
    def __init__(self):
        self.logs = []
        self.starting_time = time.time()

    def update(self, unit_name, data_type, content):
        self.logs.append(DataEntry(unit_name, data_type, content))

    def get_unit_names_list(self):
        unit_names_list = []
        for entry in self.logs:
            if entry.unit_name not in unit_names_list:
                unit_names_list.append(entry.unit_name)

        return unit_names_list

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
        unit_names_list = self.get_unit_names_list()
        for unit_name in unit_names_list:
            all_entries_of_unit = self.get_all_entries_of_unit(unit_name)
            unit_data_types_list = self.get_unit_data_types_list(all_entries_of_unit)
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

    @staticmethod
    def get_unit_data_types_list(all_entries_of_unit):
        unit_data_types_list = []
        for entry in all_entries_of_unit:
            if entry.data_type not in unit_data_types_list:
                unit_data_types_list.append(entry.data_type)
        return unit_data_types_list

    def get_all_entries_of_unit(self, unit_name):
        all_entries = []
        for entry in self.logs:
            if entry.unit_name == unit_name:
                all_entries.append(entry)
        return all_entries

    def serialize(self, file_name):
        file_name = file_name + ".pickle"
        file = open(file_name, "wb")
        pickle.dump(self, file)

    def save(self):
        time_stamp = Helpers.date_string(self.starting_time)
        package_name = time_stamp
        data_folder_name = "data"
        if not os.path.exists(data_folder_name):
            os.mkdir(data_folder_name)
        path = data_folder_name + "/" + package_name
        os.mkdir(path)
        self.serialize(path + "/" + "serialized")
        self.save_to_pdf(path + "/" + "plots")
        print("saved as " + path)
