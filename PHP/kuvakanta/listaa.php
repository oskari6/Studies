<H2>Tallentamasi tiedostot aakkosjärjestyksessä</H2>
<ul>
<?php
require "aputoiminnot.php";
$istuntotunnus = htmlspecialchars($_COOKIE["istuntotunnus"]);

if(!$kysely = mysqli_query($yhteys, "SELECT id,nimi,tiedostonimi FROM tiedostot,kayttaja
    WHERE tallentaja=kayttaja.tunnus AND istuntotunnus='$istuntotunnus' ORDER BY nimi"))
{
    print "<LI>Haku epäonnistui!";
}
else
{
    while($tiedosto = mysqli_fetch_row($kysely))
    {
        print "<LI>" . $tiedosto[1];
        print " - <A HREF=\"tallennuslomake.php?id=";
        print $tiedosto[0] . "\"> [Muuta tietoja]</A>\n";
        print " - <A HREF=\"avaa.php?id=";
        $link = $tiedosto[2];
        print $tiedosto[0] . "\">$tiedosto[2]</A>\n";
    }
}
?>
</ul>
<p>
<a href="index.php">Takaisin etusivulle</A>