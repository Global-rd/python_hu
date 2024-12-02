def get_tesco_main_categories_xpath() -> str:
    return '//*[@id="groceries"]/div/div/ul/li'

def get_tesco_mid_categories_xpath(main_category_id) -> str:
    return f'//*[@id="groceries"]/div/div[2]/ul/li[{main_category_id}]/ul/li'

def get_tesco_sub_categories_xpath(main_category_id, mid_category_id) -> str:
    return f'//*[@id="groceries"]/div/div[2]/ul/li[{main_category_id}]/ul/li[{mid_category_id}]/ul/li'

def get_tesco_subcategory_pagination_btn_class() -> str:
    return f'pagination-btn-holder'

def get_tesco_subcategory_pagination_button_xpath(index) -> str:
    return f'//*[@id="product-list"]/div[2]/div[8]/nav/ul/li[{index}]/a'

def get_tesco_product_list_xpath(page_index_plus_one) -> str:
    return f'//*[@id="product-list"]/div[2]/div[6]/div/div/div[{page_index_plus_one}]/div/ul/li'

def get_pagination_container_class() -> str:
    return f'pagination--page-selector-wrapper'


