
<br></br>

<?php 
        echo " Clé API actuelle : ";
        $monfichier = fopen('cle.txt', 'r+'); // On ouvre le fichier contenant la clé

        $cle = fgets($monfichier);
        print($cle);
?>

<br></br>
        <form name="inscription" method="post" action="index.php">
            Nouvelle clé API : <input type="text" name="Cle"/> <br/>
            <input type="submit" name="valider" value="Envoyer"/>
        </form>

<?php
if(isset($_POST['valider'])){
        $cle=$_POST['Cle'];
        ftruncate($monfichier,0);
        fseek($monfichier, 0);
        fputs($monfichier, "$cle"); //On remplace la clé actuelle par celle saisie par l'tuilisateur
        header('Location: index.php');
}
?>

<?php
        close($monfichier); // On ferme le fichier
 ?>





