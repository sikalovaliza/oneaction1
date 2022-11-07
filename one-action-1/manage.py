from flask import Flask
from flask import render_template
from flask import request

def toweb(f):
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def myfunc():
        about = f.__doc__
        a = f.__annotations__
        if 'return' in a:
            a.pop('return') 

        if request.form:
            res = f(**request.form)
        else:
            res = None

        return render_template('temp.html', about = 'Введите дату рождения', a = a, res = res)

    return app

# s = toweb(s)
@toweb
def s(date: str) -> str:
    answer = ""
    if date[3] + date[4] == '01':
        if int(date[0] + date[1]) <= 19:
            answer = 'КОЗЕРОГ'
        if int(date[0] + date[1]) > 19:
            answer = 'ВОДОЛЕЙ'
    if date[3] + date[4] == '02':
        if int(date[0] + date[1]) <= 18:
            answer = 'ВОДОЛЕЙ'
        if int(date[0] + date[1]) > 18:
            answer = 'РЫБЫ'
    if date[3] + date[4] == '03':
        if int(date[0] + date[1]) <= 20:
            answer = 'РЫБЫ'
        if int(date[0] + date[1]) > 20:
            answer = 'ОВЕН'
    if date[3] + date[4] == '04':
        if int(date[0] + date[1]) <= 20:
            answer = 'ОВЕН'
        if int(date[0] + date[1]) > 20:
            answer = 'ТЕЛЕЦ'
    if date[3] + date[4] == '05':
        if int(date[0] + date[1]) <= 20:
            answer = 'ТЕЛЕЦ'
        if int(date[0] + date[1]) > 20:
            answer = 'БЛИЗНЕЦЫ'
    if date[3] + date[4] == '06':
        if int(date[0] + date[1]) <= 20:
            answer = 'БЛИЗНЕЦЫ'
        if int(date[0] + date[1]) > 20:
            answer = 'РАК'
    if date[3] + date[4] == '07':
        if int(date[0] + date[1]) <= 22:
            answer = 'РАК'
        if int(date[0] + date[1]) > 22:
            answer = 'ЛЕВ'
    if date[3] + date[4] == '08':
        if int(date[0] + date[1]) <= 22:
            answer = 'ЛЕВ'
        if int(date[0] + date[1]) > 22:
            answer = 'ДЕВА'
    if date[3] + date[4] == '09':
        if int(date[0] + date[1]) <= 23:
            answer = 'ДЕВА'
        if int(date[0] + date[1]) > 23:
            answer = 'ВЕСЫ'
    if date[3] + date[4] == '10':
        if int(date[0] + date[1]) <= 23:
            answer = 'ВЕСЫ'
        if int(date[0] + date[1]) > 23:
            answer = 'СКОРПИОН'
    if date[3] + date[4] == '11':
        if int(date[0] + date[1]) <= 21:
            answer = 'СКОРПИОН'
        if int(date[0] + date[1]) > 21:
            answer = 'СТРЕЛЕЦ'
    if date[3] + date[4] == '12':
        if int(date[0] + date[1]) <= 21:
            answer = 'СТРЕЛЕЦ'
        if int(date[0] + date[1]) > 21:
            answer = 'КОЗЕРОГ'
    return answer

s.run(host='0.0.0.0', port="5001")