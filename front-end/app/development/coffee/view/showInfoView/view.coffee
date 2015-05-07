module.exports = do ->
	Backbone = require 'backbone'
	$		 = require 'jquery'
	mustache = require 'mustache'

	getTemplate = (baseTemplte) -> 

		(model) ->
			mustache.render baseTemplte, model 

	class ShowInfoView extends Backbone.View
		el: '#show-info'
		template: getTemplate $('#astro-show-info').html()
		events: {}

		initialize: ->
			do @bindEvents

		bindEvents: ->
			@collection.on 'change:isShowing', @redrawView

		redrawView: (model) =>
			@$el.removeClass 'un-displayed' if @$el.hasClass 'un-displayed'
			@render model

		render: (model) =>
			@$el.empty().append @template model.toJSON()

	ShowInfoView