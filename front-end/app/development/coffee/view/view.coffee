module.exports = do ->
	Backbone = require 'backbone'
	$		 = require 'jquery'
	mustache = require 'mustache'

	getTemplate = (baseTemplte) -> 

		(model) ->
			mustache.render baseTemplte, model 

	class View extends Backbone.View
		el: '.astro-calendar-list'
		template: getTemplate $('#astro-week-template').html()
		initialize: ->
			do @bindEvents
			do @collection.requestModels
		
		bindEvents: ->
			@listenTo @collection, 'reset', @render

		render: (collection) =>
			template = ''

			for ind, val of collection
				template += @template val

			@$el.empty().append template

	View