import tkinter as tk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from PIL import Image

import customtkinter as Ctk

from create_password import *


class App(Ctk.CTk):
    def __init__(self):
        super().__init__()

        self._create_window()
        self._create_logo()
        self._create_password_frame()
        self._create_entry_password()
        self._create_settings_frame()
        self._password_length_slider()
        self._set_default_values()

    def _create_window(self):
        """Создание окна и его параметров"""
        self.geometry('450x350')
        self.title('Password generator')
        self.resizable(False, False)

    def _create_logo(self):
        """Создание логотипа и его размещение"""
        self.logo = Ctk.CTkImage(dark_image=Image.open('img.png'), size=(460, 150))
        self.logo_label = Ctk.CTkLabel(master=self, text='', image=self.logo)
        self.logo_label.grid(row=0, column=0)

    def _create_password_frame(self):
        """Фрейм для поля вывода пароля и кнопки"""
        self.password_frame = Ctk.CTkFrame(master=self, fg_color='transparent')
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky='nsew')

    def _create_entry_password(self):
        """Поле для вывода пароля и кнопки"""
        self.password_entry = Ctk.CTkEntry(master=self.password_frame, width=300)
        self.password_entry.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = Ctk.CTkButton(master=self.password_frame, text='Generate', width=90,
                                          command=self._set_password)
        self.btn_generate.grid(row=0, column=1)

    def _create_settings_frame(self):
        """Создание фрейма кнопок сложности пароля"""
        self.settings_frame = Ctk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky='nsew')

    def _password_length_slider(self):
        """Слайдер длины пароля"""
        self.slider = Ctk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                    command=self._slider_event)
        self.slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky='we')

        self.password_length_entry = Ctk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky='we')

        self.cb_digits_vars = tk.StringVar()
        self.cb_digits = Ctk.CTkCheckBox(master=self.settings_frame, text='0-9', variable=self.cb_digits_vars,
                                         onvalue=digits, offvalue='')
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tk.StringVar()
        self.cb_lower = Ctk.CTkCheckBox(master=self.settings_frame, text='a-z', variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue='')
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tk.StringVar()
        self.cb_upper = Ctk.CTkCheckBox(master=self.settings_frame, text='A-Z', variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue='')
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbols_var = tk.StringVar()
        self.cb_symbols = Ctk.CTkCheckBox(master=self.settings_frame, text='@#$%', variable=self.cb_symbols_var,
                                          onvalue=punctuation, offvalue='')
        self.cb_symbols.grid(row=2, column=3)

    def _set_default_values(self):
        """"Установка значений по умолчанию"""
        self.appearance_mode_option_menu = Ctk.CTkOptionMenu(self.settings_frame,
                                                             values=['Light', 'Dark', 'System'],
                                                             command=self._change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        self.appearance_mode_option_menu.set('System')
        self.password_length_entry.insert(0, '12')
        self.slider.set(12)

    def _change_appearance_mode_event(self, new_appearance_mode):
        Ctk.set_appearance_mode(new_appearance_mode)

    def _slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def _get_characters(self):
        chars = ''.join(self.cb_digits_vars.get() + self.cb_lower_var.get() + self.cb_symbols_var.get() +
                        self.cb_upper_var.get())
        return chars

    def _set_password(self):
        """Отправка пароля в окно с паролем"""
        try:
            self.password_entry.delete(0, 'end')
            self.password_entry.insert(0, create_new(length=int(self.slider.get()),
                                                     characters=self._get_characters()))

        except IndexError:
            self.password_entry.delete(0, 'end')
            self.password_entry.insert(0, 'Ошибка! Выберите сложность пароля')


if __name__ == '__main__':
    app = App()
    app.mainloop()
