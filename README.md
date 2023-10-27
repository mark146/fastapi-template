# FastAPI 템플릿

이 프로젝트는 fastapi 생성시 기본으로 사용할 폴더 구조입니다.

프로젝트 구조는 설계에 대한 공부를 진행하면서 지금보다 더 나은 구조를 알게 된다면 계속 업데이트할 예정입니다.  


## 실행방법

```
1. 파이썬 설치

2. poetry 설치

3. 필요 install 정보 다운로드
# 윈도우
python -m poetry add fastapi uvicorn

4. 서버 실행
# 윈도우
python -m poetry run uvicorn main:app --reload

5. 테스트
# 서버 실행 후 아래 api를 호출 할 경우 결과 확인 가능
http://localhost:8000/v1/users 
```


## 추후 업데이트 예정
- docker-compose 적용
- 개발 환경 별 .env
- 테스트 코드  
- CI/CD 세팅
- DB 연동

등..
