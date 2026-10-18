// =========================================================
// Robot Layla — Support batterie / pack de piles
// Tiroir simple qui se glisse sous la base, pour loger le
// pack 4xAA et faciliter le changement des piles.
// =========================================================
include <params.scad>

battery_pack_length = 58; // pack 4xAA standard
battery_pack_width  = 30;
battery_pack_height = 16;

module battery_tray() {
    difference() {
        cube([battery_pack_length + wall*2, battery_pack_width + wall*2, battery_pack_height + wall]);
        translate([wall, wall, wall])
            cube([battery_pack_length + tolerance, battery_pack_width + tolerance, battery_pack_height + tolerance]);
    }
    // languettes de fixation (vis M3) de chaque côté
    for (x = [0, battery_pack_length + wall*2])
        translate([x, (battery_pack_width + wall*2)/2, 0])
            difference() {
                cylinder(h = wall, d = 10, $fn = 24);
                cylinder(h = wall, d = m3_diameter, $fn = 16);
            }
}

battery_tray();

// NOTE: à fixer sous la base.scad avec 2 vis M3, ou simplement
// scotcher/velcro si vous préférez un montage amovible plus simple
// pour changer les piles facilement avec votre fille.
