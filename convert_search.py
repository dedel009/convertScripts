from bs4 import BeautifulSoup
import re

def trans_camel(code):
    words = code.split('_')    
    camelCode = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    return camelCode;

def convert_html(input_html):
    # HTML을 파싱합니다.
    soup = BeautifulSoup(input_html, 'html.parser')

    # <li> 태그를 선택합니다.
    li_tags = soup.find_all('li')

    # 각 <li> 태그를 순회하며 변환 작업을 수행합니다.
    for li_tag in li_tags:
            
        # <uis:codeselect> 태그를 <UisSelectboxMng> 태그로 변경합니다.
        codeselect_tag = li_tag.find('uis:codeselect')        
        if codeselect_tag is not None:
            # 태그를 self-closing 태그로 변경                      
            #코드값 추출
            codeName = trans_camel(codeselect_tag['name'])
            
            if codeselect_tag:
                if codeselect_tag['codetable'] == "CMT_FTRC_MA":
                    # 새로운 태그 생성
                    new_tag = soup.new_tag('UisSelectboxFtr')  
                elif codeselect_tag['codetable'] == "CMT_ADAR_MA":                    
                    new_tag = soup.new_tag('UisSelectboxHjd')  
                elif codeselect_tag['codetable'] == "CMT_LGAR_MA":                    
                    new_tag = soup.new_tag('UisSelectboxHjd2Bjd')  
                elif codeselect_tag['codetable'] == "CMT_MNGR_MA":                    
                    new_tag = soup.new_tag('UisSelectboxMng')  
                else :
                    new_tag = soup.new_tag('UisSelectboxCode')  
                    new_tag['attNam'] = codeselect_tag['codetype']
                    new_tag['tblNam'] = "{selectedWorkSubMenuInfo?.subMenu}"                                                             
                # 필요한 속성을 설정합니다.
                new_tag['sname'] = codeName
                new_tag['sid'] = codeName
                new_tag['onChange'] = "{onChange}"
                new_tag['value'] = "{searchFormData?."+codeName+"|| ''}"

                # 원래의 태그를 새로운 태그로 대체합니다.
                codeselect_tag.replace_with(new_tag)
        else :
            input_tag = li_tag.find('input')
            print("input_tag :::",input_tag)
            
            #코드값 추출              
            codeName = trans_camel(input_tag['name'])

            if input_tag:
                input_tag['id'] = codeName
                input_tag['name'] = codeName
                input_tag['onChange'] = "{onChange}"
                input_tag['defaultValue'] = "{searchFormData?."+codeName+"|| ''}"   
                if 'onlynumber' in input_tag.attrs :
                    del input_tag['onlynumber']
                    input_tag['type'] = "number"                    
                    
                
  
            
        # label 태그의 텍스트를 가져와 htmlFor로 설정합니다.
        label_tag = li_tag.find('label')        
        if label_tag:
            del label_tag['for']
            label_tag['htmlFor'] = codeName   

        # class 속성을 가진 모든 태그를 찾습니다.
        tags_with_class = soup.find_all(class_=True)

        # 각 태그의 class 속성을 className 속성으로 변경합니다.
        for tag in tags_with_class:
            tag['className'] = tag['class']
            del tag['class']           

    # 변환된 HTML 코드를 문자열로 반환합니다.
    return str(soup.prettify())

