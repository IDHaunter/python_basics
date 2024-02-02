from ftplib import FTP

def list_ftp_directory(ftp, directory="."):
    try:
        ftp.cwd(directory)
        data = []
        ftp.dir(data.append)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    ftp_host = "192.168.1.198"
    ftp_user = "anonymous"
    ftp_password = ""

    try:
        with FTP(ftp_host) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_password)

            # Getting a list of files and directories in the current directory
            files_and_dirs = list_ftp_directory(ftp)

            if files_and_dirs:
                print("List of files and directories:")
                for item in files_and_dirs:
                    print(item)
    except Exception as e:
        print(f"Error: {e}")


main()