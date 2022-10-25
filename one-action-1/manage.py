from email import message
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['post', 'get'])
def hello_world():
  answer = ''
  if request.method == 'POST':
    answer = ''
    date = request.form.get('date')
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
    print(answer)
  return render_template("temp.html", message = answer)

if __name__ == "__main__":
    app.run()