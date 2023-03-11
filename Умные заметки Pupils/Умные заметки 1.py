from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import json

notes = {
    "Название заметки" :
{
        "текст" : "Очень важный текст заметки",
        "теги" : ["черновик", "мысли"]
    	}
}

with open('notes_data.json', 'w') as file:
    json.dump(notes, file)

app = QApplication([])

'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки Pupils')
notes_win.resize(900, 600)

#виджеты окна приложения

list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')

button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')

field_text = QTextEdit()

button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')

list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')

'''расположение виджетов по лэйаутам'''
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
'''ряд calc get-запрос с кнопками'''
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
'''ряд 2 с кнопкой'''
row_2 = QHBoxLayout()
row_1.addWidget(button_note_save)
'''добавляем в колонку ряды calc get-запрос-2'''
col_2.addLayout(row_1)
col_2.addLayout(row_2)
'''добавляем остальное'''
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
'''ряд 3 Flask wtforms с кнопками'''
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
'''ряд 4 с кнопкой'''
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
'''добавляем в колонку ряды 3 Flask wtforms-4'''
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)

notes_win.setLayout(layout_notes)

'''Функционал приложения'''
def show_note():
    '''получаем текст из заметки с выделенным название и отображаем его
    в поле редактирования'''
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[name]["теги"])
'''подключение обработки событий'''
list_notes.itemClicked.connect(show_note)
'''запуск приложения'''
notes_win.show()
app.exec()