docker run -d  --restart=unless-stopped  --name=kuboard  -p 8089:80/tcp  -p 30081:10081/tcp  -e KUBOARD_ENDPOINT="http://192.168.3.5:8089"  -e KUBOARD_AGENT_SERVER_TCP_PORT="30081" -e KUBOARD_ADMIN_DERAULT_PASSWORD="admin" -v C:\kuboard-data:/data  eipwork/kuboard:v3

# 参考官网：https://kuboard.cn/install/v3/install-built-in.html#%E5%AE%89%E8%A3%85
# 默认账号密码： admin/Kuboard123