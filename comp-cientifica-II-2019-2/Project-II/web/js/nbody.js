////////////// N-Body problem simulator with Simpletic Velocity-Verlet Integrator
//////// Author: Gil Miranda
//////// Contact: gilsmneto@gmail.com; gil.neto@ufrj.br
////////////// Last Update: 02/11/2019

var canvas = document.querySelector('canvas');
var context = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const G = 6.67428e-11;
var AU = 149.6e7;
var meterPerPixel = AU/2;
var i, j;


var set_UI = function(body_count, cm_x, cm_y) {
  var body_counter = document.getElementById('body_counter');
  body_counter.innerHTML = body_count;

  var cm_posx = document.getElementById('cm_posx');
  var cm_posy = document.getElementById('cm_posy');
  cm_posx.innerHTML = cm_x;
  cm_posy.innerHTML = cm_y;
}

var set_rx = function(x) {
  return x/meterPerPixel + 0.5*canvas.width;
}

var set_ry = function(y) {
  return y/meterPerPixel + 0.5*canvas.height;
}

function mass_center(bodies) {
  this.r_x = 0;
  this.r_y = 0;
  this.plot_x = 0;
  this.plot_y = 0;
  this.mass = 0;

  this.draw = function() {
    context.beginPath();
    
    //context.arc(this.plot_x, this.plot_y, 1, 0, 2*Math.PI, false);
    context.strokeStyle = 'DeepPink';
    context.moveTo(this.plot_x, this.plot_y);
    context.lineTo(this.plot_x + 5, this.plot_y);
    context.lineTo(this.plot_x - 5, this.plot_y);
    context.moveTo(this.plot_x, this.plot_y);
    context.lineTo(this.plot_x, this.plot_y+5);
    context.lineTo(this.plot_x, this.plot_y-5);
    context.stroke();
  }

  this.set_CM = function() {
    temp_x = 0;
    temp_y = 0;
    temp_m = 0;
    for(var i = 0; i < bodies.length; i++) {
      temp_x += bodies[i].mass*bodies[i].r_x;
      temp_y += bodies[i].mass*bodies[i].r_y;
      temp_m += bodies[i].mass;
    }
    this.r_x = temp_x/temp_m;
    this.r_y = temp_y/temp_m;
    this.plot_x = set_rx(this.r_x);
    this.plot_y = set_ry(this.r_y);
    //console.log('CM -> ' + this.plot_x + ' - ' + this.plot_y);
    this.draw();
  }
}

function body(mass, r_x, r_y, v_x, v_y, ra,color, name) {
  this.mass = mass; // mass of the planet
  this.r_x = r_x;
  this.r_y = r_y;
  this.plot_x = set_rx(r_x);
  this.plot_y = set_rx(r_y);
  this.lastpos_x = [this.plot_x];
  this.lastpos_y = [this.plot_y];
  this.v_x = v_x;
  this.v_y = v_y;
  this.ra = ra;
  this.color = color;
  this.name = name;
  this.draw = function() {
    context.beginPath();
    context.arc(this.plot_x, this.plot_y, this.ra,0,Math.PI*2, false);
    context.fillStyle = this.color;
    context.fill();
  };
}


// Functions that calculate the acceleration on both coordinates //

var acceleration_x = function(body_1, body_2, i, j) {
  if (i == j) {
    return 0;
  }
  else {
    return (body_2.r_x-body_1.r_x) * G * body_2.mass / Math.sqrt((body_1.r_x - body_2.r_x)**2 + (body_1.r_y - body_2.r_y)**2)**3;
  }
}

var acceleration_y = function(body_1, body_2, i, j) {
  if (i == j) {
    return 0;
  }
  else {
    return (body_2.r_y-body_1.r_y) * G * body_2.mass / Math.sqrt((body_1.r_x - body_2.r_x)**2 + (body_1.r_y - body_2.r_y)**2)**3;
  }
}
// Special LEAPFROG Functions that calculate the acceleration //

var lf_acceleration_x = function(body_1x, body_1y, body_2, i, j) {
  if (i == j) {
    return 0;
  }
  else {
    return (body_2.r_x-body_1x) * G * body_2.mass / Math.sqrt((body_1x - body_2.r_x)**2 + (body_1y - body_2.r_y)**2)**3;
  }
}

