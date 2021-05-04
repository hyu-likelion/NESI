# REST vs REST API vs RESTful

## REST
: 웹에 존재하는 모든 자원(이미지, 동영상, DB자원)에 공유한 URI를 부여해 활용

### 구성
1. URI: HTTP에서 자원을 구별하는 ID
2. Method: URI로 자원을 지정, 조작하기 위해 사용/HTTP프로토콜에서는 GET,POST,PUT,DELETE...
3. Representation: client가 서버로 요청 시 응답으로 보내주는 자원의 상태(=요점 시점에서의 상태)
ex. JSON,XML,TEXT,RSS

### 특징
- Client-server구조
- 분산 하이퍼 시스템(ex. www)을 위한 소프트웨어 개발 아키텍처의 한 형식
- Stateless(무상태)-client의 context 서버에 저장X
- Layered system(계층화)->구조의 유연성
- Cashable-웹 표준 HTTP 프로토콜을 그대로 사용헤 기존 인프라 활용,대량 요청 효율적 처리
- Uniform interface


## REST API
: REST를 기반으로 서비스 API(:데이터 기능의 집합을 제공해 컴퓨터 프로그램 간 상호작용을 촉진하고 서로 정보 교환 가능하게 함)를 구현한 것

### 특징
- 델파이 클라이언트 뿐 아니라 자바, C#, 웹 등을 이용해 클라이언트 제작 가능
- REST 기반 시스템 분산을 통한 확장성과 재사용성 증가에 따른 편리한 유지보수 및 운용

### 설계규칙
1. URI는 정보의 자원을 표현-동사보다 명사,대문자보다 소문자/도큐먼트-단수,컬렉션&스토어-복수
2. 자원에 대한 행위는 HTTP Method로-경로 중 변하는 부분은 유일한 값으로 대체
3. / : 계층관계 나타냄-URI 마지막 문자로 포함X
4. URI에 -는 가독성을 높이기 위해 사용, _는 사용X
5. 파일 확장자 URI에 포함X-Accept header사용
6. 리소스 간 연관관계 있을 시: 리소스명/리소스ID/관계 있는 리소스명


## RESTful
: REST 형식을 따르는 시스템을 나타냄

'REST API'를 제공하는 웹 서비스 = 'RESTful'하다 라고 표현 가능

### RESTful하지 못한 경우
- CRUD기능을 POST로만 처리하는 API
- route에 자원, id 외 정보가 들어가는 경우