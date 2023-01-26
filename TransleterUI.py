from tkinter import *
from tkinter import ttk

from translatepy import Translator


class TranslaterTkinter:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x450')
        self.root.title('Переводчик')
        self.root.resizable(width=False, height=False)
        self.root['bg'] = '#002137'
        self.translator = Translator()

        self.languages = {'Русский': 'ru', 'Английский': 'en', 'Французский': 'fr'}

        self._set_header()
        self._input_text()
        self._set_button()
        self._output_text()

        self.root.mainloop()

    def _set_header(self):
        header_frame = Frame(self.root)
        header_frame['bg'] = '#002137'
        header_frame.pack(fill=X)

        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=1)
        header_frame.grid_columnconfigure(2, weight=1)

        self.comboOne = ttk.Combobox(header_frame, values=[language for language in self.languages])
        self.comboOne.current(0)
        self.comboOne.grid(row=0, column=0)

        label = Label(header_frame, fg='white', font='Arial 17 bold', text='>>')
        label['bg'] = '#002137'
        label.grid(row=0, column=1)

        self.comboTwo = ttk.Combobox(header_frame, values=[language for language in self.languages])
        self.comboTwo.current(1)
        self.comboTwo.grid(row=0, column=2)

    def _input_text(self):
        self.text_input = Text(self.root, width=50, height=8, font='Arial 12 bold', fg='white')
        self.text_input['bg'] = '#002137'
        self.text_input.pack(pady=20)

    def _set_button(self):
        button = Button(self.root, width=35, font='Arial 14 bold', fg='white', text='Перевести',
                        command=self._translater)
        button['bg'] = '#002137'
        button.pack()

    def _output_text(self):
        self.text_output = Text(self.root, width=50, height=8, font='Arial 12 bold', fg='white')
        self.text_output['bg'] = '#002137'
        self.text_output.pack(pady=20)

    def _translater(self):
        for language, suffix in self.languages.items():
            if self.comboTwo.get() == language:
                text = self.text_input.get('1.0', END)
                result = self.translator.translate(text, destination_language=suffix)
                self.text_output.delete('1.0', END)
                self.text_output.insert('1.0', str(result))


UI = TranslaterTkinter()
