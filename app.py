from flask import Flask, render_template, request
import requests
import json
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('magician.html')


@app.route('/run', methods=['GET'])
def run():
    select = request.args.get('select')
    text = request.args.get('input')
     
    if select == '0':
        return render_template(
            'ai.html', 
            input1=text, 
            output1='Successful translation', 
            selected0='selected',
            model='Transformer',
            data='ai_tranformer_data',
            library1='Pytorch : 1.9.0',
            library2='transformers : 4.30.0',
            link="https://www.google.com/",
            )

    elif select == '1':
        return render_template(
            'ai.html',
            input1=text, 
            output1='요약 성공', 
            selected1='selected',
            model='T5',
            data='ai_sum_data',
            library1='Pytorch : 1.9.0',
            library2='transformers : 4.30.0',
            library3='test',
            link="https://www.naver.com/",
            )
    
    elif select == '2':
        return render_template(
            'ai.html',
            input1=text, 
            output1='챗봇 성공', 
            selected2='selected',
            model='GPT-2',
            data='ai_chatbot_data',
            library1='Pytorch : 1.9.0',
            library2='transformers : 4.30.0',
            library3='test',
            library4='test2',
            link="https://www.google.com/",
            )

    else:
        return render_template(
            'ai.html', 
            input1=text, 
            output1='분류 성공', 
            selected3='selected',
            model='BERT',
            data='ai_classification_data',
            library1='Pytorch : 1.9.0',
            library2='transformers : 4.30.0',
            link="https://www.google.com/",
            )


@app.route('/o', methods=['GET'])
def o():
    inp_text = request.args.get('input')
    out_text = request.args.get('output')
    print('===o :', inp_text)
    print('===o :', out_text)

    return render_template('magician.html')
    

@app.route('/x', methods=['GET'])
def x():

    inp_text = request.args.get('input')
    out_text = request.args.get('output')
    print('===x :', inp_text)
    print('===x :', out_text)

    return render_template('x.html', input1=inp_text)


@app.route('/insert', methods=['GET'])
def insert():
    inp_text = request.args.get('input')
    out_text = request.args.get('output')
    print('===insert :', inp_text)
    print('===insert :', out_text)
    if out_text == '':
        return render_template('x.html', input1=inp_text)

    return render_template('magician.html', input1=inp_text)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=8080,
        debug=True
        )
