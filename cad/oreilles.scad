// =========================================================
// Robot Layla — Oreilles amovibles
// Imprimées séparément pour pouvoir les personnaliser
// facilement (couleur différente, forme, etc.) avec votre fille.
// =========================================================
include <params.scad>

module ear() {
    difference() {
        union() {
            cylinder(h = ear_height, d1 = ear_base_diameter, d2 = ear_base_diameter*0.3, $fn = 48);
        }
        // on évide pour alléger et économiser du filament
        translate([0, 0, wall])
            cylinder(h = ear_height, d1 = ear_base_diameter - wall*2, d2 = 1, $fn = 48);
    }
    // tenon de fixation (s'enfiche dans un trou de la tête)
    translate([0, 0, -6])
        cylinder(h = 6, d = ear_base_diameter*0.4 - tolerance, $fn = 32);
}

// Deux oreilles, espacées pour l'impression
translate([-ear_spacing/2, 0, 0]) ear();
translate([ear_spacing/2, 0, 0]) ear();

// NOTE: imprimez "à plat" comme ci-dessus (base vers le bas),
// pas de support nécessaire. Changez de filament entre les deux
// oreilles si vous voulez 2 couleurs différentes !
