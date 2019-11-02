var canvas = document.querySelector('canvas');
var canv = canvas.getContext('2d');
const G = 6.67428e-11;
var meterPerPixel = 100;

function mass_center(bodies) {
  this.rx = 0;
  this.ry = 0;
  this.m = 0;

  this.draw = function() {
    canv.beginPath();
    canv.arc(this.rx, this.ry, 3, 0, 2*Math.PI, false);
    canv.fillStyle = 'red';
    canv.fill();
  }

  this.set_CM = function() {
    temp_x = 0;
    temp_y = 0;
    temp_m = 0;
    for(var i = 0; i < bodies.length; i++) {
      temp_x += bodies[i].m*bodies[i].rx;
      temp_y += bodies[i].m*bodies[i].ry;
      temp_m += bodies[i].m;
    }
    this.rx = temp_x/temp_m;
    this.ry = temp_y/temp_m;
    this.draw();
  }
}

function body(m, rx, ry, vx, vy, ra,color) {
  this.m = m; // mass of the planet

  this.set_rx = function(x) {
    return x/meterPerPixel + 0.5*canvas.width;
  }

  this.set_ry = function(y) {
    return y/meterPerPixel + 0.5*canvas.height;
  }

  this.rx = this.set_rx(rx);
  this.ry = this.set_ry(ry);
  this.vx = vx;
  this.vy = vy;
  this.ra = ra;
  this.color = color;
  this.draw = function() {
    canv.beginPath();
    canv.arc(this.rx, this.ry, this.ra,0,Math.PI*2, false);
    canv.fillStyle = this.color;
    canv.fill();
  };
}


// Calculating the acceleration on both coordinates //

var acceleration_x = function(body_1, body_2, i, j) {

  if (i == j) {
    return 0;
  }
  else {
    return (body_2.rx-body_1.rx) * G * body_2.m / Math.sqrt((body_1.rx - body_2.rx)**2 + (body_1.ry - body_2.ry)**2)**3;
  }
}

var acceleration_y = function(body_1, body_2, i, j) {
  if (i == j) {
    return 0;
  }
  else {
    return (body_2.ry-body_1.ry) * G * body_2.m / Math.sqrt((body_1.rx - body_2.rx)**2 + (body_1.ry - body_2.ry)**2)**3;
  }
}


function simulate(h, bodies) {
  this.h = h;
  this.bodies = bodies;

  this.draw = function() {
    for(var i = 0; i < this.bodies.length; i++) {
      this.bodies[i].draw();
    }
  }

  this.velocity_verlet = function() {
    var novosposx = [];
    var novosposy = [];
    var novosvelx = [];
    var novosvely = [];
    var accx = [];
    var accy = [];
    for (var i = 0; i < this.bodies.length; i++) {
      var acx = 0;
      var acy = 0;
      for (var j = 0; j < this.bodies.length; j++) {
        acx += acceleration_x(this.bodies[i], this.bodies[j], i, j);
        acy += acceleration_y(this.bodies[i], this.bodies[j], i, j);
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
        acx += acceleration_x(this.bodies[i], this.bodies[j], i, j);
        acy += acceleration_y(this.bodies[i], this.bodies[j], i, j);
      }
      }
      novosvelx.push(this.bodies[k].vx + 0.5*(accx[k]+acnewx)*this.h);
      novosvely.push(this.bodies[k].vy + 0.5*(accy[k]+acnewy)*this.h);
    }
    for (var t = 0; t < this.bodies.length; t++) {
       this.bodies[t].rx = novosposx[t];
       this.bodies[t].ry = novosposy[t];
       this.bodies[t].vx = novosvelx[t];
       this.bodies[t].vy = novosvely[t];
     }
       this.draw();
  } // End verlet
} // End Simulate

// (m, rx, ry, vx, vy, ra,color)
//var planetas = [new body(10**15,20,20,-20,0,10,'yellow'), new body(10**15, 30,30,20,0,10,'blue'),new body(10**15, 120,120,0,-20,10,'green'), new body(10**15,50,30,0,20,10,'red')];
sol = new body(10**15,0,0,-20,0,5,'yellow');
terra = new body(10**15, 3000,5000,20,0,5,'blue');
jupiter = new body(1, -100, -25, 2, -1.5, 5, 'red');
var planetas = [sol, terra];
system = new simulate(0.1,planetas);
cm = new mass_center(planetas);
function animate() {
    requestAnimationFrame(animate);
    canv.clearRect(0,0,innerWidth,innerHeight);
    system.velocity_verlet();
    cm.set_CM();
}
animate();
