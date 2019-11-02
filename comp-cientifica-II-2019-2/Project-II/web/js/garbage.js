
function animate() {
    requestAnimationFrame(animate);
    canv.clearRect(0,0,innerWidth,innerHeight);
    system.velocity_verlet();
    cm.set_CM();
}
animate();




var novosposx = [];
alert(novosposx);
var novosposy = [];
var novosvelx = [];
var novosvely = [];
var accx = [];
var accy = [];
for (var i = 0; i < this.bodies.length; i++) {
  var acx = 0;
  var acy = 0;
  for (var j = 0; j < this.bodies.length; j++) {
    if (i == j) {
      acx += 0;
      acy += 0;
// *this.bodies[j].m*G / Math.sqrt((this.bodies[i].rx - this.bodies[j].rx)*(this.bodies[i].rx - this.bodies[j].rx) + (this.bodies[i].ry - this.bodies[j].ry)(this.bodies[i].rx - this.bodies[j].rx))**3
    }
    else {
      acx += (this.bodies[j].rx-this.bodies[i].rx) * G * this.bodies[j].m / Math.sqrt((this.bodies[i].rx - this.bodies[j].rx)**2 + (this.bodies[i].ry - this.bodies[j].ry)**2)**3;
      acy += (this.bodies[j].ry-this.bodies[i].ry) * G * this.bodies[j].m / Math.sqrt((this.bodies[i].rx - this.bodies[j].rx)**2 + (this.bodies[i].ry - this.bodies[j].ry)**2)**3;
    }
    // ATE AQUI OK

  }

  novosposx.push(this.bodies[i].rx + this.h*this.bodies[i].vx + this.h*this.h*acx/2);

  novosposy.push(this.bodies[i].ry + this.h*this.bodies[i].vy + this.h*this.h*acy/2);
  accx.push(acx);
  accy.push(acy);
}
for (var k = 0; k < this.bodies.length; k++) {
  var acnewx = 0;
  var acnewy = 0;
  for (var l = 0; l < this.bodies.length; l++) {
    if (k == l) {
    acnewx += 0;
    acnewy += 0;
  }
  else {

    acx += (this.bodies[l].rx-this.bodies[k].rx) * G * this.bodies[l].m / Math.sqrt((this.bodies[k].rx - this.bodies[l].rx)**2 + (this.bodies[k].ry - this.bodies[l].ry)**2)**3;
    acy += (this.bodies[l].ry-this.bodies[k].ry) * G * this.bodies[l].m / Math.sqrt((this.bodies[k].rx - this.bodies[l].rx)**2 + (this.bodies[k].ry - this.bodies[l].ry)**2)**3;
  }
  }
  novosvelx.push(this.bodies[k].vx + 0.5*(accx[k]+acnewx)*this.h);
  novosvely.push(this.bodies[k].vy + 0.5*(accy[k]+acnewy)*this.h);
}
