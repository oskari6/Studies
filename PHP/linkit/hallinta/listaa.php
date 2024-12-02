<html>
<head>
<title>Linkkitietokanta: linkit aakkosjärjestysessä</title>
</head>
<body bgcolor="#ffffff">
<H2>All links alphabetically</H2>
<ul>
<?php
require "funktiot.php";
$yhteys = AvaaTietokanta();

if(!$kysely = mysqli_query($yhteys, "SELECT id,otsikko FROM linkit ORDER BY otsikko"))
{
    print "<LI>Search failed!";
}
else
{
    while($linkki = mysqli_fetch_row($kysely))
    {
        print "<LI>" . $linkki[1];
        print " - <A HREF=\"yllapitolomake.php?id=";
        print $linkki[0] . "\">[Muuta tietoja]</A>";
    }
}
?>
</ul>
<p>
<a href="index.php">Takaisin etusivulle</A>
</body>
</html>