var lf_acceleration_y = function(body_1x, body_1y, body_2, i, j) {
  if (i == j) {
    return 0;
  }
  else {
    return (body_2.r_y-body_1y) * G * body_2.mass / Math.sqrt((body_1x - body_2.r_x)**2 + (body_1y - body_2.r_y)**2)**3;
  }
}


// Physics Simulation Function

function simulate(step, bodies) {
  this.step = step;
  this.bodies = bodies;

  this.draw = function() {
    for(var i = 0; i < this.bodies.length; i++) {
      this.bodies[i].draw();
    }
  }

  this.drawLines = function(x, lastx, y, lasty, color) {
    //console.log(x + ' -> ' + y + '->' + lastx + '->' + lasty);
    /*context.beginPath();
    context.strokeStyle = color;
    context.lineTo(0, 0);
    context.lineTo(x, y);
    context.stroke();
    lastx = x;
    lasty = y;*/
  }

  this.drawOrbitalLines = function() {
    for (i = 0; i < this.bodies.length; i++) {
      for(j = 10; j < this.bodies[i].lastpos_x.length; j++) {
        context.beginPath();
        context.strokeStyle = this.bodies[i].color;
        context.moveTo(this.bodies[i].lastpos_x[j-1], this.bodies[i].lastpos_y[j-1]);
        context.lineTo(this.bodies[i].lastpos_x[j], this.bodies[i].lastpos_y[j]);
        context.stroke();
      }
      this.drawLines(this.bodies[i].plot_x, this.bodies[i].lastpos_x, this.bodies[i].plot_y, this.bodies[i].lastpos_y, this.bodies[i].color);
    }
  }

  this.velocity_verlet = function() {
    var pos_x = [];
    var pos_y = [];
    var vel_x = [];
    var vel_y = [];
    var acc_x = [];
    var acc_y = [];
    for (i = 0; i < this.bodies.length; i++) {
      var a_x = 0;
      var a_y = 0;
      for (j = 0; j < this.bodies.length; j++) {
        a_x += acceleration_x(this.bodies[i], this.bodies[j], i, j);
        a_y += acceleration_y(this.bodies[i], this.bodies[j], i, j);
      }

      // var vhalf_x = this.bodies[i].v_x + 0.5 * step * a_x;
      // var vhalf_y = this.bodies[i].v_y + 0.5 * step * a_y;

      var new_x = this.bodies[i].r_x + this.bodies[i].v_x * step + 0.5 * a_x * step**2;
      var new_y = this.bodies[i].r_y + this.bodies[i].v_y * step + 0.5 * a_y * step**2;

      // pos_x.push(this.bodies[i].r_x + this.step*this.bodies[i].v_x + this.step*this.step*a_x/2);
      pos_x.push(new_x);
      pos_y.push(new_y);
      acc_x.push(a_x);
      acc_y.push(a_y);
    }
    for (i = 0; i < this.bodies.length; i++) {
      var ax_new = 0;
      var ay_new = 0;
      for (var j = 0; j < this.bodies.length; j++) {
        ax_new += lf_acceleration_x(pos_x[i], pos_y[i], this.bodies[j], i, j);
        ay_new += lf_acceleration_y(pos_x[i], pos_y[i], this.bodies[j], i, j);
      }
      new_vx = this.bodies[i].v_x + 0.5*(acc_x[i] + ax_new)*this.step;
      new_vy = this.bodies[i].v_y + 0.5*(acc_y[i] + ay_new)*this.step;
      vel_x.push(new_vx);
      vel_y.push(new_vy);
    }
    for (i = 0; i < this.bodies.length; i++) {
      // x coordinate
      this.bodies[i].r_x = pos_x[i];
      this.bodies[i].lastpos_x = this.bodies[i].plot_x;
      this.bodies[i].plot_x = set_rx(this.bodies[i].r_x);
      
      // y coordinate
      this.bodies[i].r_y = pos_y[i];
      this.bodies[i].lastpos_y = this.bodies[i].plot_y;
      this.bodies[i].plot_y = set_ry(this.bodies[i].r_y);
      
      // velocities
      this.bodies[i].v_x = vel_x[i];
      this.bodies[i].v_y = vel_y[i];
      // console.log(this.bodies[i].r_x + ' - ' + this.bodies[i].r_y + ' \n ' + this.bodies[i].plot_x + ' - ' + this.bodies[i].plot_y);
     }
       this.draw();
       this.drawOrbitalLines();
  } // End verlet

  this.leapfrog = function() {
    var pos_x = [];
    var pos_y = [];
    var vel_x = [];
    var vel_y = [];
    var acc_x = [];
    var acc_y = [];

    w = 1.2599210498948732; // 2**(1./3.)
    f = 0.7400789501051268; // 2 - w

    lf1 = (0.5 * step / f);
    lf2 = step / f;
    lf3 = (1-w) * step * 0.5 / f;
    lf4 = -step * w / f;
    for ( i = 0; i < this.bodies.length; i++) {
        p1_x = this.bodies[i].r_x + lf1 * this.bodies[i].v_x;
        p1_y = this.bodies[i].r_y + lf1 * this.bodies[i].v_y;
        // alert(p1_x);
        ax_new1 = 0;
        ay_new1 = 0;
        for (j = 0; j < this.bodies.length; j++){
          ax_new1 += lf_acceleration_x(p1_x, p1_y, this.bodies[j], i, j);
          ay_new1 += lf_acceleration_y(p1_x, p1_y, this.bodies[j], i, j);
        }
        v2_x = this.bodies[i].v_x + lf2 * ax_new1;
        v2_y = this.bodies[i].v_y + lf2 * ay_new1;

        p3_x = p1_x + lf3 * v2_x;
        p3_y = p1_y + lf3 * v2_y;
        
        ax_new2 = 0;
        ay_new2 = 0;
        for (j = 0; j < this.bodies.length; j++){
          ax_new2 += lf_acceleration_x(p3_x, p3_y, this.bodies[j], i, j);
          ay_new2 += lf_acceleration_y(p3_x, p3_y, this.bodies[j], i, j);
        }

        v4_x = v2_x + lf4 * ax_new2;
        v4_y = v2_y + lf4 * ay_new2;

        p5_x = p3_x  + lf3 * v4_x;
        p5_y = p3_y + lf3 * v4_y;

        ax_new3 = 0;
        ay_new3 = 0;
        for (j = 0; j < this.bodies.length; j++){
          ax_new3 += lf_acceleration_x(p5_x, p5_y, this.bodies[j], i, j);
          ay_new3 += lf_acceleration_y(p5_x, p5_y, this.bodies[j], i, j);
        }

        v6_x = v4_x + lf2 * ax_new3;
        v6_y = v4_y + lf2 * ay_new3;

        p7_x = p5_x + lf1 * v6_x;
        p7_y = p5_y + lf1 * v6_y;

        pos_x.push(p7_x);
        pos_y.push(p7_y);
        vel_x.push(v6_x);
        vel_y.push(v6_y);
    }
    for (i = 0; i < this.bodies.length; i++) {
      // x coordinate
      this.bodies[i].r_x = pos_x[i];
      this.bodies[i].lastpos_x.push(this.bodies[i].plot_x);
      this.bodies[i].plot_x = set_rx(this.bodies[i].r_x);
      
      // y coordinate
      this.bodies[i].r_y = pos_y[i];
      this.bodies[i].lastpos_y.push(this.bodies[i].plot_y);
      this.bodies[i].plot_y = set_ry(this.bodies[i].r_y);
      if (this.bodies[i].lastpos_x.length > 800) {
        this.bodies[i].lastpos_y.splice(0, this.bodies[i].lastpos_y.length-50);
        this.bodies[i].lastpos_x.splice(0, this.bodies[i].lastpos_x.length-50);
      }
      // velocities
      this.bodies[i].v_x = vel_x[i];
      this.bodies[i].v_y = vel_y[i];
      //console.log(this.bodies[i].r_x + ' - ' + this.bodies[i].r_y + ' \n ' + this.bodies[i].plot_x + ' - ' + this.bodies[i].plot_y);
     }
      this.draw();
      this.drawOrbitalLines();
  }
    
} // End Simulate

