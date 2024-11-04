from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'title', 'body', 'slug', 'category', 'created', 'updated']

        
# pip install djangorestframework

# CRUD (Create / Read / Update / Delete) 
# RESTful API (Representational State Transfer)
# - 제어하려하는 자원의 상태값 전송 방식
# - CRUD 구현을 위해 실제 사용해야 되는 개발 방법론 지칭
# - HTTP 통신을 위한 메서드 방식 (GET;조회 / POST;생성 / PUT;변경 / DELETE;삭제)

# Django 프레임워크에서 굳이 DRF를 써야 하는 이유 및 DRF가 하는 일
# - 장고 프로젝트 기반의 RESTful API 제작을 돕는 라이브러리 (직렬화, 역직렬화 기능 제공)
# - serializer (직렬화): 장고의 모델 인스턴스를 클라이언트에서 읽기 편하도록 json포맷으로 변환 처리
# - deserializer (역직렬화): 클라이언트로 전달받은 json데이터를 장고 전용의 모델 인스턴스 구조로 역변환 처리
# - validation (데이터검증): 역직렬화시 클라이언트가 보낸 데이터를 필드별로 유효성 검사 처리
