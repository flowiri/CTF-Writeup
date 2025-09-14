# Welcome

Ban tổ chức đã ép cung tội phạm mã hóa tống tiền Tổng công ty SBC, đây là step-by-step cách giải mã hệ thống.

# Con mã độc nằm trên mỗi đội

| Đội | Binary Name          |
| --- | -------------------- |
| 1   | haltVms              |
| 2   | restartVms           |
| 3   | rebootVms            |
| 4   | esxiRecover          |
| 5   | vwhoosh              |
| 6   | vhaltsc              |
| 7   | vcconnecthost        |
| 8   | esxiHealthMon        |
| 9   | esxiWorkspaceManager |
| 10  | netstat              |
| 11  | dig                  |
| 12  | ss                   |
| 13  | powerOnVms           |
| 14  | lock                 |
| 15  | squid                |
| 16  | squashfs             |
| 17  | mkfs                 |
| 18  | excdowngrade         |
| 19  | exchostconf          |
| 20  | pphost               |
| 21  | xterm                |
| 22  | bat                  |
| 23  | socat                |
| 24  | foreach              |
| 25  | ip                   |
| 26  | haltVms              |

# Hướng dẫn giải

> **VERY IMPORTANT**: Các file bị mã hóa có đuôi `.crt`, rename lại bỏ đi extension `.crt`. Ví dụ: `SBC-ABCXYZ.vmx.crt` -> `SBC-ABCXYZ.vmx`

1. Test decrypt flag

```bash
<binary_ma_doc> -d <path_toi_folder_chua_flag>
```

Ví dụ:

Team 7 có file flag `secret_7.iso.crt` nằm ở path `/vmfs/volumes/datastore1 (2)/`

```bash
ls "/vmfs/volumes/datastore1 (2)/"
    secret_7.iso.crt ...
mv "/vmfs/volumes/datastore1 (2)/secret_7.iso.crt" "/vmfs/volumes/datastore1 (2)/secret_7.iso"
ls "/vmfs/volumes/datastore1 (2)/"
    secret_7.iso ... 
./vcconnecthost -d "/vmfs/volumes/datastore1 (2)/"
ls "/vmfs/volumes/datastore1 (2)/"
    secret_7.iso.crt ... 
mv "/vmfs/volumes/datastore1 (2)/secret_7.iso.crt" "/vmfs/volumes/datastore1 (2)/secret_7.iso"
cat "/vmfs/volumes/datastore1 (2)/secret_7.iso"
    SBC{FLAG}
```

2. Sau khi decrypt flag thành công, dựa vào section `Command used` để lấy command attacker đã dùng để encrypt hệ thống và chạy lại. (`201` tương ứng với server 172.16.1.201)

> **VERY IMPORTANT**: Các file bị mã hóa có đuôi `.crt`, rename lại bỏ đi extension `.crt`. Ví dụ: `SBC-ABCXYZ.vmx.crt` -> `SBC-ABCXYZ.vmx`

> **VERY IMPORTANT**: Các file bị mã hóa có đuôi `.crt`, rename lại bỏ đi extension `.crt`. Ví dụ: `SBC-ABCXYZ.vmx.crt` -> `SBC-ABCXYZ.vmx`

> **VERY IMPORTANT**: Các file bị mã hóa có đuôi `.crt`, rename lại bỏ đi extension `.crt`. Ví dụ: `SBC-ABCXYZ.vmx.crt` -> `SBC-ABCXYZ.vmx`

Khi thấy dòng `Never gonna give you up` có nghĩa là done.

3. Sau khi decrypt hệ thống thành công, nếu esxi chưa nhận vm thì tiến hành unregister vm và register lại vm (google for tutorial)

# Command used

