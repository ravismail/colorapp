docker build -t color-demo:1.0 .

docker run -p 8081:8080 docker.io/library/color-demo:1.0

docker run -e COLOR=green -p 8080:8080 color-demo:1.0


https://www.youtube.com/watch?v=XBRkFyK6D0k


my gke:
https://console.cloud.google.com/kubernetes/gateways?cloudshell=true&project=innate-entry-457123-h2

argocd:
https://34.26.66.191/applications/argocd/colorapp?view=tree&resource=
admin/NAtsWTZxGM-YU8YT

gitbuh: helm repo
https://github.com/ravismail/colorapp/blob/main

docker hub repo:
https://hub.docker.com/repository/docker/ravismail/color-demo/ 

app url:
http://34.26.24.77:8080/