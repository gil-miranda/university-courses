#include <math.h>

double acceleration(double other_m, double self_px, double self_py, double self_pz, double other_px, double other_py, double other_pz, double G) {
    double d_x, d_y, d_z, d, a_x, a_y, a_z;
    d_x = fabs(other_px - self_px);
    d_y = fabs(other_py - self_py);
    d_z = fabs(other_pz - self_pz);

    d = sqrt(d_x * d_x + d_y * d_y + d_z * d_z);

    a_x = -G * other_m * self_px / (d * d * d);
    a_y = -G * other_m * self_py / (d * d * d);
    a_z = -G * other_m * self_pz / (d * d * d);

    return a_x;
}
