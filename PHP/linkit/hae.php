<html>
<head>
<title>Sanahaun tulokset aakkosjärjestyksessä</title>
</head>
<body bgcolor="#ffffff">
<H2>Sanahaun tulokset</H2>
<ul>
<?php
$hakusanat = htmlspecialchars($_POST["hakusanat"]);

ini_set('display_errors', 0);   //error handling
error_reporting(0);

require "funktiot.php";
$yhteys = AvaaTietokanta();

if(!$kysely = mysqli_query($yhteys, "SELECT id,linkki,otsikko,kuvaus
    FROM linkit WHERE otsikko LIKE '%$hakusanat%' OR kuvaus LIKE '%$hakusanat%'
    OR avainsana LIKE '%$hakusanat%'"))
{
    print "<LI>Haku epäonnistui!";
}
else
{
    while($linkki = mysqli_fetch_row($kysely))
    {
        print "<LI><A HREF=\"". $linkki[1];
        print "\">" . $linkki[2];
        print "</A> <I>" . $linkki[3] . "</I>";
    }
}
?>

</ul>
<p>
<a href="hakulomake.php">Tee uusi haku</A>
</body>
</html>