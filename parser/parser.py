from BeautifulSoup import BeautifulSoup

def parse(content):
    code = BeautifulSoup(content)
    course = {}
    tmp = code.find('span', {'id': 'DERIVED_CLSRCH_DESCR200'}).string.split('&nbsp;&nbsp;')
    course['code'] = tmp[0].strip()
    course['name'] = tmp[-1].strip()
    tmp = code.find('span', {'id': 'DERIVED_CLSRCH_SSS_PAGE_KEYDESCR'}).string.split(' | ')
    course['location'] = tmp[0].strip()
    course['term'] = tmp[1].strip()
    course['type'] = tmp[2].strip()
    course['status'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_SSR_DESCRSHORT'}).string.strip()
    course['number'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_CLASS_NBR'}).string.strip()
    course['level'] = code.find('span', {'id': 'PSXLATITEM_XLATLONGNAME'}).string.strip()
    course['dates'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_SSR_DATE_LONG'}).string.strip()
    course['units'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_UNITS_RANGE'}).string.strip()
    course['campus'] = code.find('span', {'id': 'CAMPUS_TBL_DESCR'}).string.strip()
    course['requirements'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_SSR_REQUISITE_LONG'}).string.strip()
    course['designation'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_DESCRFORMAL'}).string.strip()
    course['description'] = code.find('span', {'id': 'DERIVED_CLSRCH_DESCRLONG'}).string.strip()
    course['materials'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_SSR_CLS_TXB_MSG'}).string.strip()
    course['capacity'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_ENRL_CAP'}).string.strip()
    course['enrolled'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_ENRL_TOT'}).string.strip()
    course['available'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_AVAILABLE_SEATS'}).string.strip()
    course['waiting_capacity'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_WAIT_CAP'}).string.strip()
    course['waiting'] = code.find('span', {'id': 'SSR_CLS_DTL_WRK_WAIT_TOT'}).string.strip()
    course['time'] = code.find('span', {'id': 'MTG_SCHED$0'}).string.strip()
    course['class'] = code.find('span', {'id': 'MTG_LOC$0'}).string.strip()
    course['instructor'] = code.find('span', {'id': 'MTG_INSTR$0'}).string.strip()
    course['date'] = code.find('span', {'id': 'MTG_DATE$0'}).string.strip()
    print course
           
for i in range(1, 5):
    f = open('testinput' + str(i) + '.html', 'r')
    content = f.read()
    parse(content)
    f.close()