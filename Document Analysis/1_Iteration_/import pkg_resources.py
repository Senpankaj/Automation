import pkg_resources

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])

with open('installed_packages.txt', 'w') as f:
    for package in installed_packages_list:
        f.write(f"{package}\n")
