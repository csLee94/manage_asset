# 거래를 Tracking하는 자산 가계부 구축

## 주요 기능 정의

- Timelapse별 변동자산 가치 추이 확인 (주, 월, 연)
- 결산일 기준 적입액으로 인한 자산상승을 제외한 '자본소득' 증감 확인 (변동자산 처분, 배당금 등 내역 포함)
- 자산의 증감 추이 확인 (현금자산과 변동자산 비율 확인)
- Timelapse별 목표에 대한 달성률 확인 (월, 연)
- 기존 작성 파일 활용으로 별도 파일 작성 X
    - 주식매매일지 파일
    - 월간 결산 파일
- **위 확인 내용들을 추출하여 시각화하는 과정 자동화**

## 필요 데이터
- 변동자산 데이터
    - 주간(금요일 기준) / MoM, YoY에도 활용가능하도록 설계
    - 주식보유량과 평균 매입가격, 당시 시점 주가
- 결산 데이터
    - 월간(결산일 기준) / MoM, YoY 산출에 활용
    - 주식보유량과 평균 매입가격, 당시 시점 주가
    - 현금가치 
   




## To do List

- 

## 버전 관리

|Name|Ver|
|---|---|
|python|3.7.9|
|gspread|3.7.0|
|oauth2client|4.1.3|