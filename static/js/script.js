// Hammer js jQuery plugin: https://github.com/hammerjs/jquery.hammer.js
(function(factory) {
  if (typeof define === 'function' && define.amd) {
      define(['jquery', 'hammerjs'], factory);
  } else if (typeof exports === 'object') {
      factory(require('jquery'), require('hammerjs'));
  } else {
      factory(jQuery, Hammer);
  }
}(function($, Hammer) {
  function hammerify(el, options) {
      var $el = $(el);
      if(!$el.data("hammer")) {
          $el.data("hammer", new Hammer($el[0], options));
      }
  }

  $.fn.hammer = function(options) {
      return this.each(function() {
          hammerify(this, options);
      });
  };

  // extend the emit method to also trigger jQuery events
  Hammer.Manager.prototype.emit = (function(originalEmit) {
      return function(type, data) {
          originalEmit.call(this, type, data);
          $(this.element).trigger({
              type: type,
              gesture: data
          });
      };
  })(Hammer.Manager.prototype.emit);
}));

var TxtRotate = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
  };
  
  TxtRotate.prototype.tick = function() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];
  
    if (this.isDeleting) {
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }
  
    this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';
  
    var that = this;
    var delta = 300 - Math.random() * 100;
  
    if (this.isDeleting) { delta /= 2; }
  
    if (!this.isDeleting && this.txt === fullTxt) {
      delta = this.period;
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      this.loopNum++;
      delta = 500;
    }
  
    setTimeout(function() {
      that.tick();
    }, delta);
  };
  
  window.onload = function() {
    var elements = document.getElementsByClassName('txt-rotate');
    for (var i=0; i<elements.length; i++) {
      var toRotate = elements[i].getAttribute('data-rotate');
      var period = elements[i].getAttribute('data-period');
      if (toRotate) {
        new TxtRotate(elements[i], JSON.parse(toRotate), period);
      }
    }
    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".txt-rotate > .wrap { border-right: 0.08em solid #666 }";
    document.body.appendChild(css);

    
    // Click map
    $("#map").click(
      function(){console.log("Hello")}
    )
    var el = document.querySelector(".pinch");
    var ham = new Hammer( el, {
      domEvents: true
    } );
    var width = 1900;
    var height = 400;
    var left = 950;
    var top = 220;

    ham.get('pinch').set({ enable: true });

    ham.on( "pinch", function( e ) {
      console.log( "pinch" );
      if ( width * e.scale >= 300 ) {
        var img = el.childNodes[1];
        img.style.width = (width * e.scale) + 'px';
        img.style.marginLeft = (-left * e.scale) + 'px';
        img.style.height = (height * e.scale) + 'px';
        img.style.marginTop = (-top * e.scale) + 'px';
       }
       console.log( e.scale );
    } );

    ham.on( "pinchend", function( e ) {
      width = width * e.scale;
      height = height * e.scale;
      left = left * e.scale;
      top = top * e.scale;
      console.log( width );
    } );

  };