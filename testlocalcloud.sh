curl -X POST --data "name=bob&ident=12345&purl=httpcolonslash1" http:/localhost:5000/register
curl -X POST --data "name=tom&ident=12346&purl=httpcolonslash2" http://localhost:5000/register
curl -X POST --data "name=larry&ident=12347&purl=httpcolonslash3" http://localhost:5000/register

curl -X GET http://localhost:5000/getnearby

