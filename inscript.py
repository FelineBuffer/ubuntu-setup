import subprocess

'''
task to accomblish:
done - download zsh
change shell from bash to zsh
download oh-my-zsh
change couple things in the .zshrc file
'''


def zsh_install():
    sudo = 'sudo'
    package = 'zsh'
    cmd = 'apt'
    argument = 'install'
    
    subprocess.run([sudo, cmd, argument, package], shell=False)
    
    subprocess.run(['chsh', '-s', '$(which zsh)'])

zsh_install()

"""/var/log/apt/history.log"""
