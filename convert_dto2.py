import re

# SQL 쿼리
sql_query = """
        	<if test="RDA_IDN != null and RDA_IDN !='' ">
				AND A.RDA_IDN LIKE '%'||#{RDA_IDN}||'%'
			</if>
			<if test="FTR_CDE != null and FTR_CDE !='' ">
				AND A.FTR_CDE = #{FTR_CDE}
			</if>
			<if test="BLC_CDE != null and BLC_CDE !='' ">
				AND C.BLC_CDE = #{BLC_CDE} 
			</if>
			<if test="ADD_CDE != null and ADD_CDE !='' ">
				AND B.ADD_CDE = #{ADD_CDE} 
			</if>
			<if test="LMA_CDE != null and LMA_CDE !='' ">
				AND C.LMA_CDE = #{LMA_CDE} 
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
