from bottle import *
from beaker.middleware import SessionMiddleware
from sys import argv

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data2',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

@route('/')
def verslun():
    return template('templates/index.tpl')

@route('/karfa', method="POST")
def karfa():
    buxur=request.forms.get('buxur')
    peysa=request.forms.get('peysa')
    bolur=request.forms.get('bolur')
    hattur=request.forms.get('hattur')
    submit=request.forms.get('submit')
    print(submit)
    if submit=="add to cart":
        s=request.environ.get('beaker.session')
        if buxur!="1":
            buxur=0
        if peysa!="1":
            peysa=0
        if bolur!="1":
            bolur=0
        if hattur!="1":
            hattur=0
        s['buxur'] = s.get('buxur', 0) + int(buxur)
        buxur=0
        s['peysa'] = s.get('peysa',0)+ int(peysa)
        peysa=0
        s['bolur'] = s.get('bolur', 0) + int(bolur)
        bolur = 0
        s['hattur'] = s.get('hattur', 0) + int(hattur)
        hattur = 0
        s.save()
        buxur2='buxur: %d' % s['buxur']
        peysa2=' peysa %d' % s['peysa']
        bolur2=' bolur: %d' % s['bolur']
        hattur2=' hattur %d' % s['hattur']
        dict={"buxur":'buxur: %d' % s['buxur'],"peysa":' peysa %d' % s['peysa'],"bolur":' bolur: %d' % s['bolur'],"hattur":' hattur %d' % s['hattur']}
        return template('templates/karfa.tpl',dict)
    elif submit=="delete from cart":
        s = request.environ.get('beaker.session')
        if buxur != "1":
            buxur = 0
        if peysa != "1":
            peysa = 0
        if bolur != "1":
            bolur = 0
        if hattur != "1":
            hattur = 0
        s['buxur'] = s.get('buxur', 0) - int(buxur)
        if s ['buxur']<0:
            s['buxur']=0
        buxur = 0
        s['peysa'] = s.get('peysa', 0) - int(peysa)
        if s ['peysa']<0:
            s['peysa']=0
        peysa = 0
        s['bolur'] = s.get('bolur', 0) - int(bolur)
        if s ['bolur']<0:
            s['bolur']=0
        bolur = 0
        s['hattur'] = s.get('hattur', 0) - int(hattur)
        if s ['hattur']<0:
            s['hattur']=0
        hattur = 0
        s.save()
        buxur2 = 'buxur: %d' % s['buxur']
        peysa2 = ' peysa %d' % s['peysa']
        bolur2 = ' bolur: %d' % s['bolur']
        hattur2 = ' hattur %d' % s['hattur']
        dict = {"buxur": 'buxur: %d' % s['buxur'], "peysa": ' peysa %d' % s['peysa'],
                "bolur": ' bolur: %d' % s['bolur'], "hattur": ' hattur %d' % s['hattur']}
        return template('templates/karfa.tpl', dict)
@route('/s')
def delete():
    return template('templates/index2.tpl')
run(app=app, host='0.0.0.0', port=argv[1])
