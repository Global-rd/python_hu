# 2. XPATH SELECTOROK definiálása, külön .py állományban:

# XPath, hozzáférés a tag-ekhez
def get_top_tags_xpath() -> str:
    return '//*[@class="tag-item"]/a'  


# XPath hozzáférés magukhoz az idézetekhez:
def get_quote_elements_xpath() -> str:
    return '//*[@class="quote"]'  


# XPath, pagination kezelése, a következő oldalra "lapozás":
def get_next_page_button_xpath() -> str:
    return '//*[@class="next"]/a' 
