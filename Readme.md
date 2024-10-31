# Cấu hình Project Freestyle sử dụng phương thức xác thực API Key

## 1. Cấu hình Conjur

- Copy 2 file `add_user_jenkins.sh` và `jenkins.yaml` lên server cài đặt Conjur Master
- Chỉnh sửa file `jenkins.yaml` theo tên user mà bạn muốn tạo, phân quyền vào các secret
- Sử dụng lệnh `conjur login` để login vào Conjur CLI
- Chạy tập lệnh `./add_user_jenkins.sh` để tạo user và phân quyền
- In key của user jenkinstest vừa tạo ở trên ra thành file `jenkinstest.key` để tiện đăng nhập sau này
- Sử dụng lệnh `conjur login` và login vào Conjur CLI bằng user jenkinstest vừa tạo. Dùng lệnh `conjur list` để kiểm tra xem quyền phân vào các secret đã đúng chưa.

![Conjur CLI](https://github.com/user-attachments/assets/c53d72c5-ce5d-43e9-a53a-480a64564383)

- Sử dụng đoạn code `test_auth_api.py` để test việc authentication (nếu muốn)

## 2. Cấu hình Jenkins

- SSH vào server Jenkins, add host cho máy chủ conjur 
- Copy rootca của conjur vào đường dẫn `/etc/pki/ca-trust/source/anchors`. Sau đó sử dụng command sau để trust root ca:  
`update-ca-trust extract`   
- Sử dụng command sau để kiểm tra xem cert đã trust chưa:  
`openssl s_client -connect conjur-master.poc.local:443`    
- Truy cập vào Jenkins portal cài đặt plugin cho CyberArk Conjur

![Jenkins Plugin](https://github.com/user-attachments/assets/3362b100-8220-4c47-bc4b-c2d041ccf25a)

- Tạo một credential cho user jenkinstest, password là api key đã in ra ở bước trên.

![Jenkins Credential](https://github.com/user-attachments/assets/14f317b8-7101-4508-9c5a-0b96d12a43c7)

- Tạo một credential cho secret từ conjur

![Conjur Secret Credential](https://github.com/user-attachments/assets/fcbdcc04-140b-4124-9cec-2160232b668b)

- Tạo một project Freestyle để kiểm tra việc lấy password từ Conjur
- Ở tab General, điền thông tin của Conjur Master, phần Conjur Auth Credential chọn Credential cho user jenkinstest đã tạo ở bước trên

![Jenkins Project General](https://github.com/user-attachments/assets/6e1da309-e79b-42a3-9537-d5c00f39c06c)

- Ở tab Build Env, chọn use secret text or file, credential chọn credential cho secret đã tạo ở trên

![Jenkins Build Environment](https://github.com/user-attachments/assets/4c61b77e-8e50-4185-970d-a85f184abc13)

- Ở tab build step, chọn thực thi một command đơn giản in ra secret 

![Jenkins Build Step](https://github.com/user-attachments/assets/66359685-17db-4a50-a3b5-8332a0ee9a02)

- Chạy thử project và kiểm tra đã lấy thành công secret 

![Jenkins Build Result](https://github.com/user-attachments/assets/93551ac0-9016-4351-816d-40e2c6cfb25d)

# Cấu hình Pipeline sử dụng phương thức xác thực JWT

(Phần này chưa có nội dung)