<html>
<head>
</head>
<title></title>
<body>
<H2>Alphabetical wordsearch</H2>
<ul>
<?php
require "funktiot.php";
$yhteys = AvaaTietokanta();

if(!$kysely = mysqli_query($yhteys, "SELECT DISTINCT avainsana FROM linkit ORDER BY avainsana "))
{
    print "<LI>Keyword search failed!";
}
else
{
    while($linkki = mysqli_fetch_row($kysely))
    {
        print "<LI><A HREF=\"linkit_avainsana.php?avainsana=" . $linkki[0];
        print "\">" . $linkki[0];
        print "</A> " ;
    }
}
?>
</ul>
<p>
    <a href="index.php">Takaisin linkki tietokannan etusivuille</A>
</body>
</html>