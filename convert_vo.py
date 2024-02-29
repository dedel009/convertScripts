import psycopg2

def generate_java_class(table_name, columns):
    # 클래스명 생성

    print("table_name :::",table_name)
    class_name = table_name.capitalize()
    
    # 필드 생성
    fields = []
    for column in columns:
        field_name = column[0]
        field_type = column[1]
        field_comment = column[2]        
                
        fields.append(f'    @Comment(value="{append_comment_field(field_comment)}")\n')
        fields.append(f"    private {convert_to_java_type(field_type)} {to_camel_case(field_name)};\n")
    
    # 클래스 생성    
    java_code = f'import lombok.Getter;\nimport org.hibernate.annotations.Comment;\n\n\n@Getter\n'
    java_code += f"""public class {class_name.upper()} {{       
    // 필드
    \n{''.join(fields)}
    }}
    """
    return java_code

#필드 타입을 java 타입으로 변경하는 함수
def convert_to_java_type(postgres_type):
    #현재 String 타입으로만 변경
    if 'character varying' in postgres_type:
        return 'String'
    elif postgres_type == 'integer':
        return 'Integer'
    elif postgres_type == 'timestamp':
        return 'String'
    elif postgres_type == 'double precision':
        return 'String'
    elif postgres_type == 'numeric':
        return 'String'
    # 추가적인 데이터 타입에 대한 매핑을 여기에 추가할 수 있습니다.
    else:
        return 'Object'  # 기본값으로 Object를 반환합니다.
    
#필드명 카멜케이스로 변경하는 함수
def to_camel_case(column_name):    
    parts = column_name.split('_')
    camel_case_name = parts[0] + ''.join(part.capitalize() for part in parts[1:])
    return camel_case_name    

#코멘트가 없으면 빈 문자열 출력
def append_comment_field(field_comment):
    if field_comment is None:
        return ""
    else:
        return field_comment


def main():
    # 데이터베이스 연결
    conn = psycopg2.connect(
        dbname='ysuis',
        user='uis',
        password='u10101s',
        host='192.168.10.99',
        port='5432'
    )
    
    # 커서 생성
    cursor = conn.cursor()
    
    #테이블 명
    table_name = 'rdl_rdar_as';

    
    #컬럼명, 컬럼 타입, 컬럼 코멘트 조회 쿼리
    cursor.execute(f"""SELECT 
    a.attname AS column_name,
    format_type(a.atttypid, a.atttypmod) AS data_type,
    d.description AS column_comment
FROM 
    pg_catalog.pg_class AS c
JOIN 
    pg_catalog.pg_attribute AS a ON c.oid = a.attrelid
LEFT JOIN 
    pg_catalog.pg_description AS d ON (c.oid = d.objoid AND a.attnum = d.objsubid)
WHERE 
    c.relname = '{table_name}'
    AND a.attnum > 0
ORDER BY 
    a.attnum;""")
    columns = cursor.fetchall()

    print("columns :::",columns)
        
    # 자바 클래스 생성
    java_code = generate_java_class(table_name, columns)
        
    # 생성된 자바 클래스 파일 저장
    with open(f"{table_name.upper()}.java", 'w', encoding="utf-8") as file:
        file.write(java_code)
    
    # 커넥션 및 커서 닫기
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()