```bash
201 || haltVms -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (6)/Team01-k8s-core" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (6)/SBC-Webpage" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (6)/SBC-LabFor-UserHR2" 

202 || restartVms -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/ds1 (7)/Team02-k8s-core" -d "/vmfs/volumes/ds1 (7)/k8s-master" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (7)/SBC-Webpage" -d "/vmfs/volumes/ds1 (7)/k8s-core" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (7)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (7)/k8s-dmz" 

203 || rebootVms -d "/vmfs/volumes/DS1/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1/k8s-dmz" -d "/vmfs/volumes/DS1/SBC-LabFor-DB" -d "/vmfs/volumes/DS1/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1/Team03-k8s-core" -d "/vmfs/volumes/DS1/k8s-master" -d "/vmfs/volumes/DS1/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1/SBC-Webpage" -d "/vmfs/volumes/DS1/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1/SBC_Probe VPN server" -d "/vmfs/volumes/DS1/k8s-core" 

204 || esxiRecover -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (1)/k8s-dmz" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (1)/Team04-k8s-core" -d "/vmfs/volumes/DS1 (1)/k8s-master" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (1)/SBC-Webpage" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (1)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (1)/k8s-core" 

205 || vwhoosh -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (5)/SBC-Webpage" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (5)/Team05-k8s-core" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (5)/k8s-core" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (5)/k8s-dmz" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (5)/k8s-master" -d "/vmfs/volumes/ds1 (5)/SBC-LabFor-UserHR2" 

206 || vhaltsc -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (7)/SBC-Webpage" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (7)/Team06-k8s-core" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (7)/k8s-core" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (7)/k8s-dmz" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (7)/k8s-master" -d "/vmfs/volumes/DS1 (7)/SBC-LabFor-UserHR2" 

207 || vcconnecthost -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (3)/SBC-Webpage" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (3)/k8s-core" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (3)/k8s-dmz" -d "/vmfs/volumes/DS1 (3)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (3)/k8s-master" 

208 || esxiHealthMon -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-UserHR2 (1)" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-DB (1)" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-ELK (1)" -d "/vmfs/volumes/ds1 (8)/SBC-Webpage" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-FTPSvr (1)" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-MailServer (1)" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-ServerAD2k12 (1)" -d "/vmfs/volumes/ds1 (8)/k8s-core" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-SquidProxy (1)" -d "/vmfs/volumes/ds1 (8)/k8s-dmz" -d "/vmfs/volumes/ds1 (8)/SBC-LabFor-UserHR1 (1)" -d "/vmfs/volumes/ds1 (8)/k8s-master" 

209 || esxiWorkspaceManager -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (9)/SBC-Webpage" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (9)/k8s-core" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (9)/k8s-dmz" -d "/vmfs/volumes/ds1 (9)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (9)/k8s-master" 

210 || netstat -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (2)/SBC-Webpage" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (2)/k8s-core" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (2)/k8s-dmz" -d "/vmfs/volumes/DS1 (2)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (2)/k8s-master" 

211 || dig -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-UserHR2 (1)" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-DB (1)" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-UserIT (1)" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-ELK (1)" -d "/vmfs/volumes/ds1 (10)/SBC-Webpage" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-FTPSvr (1)" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-MailServer (1)" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-ServerAD2k12 (1)" -d "/vmfs/volumes/ds1 (10)/k8s-core" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-SquidProxy (1)" -d "/vmfs/volumes/ds1 (10)/k8s-dmz" -d "/vmfs/volumes/ds1 (10)/SBC-LabFor-UserHR1 (1)" -d "/vmfs/volumes/ds1 (10)/k8s-master" 

212 || ss -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (3)/SBC-Webpage" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (3)/k8s-core" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (3)/k8s-dmz" -d "/vmfs/volumes/ds1 (3)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (3)/k8s-master" 

213 || powerOnVms -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-MailServer (1)" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-UserHR2 (1)" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-DB (1)" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-ServerAD2k12 (1)" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-UserIT (1)" -d "/vmfs/volumes/DS1 (8)/k8s-core" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-ELK (1)" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-SquidProxy (1)" -d "/vmfs/volumes/DS1 (8)/SBC-Webpage" -d "/vmfs/volumes/DS1 (8)/k8s-dmz" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-FTPSvr (1)" -d "/vmfs/volumes/DS1 (8)/SBC-LabFor-UserHR1 (1)" -d "/vmfs/volumes/DS1 (8)/k8s-master" 

214 || lock -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (4)/SBC-Webpage" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (4)/k8s-core" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-ServerAD2k12_1" -d "/vmfs/volumes/DS1 (4)/k8s-dmz" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (4)/k8s-master" -d "/vmfs/volumes/DS1 (4)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (4)/k8s-master_1" 

215 || squid -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (9)/SBC-Webpage" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (9)/k8s-core" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (9)/k8s-dmz" -d "/vmfs/volumes/DS1 (9)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (9)/k8s-maste" 

216 || squashfs -d "/vmfs/volumes/DS1 (10)/ISO" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (10)/SBC-Webpage" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (10)/k8s-core" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (10)/k8s-dmz" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (10)/k8s-master" -d "/vmfs/volumes/DS1 (10)/SBC-LabFor-UserHR1" 

217 || mkfs -d "/vmfs/volumes/ds1/SBC-LabFor-UserHR2" -d "/vmfs/volumes/ds1/SBC-LabFor-DB" -d "/vmfs/volumes/ds1/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1/SBC-Webpage" -d "/vmfs/volumes/ds1/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1/k8s-core" -d "/vmfs/volumes/ds1/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1/k8s-dmz" -d "/vmfs/volumes/ds1/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1/k8s-master" 

218 || excdowngrade -d "/vmfs/volumes/ds1 (1)/ISO" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (1)/SBC-Webpage" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (1)/k8s-core" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (1)/k8s-dmz" -d "/vmfs/volumes/ds1 (1)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (1)/k8s-master" 

219 || exchostconf -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (11)/SBC-Webpage" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (11)/k8s-core" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (11)/k8s-dmz" -d "/vmfs/volumes/DS1 (11)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (11)/k8s-master" 

220 || pphost -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (12)/SBC-Webpage" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (12)/k8s-core" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (12)/k8s-dmz" -d "/vmfs/volumes/DS1 (12)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (12)/k8s-master" 

221 || xterm -d "/vmfs/volumes/DS1 (5)/ISO" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (5)/SBC-Webpage" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (5)/k8s-core" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (5)/k8s-dmz" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (5)/k8s-master" -d "/vmfs/volumes/DS1 (5)/SBC-LabFor-UserHR1" 

222 || bat -d "/vmfs/volumes/105-datastore2/ISO" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-UserHR2" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-UserIT" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-DB" -d "/vmfs/volumes/105-datastore2/SBC-Webpage" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-ELK" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-MailServer" -d "/vmfs/volumes/105-datastore2/k8s-core" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/105-datastore2/k8s-dmz" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/105-datastore2/k8s-master" -d "/vmfs/volumes/105-datastore2/SBC-LabFor-UserHR1" 

223 || socat -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (2)/SBC-Webpage" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (2)/k8s-core" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (2)/k8s-dmz" -d "/vmfs/volumes/ds1 (2)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (2)/k8s-master" 

224 || foreach -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-UserIT" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-DB" -d "/vmfs/volumes/ds1 (4)/SBC-Webpage" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-ELK" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-MailServer" -d "/vmfs/volumes/ds1 (4)/k8s-core" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/ds1 (4)/k8s-core_1" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/ds1 (4)/k8s-dmz" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/ds1 (4)/k8s-master" -d "/vmfs/volumes/ds1 (4)/SBC-LabFor-UserHR2" 

225 || ip -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (13)/SBC-Webpage" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-FTPSv" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (13)/k8s-core" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (13)/k8s-dmz" -d "/vmfs/volumes/DS1 (13)/SBC-LabFor-UserHR1" -d "/vmfs/volumes/DS1 (13)/k8s-master" 

226 || haltVms -d "/vmfs/volumes/DS1 (6)/ISO" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-UserHR2" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-UserIT" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-DB" -d "/vmfs/volumes/DS1 (6)/SBC-Webpage" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-ELK" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-FTPSvr" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-MailServer" -d "/vmfs/volumes/DS1 (6)/k8s-core" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-ServerAD2k12" -d "/vmfs/volumes/DS1 (6)/k8s-dmz" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-SquidProxy" -d "/vmfs/volumes/DS1 (6)/k8s-master" -d "/vmfs/volumes/DS1 (6)/SBC-LabFor-UserHR1" 
```