DISTRO_INFO = {
        'centos8': {
            'description': 'CentOS 8',
            'url': 'http://mirror.centos.org/centos/8/BaseOS/x86_64/os/images/pxeboot',
            'answerfile': 'inst.ks=https://raw.githubusercontent.com/acefei/ace-osinstaller/master/answerfiles/kickstart',
            'kernel_args': 'inst.repo=http://mirror.centos.org/centos/8/BaseOS/x86_64/kickstart inst.text ip=dhcp ipv6.disable'
            },
        'debian-stable': {
            'description': 'Debian Stable',
            'url': 'http://ftp.debian.org/debian/dists/stable/main/installer-amd64/current/images/netboot/debian-installer/amd64',
            'answerfile': 'url=https://raw.githubusercontent.com/acefei/ace-osinstaller/master/answerfiles/preseed',
            'kernel_args': 'auto=true priority=critical'
            },
        'ubuntu': {
            'description': 'Ubuntu',
            'url': 'http://archive.ubuntu.com/ubuntu/dists/eoan/main/installer-amd64/current/images/netboot/ubuntu-installer/amd64/',
            'answerfile': 'url=https://raw.githubusercontent.com/acefei/ace-osinstaller/master/answerfiles/autoinstall',
            'kernel_args': 'auto=true priority=critical'
            }
        }
