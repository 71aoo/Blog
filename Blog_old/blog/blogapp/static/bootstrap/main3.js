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
		this.DOM.caption = this.DOM.el.querySelector('.grid__item-caption');
		this.DOM.title = this.DOM.caption.querySelector('.grid__item-title');
		this.DOM.columns = {left: this.DOM.caption.querySelector('.column--left'), right: this.DOM.caption.querySelector('.column--right')};
	}

	StackFx.prototype._removeAnimeTargets = function() {
		anime.remove(this.DOM.stackItems);
		anime.remove(this.DOM.img);
		anime.remove(this.DOM.title);
		anime.remove(this.DOM.columns.left);
		anime.remove(this.DOM.columns.right);
	};

	

	/************************************************************************
	 * CanopusFx.
	 ************************************************************************/
	function CanopusFx(el) {
		StackFx.call(this, el);
		this._initEvents();
	}

	CanopusFx.prototype = Object.create(StackFx.prototype);
	CanopusFx.prototype.constructor = CanopusFx;

	CanopusFx.prototype._initEvents = function() {
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

	CanopusFx.prototype._in = function() {
		var self = this;

		this.DOM.stackItems.map(function(e, i) {
			e.style.opacity = i !== self.totalItems - 1 ? 0 : 1
		});

		var self = this;
		anime({
			targets: this.DOM.stackItems,
			translateZ: {
				value: function(target, index, cnt) {
					return -1*(cnt-index-1)*20;
				},
				duration: 800,
				easing: 'easeOutExpo',
				delay: function(target, index, cnt) {
					return (cnt-index-1)*70 + 200;
				}
			},
			translateY: [
				{ 
					value: function(target, index) {
						return -1*index*20 - 30;
					}, 
					duration: 800, 
					delay: function(target, index, cnt) {
						return (cnt-index-1)*70 + 200;
					}, 
					elasticity: 500 
				},
			],
			scaleY: [
				{ 
					value: function(target, index, cnt) {
						return index === cnt-1 ? 0.6 : 1;
					}, 
					duration: 200, 
					easing: 'easeOutExpo' 
				},
				{ 
					value: 0.8, 
					duration: 800, 
					elasticity: 450 
				}
			],
			scaleX: [
				{ 
					value: function(target, index, cnt) {
						return index === cnt-1 ? 1.1 : 1;
					},
					duration: 200, 
					easing: 'easeOutExpo' 
				},
				{ 
					value: 0.8, 
					duration: 800, 
					elasticity: 300 
				}
			],
			opacity: {
				value: function(target, index, cnt) {
					return index === cnt-1 ? 1 : [0,0.2*index+0.2];
				},
				duration: 200,
				easing: 'linear',
				delay: function(target, index, cnt) {
					return (cnt-index-1)*70 + 200;
				}
			}
		});

		anime({
			targets: this.DOM.img,
			scale: [
				{
					value: 1.8,
					duration: 200,
					easing: 'easeOutExpo'
				},
				{
					value: 0.7,
					duration: 1100,
					easing: 'easeOutExpo'
				}
			]
		});

		anime({
			targets: [this.DOM.title, this.DOM.columns.left, this.DOM.columns.right],
			duration: 1000,
			easing: 'easeOutElastic',
			translateY: -30,
			delay: 200
		});
	};

	CanopusFx.prototype._out = function() {
		var self = this;

		anime({
			targets: this.DOM.stackItems,
			duration: 500,
			easing: 'easeOutExpo',
			translateZ: 0,
			translateY: 0,
			scaleY: 1,
			scaleX: 1,
			opacity: function(target, index, cnt) {
				return index !== cnt - 1 ? 0 : 1
			}
		});

		anime({
			targets: this.DOM.img,
			duration: 500,
			easing: 'easeOutExpo',
			scale: 1
		});

		anime({
			targets: [this.DOM.title, this.DOM.columns.left, this.DOM.columns.right],
			duration: 500,
			easing: 'easeOutExpo',
			translateY: 0
		});
	};

	window.CanopusFx = CanopusFx;



})(window);