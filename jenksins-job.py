import jenkins


host="http://localhost:8080"
username="" #jenkins username here
password="" # Jenkins user password / api token here
server = jenkins.Jenkins(host,username=username, password=password)

# create a empty Job
server.create_job("job1", jenkins.EMPTY_CONFIG_XML)

# create a preconfigured job job using config.xml
job2_xml = open("jobconfig.xml", mode='r', encoding="utf-8").read()
server.create_job("job2", job2_xml)



# copy job
server.copy_job('job2','copyjob3')

# view jobs
jobs = server.get_jobs()
print(jobs)

# update job
updated_copyjob3 = open("jobconfig_update.xml", mode='r', encoding="utf-8").read()
server.reconfig_job("copyjob3", updated_copyjob3)

# disable job
server.disable_job("copyjob3")