// (m, rx, ry, vx, vy, ra,color)
//var bodies = [new body(10**15,20,20,-20,0,10,'yellow'), new body(10**15, 30,30,20,0,10,'blue'),new body(10**15, 120,120,0,-20,10,'green'), new body(10**15,50,30,0,20,10,'red')];

/// Initial conditions for real solar system simulation

sun = new body(1.98855e30,0,0,0,0,15,'yellow', 'Sun');
earth = new body(5.9742e24, 147.1e9,0,0,-30.29e3,10,'blue', 'Earth');
venus = new body(4.8685e24, 107.5e9, 0, 0, -35.26e3, 10, 'salmon', 'Venus');
mercury = new body(0.3e24, 46e9, 0, 0, -58.98e3, 10, 'darkmagenta', 'Mercury');
mars = new body(0.642e24, 206.6e9, 0, 0, -26.5e3, 10, 'red', 'Mars');
jupiter = new body(1.898e27, 740.5e9, 0, 0, -13.72e3, 10, 'orange', 'Jupiter');
saturn = new body(5.68e26, 1352.6e9, 0, 0, -10.18e3, 10, 'maroon', 'Saturn');
uranus = new body(8.6e25, 2741.3e9, 0, 0, -7.11e3, 10, 'darkgreen', 'Uranus');
neptune = new body(1.02e26, 4444.5e9, 0, 0, -5.5e3, 10, 'navy', 'Neptune');
var solar_system = [sun, earth, venus, mercury, mars, jupiter, saturn, uranus, neptune];

