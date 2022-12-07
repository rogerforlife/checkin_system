# checkin_system

此專案為打卡系統，採用Python語言、Django框架實作。

## 重點項目:
1. 基本的CRUD上，且採用的是RESTful API風格，以'rest_framework'實作。
2. 熟悉'django_filters'，使查詢參數程式碼可以更加簡潔。

## API:
1. 127.0.0.1/api/Hrdata
  創建人員資料，以RESTful API實作CRUD，
  且可以查詢特定主管或部門下的員工，以django_filters實作。
2. 127.0.0.1/api/Checkindata
  只能查詢打卡紀錄，以rest_framework中的ReadOnlyModelViewSet實作，
  且可以查詢特定員工打卡紀錄，以django_filters實作。
3. 127.0.0.1/api/checkin
  打卡。
4. 127.0.0.1/api/SupervisorCheck
  查詢特定日期與特定主管下的員工打卡紀錄。
