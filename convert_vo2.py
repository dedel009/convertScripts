import re

# SQL 쿼리
java_fields  = """
private String OBJECTID;
	    private String FTR_CDE;
	    private String FTR_CDE_NAME;
	    private String FTR_IDN;
	    private String HJD_CDE;
	    private String HJD_CDE_NAME;
	    private String MNG_CDE;
	    private String MNG_CDE_NAME;
	    private String SEC_IDN;
	    private String CNT_NUM;
	    private String BYC_LOC;
	    private String BYC_YMD;
	    private String BYC_NAM;
	    private String BYC_CDE;
	    private String BYC_CDE_NAME;
	    private String PLC_CDE;
	    private String PLC_CDE_NAME;
	    private String BMT_CDE;
	    private String BMT_CDE_NAME;
	    private     double                   BYC_LEN;
	    private     double                   BYC_WID;
	    private     long                       NAT_AMT;
	    private     long                       CIT_AMT;
	    private     long                      ETC_AMT;
	    private String DWY_CDE;
	    private String DWY_CDE_NAME;
	    private String SYS_CHK;
	    private String BJD_CDE;
	    private String BJD_CDE_NAME;
	    //추가
	    private String RUT_IDN;
	    private String RUT_NAM;
	    private String RUT_NUM;
"""
# 정규 표현식을 사용하여 변수명 추출
field_infos = re.findall(r'private\s+(\w+)\s+(\w+);', java_fields)

# 스네이크 케이스를 카멜 케이스로 변경하는 함수
def snake_to_camel(name):
    parts = name.split('_')    
    new_parts = [parts[0].lower()] + [part[0:3].title() if part == 'NAME' else part.title() for part in parts[1:]]
    return ''.join(new_parts)

# 변경된 변수 정보 출력
for field_type, field_name in field_infos:
    camel_name = snake_to_camel(field_name)
    print(f"private {field_type} {camel_name};")