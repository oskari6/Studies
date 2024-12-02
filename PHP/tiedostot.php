<html>
    <head>
        <title>Esimerkki tiedostonkäsittely funktioista</title>
</head>
<body bgcolor="#ffffff">
    <H2>Esimerkki tiedostonkäsittely funktioista</H2>
<?php
$tiedosto = "testi.txt";
print "Tarkistetaan <B>file_exists</B> -komennolla, löytyykö tarvitsemaamme tietodostoa...";
if(!file_exists($tiedosto))
{
    print "Tiedostoa '$tiedosto' ei löytynyt.<BR>\n";
}
else
{
    print "Löytyi!<BR>\n";
    print "Tiedoston koko (<B>filesize</B>): " . filesize($tiedosto) . " tavua<BR><BR>\n";
    print "tiedosto on ";
    if(is_writeable($tiedosto)) print "kirjoitettavissa (<B> is_writeable</B>)...";
    if(is_readable($tiedosto)) print "luettavissa (<B> is_readable</B>)...";
    print "<BR><BR>\n";
    $osoitin = fopen($tiedosto, "r");
    print "Avataan tiedosto käyttäen komentoa <B>fopen</B> ja tulostetaan 2 ensimmäistä kirjainta tiedostosta <B>fgetc</B> -komennolla.<BR>\n";
    print "Samalla tarkistetaan <B>feof</B> -komennolla, ettei olla olla tiedoston lopussa:<BR>\n";
    
    for($kierros = 1; $kierros<=2;$kierros++)
    {
        $kirjain = fgetc($osoitin);
        if(!feof($osoitin))
            print $kirjain;
    }
    print "<BE><BR>\n";
    print "Tulostuuko koko sana, kun seuraavaksi käytetään <B>fgets</B> -komentoa?<BR>\n";
    print fgets($osoitin, 7);
    print "<BR><BR>\n";
    print "Ei. Tarkistetaan <B>ftell</B> -komennolla ollaanko tiedoston alussa.";
    print "<BR><BR>\n" . ftell($osoitin) . "<BR><BR>\n";
    print "Ei olla, joten palataan tiedoston alkuun <B>rewinf</B> -komennon avulla ja yritetään uudelleen:<BR>\n";
    rewind($osoitin);
    print fgets($osoitin,7);
    print "<BR><BR>\n";
    print "Luetaan tiedosto taulukkoon <B>file</B> -komennolla...<BR>\n";
    $teksti = file($tiedosto);
    print "Tulostetaan kolme riviä taulukosta:<BR>\n";
    
    for($h = 0; $h <= 2; $h++)
    {
        print $teksti[$h] . "<BR>\n";
    }
    print "<BR>Suljetaan tiedosto(<B>fclose</B>).";
    fclose($osoitin);
    print "<BR>\nTiedosto on luotu (<B>filectime</B>): ";
    print date("jS \of F Y H:i:s", filectime($tiedosto)) . "<BR>\n";
    print "Tiedostoon on viimeksi kirjoitettu (<B>filemtime</B>): ";
    print date("jS \of F Y H:i:s", filemtime($tiedosto)) . "<BR>\n";
}
?>
</body>
</html>