import re

# SQL 쿼리
sql_query = """
				<if test="SEC_IDN != null and SEC_IDN !='' ">
					AND TRIM(A.SEC_IDN) LIKE '%'||#{SEC_IDN}||'%'
				</if>
	        	<if test="FTR_IDN != null and FTR_IDN !='' ">
					AND TRIM(A.FTR_IDN) LIKE '%'||#{FTR_IDN}||'%'
				</if>
				<if test="RAW_CDE != null and RAW_CDE !='' ">
					AND TRIM(C.RAW_CDE) LIKE '%'||#{RAW_CDE}||'%'
				</if>
				<if test="RUT_NAM != null and RUT_NAM !='' ">
					AND TRIM(C.RUT_NAM) LIKE '%'||#{RUT_NAM}||'%'
				</if>
				<if test="RUT_NUM != null and RUT_NUM !='' ">
					AND TRIM(C.RUT_NUM) LIKE '%'||#{RUT_NUM}||'%'
				</if>
				<if test="FNC_CDE != null and FNC_CDE !='' ">
					AND TRIM(C.FNC_CDE) LIKE '%'||#{FNC_CDE}||'%'
				</if>
"""

# 정규 표현식을 사용하여 #{...} 안의 내용 추출
parameters = re.findall(r'#\{([^}]*)\}', sql_query)


for code in parameters:
    if code.find("_"):
        # 언더스코어를 기준으로 단어 분리 후 카멜케이스로 변환
        words = code.split('_')
        camel_case_expression = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        print("private String " +camel_case_expression+";")    
