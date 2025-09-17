# Stub prerequisites: always satisfied, no prompts, no installs
def check_and_install_default_prerequisites():
    return True

class Prerequisite:
    def is_installed(self):
        return True
    def ask_to_install(self):
        return True
    def install(self):
        return True
    def darwin_installer(self):
        return True
    def linux_installer(self):
        return True

class HomebrewPrerequisite(Prerequisite):
    pass
