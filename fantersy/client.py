#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from fantersy import Fantersy
from color import Color
import tkinter
import tkinter.filedialog


class Client:
    """
    Fantersy Client.
    """

    @classmethod
    def execute(cls):
        """
        Execute client.
        """
        config_path = cls.__select_file()
        f = Fantersy(config_path)
        while True:
            command = input(Color.GREEN + 'Fantersy >> ' + Color.END)
            if command == 'exit':
                break
            else:
                if command != '':
                    cls.__execute_command(f, command)

    @classmethod
    def __execute_command(cls, f, command):
        """
        Execute command.

        :param f: Fantersy object.
        :param command: command.
        """
        command_list = command.split()
        # Fantersy API name
        method = command_list[0]
        # args
        args = command_list[1:]
        # execute
        getattr(f, method)(args)

    @classmethod
    def __select_file(cls):
        """
        Select config yaml from GUI.
        """
        root = tkinter.Tk()
        root.withdraw()
        return tkinter.filedialog.askopenfilename()


if __name__ == '__main__':
    Client.execute()
