from googleapiclient.discovery import build
from googleclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file

# API 연결 및 사전정보 입력
store = file.Storage('storage.json')
credis = store.get()

service = build('drive', 'v3', http=creds.authorize(Http()))

folder_id = "1V34t-x2Ld8SSmuQDmmrL_vd2Tk5-SWP-"
file_paths = "기능명세서.csv"  # 업로드 하고자 하는 파일

# 파일을 구글 드라이브에 업로드 하기
request_body = {'name': file_paths, 'parents': [
    folder_id], 'uploadType': 'multipart'}  # 업로드할 파일정보 저장
media = MediaFileUpload(file_paths, mimetype='text/csv')  # 업로드할 파일
file_info = service.files().create(body=request_body, media_body=media,
                                   fields='id,webBiewLink').execute()

# 구글 드라이브 링크 얻기
print("File webBiewLink : ", file_info.get('webViewLink'))
webviewlink = file_info.get('webBiewLink')
