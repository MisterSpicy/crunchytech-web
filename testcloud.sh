curl -X POST --data "name=bob&ident=12345&purl=http%3A%2F%2Fwww.linkedout.com%2Fsomeprofile1.jpg&headline=I%20AM%20A%20BANANA" http://107.170.245.92:5000/register
curl -X POST --data "name=tom&ident=12346&purl=http%3A%2F%2Fwww.linkedout.com%2Fsomeprofile2.jpg&headline=I%20AM%20A%20BANANA" http://107.170.245.92:5000/register
curl -X POST --data "name=larry&ident=12347&purl=http%3A%2F%2Fwww.linkedout.com%2Fsomeprofile3.jpg&headline=I%20AM%20A%20BANANA" http://107.170.245.92:5000/register

curl -X GET http://107.170.245.92:5000/getnearby

