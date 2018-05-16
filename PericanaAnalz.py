import pandas as pd

filename = 'pericana.csv'
pericana_table = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
pericana_table.sido.unique()

#필요없는 값 '0'제거
print(pericana_table[pericana_table['sido']=='0'])
#sido가 0인것은 index가 1166였음.
#pericana_table = pericana_table.drop(pericana_table.index[1166])
pericana_table[pericana_table['sido']=='0']

#필요없는 값 '테스트'찾기.
print(pericana_table[pericana_table['sido']=='테스트'])

pericana_table = pericana_table.drop(pericana_table.index[798])
print(pericana_table[pericana_table['sido']=='테스트'])

print(pericana_table[pericana_table['sido']==''])

print(pericana_table[pericana_table['sido']==' '])
pericana_table = pericana_table[pericana_table['sido'] != ' ']
pericana_table = pericana_table.drop(pericana_table.index[111])
pericana_table = pericana_table.drop(pericana_table.index[227])
pericana_table = pericana_table.drop(pericana_table.index[243])
pericana_table = pericana_table.drop(pericana_table.index[430])
pericana_table = pericana_table.drop(pericana_table.index[592])
pericana_table = pericana_table.drop(pericana_table.index[731])
pericana_table = pericana_table.drop(pericana_table.index[832])
pericana_table = pericana_table.drop(pericana_table.index[855])
pericana_table = pericana_table.drop(pericana_table.index[897])
pericana_table = pericana_table.drop(pericana_table.index[913])
pericana_table = pericana_table.drop(pericana_table.index[1022])
pericana_table = pericana_table.drop(pericana_table.index[1143])
pericana_table.sido.unique()

sido_table = pd.read_csv('district.csv', encoding='CP949', index_col=0, header=0)
print(sido_table)

m = pericana_table.merge(sido_table, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)

m_result = m.query('_merge=="left_only" ')
m_result
print(m_result[['sido','gungu']])

gungu_alias= """ 청주시흥덕구:청주시  여주군:여주시   청주시서원구:청주시  용인시기흥구:용인시   
고양시일산서구:고양시  부천시오정구:부천시  천안시동남구:천안시  부강면:세종시  연서면:세종시  
창원시진해구:창원시  나리로:세종시  갈매로:세종시  성남시수정구:성남시   청주시상당구:청주시  
전의면:세종시  조치원읍:세종시  전주시완산구:전주시  창원시마산합포구:창원시   당진군:당진시 
안산시단원구:안산시  부천시소사구:부천시  안산시상록구:안산시  수원시장안구:수원시 
고양시일산동구:고양시  천안시서북구:천안시  안양시동안구:안양시  부천시원미구:부천시  
전주시덕진구:전주시  포항시북구:포항시  창원시마산회원구:창원시   창원시성산구:창원시  
안양시만안구:안양시  포항시남구:포항시  수원시권선구:수원시   고양시덕양구:고양시 
청원군:청주시   용인시수지구:용인시   수원시영릉구:수원시  용인시처인구:용인시 
수원시팔달구:수원시   수원시영통구:수원시   성남시중원구:성남시  성남시분당구:성남시  """

gungu_dict = dict(aliasset.split(':') for aliasset in gungu_alias.split())

pericana_table.gungu = pericana_table.gungu.apply(lambda v: gungu_dict.get(v,v))

m = pericana_table.merge(sido_table, on= ['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)

m_result = m.query('_merge =="left_only"')

print(m_result)
print(pericana_table)
pericana_table.to_csv('pericana_modify.csv', encoding='CP949', header=0)
