<?php
require "aputoiminnot.php";
$istuntotunnus = htmlspecialchars($_COOKIE["istuntotunnus"]);
$id = $_GET['id'];

$tiedosto = array(); 

if($id != "")
{
    if(!$kysely = mysqli_query($yhteys, "SELECT id,nimi,tiedostonimi,kuvaus
            FROM tiedostot,kayttaja WHERE id=$id AND tallentaja=
            kayttaja.tunnus AND istuntotunnus='$istuntotunnus'"))
    {
        print "<LI>Haku epäonnistui!";
        exit;
    }
    else
    {
        $tiedosto = mysqli_fetch_row($kysely);
    }
}
?>

<html>
<head>
<title>Tiedostopalvelun tallennuslomake</title>
</head>
<body bgcolor="#ffffff">
<H2>Tallennuslomake</H2>
<form method="post" action="tallenna.php"
enctype="multipart/form-data">
<?php

if(!empty($tiedosto))
{
?>
    <input type=hidden name="id" value="<?php print $id; ?>">
    <?php
}
?>

<?php
if(!empty($tiedosto))
{
?>
Anna tiedostolle nimi:<BR>
<input type=text name="nimi"
value="<?php print $tiedosto[1]; ?>"
size=30 maxlength=150><P>

Kuvaile tiedostoa:<BR>
<textarea name="kuvaus"
rows=6 cols=50><?php print $tiedosto[3]; ?></textarea><P>
<?php
}
else
{
?>
Anna tiedostolle nimi:<BR>
<input type=text name="nimi"
size=30 maxlength=150><P>

Kuvaile tiedostoa:<BR>
<textarea name="kuvaus"
rows=6 cols=50></textarea><P>
<?php 
}
?>

Valitse tallennettava tiedosto:<BR>
<input type=file name="tiedosto">
<P>
<input type=submit value="Tallenna kuvaus ja tiedosto">
</form>
</body>
</html>
