import sys, os

class Package:
    def __init__(self, packageName:str, **kwargs):
        self.package = packageName

        try: self.package+="=="+kwargs['version']
        except: pass

class pip:
    def installPackage(package:Package):
        os.system('pip install {}'.format(package.package))
    
    def uninstallPackage(package:Package):
        os.system('pip uninstall {}'.format(package.package))

    def installPackages(packages:list):
        for package in packages:
            os.system('pip install {}'.format(package.package))
    
    def uninstallPackages(packages:list):
        for package in packages:
            os.system('pip uninstall {}'.format(package.package))

    def freezeToRequirements(fileName:str="requirements.txt"):
        os.system('pip freeze > {}'.format(fileName))