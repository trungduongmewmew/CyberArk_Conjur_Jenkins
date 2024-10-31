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
'update-ca-trust extract'