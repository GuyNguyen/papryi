# Papryi - Book Inventory Management

## Features
- Allow user to add books manually
- Allow user to view books in database/json/csv/file/etc
- User has a gui
- User can import books from images of bar tags from folder of images
- User can output list of books into an html table block

## Stack
- Python
- Poetry
- Ruff
- PySimpleGUI
- Sqlite3
- Opencv

## User Stories
work in progress

## Notes
- Upgrade to aiosqlite if file IO performance takes a hit
- Use multicore for interface/gui for funzies
- Enforce mypy with pydantic
- Rename "file_manager" to something more appropriate
- Consider using a MVC pattern

## Helpful Links
- https://data-flair.training/blogs/library-management-system-python-project/
- https://www.c-sharpcorner.com/UploadFile/ea3ed6/database-design-for-library-management-system/
- https://stackoverflow.com/questions/2717590/sqlite-insert-on-duplicate-key-update-upsert
- https://github.com/omnilib/aiosqlite
- https://lynn-kwong.medium.com/python-typing-and-validation-with-mypy-and-pydantic-a2563d67e6d
- https://blog.laurentcharignon.com/post/laptop-setup-with-ansible/
- https://medium.com/swlh/python-oop-mvc-data-science-tkinter-23c3e8dab70f