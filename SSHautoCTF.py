import paramiko

try:
    in_hostname = input("Enter IP / Hostname: ")
    in_username = input("Enter Username: ")
    in_password = input("Enter Password: ")

    def sshClient():

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=in_hostname,username=in_username,password=in_password)
        stdin,stdout,stderr = ssh_client.exec_command("ls -la")
        print("====== Current Folder =======")
        print(stdout.readlines())

        stdin, stdout, stderr = ssh_client.exec_command("getcap -r / 2>/dev/null")
        print("====== Capabilities ======")
        print(stdout.readlines())

        stdin, stdout, stderr = ssh_client.exec_command("cat /etc/passwd")
        print("====== passwd File ======")
        print(stdout.readlines())

        stdin, stdout, stderr = ssh_client.exec_command("cat /etc/shadow")
        print("====== shadow File ======")
        print(stdout.readlines())

        stdin, stdout, stderr = ssh_client.exec_command("sudo -l")
        stdin.write(in_password)
        print("====== sudo -l ======")
        sd = stdout.readlines()
        for line in sd:
            print(line)

        # Upload SUID3NUM
        ftp_client = ssh_client.open_sftp()
        ftp_client.put("/root/tools/suid3num.py","/tmp/suid3num.py")
        ftp_client.close()

        stdin, stdout, stderr = ssh_client.exec_command("python /tmp/suid3num.py")
        print("====== suid3num ======")
        s = stdout.readlines()
        for line in s:
            print(line)

    sshClient()

except Exception as e:
    print(e)