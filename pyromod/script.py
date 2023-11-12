import subprocess

def main():
    subprocess.run(['curl', '-sSL', 'https://raw.githubusercontent.com/WhaleFell/TGBot/main/exc.sh', '|', 'sudo', '/bin/bash'], check=True)

if __name__ == '__main__':
    main()
