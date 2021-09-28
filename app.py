from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = ''
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    # データベースに情報を送る時
    if request.method == 'POST':
        session.permanent = True #makes the permanent session
        user = request.form['nm'] #ユーザー情報を保存する
        session['user'] = user #sessionにuser情報を保存
        return redirect(url_for('user'))
    #情報を受け取る時
    else:
        if 'user' in session: #sessionにユーザー情報があった時
            return redirect(url_for('user')) #userページに遷移
        return render_template('login.html') #sessionにuser情報が無かった時loginページに遷移


@app.route('/user')
def user():
    if 'user' in session:
        user = session['user'] #sessionからuser情報を取ってくる
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None) #削除
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
