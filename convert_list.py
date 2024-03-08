def array_to_html_table(array):  
    return "".join([f"<th>{item}</th>\n" for item in array])

array = ["구분", "노선명", "노선번호", "구간(시점~종점)", "연장", "포장", "미포장"]
html_table = array_to_html_table(array)
print(html_table)