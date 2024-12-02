<?php
require "funktiot.php";
$yhteys = AvaaTietokanta();
$id = htmlspecialchars($_GET["id"]);

if(!$kysely = mysqli_query($yhteys, "SELECT id,linkki,otsikko,avainsana,
        kuvaus FROM linkit WHERE id=$id"))
{
    print "Haku epäonnistui";
    exit;
}
else
{
    $linkki = mysqli_fetch_row($kysely);
}
?>

<html>
<head>
<title>Linkki tietokannan ylläpitolomake</title>
</head>
<body bgcolor="#ffffff">
<H2>Linkkitietokannan ylläpitolomake</H2>
<form method=post action="paivitetty.php">
    <input type=hidden name="id"
    value="<?php print $linkki[0]; ?>">
Linkki:<br><input type=text name="linkki"
size=50 maxlength=255 value="<?php print $linkki[1]; ?>"><br>
Otsikko:<br><input type=text name="otsikko"
size=50 maxlength=150 value="<?php print $linkki[2]; ?>"><br>
Avainsana:<br><input type=text name="avainsana"
size=50 maxlength=100 value="<?php print $linkki[3]; ?>"><br>
Kuvaus:<br><textarea name="kuvaus"
cols=50 rows=5><?php print $linkki[4]; ?></textarea><P>

<input type=submit name="toiminto" value="Tallenna">
<input type=submit name="toiminto" value="Poista">
</form>
</body>
</html>

