import jenkins


host="http://localhost:8080"
username=""
password="" # Jenkins user password / api token here
server = jenkins.Jenkins(host,username=username, password=password)

# Jenkins user Info and version
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s'%(user['fullName'],version))