import re

# SQL 쿼리
sql_query = """
   <if test="FTR_IDN != null and FTR_IDN !='' ">
				AND A.FTR_IDN LIKE '%'||#{FTR_IDN}||'%'
			</if>
			<if test="HJD_CDE != null and HJD_CDE !='' ">
				AND A.HJD_CDE = #{HJD_CDE}
			</if>
			<if test="BJD_CDE != null and BJD_CDE !='' ">
				AND A.BJD_CDE = #{BJD_CDE} 
			</if>
			<if test="MNG_CDE != null and MNG_CDE !='' ">
				AND A.MNG_CDE = #{MNG_CDE} 
			</if>
			<if test="PLC_CDE != null and PLC_CDE !='' ">
				AND A.PLC_CDE = #{PLC_CDE} 
			</if>
			<if test="BYC_CDE != null and BYC_CDE !='' ">
				AND A.BYC_CDE = #{BYC_CDE} 
			</if>
			<if test="DWY_CDE != null and DWY_CDE !='' ">
				AND A.DWY_CDE = #{DWY_CDE} 
			</if>
			<if test="BMT_CDE != null and BMT_CDE !='' ">
				AND A.BMT_CDE = #{BMT_CDE} 
			</if>
			<if test="BYC_YMD_str != null and BYC_YMD_str !='' ">
				<![CDATA[
				AND A.BYC_YMD >= #{BYC_YMD_str} 
				]]>
			</if>
			<if test="BYC_YMD_end != null and BYC_YMD_end !='' ">
				<![CDATA[
				AND A.BYC_YMD <= #{BYC_YMD_end} 
				]]>
			</if>
			<if test="RAW_CDE != null and RAW_CDE !='' ">
				AND C.RAW_CDE = #{RAW_CDE} 
			</if>
			<if test="FNC_CDE != null and FNC_CDE !='' ">
				AND C.FNC_CDE = #{FNC_CDE} 
			</if>  
			<if test="RUT_NAM != null and RUT_NAM !='' ">
				AND C.RUT_NAM LIKE '%'||#{RUT_NAM}||'%'
			</if>
			<if test="RUT_IDN != null and RUT_IDN !='' ">
				AND B.RUT_IDN LIKE '%'||#{RUT_IDN}||'%'
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
