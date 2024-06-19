import jenkins

host="http://localhost:8080"
username="" #jenkins username here
password="" # Jenkins user password / api token here
server = jenkins.Jenkins(host,username=username, password=password)

# Run a build and get build number and more info
server.build_job('job1')

last_build_number = server.get_job_info('job2')['lastCompletedBuild']['number']
print('Build number : ',last_build_number)

build_info= server.get_job_info('job2',last_build_number)
print('Build info : ',build_info)

# Delete a job
server.delete_job('copyjob3')