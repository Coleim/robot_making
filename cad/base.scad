// =========================================================
// Robot Layla — Base / châssis
// Plaque principale qui accueille : Raspberry Pi, driver
// moteur, pack de piles, les 2 moteurs et la roulette folle.
// =========================================================
include <params.scad>

module rounded_plate(l, w, h, r) {
    hull() {
        for (x = [r, l - r])
            for (y = [r, w - r])
                translate([x, y, 0])
                    cylinder(h = h, r = r, $fn = 48);
    }
}

module base_plate() {
    difference() {
        rounded_plate(base_length, base_width, wall, corner_radius);

        // Trous de fixation du Raspberry Pi (gabarit officiel 58x49mm,
        // trous à 3.5mm des bords, diamètre 2.75mm -> on perce 3.2mm)
        translate([base_length/2 - 29, base_width/2 - 24.5, -1])
            cylinder(h = wall + 2, d = m3_diameter, $fn = 20);
        translate([base_length/2 + 29, base_width/2 - 24.5, -1])
            cylinder(h = wall + 2, d = m3_diameter, $fn = 20);
        translate([base_length/2 - 29, base_width/2 + 24.5, -1])
            cylinder(h = wall + 2, d = m3_diameter, $fn = 20);
        translate([base_length/2 + 29, base_width/2 + 24.5, -1])
            cylinder(h = wall + 2, d = m3_diameter, $fn = 20);
    }
}

module motor_mount(x, y, mirror_x = false) {
    translate([x, y, 0]) {
        mirror([mirror_x ? 1 : 0, 0, 0]) {
            difference() {
                cube([motor_length + wall*2, motor_width + wall*2, base_height]);
                translate([wall, wall, motor_shaft_offset])
                    cube([motor_length + tolerance, motor_width + tolerance, motor_height]);
            }
        }
    }
}

module caster_mount() {
    difference() {
        cylinder(h = base_height/2, d = caster_diameter + wall*2, $fn = 40);
        translate([0, 0, -1])
            cylinder(h = base_height/2 + 2, d = caster_diameter + tolerance, $fn = 40);
        // trous de fixation de la roulette
        for (a = [0, 90, 180, 270])
            rotate([0, 0, a])
                translate([caster_diameter/2 + wall/2, 0, -1])
                    cylinder(h = base_height, d = caster_mount_hole, $fn = 16);
    }
}

// --- Assemblage ---
base_plate();

// Moteur gauche, à l'avant-gauche de la base
translate([10, 5, wall]) motor_mount(0, 0);

// Moteur droit (symétrique), à l'avant-droite
translate([10, base_width - motor_width - wall*2 - 5, wall]) motor_mount(0, 0);

// Roulette folle à l'arrière, centrée
translate([base_length - caster_diameter - wall*2, base_width/2, wall])
    caster_mount();

// NOTE: ceci est un gabarit de départ. Ajustez les positions selon
// vos moteurs réels avant impression (imprimez d'abord un essai
// rapide en "brouillon" / 15% infill pour vérifier les côtes).
