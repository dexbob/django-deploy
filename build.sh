# 스크립트 실행 중 오류 발생시 빌드 중단하고 오류 내용 반환
set -o errexit
# 클라우드 서비스상에 파이썬 프로젝트 구동시 필요한 파이썬 전용 패키지를 자동 설치
pip install -r requirements.txt
# 배포시 효율적인 리소스 관리를 위해 장고 프로젝트 안쪽의 css, js, image같은 정적 파일들을 한곳에 모아줌
python manage.py collectstatic --no-input
# migrations에 생성된 파일의 구조에 맞게 테이블을 생성하거나 업데이트
python manage.py migrate