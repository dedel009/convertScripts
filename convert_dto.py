def generate_sql_conditions(sql_conditions):
    conditions = []
    for condition in sql_conditions:
        if "TRIM(" in condition:
            # TRIM() 함수로 문자열 추출
            trimmed_expression = condition.split("TRIM(")[1].split(")")[0]
            # 언더스코어를 기준으로 단어 분리 후 카멜케이스로 변환
            words = trimmed_expression.split('_')
            camel_case_expression = words[0].split('.')[1].lower() + ''.join(word.capitalize() for word in words[1:])
            conditions.append(camel_case_expression)
    return conditions

# 예시 SQL 조건들
sql_conditions = [
    "AND TRIM(A.RUT_IDN) LIKE '%'||#{rutIdn}||'%'",
    "AND TRIM(A.RUT_NAM) LIKE '%'||#{rutNam}||'%'",
    "AND TRIM(A.RUT_CDE) = #{rutCde}",
    "AND TRIM(A.ADA_CDE) = #{adaCde}",
    "AND TRIM(A.FNC_CDE) = #{fncCde}",
    "AND TRIM(A.SIZ_CDE) = #{sizCde}",
    "AND TRIM(A.BEG_LOC) LIKE '%'||#{begLoc}||'%'",
    "AND TRIM(A.END_LOC) LIKE '%'||#{endLoc}||'%'",
    "AND TRIM(A.IMP_LOC) LIKE '%'||#{impLoc}||'%'",
    "AND TRIM(A.MNG_CDE) = TRIM(#{mngCde})",
    "AND TRIM(A.REG_CDE) = TRIM(#{regCde})",
    "AND TRIM(A.RAW_CDE) = TRIM(#{rawCde})",
    "AND TRIM(A.RUT_NUM) LIKE '%'||#{rutNum}||'%'"
]

# SQL 조건들을 카멜케이스로 변환하여 출력
camel_case_conditions = generate_sql_conditions(sql_conditions)
for condition in camel_case_conditions:
    print("private String "+condition+";")
