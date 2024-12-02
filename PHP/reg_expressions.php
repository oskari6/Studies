<?php
//security check
if(ereg("^../",$tiedostonimi))
{
    print "Tiedostopolkujen antaminen kiellettyä";
}
else
{
    $tiedostohandle = fopen("C:(temp/$tiedostonimi","r");
    fpassthru($tiedostokahva);
}
//email checker
if(ereg("^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+", $email))
{
    //oikein
}
else
{
    //väärin
}
