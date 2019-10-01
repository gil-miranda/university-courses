#include <math.h>
#include <stdio.h>

double acceleration_x(double other_m, double self_px, double self_py, double self_pz, double other_px, double other_py, double other_pz) {
    double d_x, d_y, d_z, d, a_x;
    double G = 6.6e-11;
    d_x = fabs(other_px - self_px);
    d_y = fabs(other_py - self_py);
    d_z = fabs(other_pz - self_pz);

    d = sqrt(d_x * d_x + d_y * d_y + d_z * d_z);

    a_x = -G * other_m * self_px / (d * d * d);

    return a_x;
}

double acceleration_y(double other_m, double self_px, double self_py, double self_pz, double other_px, double other_py, double other_pz) {
    double d_x, d_y, d_z, d, a_y;
    double G = 6.6e-11;
    d_x = fabs(other_px - self_px);
    d_y = fabs(other_py - self_py);
    d_z = fabs(other_pz - self_pz);

    d = sqrt(d_x * d_x + d_y * d_y + d_z * d_z);

    a_y = -G * other_m * self_py / (d * d * d);

    return a_y;
}

double acceleration_z(double other_m, double self_px, double self_py, double self_pz, double other_px, double other_py, double other_pz) {
    double d_x, d_y, d_z, d, a_z;
    double G = 6.6e-11;
    d_x = fabs(other_px - self_px);
    d_y = fabs(other_py - self_py);
    d_z = fabs(other_pz - self_pz);

    d = sqrt(d_x * d_x + d_y * d_y + d_z * d_z);

    a_z =  -G * other_m * self_pz / (d * d * d);

    return a_z;
}

int main(){
    double acc = acceleration_z(1.98855e30, 147.1e9, 0, 0,0, 0, 0);
    printf("\n acc: %lf", acc);
    return 0;
}
