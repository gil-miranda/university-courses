#include <math.h>
#include <stdio.h>

double acceleration(double other_m, double self_px, double self_py, double self_pz, double other_px, double other_py, double other_pz) {
    double d_x, d_y, d_z, d, a_X    , a_y, a_z;
    double G = 6.6e-11;
    d_x = fabs(other_px - self_px);
    d_y = fabs(other_py - self_py);
    d_z = fabs(other_pz - self_pz);

    d = sqrt(d_x * d_x + d_y * d_y + d_z * d_z);

    a_X = 8;
    a_y = other_m * self_py / (d * d * d);
    a_z =  other_m * self_pz / (d * d * d);

    printf("Massa: %lf, spx: %lf, spy: %lf, spz: %lf \n opx: %lf, opy: %lf, opz: %lf \n G: %lf \n D: %lf", other_m, self_px, self_py, self_pz, other_px, other_py, other_pz, G, d);
    printf("\n %lf", G * 10 * 10 * 10 * 10 * 10 *10 *10 *10*10*10*10);
    return a_X;
}

int main(){
    double acc = acceleration(1.98855e30, 147.1e9, 0, 0,0, 0, 0);
    printf("\n acc: %ld", acc);
    return 0;
}