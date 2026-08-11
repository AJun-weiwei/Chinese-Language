import flask
import os
import sys
from io import StringIO
import 模块识别器1
app = flask.Flask(__name__)
@app.route('/')
def clang():
  DataList = dict(zip(os.listdir('static/data'),map(lambda a:'../static/data/'+a,os.listdir('static/data'))))
  FileList = []
  for i in os.listdir('static/files'):
    with open(f'static/FileUsers/{i}','r') as f:
      u = f.read()
    with open(f'static/FileStars/{i}','r') as f:
      s = f.read()
    FileList.append([i,u,"/"+i[:-4],f'../static/files/{i}',s,'/star/'+i[:-4]])
  return flask.render_template('网站.html',data=DataList,files=FileList)
@app.route('/ask')
def ask():
  return flask.render_template('其他问题.html')
@app.route('/xp')
def xp():
  return flask.render_template('XP.html')
@app.route('/file',methods=['POST'])
def file():
  name = flask.request.form.get('FileName')
  file_content = flask.request.form.get('File')
  with open('static/data/' + name + '.txt', 'w') as f:
    f.write(file_content)
  return flask.render_template('上传成功.html')
@app.route('/upload',methods=['POST'])
def upload():
  FileName = flask.request.form.get('FN')
  FileUser = flask.request.form.get('FU')
  FileHtml = flask.request.files['FH']
  File = flask.request.files['F']
  FileHtml.save('templates/FileHtml/'+FileName+'.html')
  File.save('static/files/'+FileName+'.txt')
  with open('static/FileUsers/'+FileName+'.txt','w') as f:
    f.write(FileUser)
  with open('static/FileStars/'+FileName+'.txt','w') as f:
    f.write('0')
  return flask.render_template('开源成功.html')
@app.route('/<FileName>')
def FHtml(FileName):
  try:
    return flask.render_template(f'FileHtml/{FileName}.html')
  except:
    return "非常抱歉，页面加载失败，请检查链接是否正确。",404
@app.route('/star/<name>')
def star(name):
  try:
    with open(f'static/FileStars/{name}.txt','r') as f:
      stars = int(f.read())
    with open(f'static/FileStars/{name}.txt','w') as f:
      f.write(str(stars+1))
    return '感谢您对Chinese-Language社区项目的支持，您的点赞数据将会被上传至服务器。'
  except Exception as e:
    print(e)
    return '非常抱歉，您点赞的文件不存在，请检查链接是否正确。',404
@app.route('/api/user',methods=['POST'])
def run():
    data = flask.request.get_json()
    CodeData = data.get('CodeData')
    MainFile = data.get('MainFile')
    old_stdout = sys.stdout
    if MainFile not in CodeData:
        return flask.jsonify({'OutPut': '', 'IsError': False, 'VarData': {}, 'FunctionData': {}, 'RunTime': 0,'RunCode': 5})
    sys.stdout = StringIO()
    log = 模块识别器1.job1(MainFile,{},{},CodeData,True)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return flask.jsonify({'OutPut':output,'IsError':log[2]=='1','VarData':log[0],'FunctionData':log[1],'RunTime':log[3],'RunCode':2})
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
