import jenkins

host="http://localhost:8080"
username="" #jenkins username here
password="" # Jenkins user password / api token here
server = jenkins.Jenkins(host,username=username, password=password)

# Create view
view_config = open("viewconfig.xml", mode='r', encoding="utf-8").read()
server.create_view("My Job List 2 ",view_config)

# Get list of views
views = server.get_views()
print(views)

# Update view
view_config = open("viewconfigupdate.xml", mode='r', encoding="utf-8").read()
server.reconfig_view("My Job List",view_config)

# Delete view
server.delete_view("My Job List")