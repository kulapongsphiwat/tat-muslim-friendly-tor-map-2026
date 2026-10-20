"""Build the static map from the Excel workbook; Python standard library only."""
import datetime,html,json,re,zipfile,xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
GROUPS=['พร้อมขาย','พัฒนาเพื่อพร้อมขาย','มีศักยภาพ แต่ต้องพัฒนามาตรฐาน']

def read_sheet(archive,name):
    strings=[]
    if 'xl/sharedStrings.xml' in archive.namelist():
        strings=[''.join(el.itertext()) for el in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
    result=[]
    for row in ET.fromstring(archive.read(name)).findall('.//s:sheetData/s:row',NS):
        values={}
        for c in row.findall('s:c',NS):
            col=re.match(r'[A-Z]+',c.attrib['r']).group()
            v=c.find('s:v',NS);value=v.text if v is not None else ''
            if c.attrib.get('t')=='s':value=strings[int(value)]
            elif c.attrib.get('t')=='inlineStr':value=''.join(c.find('s:is',NS).itertext())
            values[col]=value or ''
        result.append(values)
    return result

def build():
    coordinate_rows=json.loads((ROOT/'data/locations.json').read_text(encoding='utf-8'))
    lookup={(r['n'].strip(),r['p'].strip()):r for r in coordinate_rows}
    audit_file=ROOT/'data/revalidation.json'
    audit={r['id']:r for r in json.loads(audit_file.read_text(encoding='utf-8'))} if audit_file.exists() else {}
    areas={'TMF-124':'เขาใหญ่–ปากช่อง','TMF-126':'เขาใหญ่–ปากช่อง','TMF-128':'เขาใหญ่–ปากช่อง','TMF-130':'เขาใหญ่–ปากช่อง','TMF-352':'เขาใหญ่–ปากช่อง','TMF-357':'เขาใหญ่–ปากช่อง','TMF-560':'ทางขึ้นเขาใหญ่ฝั่งปราจีนบุรี','TMF-227':'มวกเหล็ก–ปากช่อง'}
    for n in [122,123,125,127,129,131,133,134,135,353,354]:areas['TMF-'+str(n)]='เขายายเที่ยง–สีคิ้ว'
    with zipfile.ZipFile(ROOT/'data/places.xlsx') as archive:sheet=read_sheet(archive,'xl/worksheets/sheet1.xml')
    required=['ชื่อแหล่ง','จังหวัด','กลุ่ม','ประเภท','อัพเดตวันที่']
    header=next((i for i,row in enumerate(sheet) if all(x in row.values() for x in required)),None)
    if header is None:raise ValueError('Missing required Excel column headers')
    headers={v:k for k,v in sheet[header].items()}
    data=[]
    for row in sheet[header+1:]:
        name=row.get(headers['ชื่อแหล่ง'],'').strip()
        if not name:continue
        province=row.get(headers['จังหวัด'],'').strip();group=row.get(headers['กลุ่ม'],'').strip()
        if group not in GROUPS:raise ValueError('Unknown proposed group for '+name+': '+group)
        original=lookup.get((name,province),{})
        serial=row.get(headers['อัพเดตวันที่'],'')
        try:date=(datetime.datetime(1899,12,30)+datetime.timedelta(days=float(serial))).strftime('%d/%m/%Y')
        except (ValueError,TypeError):date=str(serial)
        item=dict(original)
        item.update({'id':original.get('id') or 'TMF-'+str(len(data)+1).zfill(3),'n':name,'p':province,'g':GROUPS.index(group)+1,'t':row.get(headers['ประเภท'],''),'u':date})
        item['a']=areas.get(item['id'],'')
        item.update(audit.get(item['id'],{}))
        item.setdefault('xy',None);item.setdefault('note','');item.setdefault('cs','')
        item.setdefault('url','https://www.google.com/maps/search/?api=1&query='+__import__('urllib.parse',fromlist=['quote']).quote(name+' '+province))
        if item['xy']:
            lon,lat=item['xy']
            if not (97<lon<106 and 5<lat<21):raise ValueError('Invalid coordinates: '+name)
        data.append(item)
    if not data:raise ValueError('No venues in Excel')
    if len({(r['n'],r['p']) for r in data})!=len(data):raise ValueError('Duplicate name and province in Excel')
    payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    template=(ROOT/'template/page.html').read_text(encoding='utf-8')
    assert template.count('__EXCEL_DATA__')==1
    document=template.replace('__EXCEL_DATA__',html.escape(payload,quote=True))
    out=ROOT/'site';out.mkdir(exist_ok=True)
    (out/'index.html').write_text(document,encoding='utf-8')
    (out/'.nojekyll').write_text('',encoding='utf-8')
    mapped=sum(bool(r['xy']) for r in data)
    summary={'title':'TAT Muslim Friendly TOR Map 2026','venues':len(data),'mapped':mapped,'pending_coordinates':len(data)-mapped,'groups':{g:sum(r['g']==i+1 for r in data) for i,g in enumerate(GROUPS)}}
    (out/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=True))
    return summary

if __name__=='__main__':build()