//// condições iniciais 2 planetas ao redor de 1 estrela

sim_1_ball1 = new body(1, 80e9, 0, -15e3, 15e3, 7, 'green');
sim_1_ball2 = new body(1, -90e9, 0,15e3, -15e3, 7, 'gold');
sim_1_ball3 = new body(5e29, 0, 0, 0, 0, 15, 'red');
sim1 = [sim_1_ball1, sim_1_ball2, sim_1_ball3];

//// Cond iniciais
sim_2_ball1 = new body(1, 80e9, 0, 0, -15e3, 7, 'green');
sim_2_ball2 = new body(1, -80e9, 0,0, -15e3, 7, 'gold');
sim_2_ball3 = new body(1, 0, 0, 0, 30e3, 7,'red');
sim2 = [sim_2_ball1, sim_2_ball2, sim_2_ball3];


pause = 0;

to_simulate = solar_system;

system = new simulate(24*3600,to_simulate);
cm = new mass_center(to_simulate);


document.body.onkeyup = function(e){
  if(e.keyCode == 32){
      if (pause == 0) {
        pause = 1;
      }
      else {
        pause = 0;
        animate();
      }
  }
  if (e.keyCode == 109 || e.keyCode == 173) {
    for (i = 0; i < to_simulate.length; i++){
      to_simulate[i].lastpos_y.splice(0, to_simulate[i].lastpos_y.length);
      to_simulate[i].lastpos_x.splice(0, to_simulate[i].lastpos_x.length);
    }
    meterPerPixel += .5*meterPerPixel;
    canvas.width += .5*window.innerWidth;
    canvas.height += .5*window.innerHeight;
  }
  if (e.keyCode == 107 || e.keyCode == 61) {
    for (i = 0; i < to_simulate.length; i++){
      to_simulate[i].lastpos_y.splice(0, to_simulate[i].lastpos_y.length);
      to_simulate[i].lastpos_x.splice(0, to_simulate[i].lastpos_x.length);
    }
    meterPerPixel -= .5*meterPerPixel;
    canvas.width -= .5*window.innerWidth;
    canvas.height -= .5*window.innerHeight;
  }
}

function animate() {
    if (pause == 0) {
    requestAnimationFrame(animate);
    context.clearRect(0,0,canvas.width,canvas.height);
    system.leapfrog();
    cm.set_CM();
    set_UI(to_simulate.length, parseInt(cm.plot_x), parseInt(cm.plot_y));
    system.drawOrbitalLines();
    } else {
    }
}
animate();
