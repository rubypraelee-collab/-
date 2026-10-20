<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>ตารางรถไฟการเลือกตั้งท้องถิ่น</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&display=swap">
<style>
:root{--bg:#e9edf2;--panel:#fff;--ink:#1c2733;--mut:#5c6b7a;--line:#d3dae2;--acc:#1d4f9c;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#161b21;--panel:#212830;--ink:#e8edf2;--mut:#9aa8b6;--line:#38424d;--acc:#7fb0ff}}
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Sarabun,Tahoma,sans-serif;font-size:14px}
.app{display:flex;height:100%}
aside{width:390px;max-width:100%;background:var(--panel);border-right:1px solid var(--line);overflow-y:auto;padding:16px}
main{flex:1;overflow:auto;padding:16px}
h1{font-size:18px;margin:0 0 4px}h2{font-size:14px;margin:18px 0 6px;color:var(--acc)}
p.h{margin:0 0 8px;color:var(--mut);font-size:12.5px}
label.f{display:block;margin:6px 0;font-size:12.5px;color:var(--mut)}
select,input{font:inherit;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:5px 7px;width:100%}
.row{border-left:4px solid var(--c);padding:4px 0 4px 8px;margin:7px 0}
.row .t{font-size:12.5px;line-height:1.35;margin-bottom:3px}
.row .d{display:flex;gap:6px;align-items:center}.row .d span{font-size:12px;color:var(--mut)}
.be{font-size:11.5px;color:var(--mut);min-height:15px}
.btns{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
button{font:inherit;border:1px solid var(--acc);background:var(--acc);color:#fff;border-radius:4px;padding:7px 12px;cursor:pointer}
button.s{background:transparent;color:var(--acc)}
.pg{background:#fff;margin:0 auto 16px;box-shadow:0 1px 6px rgba(0,0,0,.2);max-width:1050px}
.pg svg{display:block;width:100%;height:auto}
.empty{padding:40px;color:var(--mut);text-align:center}
@media (max-width:820px){.app{flex-direction:column;height:auto}aside{width:100%;overflow:visible}main{overflow:visible}}
@media print{@page{size:A4 landscape;margin:0}body{background:#fff}aside{display:none}.app,main{display:block;padding:0;overflow:visible}.pg{box-shadow:none;margin:0;page-break-after:always;max-width:none}.pg svg{width:297mm;height:209.5mm;max-width:none;max-height:none;margin:0}.pg:last-child{page-break-after:auto}}
</style>
</head>
<body>
<div class="app">
<aside>
<h1>ตารางรถไฟการเลือกตั้ง</h1>
<p class="h">กรอกวันที่ ตารางและลูกศรจะสร้างให้อัตโนมัติ ข้อมูลถูกเก็บไว้ในเครื่องนี้</p>
<h2>ข้อมูลหน่วยงาน</h2>
<div id="meta"></div>
<h2>วันที่แต่ละขั้นตอน</h2>
<p class="h">ช่องวันที่ ม.40 และผลการเลือกตั้ง ม.17 คำนวณจากวันเลือกตั้งให้ก่อน แก้ไขเองได้</p>
<div id="steps"></div>
<div class="btns"><button id="png">ดาวน์โหลด PNG</button><button id="prt">พิมพ์ / บันทึก PDF</button><button id="clr" class="s">ล้างวันที่</button></div>
</aside>
<main id="out"></main>
</div>
<script>
const TM=['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม'];
const TS=['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.'];
const WD=['อา','จ','อ','พ','พฤ','ศ','ส'],WF=['อาทิตย์','จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์'];
const COL={b:'#1d4f9c',r:'#c8232c',g:'#178a3c'},TINT={b:'#cfe0f8',r:'#f9cfd0',g:'#cdeed8'};
const num=s=>{if(!s)return null;const[y,m,d]=s.split('-').map(Number);return Date.UTC(y,m-1,d)/864e5};
const str=n=>new Date(n*864e5).toISOString().slice(0,10);
const D=n=>new Date(n*864e5);
const fmt=n=>{const d=D(n);return `${d.getUTCDate()} ${TM[d.getUTCMonth()]} ${d.getUTCFullYear()+543}`};
const sh=n=>{const d=D(n);return `${d.getUTCDate()} ${TS[d.getUTCMonth()]} ${(d.getUTCFullYear()+543)%100}`};
const esc=s=>String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
 
const BB='#0000FF',RR='#FF0000',K='#000000',B='#0000CC',Gr='#008000',R='#C00000',N='#000099';
const G=[
{id:'v',t:'d',i:[['วันที่ถูกสั่งให้พ้นจากตำแหน่ง',B]]},
{id:'g2',t:'d',i:[['ผอ.กต.ท้องถิ่นเสนอร่าง ส.ถ.1/1',B]]},
{id:'g3',t:'d',i:[['วันที่ ผอ.กต.จว.\nให้ความเห็นชอบ',Gr]]},
{id:'g4',t:'d',i:[['ผอ.กต.ท้องถิ่นประกาศ\nให้มีการเลือกตั้ง (ม.12)',N],['แต่งตั้ง กกต.ท้องถิ่น',Gr]]},
{id:'reg',t:'r',i:[['วันรับสมัครเลือกตั้ง (ม.12)',RR]]},
{id:'g6',t:'d',i:[['ประกาศกำหนดหน่วยเลือกตั้ง/\nที่เลือกตั้ง (ม.23)',N],['ประกาศบัญชีรายชื่อ\nผู้มีสิทธิเลือกตั้ง (ม.43)',Gr]]},
{id:'g7',t:'d',i:[['วันสุดท้ายแต่งตั้ง จพง.ปน. (ม.28)',B],['วันสุดท้ายการยื่นคำร้องคัดค้านการรับสมัคร\nกรณีก่อนวันเลือกตั้งไม่น้อยกว่า 20 วัน (ม.56)',Gr]]},
{id:'g8',t:'d',i:[['ประกาศบัญชีรายชื่อผู้สมัคร (ม.52)',Gr]]},
{id:'g9',t:'d',i:[['วันสุดท้ายส่งหนังสือ\nแจ้งเจ้าบ้าน (ม.43)',B]]},
{id:'g10',t:'d',i:[['วันสุดท้ายยื่นคำร้องต่อ กกต.\nกรณีไม่รับสมัคร (ม.55)',B]]},
{id:'g11',t:'d',i:[['วันสุดท้ายเพิ่มชื่อ/ถอนชื่อ (ม.44 , ม.45)',Gr],['วันสุดท้ายที่ กกต.วินิจฉัยสิทธิสมัคร (ม.56)','#003399'],['วันสุดท้ายเปลี่ยนแปลงหน่วยเลือกตั้ง/\nที่เลือกตั้ง (ม.23)',Gr]]},
{id:'g12',t:'d',i:[['วันสุดท้ายแจ้งการแต่งตั้ง\nตัวแทนผู้สมัคร (ม.58)',Gr]]},
{id:'m40b',t:'r',a:1,i:[['แจ้งเหตุที่ไม่อาจไปใช้\nสิทธิเลือกตั้ง (ม.40)',R]],n:'ก่อนวันเลือกตั้ง 7 วัน'},
{id:'el',t:'d',el:1,i:[['วันเลือกตั้ง',RR]]},
{id:'m40a',t:'r',a:1,i:[['แจ้งเหตุที่ไม่อาจไปใช้\nสิทธิเลือกตั้ง (ม.40)',R]],n:'หลังวันเลือกตั้ง 7 วัน'},
{id:'g16',t:'d',i:[['วันสุดท้ายศาลอุทธรณ์/ศาลอุทธรณ์ภาค\nวินิจฉัยสิทธิสมัคร (ม.56)',Gr],['วันสุดท้ายมอบวัสดุอุปกรณ์',B],['วันสุดท้ายอบรม จพง.ปน',Gr]]},
{id:'g17',t:'d',i:[['วันสุดท้ายจัดส่งบัญชีรายชื่อผู้มีสิทธิเลือกตั้ง\nเพื่อจัดทำบัญชีผู้ถูกจำกัดสิทธิ',N]]},
{id:'g18',t:'d',a:1,i:[['ประกาศผลการเลือกตั้ง\nกรณีไม่มีเรื่องร้องคัดค้าน (ม.17 ว.1)',R]],n:'ครบ 30 วันหลังเลือกตั้ง'},
{id:'g19',t:'d',a:1,i:[['ประกาศบัญชีรายชื่อผู้ไม่ไปใช้สิทธิเลือกตั้ง\nและมิได้แจ้งเหตุหรือแจ้งเหตุไว้แล้ว\nแต่เหตุนั้นมิใช่เหตุอันสมควร (ม.41)',N],['ประกาศผลการเลือกตั้ง\nกรณีมีเรื่องร้องคัดค้าน (ม.17 ว.2)',Gr]],n:'ครบ 60 วันหลังเลือกตั้ง'}];
const eb=n=>g=>{const e=g('el',0);return e==null?null:[e-n]};
const ea=n=>g=>{const e=g('el',0);return e==null?null:[e+n]};
const AUTO={
 reg:{end:1,f:g=>{const a=g('reg',0);return a==null?null:[a+4]},n:'วันปิดรับสมัครคำนวณให้ 5 วัน (ใส่แค่วันแรกก็ได้)'},
 g6:{f:eb(26),n:'ก่อนวันเลือกตั้ง 26 วัน'},
 g7:{f:eb(21),n:'ก่อนวันเลือกตั้ง 21 วัน'},
 g8:{f:g=>{const r=g('reg',1)??g('reg',0);return r==null?null:[r+7]},n:'วันที่ 7 นับแต่วันปิดรับสมัคร'},
 g9:{f:eb(16),n:'ก่อนวันเลือกตั้ง 16 วัน'},
 g10:{f:g=>{const x=g('g8',0);return x==null?null:[x+3]},n:'3 วันนับแต่วันประกาศรายชื่อ (ม.52)'},
 g11:{f:eb(11),n:'ก่อนวันเลือกตั้ง 11 วัน'},
 g12:{f:eb(8),n:'ก่อนวันเลือกตั้ง 8 วัน'},
 m40b:{f:g=>{const e=g('el',0);return e==null?null:[e-7,e-1]},n:'ก่อนวันเลือกตั้ง 7 วัน'},
 m40a:{f:g=>{const e=g('el',0);return e==null?null:[e+1,e+7]},n:'หลังวันเลือกตั้ง 7 วัน'},
 g16:{f:eb(1),n:'ก่อนวันเลือกตั้ง 1 วัน'},
 g17:{f:ea(15),n:'วันที่ 15 นับแต่วันเลือกตั้ง'},
 g18:{f:ea(30),n:'30 วันนับแต่วันเลือกตั้ง'},
 g19:{f:ea(60),n:'60 วันนับแต่วันเลือกตั้ง'}};
const TYPES=[['pao','องค์การบริหารส่วนจังหวัด (อบจ.)','อบจ.'],['tn','เทศบาลนคร (ทน.)','ทน.'],['tm','เทศบาลเมือง (ทม.)','ทม.'],['tt','เทศบาลตำบล (ทต.)','ทต.'],['tao','องค์การบริหารส่วนตำบล (อบต.)','อบต.']];
const POS=[['member','สมาชิกสภา'],['head','นายก (นายก อบจ. / นายกเทศมนตรี / นายก อบต.)']];
const DEF={type:'tt',pos:'member',name:'บึงระมาณ',zone:'1',amp:'บางระกำ',case:'removed',person:'',foot:'กลุ่มงานจัดการเลือกตั้งและการมีส่วนร่วม สนง.กกต.จว.พิษณุโลก'};
 
let S={meta:{},v:{},touched:{}};
try{S=Object.assign(S,JSON.parse(localStorage.getItem('trainsched')||'{}'))}catch(e){}
S.meta=S.meta||{};S.v=S.v||{};S.touched=S.touched||{};
Object.keys(DEF).forEach(k=>{if(S.meta[k]===undefined||(k==='pos'&&!['member','head'].includes(S.meta.pos)))S.meta[k]=DEF[k]});
const CASES=[['removed','กรณีถูกสั่งให้พ้นจากตำแหน่ง'],['dead','กรณีแทนตำแหน่งที่ว่าง — ตาย'],['resign','กรณีแทนตำแหน่งที่ว่าง — ลาออก'],['term','กรณีครบวาระ']];
const MI=()=>{const m=S.meta,T=TYPES.find(t=>t[0]===m.type)||TYPES[3],head=m.pos==='head',org=T[2]+(m.name||''),mun=['tn','tm','tt'].includes(m.type);
  const posTitle=head?(mun?'นายกเทศมนตรี':'นายก'):'สมาชิกสภา';
  return{org,head,posTitle,zone:m.zone,pao:m.type==='pao',
   amp:m.type==='pao'||!m.amp?'':'อ.'+String(m.amp).replace(/^อ\./,''),
   sum:`สรุปแผนการจัดการเลือกตั้ง${head?posTitle:'สมาชิก'} ${org}${head?'':` เขต ${m.zone}`}${m.type==='pao'||!m.amp?'':' อ.'+String(m.amp).replace(/^อ\./,'')}`}};
const CI=()=>{const m=S.meta,mi=MI(),cs=m.case||'removed',why=cs==='dead'?'ตาย':'ลาออก',ps=cs==='dead'||cs==='resign',nm=m.person||'ชื่อ-สกุล';
  return{cs,lim:cs==='term'?45:60,keep:ps,
   form:{removed:'วันที่ถูกสั่งให้พ้นจากตำแหน่ง',dead:'วันที่ตำแหน่งว่างลง (ตาย)',resign:'วันที่ตำแหน่งว่างลง (ลาออก)',term:'วันที่ครบวาระ'}[cs],
   first:cs==='removed'?'วันที่ถูกสั่งให้พ้นจากตำแหน่ง':cs==='term'?'วันที่ครบวาระ':mi.head?`${nm}\n${mi.posTitle} ${mi.org}\n(${why})`:`${nm}\nส.${mi.org}\nเขตเลือกตั้งที่ ${mi.zone} (${why})`,
   sum:cs==='term'?'วันที่ครบวาระ':'วันที่ตำแหน่งว่างลง',cnt:cs==='term'?'นับจากวันที่ครบวาระ':'นับจากวันที่ตำแหน่งว่างลง',
   title:cs==='removed'?'กรณีถูกสั่งให้พ้นจากตำแหน่ง':cs==='term'?'กรณีครบวาระ':`${m.person||''} ${why}`}};
const save=()=>{try{localStorage.setItem('trainsched',JSON.stringify(S))}catch(e){}};
const val=(id,k)=>(S.v[id]||[])[k]||'';
const $=q=>document.querySelector(q);
 
// ---------- ฟอร์ม ----------
const opt=(arr,cur)=>arr.map(c=>`<option value="${c[0]}"${cur===c[0]?' selected':''}>${c[1]}</option>`).join('');
$('#meta').innerHTML=`<label class="f">กรณีการเลือกตั้ง<select data-m="case">${opt(CASES,S.meta.case)}</select></label>
<label class="f">ประเภท อปท.<select data-m="type">${opt(TYPES,S.meta.type)}</select></label>
<label class="f">ตำแหน่งที่เลือกตั้ง<select data-m="pos">${opt(POS,S.meta.pos)}</select></label>
<label class="f">ชื่อ อปท. (ไม่ต้องพิมพ์ ทต./อบต. นำหน้า)<input data-m="name" value="${esc(S.meta.name)}"></label>
<label class="f" id="zoneRow">เขตเลือกตั้งที่<input data-m="zone" value="${esc(S.meta.zone)}"></label>
<label class="f" id="ampRow">อำเภอ (ไม่ต้องพิมพ์ อ. นำหน้า)<input data-m="amp" value="${esc(String(S.meta.amp).replace(/^อ\./,''))}"></label>
<label class="f" id="personRow">ชื่อ-สกุล ผู้ที่ตาย/ลาออก<input data-m="person" value="${esc(S.meta.person)}"></label>
<label class="f">ผู้จัดทำ (ท้ายหน้า)<input data-m="foot" value="${esc(S.meta.foot)}"></label>`;
const ORDER=['v','el'].concat(G.map(g=>g.id).filter(i=>i!=='v'&&i!=='el')).map(id=>G.find(g=>g.id===id));
$('#steps').innerHTML=ORDER.map(g=>{
  const two=g.t==='r',A=AUTO[g.id],note=A?`อัตโนมัติ: ${A.n}`:g.id==='el'?'วันสำคัญ — กรอกก่อน ขั้นตอนอื่นจะคำนวณวันที่ให้':'';
  return `<div class="row" style="--c:${g.i[0][1]}"><div class="t" id="t-${g.id}">${esc(g.i.map(x=>x[0]).join(' / ').replace(/\n/g,' '))}</div>
  ${note?`<div class="be">${esc(note)} <a href="#" class="rst" data-rst="${g.id}" style="display:none">↺ ใช้ค่าอัตโนมัติ</a></div>`:''}
  <div class="d"><input type="date" data-id="${g.id}" data-k="0" value="${val(g.id,0)}">${two?`<span>ถึง</span><input type="date" data-id="${g.id}" data-k="1" value="${val(g.id,1)}">`:''}</div>
  <div class="be" id="be-${g.id}"></div></div>`}).join('');
 
function applyAuto(){
  const g=(id,k)=>num(val(id,k));
  for(const id in AUTO){
    if(S.touched[id])continue;
    const A=AUTO[id],v=A.f(g),cur=S.v[id]=S.v[id]||['',''];
    if(A.end)cur[1]=v?str(v[0]):'';else{cur[0]=v?str(v[0]):'';cur[1]=v&&v[1]!=null?str(v[1]):''}
    document.querySelectorAll(`[data-id="${id}"]`).forEach(el=>el.value=cur[el.dataset.k]||'');
  }
}
function showBE(){G.forEach(g=>{const a=num(val(g.id,0)),b=num(val(g.id,1));
  $('#be-'+g.id).textContent=a==null?'':`${WF[D(a).getUTCDay()]}ที่ ${fmt(a)}`+(b!=null?` – ${fmt(b)}`:'')});
  const ci=CI(),mi=MI();$('#t-v').textContent=ci.form;
  $('#personRow').style.display=ci.keep?'':'none';$('#zoneRow').style.display=mi.head?'none':'';$('#ampRow').style.display=mi.pao?'none':'';
  document.querySelectorAll('.rst').forEach(a=>a.style.display=S.touched[a.dataset.rst]?'':'none');
  const V=num(val('v',0)),E=num(val('el',0));if(V!=null&&E!=null){const n=E-V+1,bad=n>ci.lim;$('#be-el').innerHTML=($('#be-el').textContent?esc($('#be-el').textContent)+'<br>':'')+`<span style="color:${bad?'#d22':'inherit'}">วันที่ ${n} นับจากวันว่างลง · ต้องไม่เกิน ${ci.lim} วัน${bad?' ⚠ เกินกำหนด':''}</span>`}
}
 
document.addEventListener('input',e=>{
  const t=e.target;
  if(t.dataset.m){S.meta[t.dataset.m]=t.value}
  else if(t.dataset.id){const id=t.dataset.id;(S.v[id]=S.v[id]||['',''])[+t.dataset.k]=t.value;
    if(AUTO[id]&&(id!=='reg'||+t.dataset.k===1))S.touched[id]=1;applyAuto()}
  save();showBE();draw();
});
document.addEventListener('click',e=>{const a=e.target.closest('.rst');if(!a)return;e.preventDefault();delete S.touched[a.dataset.rst];applyAuto();save();showBE();draw()});
$('#clr').onclick=()=>{if(!confirm('ล้างวันที่ทั้งหมด?'))return;S.v={};S.touched={};
  document.querySelectorAll('[data-id]').forEach(el=>el.value='');save();showBE();draw()};
$('#prt').onclick=()=>window.print();
$('#png').onclick=()=>{document.querySelectorAll('.pg svg').forEach((svg,i)=>{
  const w=+svg.viewBox.baseVal.width,h=+svg.viewBox.baseVal.height;
  const x=new XMLSerializer().serializeToString(svg);
  const img=new Image();img.onload=()=>{const c=document.createElement('canvas');c.width=w*2;c.height=h*2;
    const g=c.getContext('2d');g.fillStyle='#fff';g.fillRect(0,0,c.width,c.height);g.drawImage(img,0,0,c.width,c.height);
    const a=document.createElement('a');a.download=`ตารางรถไฟ-หน้า${i+1}.png`;a.href=c.toDataURL('image/png');a.click()};
  img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(x)})};
 
// ---------- วาดตาราง ----------
const CW=25,LX=200,RH=19,BH=RH*4,W=LX+31*CW+8,FS=10,LH=14,A4=297/210,MX=44,MT=32,MB=44,TX='font-family="Sarabun,Tahoma,sans-serif"';
const cvx=document.createElement('canvas').getContext('2d');
const tw=(s,f=FS)=>{cvx.font=`600 ${f}px Sarabun,Tahoma,sans-serif`;return cvx.measureText(s).width};
function draw(){
  const ci=CI();G[0].i[0][0]=ci.first;G[0].i[0][2]=ci.keep?'keep':undefined;
  const V=num(val('v',0)),E=num(val('el',0));
  const out=$('#out');
  if(V==null||E==null){out.innerHTML=`<div class="empty">กรอก “${ci.form}” และ “วันเลือกตั้ง” เพื่อสร้างตาราง</div>`;return}
  const groups=[];
  G.forEach(g=>{const s=num(val(g.id,0));if(s==null)return;let e=num(val(g.id,1));if(e==null||e<s||g.t==='d')e=s;groups.push({g,s,e,items:g.i})});
  const last=Math.max(E+60,...groups.map(x=>x.e));
  const a=D(V),b=D(last),months=[];
  for(let k=a.getUTCFullYear()*12+a.getUTCMonth();k<=b.getUTCFullYear()*12+b.getUTCMonth();k++){
    const y=Math.floor(k/12),m=k%12;months.push({y,m,s:Date.UTC(y,m,1)/864e5,n:new Date(Date.UTC(y,m+1,0)).getUTCDate()})}
  const singles=new Set(),ranges=[];groups.forEach(x=>{if(x.e>x.s)ranges.push([x.s,x.e]);else singles.add(x.s)});
  const mi=MI(),title=`แผนการจัดการเลือกตั้ง${mi.posTitle} ${mi.org}${mi.head?'':` เขตเลือกตั้งที่ ${mi.zone}`} (${ci.title} วันที่ ${sh(V)})`;
  const ctx={V,E,groups,title,sumHead:mi.sum,ranges,singles,lim:ci.lim,cnt:ci.cnt,sum:ci.sum};
  const chunk=mode=>{if(mode==='one'||months.length<=2)return mode==='one'?months.map(x=>[x]):[months];
    const rest=months.slice(2),np=Math.ceil(rest.length/3),base=Math.floor(rest.length/np),ex=rest.length%np,out=[months.slice(0,2)];let i=0;
    for(let p=0;p<np;p++){const n=base+(p<ex?1:0);out.push(rest.slice(i,i+n));i+=n}return out};
  const build=mode=>{const pages=chunk(mode);
    const run=()=>{FIX=0;HN=[];MIDMAX=0;pages.forEach((pm,pi)=>page(pm,pi,pages.length,ctx))};
    LFAIL=false;MIDMIN=0;run();MIDMIN=MIDMAX;run();return{pages,h:Math.max(...HN),failed:LFAIL}};
  const lim=((W+2*MX)/A4-MT-MB)*1.4;
  let r=build('std');
  if(months.length>1&&(r.failed||r.h>lim)){const r1=build('one');if(r.failed||(!r1.failed&&r1.h<r.h))r=r1}
  FIX=Math.max(W+2*MX,(r.h+MT+MB)*A4);
  out.innerHTML=r.pages.map((pm,pi)=>`<div class="pg">${page(pm,pi,r.pages.length,ctx)}</div>`).join('');
}
let FIX=0,HN=[];
function block(mo,gt,c){
  const fit=(t,w)=>Math.min(10,10*w/(tw(t,10)*1.06));
  const mt='เดือน'+TM[mo.m];
  let s=`<text x="38" y="${gt+BH/2-3}" text-anchor="middle" font-size="${fit(mt,74).toFixed(1)}" font-weight="700" ${TX}>${mt}</text><text x="38" y="${gt+BH/2+12}" text-anchor="middle" font-size="10" font-weight="700" ${TX}>${mo.y+543}</text>`;
  [['วัน',K],['วันที่',K],[c.cnt,BB],['นับจากวันเลือกตั้ง',RR]].forEach(([r,col],i)=>{
    s+=`<rect x="80" y="${gt+i*RH}" width="${LX-80}" height="${RH}" fill="#D7E4BD" stroke="#555" stroke-width=".7"/><text x="${(80+LX)/2}" y="${gt+i*RH+13}" text-anchor="middle" font-size="${fit(r,LX-80-6).toFixed(1)}" font-weight="700" fill="${col}" ${TX}>${r}</text>`});
  for(let d=1;d<=mo.n;d++){
    const dn=mo.s+d-1,x=LX+(d-1)*CW,wd=D(dn).getUTCDay(),we=wd===0||wd===6,el=dn===c.E;
    const f=el?'#FFC000':we?'#FCD5B5':'#fff';
    [WD[wd],d,dn>=c.V&&dn-c.V<c.lim?dn-c.V+1:'',dn>=c.V&&dn<=c.E+60?Math.abs(dn-c.E):''].forEach((t,i)=>{
      s+=`<rect x="${x}" y="${gt+i*RH}" width="${CW}" height="${RH}" fill="${i===0&&!el&&!we?'#D7E4BD':f}" stroke="#555" stroke-width=".7"/><text x="${x+CW/2}" y="${gt+i*RH+13}" text-anchor="middle" font-size="10" font-weight="${el||i===0?700:400}" fill="${i===2?BB:i===3?RR:K}" ${TX}>${t}</text>`});
  }
  c.ranges.forEach(([a,b])=>{const s0=Math.max(a,mo.s),e0=Math.min(b,mo.s+mo.n-1);if(s0<=e0)s+=`<rect x="${LX+(s0-mo.s)*CW}" y="${gt+RH}" width="${(e0-s0+1)*CW}" height="${RH}" fill="none" stroke="#FF0000" stroke-width="2.4"/>`});
  for(let d=1;d<=mo.n;d++)if(c.singles.has(mo.s+d-1))s+=`<rect x="${LX+(d-1)*CW}" y="${gt+RH}" width="${CW}" height="${RH}" fill="none" stroke="#FF0000" stroke-width="2.4"/>`;
  return s;
}
const hit=(a,b,mx,my)=>a.x0<b.x1+mx&&b.x0<a.x1+mx&&a.y0<b.y1+my&&b.y0<a.y1+my;
const stemHit=(ln,st,r)=>ln>r.x0-4&&ln<r.x1+4&&st[0]<r.y1+2&&st[1]>r.y0-2;
const clash=(rs,st,ln,p)=>rs.some(a=>p.rs.some(b=>hit(a,b,10,5)))||p.rs.some(r=>stemHit(ln,st,r))||rs.some(r=>stemHit(p.ln,p.st,r))||(Math.abs(ln-p.ln)<7&&st[0]<p.st[1]&&st[1]>p.st[0]);
let RVR=null,MIDMIN=0,MIDMAX=0,LFAIL=false;
function tryPlace(u,cd,Hz,P){
  const up=cd.edge==='up',cl=(x,w)=>Math.min(Math.max(x,6),W-6-w),V=[];
  u.lays.forEach((L,li)=>{
    if(!u.fan){const w=L.w;[u.ln-w/2,u.ln-w*.75+8,u.ln-w*.25-8,u.ln-12,u.ln-w+12,u.ln-w*.9+10,u.ln-w*.1-10].forEach(x=>{const x0=cl(x,w);if(u.ln>=x0+8&&u.ln<=x0+w-8)V.push({m:'s',x0,w,h:L.h,li})})}
    if(!u.el){const w=L.wf,h=L.hf;[[u.ln-3,'R'],[u.ln-w+3,'L']].forEach(([x0,m])=>{if(x0>=6&&x0+w<=W-6)V.push({m,x0,w,h,li})})}
  });
  if(RVR)for(let i=V.length-1;i>0;i--){const j=Math.floor(RVR()*(i+1));[V[i],V[j]]=[V[j],V[i]]}
  const d0=u.range?40:26;
  for(let d=d0;d<=Hz-9;d+=4)for(const v of V){
    if(d+v.h>Hz-16)continue;
    const y0=up?Hz-d-v.h:d,F={x0:v.x0,x1:v.x0+v.w,y0,y1:y0+v.h},st=up?[F.y1,Hz]:[0,F.y0],rs=[F];
    if(u.range){const a=u.xs+CW/2-3,b=u.xe-CW/2+3;rs.push(up?{x0:a,x1:b,y0:Hz-22,y1:Hz}:{x0:a,x1:b,y0:0,y1:22})}
    if(!P.some(p=>clash(rs,st,u.ln,p)))return{d,F,st,rs,ln:u.ln,mode:v.m,li:v.li};
  }
  return null;
}
function layoutZones(units,H0){
  let seed=7,lastFail=null;const rnd=()=>(seed=(seed*1103515245+12345)&0x7fffffff)/0x7fffffff;
  const base=[units.slice().sort((a,b)=>b.h*b.w-a.h*a.w),units.slice().sort((a,b)=>a.w-b.w)];
  const attempt=(order,H)=>{
    const placed=H.map(()=>[]);
    for(const u of order){
      let best=null;
      for(const cd of u.cand){const r=tryPlace(u,cd,H[cd.z],placed[cd.z]);if(r&&(!best||r.d<best.r.d))best={cd,r}}
      if(!best){lastFail=u;return false}
      placed[best.cd.z].push(best.r);u.pl=Object.assign({z:best.cd.z,edge:best.cd.edge},best.r);
    }
    return true;
  };
  const solve=(H,n)=>{for(let a=0;a<n;a++){let o;RVR=a<2?null:rnd;
    if(a<2)o=base[a];else{o=units.slice();for(let i=o.length-1;i>0;i--){const j=Math.floor(rnd()*(i+1));[o[i],o[j]]=[o[j],o[i]]}}
    if(attempt(o,H)){RVR=null;return true}}RVR=null;return false};
  let H=H0.slice(),ok=false;
  for(let g=0;g<45&&!ok;g++){ok=solve(H,16);if(!ok)H[lastFail.cand.reduce((a,b)=>H[a.z]<=H[b.z]?a:b).z]+=16}
  if(ok){
    let best={H:H.slice(),pl:units.map(u=>u.pl)};
    for(const st of[16,6])for(let z=0;z<H.length;z++)while(H[z]-st>=H0[z]){
      H[z]-=st;
      if(solve(H,10))best={H:H.slice(),pl:units.map(u=>u.pl)};else{H[z]+=st;break}}
    units.forEach((u,i)=>u.pl=best.pl[i]);return best.H;
  }
  LFAIL=true;
  units.forEach(u=>{if(u.pl)return;const z=u.cand[0].z,x0=Math.min(Math.max(u.fan?u.ln-3:u.ln-u.w/2,6),W-6-u.w),y0=H[z]-12-u.h,F={x0,x1:x0+u.w,y0,y1:y0+u.h};
    u.pl={z,edge:'up',d:12,F,ln:u.ln,mode:u.fan?'R':'s',li:0,rs:[F],st:[F.y1,H[z]]}});
  return H;
}
function page(pm,pi,np,c){
  const first=pi===0,lastp=pi===np-1,nz=pm.length+1,units=[];
  pm.forEach((mo,k)=>{
    const by={};
    c.groups.filter(g=>g.s<mo.s+mo.n&&g.e>=mo.s).forEach(g=>{
      const s=Math.max(g.s,mo.s),t=Math.min(g.e,mo.s+mo.n-1),xs=LX+(s-mo.s)*CW,xe=LX+(t-mo.s)*CW+CW,key=xs+'_'+xe;
      const o=by[key]=by[key]||{xs,xe,range:t>s,el:false,items:[]};
      o.el=o.el||!!g.g.el;g.items.forEach(it=>o.items.push({l1:it[2]==='keep'?it[0].split('\n'):(o1=>tw(o1)<=400?[o1]:it[0].split('\n'))(it[0].replace(/\n/g,' ')),l2:it[0].split('\n'),col:it[1]}));
    });
    Object.values(by).forEach(o=>{
      const items=o.items,fan=items.length>1,el=o.el&&!fan,u={k,xs:o.xs,xe:o.xe,ln:(o.xs+o.xe)/2,range:o.range,el,fan,items,cand:[{z:k,edge:'up'},{z:k+1,edge:'down'}]};
      const mkLay=wrap=>{const its=items.map(i=>({col:i.col,lines:wrap?i.l2:i.l1}));let top=0;its.forEach(i=>{i.ih=i.lines.length*LH+2;i.top=top;top+=i.ih+4});
        const hf=top-4,wt=Math.max(...its.flatMap(i=>i.lines.map(l=>tw(l)))),L={its,hf,wt,wf:wt+19};
        if(fan){L.w=L.wf;L.h=hf}else{const fs=FS,lh=el?16:LH;L.lh=lh;L.fs=fs;L.w=Math.max(...its[0].lines.map(l=>tw(l,fs)))+(el?30:16);L.h=its[0].lines.length*lh+(el?10:4)}
        return L};
      u.lays=[mkLay(false)];if(items.some(i=>i.l1.join('|')!==i.l2.join('|')))u.lays.push(mkLay(true));
      u.w=u.lays[0].w;u.h=u.lays[0].h;
      units.push(u)});
  });
  const H0=pm.map(()=>40).concat([34]);for(let k=1;k<pm.length;k++)H0[k]=Math.max(pm.length>2?80:100,pm.length>2?Math.min(MIDMIN,120):MIDMIN);
  const H=layoutZones(units,H0);for(let k=1;k<pm.length;k++)MIDMAX=Math.max(MIDMAX,H[k]);
  const zt=[],bt=[];let y=first?148:34;
  for(let z=0;z<nz;z++){zt[z]=y;y+=H[z];if(z<pm.length){bt[z]=y;y+=BH}}
  const noteH=lastp?40:0,Hn=y+noteH+8,_=HN.push(Hn),PW=FIX||Math.max(W+2*MX,(Hn+MT+MB)*A4),PH=PW/A4,ox=(PW-W)/2;
  let s=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${PW} ${PH}"><rect width="${PW}" height="${PH}" fill="#fff"/><defs>${[K,B,Gr,R,N].map(v=>`<marker id="ar${v.slice(1)}" viewBox="0 0 8 8" refX="7" refY="4" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0L8,4L0,8z" fill="${v}"/></marker>`).join('')}</defs><g transform="translate(${ox},${MT})">`;
  s+=`<text x="${W/2}" y="18" text-anchor="middle" font-size="${Math.min(18,18*(W-20)/Math.max(1,tw(c.title,18)*1.06)).toFixed(1)}" font-weight="700" ${TX}>${esc(c.title)}</text>`;
  if(first){
    const g=id=>num(val(id,0)),R1=g('reg'),R2=num(val('reg',1))||R1,m=S.meta;
    const rows=[[c.sum,fmt(c.V),R],['วันรับสมัคร',R1!=null?`${fmt(R1)}${R2>R1?` ถึง ${fmt(R2)}`:''}`:'-',N],['วันเลือกตั้ง',`วัน${WF[D(c.E).getUTCDay()]}ที่ ${fmt(c.E)}`,Gr],
      ['วันประกาศผลการเลือกตั้งตามมาตรา 17 วรรคหนึ่ง',g('g18')?fmt(g('g18')):'-',K],['วันประกาศผลการเลือกตั้งตามมาตรา 17 วรรคสอง',g('g19')?fmt(g('g19')):'-',K]];
    const head=c.sumHead;
    const vx=40+Math.max(...rows.map(r=>tw('- '+r[0])))+18,bw=Math.max(vx+Math.max(...rows.map(r=>tw(r[1])))+24,tw(head)+60)-24;
    s+=`<rect x="24" y="34" width="${bw}" height="100" rx="14" fill="#fff" stroke="#9BBB59" stroke-width="3"/><text x="40" y="54" font-size="10" font-weight="600" ${TX}>${esc(head)}</text>`;
    rows.forEach((r,i)=>{s+=`<text x="40" y="${74+i*14}" font-size="10" font-weight="700" fill="${r[2]}" ${TX}>- ${esc(r[0])}</text><text x="${vx}" y="${74+i*14}" font-size="10" font-weight="700" fill="${r[2]}" ${TX}>${esc(r[1])}</text>`});
  }
  pm.forEach((mo,k)=>{s+=block(mo,bt[k],c)});
  const mk=col=>`marker-end="url(#ar${col.slice(1)})"`;
  units.forEach(u=>{
    const p=u.pl,z0=zt[p.z],up=p.edge==='up',eY=up?z0+H[p.z]:z0,F=p.F,fy0=F.y0+z0,fy1=F.y1+z0,dir=up?-1:1;
    const ac=u.range?R:K,by=eY+dir*18,tip=eY+dir*2,start=u.range?by:tip,sw=1.8;
    if(u.range){const xa=u.xs+CW/2,xb=u.xe-CW/2;
      s+=`<line x1="${xa}" y1="${by}" x2="${xa}" y2="${tip}" stroke="${ac}" stroke-width="${sw}" ${mk(ac)}/><line x1="${xb}" y1="${by}" x2="${xb}" y2="${tip}" stroke="${ac}" stroke-width="${sw}" ${mk(ac)}/><line x1="${xa-sw/2}" y1="${by}" x2="${xb+sw/2}" y2="${by}" stroke="${ac}" stroke-width="${sw}"/>`}
    const L=u.lays[p.li];
    if(p.mode==='s'){
      const near=up?fy1:fy0,it=L.its[0];
      s+=`<line x1="${u.ln}" y1="${start}" x2="${u.ln}" y2="${near}" stroke="${ac}" stroke-width="${u.el?2.4:sw}" ${mk(ac)}/>`;
      s+=`<rect x="${F.x0}" y="${fy0}" width="${L.w}" height="${L.h}" rx="${u.el?8:2}" fill="${u.el?'#FFC000':'#fff'}" ${u.el?'stroke="#000" stroke-width="2.2"':''}/>`;
      it.lines.forEach((l,i)=>{s+=`<text x="${F.x0+L.w/2}" y="${fy0+(u.el?17:11)+i*L.lh}" text-anchor="middle" font-size="${L.fs}" font-weight="${u.el?700:600}" fill="${it.col}" ${TX}>${esc(l)}</text>`});
    }else{
      const cys=L.its.map(i=>fy0+i.top+i.ih/2),far=up?cys[0]:cys[cys.length-1],left=p.mode==='L',dr=left?-1:1;
      s+=`<line x1="${u.ln}" y1="${start}" x2="${u.ln}" y2="${far+(up?-sw/2:sw/2)}" stroke="${ac}" stroke-width="${sw}"/>`;
      L.its.forEach((it,j)=>{
        s+=`<line x1="${u.ln}" y1="${cys[j]}" x2="${u.ln+dr*10}" y2="${cys[j]}" stroke="${ac}" stroke-width="${sw}" ${mk(ac)}/>`;
        it.lines.forEach((l,i)=>{s+=`<text x="${u.ln+dr*14}" y="${fy0+it.top+11+i*LH}" text-anchor="${left?'end':'start'}" font-size="${FS}" font-weight="600" fill="${it.col}" ${TX}>${esc(l)}</text>`});
      });
    }
  });
  if(lastp){const e=c.E,b=y+18,nx=24+tw('หมายเหตุ')+12;
    s+=`<text x="24" y="${b+11}" font-size="10" font-weight="700" ${TX}>หมายเหตุ</text>`+
       `<text x="${nx}" y="${b+12}" font-size="10" fill="${RR}" ${TX}>1. วันที่ ${fmt(e+90)} : วันสุดท้ายที่ผู้สมัครต้องยื่นบัญชีรายรับและรายจ่ายในการเลือกตั้ง (ภายใน 90 วันนับจากวันเลือกตั้ง) (ม.62 /ข้อ 124)</text>`+
       `<text x="${nx}" y="${b+26}" font-size="10" fill="${RR}" ${TX}>2. วันที่ ${fmt(e+105)} : วันสุดท้าย ผอ.กต.จว. ประกาศบัญชีรายรับและรายจ่ายในการเลือกตั้งของผู้สมัคร (ภายใน 15 วันนับแต่วันครบกำหนดยื่นบัญชีใช้จ่าย) (ข้อ 125)</text>`}
  const t=new Date();
  s+=`</g><text x="${PW-MX}" y="${PH-MB+12}" text-anchor="end" font-size="10" ${TX}>${esc(S.meta.foot)} [${t.getDate()}/${t.getMonth()+1}/${t.getFullYear()}]</text></svg>`;
  return s;
}
applyAuto();showBE();draw();
if(document.fonts)document.fonts.ready.then(draw);
</script>
</body>
</html>
