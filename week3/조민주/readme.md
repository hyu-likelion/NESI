# EST, REST API, RESTful


## 1.REST (Representional State Transfer)  
**1) 등장 배경**: _애플리케이션 분리 및 통합_  


**2) 정의**  
: 자원을 이름으로 구분하여 해당 자원의 상태를 주고 받는 모든 것  
: HTTP URL을 통해 Resource 명시, HTTP METHOD를 통해 자원에 대한 CRUD opertaion 적용하는 것
: 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식  (client와 server 사이의 통신 방식 중 하나)  


**3) 특징**  
: (장)HTTP를 그대로 사용하여 별도의 인프라를 구축할 필요가 없음  
: (장)범용성을 보장  
: (단)표준이 없음  
: (단)메소드의 한계 (4개뿐)  


## 2.REST API  
**1) 정의**  
: REST 기반으로 서비스 API를 구현한 것  


**2) API란?**  
: 컴퓨터 프로그램간 상호작용을 촉진하며, 서로 정보를 교환가능 하도록 하는 것  


__3) API설계 규칙__  
### (1)리소스 형태 : GET /members/1  
    - 리소스(members)는 대문자보다는 소문자, 동사보단 명사  
    - 도큐먼트:단수 / 컬렉션:복수 / 스토어:복수  
    - CRUD 기능은URL에 포함 X  
    - 경로중 변하는 부분은 유일한 값(id)로 대체  
### (2)설계 규칙 : http://restapi.example.com/houses/apartments  
    - /는 계층관계  
    - 마지막 문자로 슬래시 포함 x  
    - (_)는 URL에 사용 x  
    - 소문자가 적합  
    - 파일 확장자 포함 x  
    - 리소스 간에 연관관계 있는 경우  
        :/users/{userid}/devices...  


## 3.RESTFUL  
**1) 정의**  
: REST라는 아키텍처를 구현하는 웹 서비스를 나타내기 위해 사용되는 용어  
: REST 원리를 따르는 시스템 ()  


**2) 목적**  
: 이해하기 쉽고 사용하기 쉬운 REST API를 만드는 것  
