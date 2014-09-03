curl -X POST --data "name=bob&ident=12345" http://107.170.245.92:5000/register
curl -X POST --data "name=tom&ident=12346" http://107.170.245.92:5000/register
curl -X POST --data "name=larry&ident=12347" http://107.170.245.92:5000/register

curl -X GET http://107.170.245.92:5000/getnearby

