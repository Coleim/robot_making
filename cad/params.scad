// =========================================================
// Robot Layla — Paramètres communs à toutes les pièces
// Modifiez ces valeurs selon vos composants réels avant
// d'exporter les STL (mesurez vos moteurs/écran au pied à
// coulisse si possible, les kits varient légèrement).
// =========================================================

// --- Général ---
wall = 3;              // épaisseur de paroi standard (mm)
tolerance = 0.3;       // jeu pour les pièces qui s'emboîtent (mm)

// --- Châssis / base ---
base_length = 120;     // longueur de la base (mm)
base_width  = 100;     // largeur de la base (mm)
base_height = 25;      // hauteur des parois de la base (mm)
corner_radius = 15;    // rayon des coins arrondis de la base

// --- Moteurs (kit "TT motor gearbox" standard) ---
motor_length = 70;     // longueur du moteur + boîte de vitesse (mm)
motor_width  = 22;     // largeur du moteur (mm)
motor_height = 18;     // hauteur du moteur (mm)
motor_shaft_offset = 9; // hauteur de l'axe par rapport au bas du moteur (mm)

// --- Roulette folle ---
caster_diameter = 25;  // diamètre de la roulette (mm)
caster_mount_hole = 3; // diamètre des trous de fixation (mm)

// --- Tête / écran OLED ---
head_diameter = 90;    // diamètre de la tête (mm)
head_height   = 60;    // hauteur de la tête (mm)
oled_width  = 27.3;    // largeur de la carte OLED SSD1306 0.96" (mm)
oled_height = 27.8;    // hauteur de la carte OLED (mm)
oled_screen_width  = 21.7; // zone d'affichage utile (mm)
oled_screen_height = 11.2;
oled_thickness = 4;    // épaisseur approx de la carte + connecteurs (mm)

// --- Capteur ultrason (le "nez") ---
us_width  = 45;        // largeur du HC-SR04 (mm)
us_height = 20;         // hauteur du HC-SR04 (mm)
us_eye_diameter = 16;   // diamètre des "yeux" du capteur (les 2 cylindres)
us_eye_spacing = 26;    // entraxe entre les 2 cylindres du capteur

// --- Oreilles ---
ear_base_diameter = 30; // diamètre à la base de l'oreille (mm)
ear_height = 35;        // hauteur de l'oreille (mm)
ear_spacing = 60;       // écart entre les 2 oreilles (mm)

// --- Vis M3 ---
m3_diameter = 3.2;      // diamètre de perçage pour vis M3 (passage libre)
m3_head_diameter = 6.5; // diamètre de la tête de vis M3 (pour fraisage)
