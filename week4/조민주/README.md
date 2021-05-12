# 내가 사용한 배포방법


## pythonanywhere 
**1) 배포를 위한 settings설정**

: _애플리케이션 분리 및 통합_  
(1) DEBUG  
(2) ALLOWED_HOST  
(3) STATIC  


**2) Pythonanywhere에 프로젝트 설치하기**  
(1) zip파일을 업로드  
(2) 콘솔 압축 해제, 가상환경 만들기, 장고 설치, migrate, exit


**3) 배포하기**  
(1) Pythonanywhere의 상단에 web을 선택합니다.  
(2) Add a new web app을 선택합니다.  
(3) Next > Manual Configuration > Python 3.7 > Next 를 차례대로 선택합니다.  
(4) Code부분 수정  
(5) 가상환경 폴더 설정  
(6) static 연결  