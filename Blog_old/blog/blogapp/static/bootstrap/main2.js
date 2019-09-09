/**
 * main.js
 * http://www.codrops.com
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 * 
 * Copyright 2017, Codrops
 * http://www.codrops.com
 */
;(function(window) {

	'use strict';

	/**
	 * StackFx: The parent class.
	 */
	function StackFx(el) {
		this.DOM = {};
		this.DOM.el = el;
		this.DOM.stack = this.DOM.el.querySelector('.stack');
		this.DOM.stackItems = [].slice.call(this.DOM.stack.children);
		this.totalItems = this.DOM.stackItems.length;
		this.DOM.img = this.DOM.stack.querySelector('.stack__figure > .stack__img');
		
		
		
	}

	StackFx.prototype._removeAnimeTargets = function() {
		anime.remove(this.DOM.stackItems);
		anime.remove(this.DOM.img);
		
		
	};

	
	
	/************************************************************************
	 * CastorFx.
	 ************************************************************************/
	function CastorFx(el) {
		StackFx.call(this, el);
		this._initEvents();
	}

	CastorFx.prototype = Object.create(StackFx.prototype);
	CastorFx.prototype.constructor = CastorFx;

	CastorFx.prototype._initEvents = function() {
		var self = this;
		this._mouseenterFn = function() {
			self._removeAnimeTargets();
			self._in();
		};
		this._mouseleaveFn = function() {
			self._removeAnimeTargets();
			self._out();
		};
		this.DOM.stack.addEventListener('mouseenter', this._mouseenterFn);
		this.DOM.stack.addEventListener('mouseleave', this._mouseleaveFn);
	};

	CastorFx.prototype._in = function() {
		var self = this;

		anime({
			targets: this.DOM.stackItems,
			rotateX: {
				value: function(target, index, cnt) {
					return index === cnt - 1 ? 0 : [70, 0];
				},
				duration: 1000,
				easing: 'easeOutExpo'
			},
			translateZ: {
				value: function(target, index, cnt) {
					return index === cnt - 1 ? index*20 : [-300, index*20];
				},
				duration: 1000,
				easing: 'easeOutExpo'
			},
			opacity: {
				value: function(target, index, cnt) {
					return index === cnt - 1 ? 1 : [0,0.2*index+0.2];
				},
				duration: 1000,
				easing: 'linear'
			},
			delay: function(target, index, cnt) {
				return (cnt-index-1)*100
			}
		});
		
		anime({
			targets: this.DOM.img,
			duration: 1000,
			easing: 'easeOutExpo',
			scale: 0.7
		});

		
	};

	CastorFx.prototype._out = function() {
		var self = this;

		anime({
			targets: this.DOM.stackItems,
			duration: 1000,
			easing: 'easeOutExpo',
			translateZ: 0,
			opacity: function(target, index, cnt) {
				return index !== cnt - 1 ? 0 : 1
			}
		});

		anime({
			targets: this.DOM.img,
			duration: 1000,
			easing: 'easeOutExpo',
			scale: 1
		});

		

		
	};

	window.CastorFx = CastorFx;

})(window);