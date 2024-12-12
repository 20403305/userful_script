docker run -d --name xxl-job-admin --network my_bridge_network -p 31009:8080 -e "SPRING_DATASOURCE_URL=jdbc:mysql://mysql-test:3306/aikms?useUnicode=true&characterEncoding=UTF-8&useSSL=false" -e "SPRING_DATASOURCE_USERNAME=root" -e "SPRING_DATASOURCE_PASSWORD=123456" -e "XXL_JOB_ACCESS_TOKEN=A87ao5t9S91JXBP6" xuxueli/xxl-job-admin:2.3.0


docker run -d --name xxl-job-executor --network my_bridge_network -p 9999:9999 -e "XXL_JOB_EXECUTOR_IP=127.0.0.1" -e "XXL_JOB_EXECUTOR_PORT=9999" -e "XXL_JOB_ADMIN_ADDRESSES=http://127.0.0.1:31009/xxl-job-admin" -e "XXL_JOB_ACCESS_TOKEN=A87ao5t9S91JXBP6" -e "XXL_JOB_EXECUTOR_APPNAME=aikms-executor" xuxueli/xxl-job-executor:latest
