<html>
<head>
<?php $avainsana = htmlspecialchars($_GET['avainsana']);?>
<title>Avainsanalla <?php print $avainsana; ?> löytyneet linkit</title>
</head>
<body bgcolor="#ffffff">
<H2>Avainsanalla <?php print $avainsana; ?> löytyi seuraavat linkit </H2>
<ul>
<?php

require "funktiot.php";
$yhteys = AvaaTietokanta();

if(!$kysely = mysqli_query($yhteys, "SELECT id,linkki,otsikko,kuvaus FROM linkit WHERE avainsana = '$avainsana'"))
{
    print "<LI>Haku epäonnistui.";
}
else
{
    while($linkki = mysqli_fetch_row($kysely))
    {
        print "<LI><A HREF=\"" . $linkki[1];
        print "\">" . $linkki[2];
        print "</A> <I>" . $linkki[3] . "</I>";
    }
}
?>
</ul>
<p>
<a href="index.php">Takaisin linkkitietokannan etusivulle</A>
</body>
</html>