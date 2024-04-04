def array_to_html_table(array):  
    return "".join([f"<th>{item}</th>\n" for item in array])

array = ["관리번호", "행정동", "도로재질", "위치구분", "도로구분", "경계종류", "노선명", "노선번호", "갱신일자", "성과심사일"]
html_table = array_to_html_table(array)
print(html_table)