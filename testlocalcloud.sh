curl -X POST --data "name=bob&ident=12345&purl=httpcolonslash4&headline=I%20AM%20A%20BANANA" http://localhost:5000/register
curl -X POST --data "name=tom&ident=12346&purl=httpcolonslash2&headline=I%20AM%20A%20BANANA" http://localhost:5000/register
curl -X POST --data "name=larry&ident=12347&purl=httpcolonslash3&headline=I%20AM%20A%20BANANA" http://localhost:5000/register

curl -X GET http://localhost:5000/getnearby

