// =========================================================
// Robot Layla — Tête (support écran OLED + capteur ultrason)
// Une sphère aplatie avec une fenêtre pour l'écran OLED (les
// yeux) et un emplacement pour le capteur ultrason (le museau).
// =========================================================
include <params.scad>

module head_shell() {
    difference() {
        // Coque sphérique aplatie
        scale([1, 0.85, 0.75])
            sphere(d = head_diameter, $fn = 64);

        // Évidement intérieur (coque creuse)
        scale([1, 0.85, 0.75])
            sphere(d = head_diameter - wall*2, $fn = 64);

        // On coupe la moitié basse pour pouvoir poser la tête
        translate([-head_diameter, -head_diameter, -head_diameter])
            cube(head_diameter*2);
    }
}

module oled_window() {
    // Fenêtre rectangulaire pour la zone d'affichage de l'écran,
    // positionnée sur le "visage" (face avant, Y = avant)
    translate([-oled_screen_width/2, -head_diameter/2 - 1, head_height*0.35])
        cube([oled_screen_width, wall + 2, oled_screen_height]);
}

module oled_card_slot() {
    // Logement intérieur pour glisser la carte OLED complète
    // (un peu plus grand que la carte pour le jeu de montage)
    translate([-oled_width/2 - tolerance, -head_diameter/2 - wall - 2,
                head_height*0.35 - (oled_height - oled_screen_height)/2 - tolerance])
        cube([oled_width + tolerance*2, oled_thickness + tolerance, oled_height + tolerance*2]);
}

module nose_sensor_slot() {
    // Logement pour le capteur HC-SR04, sous l'écran, qui fait
    // office de "museau" avec les 2 cylindres du capteur visibles
    translate([0, -head_diameter/2 - 1, head_height*0.15]) {
        for (dx = [-us_eye_spacing/2, us_eye_spacing/2])
            translate([dx, 0, 0])
                rotate([-90, 0, 0])
                    cylinder(h = wall + 4, d = us_eye_diameter + tolerance, $fn = 32);
    }
}

module head() {
    difference() {
        head_shell();
        oled_window();
        oled_card_slot();
        nose_sensor_slot();
    }
}

head();

// NOTE: imprimez la tête avec supports uniquement sous les fenêtres
// (activez "supports touching buildplate only" dans votre slicer),
// orientation recommandée : ouverture vers le bas sur le plateau.
