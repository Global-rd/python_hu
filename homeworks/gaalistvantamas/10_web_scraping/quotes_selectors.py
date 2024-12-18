"""
Author: Gaál István Tamás
Task: Homework-10
"""

def get_quotes_top_ten_category_xpath(index) -> str:
    return f'/html/body/div/div[2]/div[2]/span[{index}]'

def get_quotes_from_the_tag(index):
    return f'/html/body/div/div[2]/div[1]/div[{index}]'

def get_quote_text_from_the_chosen_tag_xpath(index):
    return f'/html/body/div/div[2]/div[1]/div[{index}]/span[1]'

def get_author_from_the_chosen_tag_xpath(index):
    return f'/html/body/div/div[2]/div[1]/div[{index}]/span[2]/small'

def get_pagination_button_xpath():
    return '/html/body/div/div[2]/div[1]/nav/ul/li/a'

