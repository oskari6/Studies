<H2>Aakkosellinen sanahakemisto</H2>
<ul>
<?php

$yhteys = odbc_connect("harjoitukset","","");

if(!$kysely = odbc_exec($yhteys, "SELECT DISTINCT avainsana FROM linkit
    ORDER BY avainsana "))
{
    print "<LI>Avainsanojen selaus epäonnistui!";
}
else
{
    while(odbc_fetch_row($kysely))
    {
        print "<LI><A HREF=\"linkit_avainsana.php?avainsana=" .
            odbc_result($kysely,"avainsana");
        print "\">" . odbc_result($kysely, "avainsana");
        print "</A> ";
    }
}
?>
</ul>
<p>
<a href="index.php">Takaisin linkkitietokannan etusivulle</A>