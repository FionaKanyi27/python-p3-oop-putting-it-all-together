#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author}"

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    # Add property for page_count to validate input
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            raise ValueError("page_count must be an integer")
    
        