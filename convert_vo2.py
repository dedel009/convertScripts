import re

# SQL 쿼리
java_fields  = """
	    private String FTR_CDE;
	    private String FTR_CDE_NAME;
	    private     long                      RDA_IDN;
	    private     long                      SEC_IDN;
	    private     long                      SHAPE;
	   //보도 RDT_SDWK_DT
	    private String HJD_CDE;
	    private String HJD_CDE_NAME;
	    private String MNG_CDE;
	    private String MNG_CDE_NAME;
	    private String MNG_NAM;
	    private String CNT_NUM;
	    private String PLC_CDE;
	    private String PLC_CDE_NAME;
	    private     double                    BDL_WID;
	    private     double                    BDL_LEN;
	    private     double                    BDL_ARA;
	    private     long                      BTK_CNT;
	    private     long                      HTK_CNT;
	    private     long                      JTK_CNT;
	    private String BYC_CDE;
	    private String BYC_CDE_NAME;
	    private String LMA_CDE;
	    private String LMA_CDE_NAME;
	    private     double                    LMA_LEN;
	    private String BLC_CDE;
	    private String BLC_CDE_NAME;
	    private     double                    BLC_LEN;
	    private     double                    BLC_ARA;
	    private String LAV_CDE;
	    private String LAV_CDE_NAME;
	    private String SYS_CHK;
	    private String BJD_CDE;
	    private String BJD_CDE_NAME;

	   //차도 RDT_RDWY_DT
	    private     long                      LNE_CNT;
	    private     double                    ICL_LEN;
	    private     double                    ICL_ARA;
	    private     double                    JYG_LEN;
	    private     double                    JYG_ARA;
	    private String ADD_CDE;
	    private String ADD_CDE_NAME;
	    private     double                    NOR_LEN;
	    private     double                    NOR_ARA;
	    private     double                    NOR_WID;
	    private     double                    NOL_LEN;
	    private     double                    NOL_ARA;
	    private     double                    NOL_WID;
	    private     double                    LRL_LEN;
	    private String RMA_CDE;
	    private String RMA_CDE_NAME;
	    private     double                    RRL_LEN;

	    //추가
	    private String RUT_IDN;
	    private String RUT_NAM;
	    private String RUT_NUM;

	// 갱신일자 , 성과심사일
	private		String					REN_YMD;
	private		String					PUE_YMD;
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