if __name__ == '__main__':
    #변환 해야할 html 소스
    input_html = """
                                  <li>
									    <label for="seq">관리번호</label>
                                        <div class="input_area">
                                            <input type="text" id="FTR_IDN" name="FTR_IDN" title="관리번호"class="form-control input-sm" onlyNumber>
                                        </div>
                                    </li>
									<li>
										<label for="mngt">관리기관</label>
										<div class="input_area">
										    <uis:codeselect name="MNG_CDE" selected="" codetable="CMT_MNGR_MA" stylestring="class='column_filter input-sm'"></uis:codeselect>
										</div>
									</li>
									<li>
										<label for="HJD_CDE">행정동</label>
										<div class="input_area">
										    <uis:codeselect name="HJD_CDE" selected="" codetable="CMT_ADAR_MA" stylestring="class='column_filter input-sm'"></uis:codeselect>
										</div>
									</li>
									<li>
                                        <label for="BJD_CDE">법정동</label>
                                        <div class="input_area">
                                            <uis:codeselect name="BJD_CDE" selected="" codetable="CMT_LGAR_MA" stylestring="class='column_filter input-sm'"></uis:codeselect>
                                        </div>
                                    </li>
                                    <li>
                                        <label for="GGB_CDE">자전거도로구분</label>
                                        <div class="input_area">
                                            <uis:codeselect name="BYC_CDE" selected="" codetable="CMT_CODE_MA" tablename="RDL_BYCP_AS" codetype="BYC_CDE" stylestring="class='column_filter input-sm'"></uis:codeselect>
                                        </div>
                                    </li>
                                    <li>
                                        <label for="GGB_CDE">위치구분</label>
                                        <div class="input_area">
                                            <uis:codeselect name="PLC_CDE" selected="" codetable="CMT_CODE_MA" tablename="RDL_BYCP_AS" codetype="PLC_CDE" stylestring="class='column_filter input-sm'"></uis:codeselect>
                                        </div>
                                    </li>
                                    <li>
                                        <label for="GGB_CDE">도로재질</label>
                                        <div class="input_area">
                                            <uis:codeselect name="BMT_CDE" selected="" codetable="CMT_CODE_MA" tablename="RDL_BYCP_AS" codetype="BMT_CDE" stylestring="class='column_filter input-sm'"></uis:codeselect>
                                        </div>
                                    </li>
                                    <li>
                                        <label for="GGB_CDE">경계종류</label>
                                        <div class="input_area">
                                            <uis:codeselect name="DWY_CDE" selected="" codetable="CMT_CODE_MA" tablename="RDL_BYCP_AS" codetype="DWY_CDE" stylestring="class='column_filter input-sm'"></uis:codeselect>
                                        </div>
                                    </li>
                                    <li>
                                        <label for="mngt">설치일자</label>
                                            <div class="input_area">
                                                <div class="myDatepicker input-group date td_dateForm" style="width:45%; display: inline-table;">
                                                    <input type="text" id="BYC_YMD_str" name="BYC_YMD_str" value="" class="form-control input-date" maxlength="8" style="padding:6px;"/>
                                                    <span class="input-group-addon" ></span>
                                                </div>
                                                <span>~</span>
                                                <div class="myDatepicker input-group date td_dateForm" style="width:45%; float:right; display: inline-table;">
                                                    <input type="text" id="BYC_YMD_end" name="BYC_YMD_end" value="" class="form-control input-date" maxlength="8" style="padding:6px;"/>
                                                    <span class="input-group-addon" ></span>
                                                </div>
                                            </div>
                                    </li>
                                    <li>
                                        <label for="RAW_CDE">도로구분</label>
                                        <div class="input_area">
                                            <uis:codeselect name="RAW_CDE" selected="" codetable="CMT_CODE_MA" tablename="RDT_ROUT_DT" codetype="RAW_CDE" stylestring="class='column_filter input-sm'"></uis:codeselect>
                                        </div>
                                    </li>
                                    <li>
                                        <label for="JYG_CDE">도로기능</label>
                                        <div class="input_area">
                                            <uis:codeselect name="FNC_CDE" selected="" codetable="CMT_CODE_MA" tablename="RDT_ROUT_DT" codetype="FNC_CDE" stylestring="class='column_filter input-sm'"></uis:codeselect>
                                        </div>
                                    </li>
                                    <li>
                                        <label for="seq">노선명</label>
                                        <div class="input_area">
                                            <input type="text" id="RUT_NAM" name="RUT_NAM" title="노선명"class="form-control input-sm" >
                                        </div>
                                    </li>
                                    <li>
                                        <label for="seq">노선번호</label>
                                        <div class="input_area">
                                            <input type="text" id="RUT_IDN" name="RUT_IDN" title="노선번호"class="form-control input-sm" onlyNumber>
                                        </div>
                                    </li>                      
    """

    # onChange, defaultValue 따옴표 제거
    converted_html = convert_html(input_html)
    modified_html = re.sub(r'"(?=[{])|(?<=[}])"', '', converted_html)
    # 정규식을 사용하여 </uis:codeselect>를 삭제하고 > 앞에 / 붙이기
    modified_html = re.sub(r'}>.*', '}/>', modified_html)
    modified_html = re.sub(r'</Uis.*\n?', '', modified_html)
    print(modified_html)
